from sqlalchemy.orm import DeclarativeBase
import asyncpg

from contextlib import asynccontextmanager
from typing import Optional

from ab_test_api.settings import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


class BaseDBModel(DeclarativeBase):
    pass


async def _connetion_init(conn):
    return conn


_pool: Optional[asyncpg.pool.Pool] = None


async def connect():
    global _pool
    if not _pool:
        _pool = await asyncpg.create_pool(
            init=_connetion_init,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
            min_size=1,
            max_size=4)
    return _pool


async def close():
    global _pool
    if not _pool:
        return
    await _pool.close()


@asynccontextmanager
async def get_connection():
    conn_pool = await connect()
    conn = await conn_pool.acquire()
    yield conn
    await conn_pool.release(conn)

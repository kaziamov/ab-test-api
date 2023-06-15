from sqlalchemy.orm import DeclarativeBase
import asyncpg
import asyncio

from contextlib import asynccontextmanager
from typing import Optional

from ab_test_api.settings import (DB_HOST,
                                  DB_NAME,
                                  DB_PASS,
                                  DB_PORT,
                                  DB_USER,
                                  MIN_CONN,
                                  MAX_CONN)


class BaseDBModel(DeclarativeBase):
    pass


_pool: Optional[asyncpg.pool.Pool] = None
_pool_lock = None


def init_pool_lock():
    global _pool_lock
    _pool_lock = asyncio.lock()


async def connection_init(conn):
    return conn


async def connect():
    global _pool
    async with _pool_lock:
        if not _pool:
            _pool = await asyncpg.create_pool(
                init=connection_init,
                database=DATABASE_URL,
                user=DB_USER,
                password=DB_PASS,
                host=DB_HOST,
                post=DB_PORT,
                min_size=MIN_CONN,
                max_size=MAX_CONN,
            )
    return _pool


async def close():
    global _pool
    if not _pool:
        return
    async with _pool_lock:
        await _pool.close()


@asynccontextmanager
async def get_connection():
    conn_pool = await connect()
    conn = await conn_pool.acquire()
    yield conn
    await conn_pool.release(conn)

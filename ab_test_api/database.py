import aiopg

from ab_test_api.settings import (DB_HOST, DB_PORT, DB_USER,
                                  DB_PASS, DB_NAME)
from contextlib import asynccontextmanager, contextmanager
# from ab_test_api.crud import get_device


# async def create_connection(*args, **kwargs):
#     """Create connection for work with PostgresSQL"""
#     return await psycopg2.connect(
#         host=DB_HOST,
#         port=DB_PORT,
#         user=DB_USER,
#         password=DB_PASS,
#         database=DB_NAME)


# async def create_pool(min_conn=1, max_conn=5):
#     """Create connection for work with PostgresSQL"""
#     return pool.SimpleConnectionPool(minconn=min_conn,
#                                      maxconn=max_conn,
#                                      connection_factory=create_connection,
#                                      host=DB_HOST,
#                                      port=DB_PORT,
#                                      user=DB_USER,
#                                      password=DB_PASS,
#                                      database=DB_NAME)


@contextmanager
def get_connection(func):
    pool = aiopg.create_pool(DSN)
    async def inner(*args, **kwargs):
        nonlocal pool
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                result = await func(*args, **kwargs, cur=cur)
                result = {'Hello': "Hello"}
                ret = []
                async for row in cur:
                    ret.append(row)
                assert ret == [(1,)]
        return result
    return inner



DSN = f'dbname={DB_NAME} user={DB_USER} password={DB_PASS} host={DB_HOST}'

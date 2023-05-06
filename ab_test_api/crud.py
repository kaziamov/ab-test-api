from datetime import datetime
import aiopg
from ab_test_api.database import DSN

from ab_test_api.database import get_connection

async def test_select(device):
    async with aiopg.create_pool(DSN) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                result = await cur.execute("""
                SELECT button_colors FROM devices WHERE device_token=%s
                LIMIT 1;""",
                (device, ))
                ret = []
                async for row in cur:
                    ret.append(row)
                assert ret == [(1,)]
    return result

@get_connection
async def get_device(device, cur=None):
    """Check if exist and return bool"""
    await cur.execute("""
                SELECT button_color FROM devices WHERE device_token=%s
                LIMIT 1;""",
                (device, ))
    response = await cur.fetchone()
    return response


@get_connection
async def add_device(device_token, experiment, value, cur=None):
    """Add new value in database"""
    await cur.execute("""
                    INSERT INTO devices (device_token, %s, created_at)
                    VALUES (%s, %s, %s);""",
                    (experiment, device_token, value, datetime.now()))

from datetime import datetime

from ab_test_api.database import get_connection


async def get_device(device):
    query = """
            SELECT button_color
            FROM devices
            WHERE device=$1 LIMIT 1;"""
    async with get_connection() as conn:
        result = await conn.fetch(query, device)
    return result


async def add_device(device, data):
    """Get device token and dict with keys and values for creating new device in database"""
    keys = data.keys()
    values = data.values()
    query = f"""
            INSERT INTO devices
            (device, created_at, $1, $2)
            VALUES ($3, now(), $4, $5)
            RETURNING *;
    """
    async with get_connection() as conn:
        result = await conn.fetch(query, device, *keys, *values)
    return result

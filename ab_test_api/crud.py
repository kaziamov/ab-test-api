from ab_test_api.database import get_connection


async def get_device(device: str) -> list:
    query = """
            SELECT *
            FROM devices
            WHERE device=$1 LIMIT 1;"""
    async with get_connection() as conn:
        result = await conn.fetch(query, device)
    return result


async def add_device(device: str, data: dict) -> list:
    """Get device token and dict with keys and values for creating new device in database"""
    values = data.values()
    query = """
            INSERT INTO devices
            (device, created_at, button_color, price)
            VALUES ($1, now(), $2, $3)
            RETURNING *;
    """
    async with get_connection() as conn:
        result = await conn.fetch(query, device, *values)
    return result


async def count_devices(test_name: str, value: str) -> int:
    query = """
            SELECT COUNT(*)
            FROM devices
            WHERE $1=$2;
    """
    async with get_connection() as conn:
        result = await conn.fetch(query, test_name, value)
    return result

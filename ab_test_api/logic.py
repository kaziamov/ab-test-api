from ab_test_api.crud import get_device, add_device
from ab_test_api.counters import colors_generator, price_generator


async def get_or_create_test(device_token: str):
    device = await get_device(device_token)
    if not device:
        params = {}
        params.update(await generate_color_test())
        params.update(await generate_price_test())
        device = await add_device(device_token, params)
    return device


async def generate_color_test() -> dict:
    async for color in colors_generator:
        test = {'button_color': color}
        return test


async def generate_price_test() -> dict:
    async for price in price_generator:
        test = {'price': price}
        return test

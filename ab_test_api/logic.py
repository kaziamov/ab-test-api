from ab_test_api.crud import get_device, add_device


async def get_or_create_test(device_token):
    device = await get_device(device_token)
    # TODO: add create device and tests random logic
    if not device:
        device = await add_device(device_token, {'button_color': '#282828', 'price': '20'})
    return device

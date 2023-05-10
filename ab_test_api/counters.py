from random import shuffle
from itertools import chain


async def get_next_color():
    index = 0
    colors = ["#FF0000", "#00FF00", "#0000FF"]
    while True:
        yield colors[index]
        index += 1
        if index >= len(colors):
            index = 0


async def get_next_price():
    index = 0
    prices = list(chain([10] * 15,
                        [20] * 2,
                        [50] * 1,
                        [5] * 2))
    shuffle(prices)
    while True:
        yield prices[index]
        index += 1
        if index >= len(prices):
            index = 0


colors_generator = get_next_color()
price_generator = get_next_price()

from pony.orm import PrimaryKey, Optional
from ab_test_api.db_connect import db


class Device(db.Entity):
    device_token = PrimaryKey(str)
    button_color = Optional(str, nullable=True)
    price = Optional(int, nullable=True)

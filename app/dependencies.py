from motor.core import AgnosticCollection
from app.db import client

def get_db() -> AgnosticCollection:
    return client["items_db"]["items"]

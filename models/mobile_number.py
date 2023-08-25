from pydantic import BaseModel
from pydantic.v1 import validator


class User(BaseModel):
    phone_number: str

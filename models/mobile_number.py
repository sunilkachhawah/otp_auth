from pydantic import BaseModel
from pydantic.v1 import validator


class SendOTPRequest(BaseModel):
    phone_number: str
    device_id:str

class VerifyOTPRequest(BaseModel):
    device_id:str
    otp:str





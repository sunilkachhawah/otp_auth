from pydantic import BaseModel


class SendOTPRequest(BaseModel):
    phone_number: str
    device_id: str


class VerifyOTPRequest(BaseModel):
    device_id: str
    otp: str

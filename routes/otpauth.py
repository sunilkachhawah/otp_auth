import random, string
from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from configuration import mongoDb
from models import mobile_number
from datetime import datetime, timedelta

otp = APIRouter()


@otp.post("/login")
async def send_otp(param: mobile_number.SendOTPRequest):
    try:
        def generate_otp(length=6):
            digits = string.digits
            otp = ''.join(random.choice(digits) for _ in range(length))
            return otp

        otp = generate_otp()  # Implement your OTP generation logic here

        otp_data = {
            "number": param.phone_number,
            "otp": otp,
            "expireAt": datetime.utcnow() + timedelta(minutes=5)
        }

        check = {
            "number": param.phone_number
        }
        existdata = mongoDb.collection.find_one(check)
        if existdata:
            mongoDb.collection.delete_one(check)

        mongoDb.collection.insert_one(otp_data)
        return {"message": "OTP sent successfully"}
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=400, detail="OTP can't be sent")


@otp.post("/verify")
async def verify_otp(param: mobile_number.VerifyOTPRequest):
    check = {
        "number": param.phone_number,
        "otp": param.otp
    }
    existdata = mongoDb.collection.find_one(check)
    if existdata:
        mongoDb.collection.delete_one(check)
        return {"message": "OTP verification successful"}
    else:
        raise HTTPException(status_code=400, detail="OTP verification failed")


@otp.post("/get")
async def get_otp(mobile_number: str):
    existdata = mongoDb.collection.find_one({"number": mobile_number})
    if existdata:
        return JSONResponse(content={"otp": existdata["otp"]})
    else:
        raise HTTPException(status_code=400, detail="otp not available")

import random, string

from fastapi import APIRouter, HTTPException

from configuration import aws_sns, mongoDb
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

        message = f"login OTP for MYeKIGAI is: {otp}"

        phone_number = param.phone_number  # Get the phone number from the POST request
        # for deliver message through SNS
        aws_sns.sns_client.publish(
            PhoneNumber=phone_number,
            Message=message,
        )

        otp_data = {
            "device_id": param.device_id,
            "otp": otp,
            "expireAt": datetime.utcnow() + timedelta(minutes=5)
        }

        mongoDb.collection.insert_one(otp_data)
        return {"message": "OTP sent successfully"}
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=400, detail="OTP can't be sent")


@otp.post("/verify")
async def verify_otp(param: mobile_number.VerifyOTPRequest):
    check = {
        "device_id": param.device_id,
        "otp": param.otp
    }
    existdata = mongoDb.collection.find_one(check)
    if existdata:
        mongoDb.collection.delete_one(check)
        return {"message": "OTP verification successful"}
    else:
        raise HTTPException(status_code=400, detail="OTP verification failed")

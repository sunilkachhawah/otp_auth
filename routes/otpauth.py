import random, string

import pytz

from fastapi import APIRouter, HTTPException

import configuration.aws_sns
import models.mobile_number
from datetime import datetime, timedelta
from configuration.mongoDb import collection

otp = APIRouter()


@otp.post("/login")
async def send_otp(send_otp_request: models.mobile_number.SendOTPRequest):
    try:
        def generate_otp(length=6):
            digits = string.digits
            otp = ''.join(random.choice(digits) for _ in range(length))
            return otp

        otp = generate_otp()  # Implement your OTP generation logic here

        message = f"login OTP for MYeKIGAI is: {otp}"

        phone_number = send_otp_request.phone_number  # Get the phone number from the POST request
        # for deliver message through SNS
        configuration.aws_sns.sns_client.publish(
            PhoneNumber=phone_number,
            Message=message,
        )
        current_time = datetime.now()
        expiration_time = current_time + timedelta(minutes=5)

        otp_data = {
            "phone_number": send_otp_request.phone_number,
            "device_id": send_otp_request.device_id,
            "otp": otp,
            "time": expiration_time
        }

        collection.insert_one(otp_data)
        return {"message": "OTP sent successfully"}
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=400, detail="OTP can't be sent")


@otp.post("/verify")
async def verify_otp(verify_otp_request: models.mobile_number.VerifyOTPRequest):
    check = {
        "device_id": verify_otp_request.device_id,
        "otp": verify_otp_request.otp
    }
    existdata=collection.find_one(check)
    if existdata:
        return {"message": "OTP verification successful"}
    else:
        raise HTTPException(status_code=400, detail="OTP verification failed")

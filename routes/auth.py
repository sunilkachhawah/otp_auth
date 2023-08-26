from fastapi import HTTPException, APIRouter
from firebase_admin import auth
from configuration.mongoDb import collection
from models.mobile_number import User  # Import the MobileNumber model

otp = APIRouter()


@otp.post("/")
async def store_number(mobile: User):  # Use the MobileNumber model here
    if len(mobile.phone_number) != 10:
        raise HTTPException(status_code=400, detail="please enter valid mobile number")
    else:
        pass
    # for add unique number
    existing_record = collection.find_one({"mobile_number": mobile.phone_number})
    if existing_record:
        raise HTTPException(status_code=400, detail="Mobile number already exists")
    # Insert the mobile number into the MongoDB collection
    result = collection.insert_one({"mobile_number": mobile.phone_number})

    if result.inserted_id:
        raise HTTPException(status_code=200, detail="mobile number stored successfully")
    else:
        raise HTTPException(status_code=500, detail="Failed to store mobile number")


@otp.post("/login")
def send_otp(user_data: User):
    try:
        user = auth.create_user(phone_number="+91"+user_data.phone_number)
        return {"message": "otp sent successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="failed to send otp")


@otp.post("/validate")
def verify_otp(user_data: User, submitted_otp: str):
    try:
        user = auth.get_user_by_phone_number(user_data.phone_number)
        id_token = submitted_otp
        auth.verify_id_token(id_token)
        return {"message": "Autnentication successfull"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Invalid otp")

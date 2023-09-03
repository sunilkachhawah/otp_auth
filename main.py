from fastapi import FastAPI

from routes import otpauth

app = FastAPI()

app.include_router(otpauth.otp)

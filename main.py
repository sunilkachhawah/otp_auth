from fastapi import FastAPI


from routes.otpauth import otp

app = FastAPI()

app.include_router(otp)



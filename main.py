from fastapi import FastAPI

from configuration.firebase import cred
import firebase_admin
from routes.auth import otp

app = FastAPI()

firebase_admin.initialize_app(cred)
app.include_router(otp)
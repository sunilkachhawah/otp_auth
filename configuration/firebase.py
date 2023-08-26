import firebase_admin
from firebase_admin import credentials

# firebase credentials integration
try:
    app = firebase_admin.get_app()
except ValueError as e:
    print(e)
    cred = credentials.Certificate("credentials/credentials.json")

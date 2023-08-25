import requests

url = "http://localhost:8000/store-number/"

# JSON data to send in the POST request
data = {
    "mobile_number": "124418241"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("API call successful:", response.json())
else:
    print("API call failed with status code:", response.status_code)

import requests

url = "http://localhost:8000/"

# JSON data to send in the POST request
data = {
    "phone_number": "9387841596"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("API call successful:", response.json())
else:
    print("API call failed with status code:", response.status_code)



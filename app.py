from fastapi import FastAPI
import requests
import dotenv
import os

# Load environment variables
dotenv.load_dotenv()

# Create our fastapi app
app = FastAPI()

auth_token = os.getenv("VAPI_AUTH_TOKEN")
call_id = "43068132-290c-4e4b-99ab-cb657d1414ef"

headers = {
    'Authorization': f'Bearer {auth_token}'
}

def get_call_data():
    response = requests.get(f'https://api.vapi.ai/call/{call_id}', headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.status_code)

if __name__ == "__main__":
    get_call_data()
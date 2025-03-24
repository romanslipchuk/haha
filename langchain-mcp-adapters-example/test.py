import requests
import os
from dotenv import load_dotenv
import uuid

rq_uid = str(uuid.uuid4())
load_dotenv()
GIGACHAT_API_KEY = os.getenv("GIGACHAT_API_KEY")

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload = 'scope=GIGACHAT_API_PERS'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'RqUID': rq_uid,
  'Authorization': f'Basic {GIGACHAT_API_KEY}'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
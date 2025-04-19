# Simulación de bypass
import requests

url = "http://target.local/admin"
headers = {"Authorization": "Bearer ghp_exampleleaktoken1337"}

r = requests.get(url, headers=headers)
print(r.status_code)

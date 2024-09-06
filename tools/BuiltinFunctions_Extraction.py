import requests
import re

url = "https://raw.githubusercontent.com/leek-wars/leek-wars/0580d239bc162111ae460198a2e3eed3cc2c4db6/src/model/functions.ts"

response = requests.get(url)

if response.status_code == 200:
    data = response.text
    names = re.findall(r"\bname: '([^']*)'", data)
    print("|".join(names))
    print("Found", len(names), "functions")
else:
    print("Failed to download file. Status code:", response.status_code)

import requests

url = "https://leekwars.com/api/function/get-all"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    names = "|".join([function["name"] for function in data["functions"]])
    print(names)
    print("Found", len(data["functions"]), "functions")
    with open("builtin_functions_highlighting.txt", "w") as file:
        file.write(names)
else:
    print("Failed to download file. Status code:", response.status_code)


import json
import requests

Constants_URL = "https://leekwars.com/api/constant/get-all"

def fetch_constants():
    """
    Fetches the Leek Wars constants from the given URL.
    """
    response = requests.get(Constants_URL)
    return response.json()

def extract_constants(constants):
    """
    Extracts the Leek Wars constants from the given data.
    """
    return [constant["name"] for constant in constants["constants"]]

def write_constants_to_file(constants, filename):
    """
    Writes the given constants to the given file.
    """
    with open(filename, "w") as file:
        file.write("|".join(constants))

def main():
    constants = fetch_constants()
    constants_names = extract_constants(constants)
    print(f"Found {len(constants_names)} constants")
    write_constants_to_file(constants_names, "constants_highlighting.txt")

if __name__ == "__main__":
    main()


import re
import requests

Constants_URL = "https://raw.githubusercontent.com/leek-wars/leek-wars/0580d239bc162111ae460198a2e3eed3cc2c4db6/src/model/constants.ts"

def fetch_constants():
    """
    Fetches the Leek Wars constants from the given URL.
    """
    response = requests.get(Constants_URL)
    return response.text

def extract_constants(constants_text):
    """
    Extracts the Leek Wars constants from the given text.
    """
    pattern = r'name: \'([A-Z_a-z0-9]+)\''
    return re.findall(pattern, constants_text)

def write_constants_to_file(constants, filename):
    """
    Writes the given constants to the given file.
    """
    with open(filename, "w") as file:
        file.write("|".join(constants))

def main():
    constants_text = fetch_constants()
    constants = extract_constants(constants_text)
    write_constants_to_file(constants, "constants_highlighting.txt")

if __name__ == "__main__":
    main()


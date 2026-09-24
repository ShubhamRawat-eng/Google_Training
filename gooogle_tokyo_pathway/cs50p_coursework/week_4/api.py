import requests


def main():
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search",{"q": "Monet"} )
        
    except requests.HTTPError:
        print("Couldn't complete request!")

    content = response.json()
    for artworks in content["data"]:
        print(f"*{artworks["title"]}")



main()
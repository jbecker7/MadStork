import requests
from bs4 import BeautifulSoup
import re

def main():
    wiki_api_url = "https://en.wikipedia.org/w/api.php"
    user_agent = "MyProjectName (merlin@example.com)"

    # Step 1: Get a random article title
    params_random = {
        "action": "query",
        "list": "random",
        "format": "json",
        "rnnamespace": 0,  # Limit to articles only
        "rnlimit": 1  
    }
    headers = {
        "User-Agent": user_agent
    }

    response_random = requests.get(wiki_api_url, params=params_random, headers=headers)
    data_random = response_random.json()
    random_title = data_random["query"]["random"][0]["title"]

    # Step 2: Get the content of the random article
    params_page = {
        "action": "parse",
        "page": random_title,
        "format": "json",
        "contentmodel": "wikitext"
    }

    response_page = requests.get(wiki_api_url, params=params_page, headers=headers)
    data_page = response_page.json()
    if "parse" in data_page and "text" in data_page["parse"]:
        content = data_page["parse"]["text"]["*"]
        # Use BeautifulSoup to parse the HTML and extract the text paragraphs
        soup = BeautifulSoup(content, "html.parser")
        paragraphs = soup.find_all("p")
        # Filter out any element with class "mw-empty-elt" and keep only English, punctuation, and numbers
        sentences = [re.sub(r"[^a-zA-Z0-9.,!?'\s]", "", p.text.strip()) for p in paragraphs if p.get("class") != ["mw-empty-elt"]]
        # Save just the first three sentences
        product = "\n".join(sentences[:3])
        return product
    else:
        print(f"Failed to retrieve content from '{random_title}'.")

main()
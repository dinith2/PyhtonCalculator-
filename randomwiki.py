import requests
from bs4 import BeautifulSoup
import webbrowser
#Wikipedia explorer that displays a random Wikipedia page:
def get_random_wikipedia_page():
    response = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    if response.status_code == 200:
        return response.url
    else:
        return None

def open_wikipedia_page(url):
    webbrowser.open(url)

if __name__ == "__main__":
    print("Welcome to Wikipedia Explorer!")
    while True:
        print("\n1. Random Wikipedia Page")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            random_page_url = get_random_wikipedia_page()
            if random_page_url:
                print("Opening Random Wikipedia Page...")
                open_wikipedia_page(random_page_url)
            else:
                print("Failed to fetch a random Wikipedia page.")
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

import requests
from bs4 import BeautifulSoup
import csv
import os

BASE_URL = "http://books.toscrape.com/catalogue/"
START_URL = "http://books.toscrape.com/catalogue/page-1.html"

# Get the current working directory (Web_Scrapping_Project folder)
SAVE_PATH = os.path.join(os.getcwd(), "scraped_books.csv")

# Function to get book data from a single page
def get_books_from_page(url):
    books = []
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return books

    soup = BeautifulSoup(response.text, "html.parser")
    book_list = soup.select("article.product_pod")

    for book in book_list:
        title = book.h3.a.attrs["title"]
        price = book.select_one("p.price_color").text.strip()
        availability = book.select_one("p.instock.availability").text.strip()
        rating = book.select_one("p.star-rating")["class"][1]
        book_url = BASE_URL + book.h3.a["href"]

        books.append([title, price, availability, rating, book_url])

    return books

# Function to scrape the first 10 pages
def scrape_first_10_pages():
    all_books = []
    
    for page_number in range(1, 11):  # Scrape only first 10 pages
        url = f"http://books.toscrape.com/catalogue/page-{page_number}.html"
        books = get_books_from_page(url)

        if not books:
            break  # Stop if a page has no books (in case site structure changes)

        all_books.extend(books)
        print(f"Scraped page {page_number}...")

    # Save to CSV in the Web_Scrapping_Project folder
    with open(SAVE_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price (£)", "Availability", "Rating", "Book URL"])
        writer.writerows(all_books)

    print(f"✅ Scraping completed! Data saved at: {SAVE_PATH}")

# Run the scraper
if __name__ == "__main__":
    scrape_first_10_pages()

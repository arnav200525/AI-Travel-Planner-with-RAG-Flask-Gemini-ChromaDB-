from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os
import re
import requests
from bs4 import BeautifulSoup

PERSIST_DIRECTORY = "db/chroma_db"


def get_wikipedia_url(city: str) -> str:
    city_formatted = city.strip().title().replace(" ", "_")
    return f"https://en.wikipedia.org/wiki/Tourism_in_{city_formatted}"

def get_wikivoyage_url(city: str) -> str:
    city_formatted = city.strip().title().replace(" ", "_")
    return f"https://en.wikivoyage.org/wiki/{city_formatted}"


def scrape_wikipedia(city: str) -> str:
    url = get_wikipedia_url(city)
    print(f"Scraping: {url}")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError(f"Wikipedia page not found. Status: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")
    text = ""

    for para in paragraphs:
        text += para.get_text()

    if not text.strip():
        raise ValueError("No content found on the page.")

    return text

def scrape_wikivoyage(city: str) -> str:
    url = get_wikivoyage_url(city)
    print(f"Scraping Wikivoyage: {url}")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Wikivoyage page not found.")
        return ""

    soup = BeautifulSoup(response.text, "html.parser")

    content = soup.find("div", {"id": "mw-content-text"})
    if not content:
        return ""

    paragraphs = content.find_all("p")

    text = ""
    for para in paragraphs:
        text += para.get_text()

    return text


def split_text(text: str, city: str):
    splitter = CharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100
    )

    documents = splitter.create_documents([text])

    for doc in documents:
        doc.metadata["city"] = city.lower()

    return documents


def create_or_update_vector_store(documents):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    os.makedirs(PERSIST_DIRECTORY, exist_ok=True)

    db = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )

    db.add_documents(documents)

    print("Vector store updated successfully.")


def main():
    print("=== Wikipedia Ingestion Pipeline ===")

    city = input("Enter city name to ingest: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    text_wiki = scrape_wikipedia(city)
    text_voyage = scrape_wikivoyage(city)
    combined_text = text_wiki + "\n\n" + text_voyage

    documents = split_text(combined_text, city)
    create_or_update_vector_store(documents)

    print(f"Ingestion completed for {city}.")


if __name__ == "__main__":
    main()
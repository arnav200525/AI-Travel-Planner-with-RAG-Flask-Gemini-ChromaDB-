# 🌍 AI Travel Planner – RAG Based Travel Itinerary Generator

An AI-powered Travel Planning Web Application that generates personalized travel itineraries using **Retrieval-Augmented Generation (RAG)**.

Built with **Flask, Google Gemini API, LangChain, HuggingFace Embeddings, and ChromaDB**, this project combines Generative AI with verified tourism data to produce accurate and structured travel plans.

---

## 🚀 Project Overview

This application allows users to:

- Enter a destination city
- Provide trip duration and preferences
- Generate a structured travel itinerary
- Get hotel & food recommendations
- Download the itinerary as a PDF

Unlike basic AI chatbots, this system uses a **RAG architecture** to retrieve verified tourism data before generating responses — improving factual accuracy.

---

## 🧠 How It Works (RAG Architecture)

1. Tourism data is scraped from Wikipedia and Wikivoyage.
2. The data is chunked and converted into embeddings.
3. Embeddings are stored in **ChromaDB** (Vector Database).
4. When a user enters a query:
   - Relevant data is retrieved from ChromaDB.
   - Retrieved context is passed to **Google Gemini**.
   - Gemini generates a structured JSON itinerary.
5. The itinerary is displayed and can be downloaded as a PDF.

---

## 🛠 Tech Stack

- **Backend:** Flask
- **LLM:** Google Gemini (Generative AI)
- **Vector Database:** ChromaDB
- **Framework:** LangChain
- **Embeddings:** HuggingFace Sentence Transformers
- **PDF Generation:** ReportLab
- **Web Scraping:** BeautifulSoup
- **Environment Management:** python-dotenv

---

## 🚀 Future Improvements

- Multi-city planning
- Live hotel & flight API integration
- User authentication system
- Trip saving feature
- Cloud deployment (Render / AWS)
- UI/UX improvements

---

## 📌 Learning Outcomes

This project demonstrates:

- Practical implementation of RAG
- Vector databases in real-world use
- LLM integration with Flask
- Prompt engineering for structured output
- End-to-end AI application development

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

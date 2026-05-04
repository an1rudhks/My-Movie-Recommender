# 🎬 My-Movie-Recommender

This project is a content-based movie recommender that suggests films similar to the ones you love. By analyzing movie metadata such as genres and plot keywords, the system finds mathematical similarities between titles to provide accurate recommendations.

# Objectives

Build a functional machine learning "engine" using Natural Language Processing (NLP).

Create a user-friendly web interface for real-time recommendations.

Demonstrate a clean, modular project structure suitable for a professional portfolio.

# Key Concepts Used

Text Vectorization (Bag of Words): Converting text tags into numerical vectors so the computer can process them.

Cosine Similarity: Calculating the "angle" between movie vectors; a smaller angle means the movies are more similar.

Content-Based Filtering: Recommending items based on the attributes (tags) of the item itself rather than user behavior.

# Tools & Technologies

Language: Python

Libraries: Pandas (Data manipulation), Scikit-Learn (Vectorization & Similarity), Requests (API handling)

Frontend: Streamlit

Data Source: The Movie Database (TMDb) API


# How to Run locally

1. Clone this repository.
2. Create a virtual environment with `python -m venv venv`.
3. Activate the environment with `.\venv\Scripts\activate`.
4. Install the required libraries using `pip install -r requirements.txt`.
5. Run the Streamlit app with `streamlit run src/app.py`.

# Project Structure

```
my-movie-recommender/
├── data/
│   └── movies_data.csv       # Raw movie dataset
├── notebooks/
│   └── movie_engine.ipynb    # Step-by-step research and logic testing
├── src/
│   └── app.py                # Main Streamlit application code
├── .gitignore                
├── requirements.txt          # List of Python dependencies
└── README.md                 # Project documentation

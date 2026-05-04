🎬 Movie Recommendation System

Description
This project is a content-based movie recommender that suggests films similar to the ones you love. By analyzing movie metadata such as genres and plot keywords, the system finds mathematical similarities between titles to provide accurate recommendations.

Objectives

Build a functional machine learning "engine" using Natural Language Processing (NLP).

Create a user-friendly web interface for real-time recommendations.

Demonstrate a clean, modular project structure suitable for a professional portfolio.

Key Concepts Used

Text Vectorization (Bag of Words): Converting text tags into numerical vectors so the computer can process them.

Cosine Similarity: Calculating the "angle" between movie vectors; a smaller angle means the movies are more similar.

Content-Based Filtering: Recommending items based on the attributes (tags) of the item itself rather than user behavior.

Tools and Technologies

Language: Python

Libraries: Pandas (Data manipulation), Scikit-Learn (Vectorization & Similarity), Requests (API handling)

Frontend: Streamlit

Data Source: TMDB API (for movie posters)

Project Structure

my-movie-recommender/
├── data/
│   └── movies_data.csv       # Raw movie dataset
├── notebooks/
│   └── movie_engine.ipynb    # Step-by-step research and logic testing
├── src/
│   └── app.py                # Main Streamlit application code
├── .gitignore                # Prevents uploading venv and cache files
├── requirements.txt          # List of Python dependencies
└── README.md                 # Project documentation (this file)

🚀 How to Run locally
Clone the repository.

Set up a virtual environment:

Bash
python -m venv venv
.\venv\Scripts\activate   # Windows

Install dependencies:

Bash
pip install -r requirements.txt
Launch the App:

Bash
   streamlit run src/app.py
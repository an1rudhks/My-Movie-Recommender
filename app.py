import streamlit as st
import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Page Configuration (Browser Tab)
st.set_page_config(page_title="My Movie Recommender", layout="wide")

# 2. Function to fetch posters
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8"
        data = requests.get(url, timeout=5).json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except:
        return "https://via.placeholder.com/500x750.png?text=Poster+Unavailable"

# 3. Load Data & AI Math
df = pd.read_csv('movies_data.csv')

# Vectorization: Turning words into numbers
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(df['tags']).toarray()
similarity = cosine_similarity(vectors)

# 4. UI Layout
st.title('🎬 Movie Recommendation System')

selected_movie = st.selectbox('Select a movie you liked:', df['title'].values)

if st.button('Show Recommendations'):
    index = df[df['title'] == selected_movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    st.subheader("Recommendations")
    cols = st.columns(5)
    
    # Get top 5 matches
    for i in range(1, 6):
        idx = distances[i][0]
        m_id = df.iloc[idx].movie_id
        name = df.iloc[idx].title
        
        with cols[i-1]:
            st.image(fetch_poster(m_id))
            st.write(name)
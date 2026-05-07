# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="My Movie Recommender", layout="wide")

FALLBACK_POSTER = "https://via.placeholder.com/300x450.png?text=No+Image"


# =========================================================
# 2. LOAD DATA
# =========================================================
@st.cache_resource
def load_data():
    df = pd.read_csv("data/movies_data.csv")

    # Clean data
    df["poster_url"] = df["poster_url"].fillna("").astype(str).str.strip()
    df["title"] = df["title"].astype(str).str.strip()
    df["tags"] = df["tags"].fillna("")

    return df


df = load_data()


# =========================================================
# 3. AI LOGIC (TEXT VECTORIZATION + SIMILARITY)
# =========================================================
@st.cache_resource
def compute_similarity(df):
    cv = CountVectorizer(max_features=5000, stop_words="english")
    vectors = cv.fit_transform(df["tags"]).toarray()
    similarity = cosine_similarity(vectors)
    return similarity


similarity = compute_similarity(df)


# =========================================================
# 4. HELPER FUNCTION (SAFE IMAGE)
# =========================================================
def safe_image(url):
    if isinstance(url, str) and url.startswith("http"):
        return url
    return FALLBACK_POSTER


# =========================================================
# 5. UI - INPUT SECTION
# =========================================================
st.title("🎬 My Movie Recommender")

selected_movie = st.selectbox(
    "Select a movie you like:",
    df["title"].values
)


# =========================================================
# 6. SELECTED MOVIE DISPLAY
# =========================================================
movie_data = df[df["title"] == selected_movie].iloc[0]
movie_poster = safe_image(movie_data["poster_url"])

st.markdown("---")
st.subheader("Selected Movie")

col1, col2 = st.columns([1, 3])

with col1:
    st.image(movie_poster, width=180)

with col2:
    st.markdown(f"### {selected_movie}")


# =========================================================
# 7. RECOMMENDATION ENGINE
# =========================================================
if st.button("Show Recommendations"):

    index = df[df["title"] == selected_movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []
    recommended_posters = []

    for i in range(1, 6):
        idx = distances[i][0]

        recommended_movies.append(df.iloc[idx].title)
        recommended_posters.append(
            safe_image(df.iloc[idx].poster_url)
        )


    # =====================================================
    # 8. OUTPUT SECTION
    # =====================================================
    st.markdown("---")
    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.image(recommended_posters[i], use_container_width=True)
            st.write(recommended_movies[i])

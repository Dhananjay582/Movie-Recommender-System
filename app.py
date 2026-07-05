import streamlit as st
import pickle
import pandas as pd
import requests
import time

def fetch_poster(movie_id):
    api_key = st.secrets["TMDB_API_KEY"]
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    for attempt in range(3):
        try:
            data = requests.get(url,timeout=10)
            data.raise_for_status()
            data = data.json()
            poster_path = data.get('poster_path')
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            if not poster_path:
                return "https://via.placeholder.com/500x750?text=No+Image"

            return full_path
        except requests.exceptions.RequestException as e:
            print(f"⚠ Attempt {attempt + 1}: Error fetching poster for {movie_id} → {e}")
            time.sleep(1)  # wait 1 second before retry
    return "https://via.placeholder.com/500x750?text=Connection+Error"





st.title('Movie Recommender System')
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


movie_list = movies['title'].values
selected_movie_name = st.selectbox(
    "Select a Movie",
    movie_list
)


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters



if st.button('Show Recommendation'):
    recommended_movies, recommended_movies_posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for idx,col in enumerate(cols):
        with col:
            st.text(recommended_movies[idx])
            st.image(recommended_movies_posters[idx])
else :
        st.write("achi movie dalo")

import pickle
import streamlit as st
import requests
import pandas as pd

##def fetch_poster(movie_id):
    #url = "https://api.themoviedb.org/3/movie/{}?api_key=fa29f69fbeca6d1b2424d2917eac435e&language=en-US".format(movie_id)
    #data = requests.get(url)
    #data = data.json()
    #poster_path = data['poster_path']
    #full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    #return full_path
#https://img.omdbapi.com/?i=tt1375666&apikey=d267fced
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3d951c8ce2f089d4a69b38849b9225f8&language=en-US"
    try:
        response = requests.get(url)
        response.raise_for_status()  # raise HTTPError if status != 200
        data = response.json()
        poster_path = data.get('poster_path')
        #st.write(poster_path)
        #st.write(data)
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path 
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie_id {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        #st.write(movie_id)
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
#movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies= pd.read_pickle("movie_list.pkl")
similarity =pd.read_pickle('similarity.pkl')
#similarity = pickle.load(open('similarity.pkl','rb'))


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

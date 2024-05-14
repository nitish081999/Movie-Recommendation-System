import pandas as pd
import streamlit as st
import pickle
import pandas
import requests
st.title('Movie Recommender System')


def fetch_poster(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=794f32f9e311a3d2f8905b6df05a12d3&language=en-US'.format(movie_id))
    data=response.json()
    poster_path=data.get('poster_path',None)
    if poster_path:
        return 'https://image.tmdb.org/t/p/w500/'+poster_path
    else:
        return None
def recommend(movie):
    movie_idx=movies[movies['title']==movie].index[0]
    distance=similarity[movie_idx]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].id

        poster_url=fetch_poster(movie_id)
        # fetch poster from api
        if poster_url:
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_poster.append(poster_url)
        else:
            continue
    return recommended_movies,recommended_movies_poster

movies_list=pickle.load(open('movie_dict.pkl','rb'))

similarity=pickle.load(open('similarity.pkl','rb'))

movies=pd.DataFrame(movies_list)
selected_movie_name=st.selectbox(
    'How would you like to be contacted ?',
    movies['title'].values
)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
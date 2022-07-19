import pickle
import streamlit as st
import requests


page_bg_img = '''
<style>
      .stApp {
  background-image: url("https://c4.wallpaperflare.com/wallpaper/531/417/272/pixar-animation-studios-toy-story-a-bug-s-life-toy-story-2-wallpaper-preview.jpg");
  background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


title = '<p style="font-family:Candara; color:White; font-size: 42px;">Movie Recommendation System</p>'
st.markdown(title,unsafe_allow_html=True)
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
sub_title = '<p style="font-family:Dungeon; color:Orange; font-size: 20px;">Type a Movie Name or pickup from drop down menu</p>'
st.markdown(sub_title,unsafe_allow_html=True)
selected_movie = st.selectbox("",movie_list)

if st.button('Get Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
    with col2:
        st.image(recommended_movie_posters[1])
    with col3:
        st.image(recommended_movie_posters[2])
    with col4:
        st.image(recommended_movie_posters[3])
    with col5:
        st.image(recommended_movie_posters[4])



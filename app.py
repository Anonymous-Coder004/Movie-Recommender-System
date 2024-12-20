
import streamlit as st
import pickle
import pandas as pd
import requests
pg_bg="""
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://imgs.search.brave.com/-lZAVLXP-sX-pGwGIci9PhmLqj8abWCqrYy40tTg1aI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJiYXQuY29t/L2ltZy80ODI2NjYt/ZHlzdG9waWFuLWZ1/dHVyaXN0aWMtd2Fs/bHBhcGVyLWFuaW1l/LXNjZW5lcnktd2Fs/bHBhcGVyLXNjZW5l/cnktd2FsbHBhcGVy/LWFuaW1lLXNjZW5l/cnkuanBn");
background-size: cover;
}
[data-testid="stHeader"]{
background-color:rgba(0,0,0,0);
}
</style>
"""
st.markdown(pg_bg,unsafe_allow_html=True)
def fetch_p(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8e2eef82623a5bc2634afe9fa204bb26'.format(movie_id))
    data=response.json()
    return  "http://image.tmdb.org/t/p/w500"+data['poster_path']
def rec(movie):
    ind=movies[movies['title']==movie].index[0]
    dis=sim[ind]
    mlist=sorted(list(enumerate(dis)),reverse=True,key=lambda x:x[1])[1:6]
    recc=[]
    reccp=[]
    for i in mlist:
        m_id=movies.iloc[i[0]].movie_id
        recc.append(movies.iloc[i[0]].title)
        reccp.append(fetch_p(m_id))
    return recc,reccp
st.title("Movie Recommender System")
movie_d=pickle.load(open('movie_d.pkl','rb'))
sim=pickle.load(open('simm.pkl','rb'))
movies=pd.DataFrame(movie_d)
selected= st.selectbox(
    "Select a Movie that you have watched",
    movies['title'].values
)
if st.button("Recommend Movies"):
    names,posters=rec(selected)
    col1, col2, col3,col4,col5 = st.columns(5)
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



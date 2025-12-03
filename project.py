#페이지 별로 나올 장면 설정하는 코드
import streamlit as st  #Streamlit 불러오기

pages=[st.Page("home.py",title="홈"),
        st.Page("playground.py",title="연습 공간"),
        st.Page("video.py",title="강의 영상")]

pg=st.navigation(pages)
pg.run()
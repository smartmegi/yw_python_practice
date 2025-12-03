import streamlit as st
st.title("Python 연습")
st.markdown(
'''이것은 Python학습을 위해 제작된 페이지입니다.  
:rainbow[양운고 10214 이관수]가 만들었으며, 강의 영상 링크는 \"나도코딩\"님의 1분 파이썬 영상입니다.''')

if st.button("SNOW",type="tertiary"):
    st.snow()
#코드1 안나옴 수정하기
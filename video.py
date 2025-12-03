import streamlit as st  #Streamlit 불러오기
def vwrite(title,*link):  #강의 영상을 나타낼 때 쉽게 쓸 수 있도록(vwrite(제목, 링크) 형식으로) 만든 함수
    st.write(title)  #제목 쓰기
    for i in link:  #link를 순서대로 i에 하나씩 넣으면서
        st.write(i)  #i를 쓰기

st.title("강의 영상")  #제목
with st.expander("자료형"):  #자료형이라는 묶음 안에
    vwrite("* 자료형","https://www.youtube.com/watch?v=kr-uIzwVcv8")  #자료형 영상
    vwrite("* 자료형 변환","https://www.youtube.com/watch?v=9CqIHmzP-Q0")  #자료형 변환 영상
with st.expander("변수"):  #변수라는 묶음 안에
    vwrite("* 변수","https://www.youtube.com/watch?v=9pMq-EjIalo")  #변수 영상
with st.expander("연산"):  #연산이라는 묶음 안에
    vwrite("* 연산자","https://www.youtube.com/watch?v=XlrRQXP9GD0")  #연산자 영상
    vwrite("* 불리언(참, 거짓)","https://www.youtube.com/watch?v=LUCpzIZJ4YA")  #불리언 영상
    vwrite("* 연산 후 대입","https://www.youtube.com/watch?v=j06b2RdJB-s")  #연산과 대입 영상
#아래에는 같은 형식이어서 설명은 여기까지
with st.expander("리스트"):
    vwrite("* 리스트 만들기","https://www.youtube.com/watch?v=uxf4cTeonY4")
    vwrite("* 리스트에서 자료 꺼내기","https://www.youtube.com/watch?v=KEhPKBpPJvI")
with st.expander("조건문"):
    vwrite("* if, if else 조건문","https://www.youtube.com/watch?v=N92M3WaLbH0")
    vwrite("* elif 조건문","https://www.youtube.com/watch?v=J9srd8Mfoyc")
    vwrite("* if 중첩","https://www.youtube.com/watch?v=eGEg98j4JQw")
with st.expander("반복문"):
    vwrite("* for 반복문","for : https://www.youtube.com/watch?v=uecZdRyiFNA","range : https://www.youtube.com/watch?v=sJrv25QnRFk","for 활용 : https://www.youtube.com/watch?v=93_2E88rvDY")
    vwrite("* while 반복문","https://www.youtube.com/watch?v=HgylrKz95tQ")
    vwrite("* 반복문 심화","break : https://www.youtube.com/watch?v=9m93pYaT0r","continue : https://www.youtube.com/watch?v=ACTM_7mwbr0")
with st.expander("함수"):
    vwrite("* 함수","함수란? : https://www.youtube.com/watch?v=YTEr1VTbe4Q","전달값 : https://www.youtube.com/watch?v=GCMrf7wThT4","반환값 : https://www.youtube.com/watch?v=DhBNQ4RqQQY")
    vwrite("* 함수의 변수","지역변수 : https://www.youtube.com/watch?v=bLJf0rnEdqU","전역변수 : https://www.youtube.com/watch?v=lMeKbV8FOX8")
vwrite("전체 영상","https://www.youtube.com/playlist?list=PLMsa_0kAjjrcxiSJnHNfzBN71D3zpYtkX")
st.write("> 혹시 저작권에 걸릴까봐 링크만 넣었습니다.")  #링크만 넣은 이유를 설명하는 글 작성
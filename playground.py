import streamlit as st  #Streamlit 불러오기
import io  #입출력 시스템 불러오기
import contextlib  #글자를 한번에 출력되지 않고 저장할 수 있게 해주는 redirect_stdout을 사용할 수 있도록 불러오기
import html  #웹과 관련된 도구들을 불러오기

#변수들이 없을 경우 그 변수들의 초기값 설정(한 번 정해진 후엔 실행 X)(일반 변수와 다르게 페이지를 이동해도 유지됨)
if "code1" not in st.session_state:
    st.session_state["code1"]="""print("Hello, World!")"""
if "code2" not in st.session_state:
    st.session_state["code2"]="""print("Hello, World!")"""
if "code3" not in st.session_state:
    st.session_state["code3"]="""print("Hello, World!")"""
if "code" not in st.session_state:
    st.session_state["code"]=st.session_state["code1"]
if "l_type" not in st.session_state:
    st.session_state["l_type"]="primary"
if "m_type" not in st.session_state:
    st.session_state["m_type"]="secondary"
if "r_type" not in st.session_state:
    st.session_state["r_type"]="secondary"
if "code_page" not in st.session_state:
    st.session_state["code_page"] = 0
if "special_text" not in st.session_state:
    if st.session_state["code_page"]==0:
        st.session_state["special_text"]=st.session_state["code1"]
    elif st.session_state["code_page"]==1:
        st.session_state["special_text"]=st.session_state["code2"]
    else:
        st.session_state["special_text"]=st.session_state["code3"]

#왼쪽의 code1버튼을 누르면 작동하는 코드
def l_click():
    prev = st.session_state["code_page"]  #누르기 전 코드의 페이지를 임시로 저장
    if prev == 1:
        st.session_state["code2"] = st.session_state["special_text"]
    elif prev == 2:
        st.session_state["code3"] = st.session_state["special_text"]  #이전 내용을 저장
    st.session_state["special_text"] = st.session_state["code1"]  #현재 나타내는 내용을 code1 내용으로 바꾸기
    st.session_state["l_type"] = "primary"  #왼쪽 버튼이 눌린 상태로 만들기
    st.session_state["m_type"] = "secondary"
    st.session_state["r_type"] = "secondary"  #나머지 버튼이 눌리지 않은 상태로 만들기
    st.session_state["code_page"] = 0

#"def l_click()"과 비슷하지만 가운데 버튼을 누르면 작동하는 코드
def m_click():
    prev = st.session_state["code_page"]
    if prev == 0:
        st.session_state["code1"] = st.session_state["special_text"]
    elif prev == 2:
        st.session_state["code3"] = st.session_state["special_text"]
    st.session_state["special_text"] = st.session_state["code2"]
    st.session_state["l_type"] = "secondary"
    st.session_state["m_type"] = "primary"
    st.session_state["r_type"] = "secondary"
    st.session_state["code_page"] = 1

#"def l_click()"과 비슷하지만 오른쪽 버튼을 누르면 작동하는 코드
def r_click():
    prev = st.session_state["code_page"]
    if prev == 0:
        st.session_state["code1"] = st.session_state["special_text"]
    elif prev == 1:
        st.session_state["code2"] = st.session_state["special_text"]
    st.session_state["special_text"] = st.session_state["code3"]
    st.session_state["l_type"] = "secondary"
    st.session_state["m_type"] = "secondary"
    st.session_state["r_type"] = "primary"
    st.session_state["code_page"] = 2

st.title("연습 공간")  #연습공간이라는 제목을 띄우기

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic+Coding&display=swap" rel="stylesheet">
<style>
div[data-testid="stTextArea"] textarea {
    font-family: 'Nanum Gothic Coding', monospace !important;
    font-size: 18px !important;
}

div.stMarkdown > pre, div.stMarkdown > code {
    font-family: 'Nanum Gothic Coding', monospace !important;
    font-size: 20px !important;
}
</style>
""", unsafe_allow_html=True)  #코딩에 맞는 글꼴 구글에서 불러오기

st.markdown("""
<style>
div[data-testid="stButton"] button {
    width: 100% !important;
}
</style>
""", unsafe_allow_html=True)  #앞으로 나올 버튼이 가로로 꽉 차게 해주는 코드(였지만 잘 실행 안됨)

l,m,r=st.columns(3)
with l:
    st.button("코드 1",type=st.session_state["l_type"],on_click=l_click)  #왼쪽 버튼
with m:
    st.button("코드 2",type=st.session_state["m_type"],on_click=m_click)  #가운데 버튼
with r:
    st.button("코드 3",type=st.session_state["r_type"],on_click=r_click)  #오른쪽 버튼

user_code = st.text_area("Python 코드를 입력하세요:", height=400, key='special_text',placeholder="코드를 입력하세요...")  #코드 입력 받고 user_code에 저장

"※ input과 같은 입력은 사용 불가 합니다"
"※ 맨 첫 번째 줄의 출력이 공백으로 실행된다면 그 공백은 나오지 않습니다."  #주의사항 안내

if st.button("실행"):  #실행할 때
    buffer = io.StringIO()
    st.session_state["code"] = user_code  #user_code를 code라는 변수로 옮김
    try:
        with contextlib.redirect_stdout(buffer):  #contextlib을 활용하여 임시 저장
            exec(user_code, {})  #코드 실행 결과를 출력
        st.success("코드 실행 성공")  #성공했다는 알림
        st.caption("실행 결과")  #'실행 결과'라는 제목을 붙임
        st.code(buffer.getvalue(), language=None)  #코드 실행 결과를 나타냄

    except Exception as e: #에러가 난다면

        st.error(f"에러 발생 : {e}")  #에러 발생이라는 문구와 함께 무슨 에러인지 출력

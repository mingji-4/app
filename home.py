import streamlit as st

st.markdown("<h1 style='text-align: center;'>📊범죄율 시각화 홈페이지📊</h1>",
            unsafe_allow_html=True)

with st.form("Form 1"):
    col1, col2 = st.columns(2)
    
    f_name = col1.text_input("Frist name", max_chars=10)
    l_name = col2.text_input("Last name", max_chars=10)
    email = st.text_input('Email address')
    password = st.text_input("password", type="password")
    
    if st.form_submit_button('가입하기'):
        if f_name=="" or l_name=="" or email=="" or password=="":
            st.warning("빈칸을 채워주세요.")
        else:
            st.success("Sumbitted sussessfully")

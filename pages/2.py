import streamlit as st

st.markdown("<h1 style='text-align: center;'>📝 Todo List</h1>",
            unsafe_allow_html=True)

if 'todos' not in st.session_state:
    st.session_state.todos = []

new_todo = st.text_input("할 일 입력:")

if st.button("추가"):
    if new_todo:
        st.session_state.todos.append(new_todo)
        st.success("할 일이 추가되었습니다!")
    else:
        st.warning("할 일을 입력하세요.")

if st.session_state.todos:
    st.subheader("현재 할 일 목록:")
    checked_todos = st.text("완료된 항목")
    todos_to_display = st.session_state.todos

    completed = st.text("체크된 항목 삭제하기")
    
    if completed:
        for i, todo in enumerate(todos_to_display):
            checked = st.checkbox(todo, key=i)
            if checked:
                st.session_state.todos.pop(i)
                st.success(f"{todo}가 삭제되었습니다!")

if st.button("모두 삭제"):
    st.session_state.todos.clear()
    st.success("모든 할 일이 삭제되었습니다.")
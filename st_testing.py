import streamlit as st
if "press" not in st.session_state:
    st.session_state["press"]=False
def lll():
    if st.session_state["ll"] == None:
        st.session_state["press"] = False
    else:
        st.session_state["press"] = True
st.selectbox("dssd",key="ll",options=[None]+["yes","no"],on_change=lll,format_func=lambda x :'select' if x==None else x)
v=st.button("pp")
if v:
    st.write(st.session_state["ll"],st.session_state["press"])
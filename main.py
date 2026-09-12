import streamlit as st
import time

st.set_page_config(layout="wide")
st.title(":orange[**STUDY**] TIMER", text_alignment="center")

if "running" not in st.session_state:
    st.session_state.running = False

if "start_time" not in st.session_state:
    st.session_state.start_time = None

if st.button("Start Timer"):
    st.session_state.running = True
    st.session_state.start_time = time.time()

if st.button("Stop Timer"):
    st.session_state.running = False
    stopped = int(time.time()-st.session_state.start_time)
    hours = stopped // 3600
    minutes = (stopped % 3600) // 60
    seconds = stopped % 60
    st.header(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

if st.button("Pause"):
    st.session_state.running = False
    st.session_state.paused = time.time()
    paused = int(time.time() - st.session_state.start_time)
    hours = paused // 3600
    minutes = (paused % 3600) // 60
    seconds = paused % 60
    st.header(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

if st.button("Resume"):
    st.session_state.running = True
    resume = int(st.session_state.paused)
    hours = resume // 3600
    minutes = (resume % 3600) // 60
    seconds = resume % 60
    st.header(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

@st.fragment(run_every=1)
def timer():
    if st.session_state.running:
        elapsed = int(time.time() - st.session_state.start_time)
        hours = elapsed // 3600
        minutes = (elapsed % 3600) // 60
        seconds = elapsed % 60
        st.header(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

timer()
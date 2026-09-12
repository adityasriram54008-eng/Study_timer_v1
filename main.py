import streamlit as st
import time

st.set_page_config(layout="wide")
st.title(":orange[**STUDY**] TIMER", text_alignment="center")

with st.container(border=True):
    if "running" not in st.session_state:
        st.session_state.running = False

    if "start_time" not in st.session_state:
        st.session_state.start_time = None

    timer_display = st.empty()

    if st.button("Start Timer"):
        st.session_state.running = True
        st.session_state.start_time = time.time()

    if "paused" not in st.session_state:
        st.session_state.paused = 0

    if st.button("Pause/Resume"):
        if st.session_state.running:
            st.session_state.running = False
            stopped = int(time.time() - st.session_state.start_time)
            st.session_state.paused = stopped
            hours = stopped // 3600
            minutes = (stopped % 3600) // 60
            seconds = stopped % 60
            timer_display.header(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        else:
            st.session_state.running = True
            st.session_state.start_time = (time.time() - st.session_state.paused)

    if st.button("Stop Timer"):
        st.session_state.running = False
        stopped = int(time.time() - st.session_state.start_time)
        hours = stopped // 3600
        minutes = (stopped % 3600) // 60
        seconds = stopped % 60
        timer_display.header(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    if st.button("Reset Timer"):
        st.session_state.running = False
        st.session_state.start_time = time.time() - time.time()

    @st.fragment(run_every=1)
    def timer():
        if st.session_state.running:
            elapsed = int(time.time() - st.session_state.start_time)
            hours = elapsed // 3600
            minutes = (elapsed % 3600) // 60
            seconds = elapsed % 60
            timer_display.header(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    timer()
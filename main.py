import streamlit as st
import time

st.set_page_config(layout="wide")
st.title(":orange[**STUDY**] TIMER", text_alignment="center")

st.text("\n")
st.text("\n")
st.text("\n")
st.text("\n")

tab1, tab2 = st.tabs(["STOPWATCH","POMODORO"])

with tab1:
    with st.container( horizontal_alignment="center", width = "stretch"):

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
                timer_display.header(f"{hours:02d}:{minutes:02d}:{seconds:02d}", text_alignment="center")

            else:
                st.session_state.running = True
                st.session_state.start_time = (time.time() - st.session_state.paused)

        if st.button("Stop Timer"):
            st.session_state.running = False
            stopped = int(time.time() - st.session_state.start_time)
            hours = stopped // 3600
            minutes = (stopped % 3600) // 60
            seconds = stopped % 60
            timer_display.header(f"{hours:02d}:{minutes:02d}:{seconds:02d}", text_alignment="center")

        if st.button("Reset Timer"):
            st.session_state.running = False
            st.session_state.start_time = 0
            st.session_state.paused = 0

        @st.fragment(run_every=1)
        def timer():
            if st.session_state.running:
                elapsed = int(time.time() - st.session_state.start_time)
                hours = elapsed // 3600
                minutes = (elapsed % 3600) // 60
                seconds = elapsed % 60
                timer_display.header(f"{hours:02d}:{minutes:02d}:{seconds:02d}",text_alignment="center")

        timer()

with tab2:

    duration = 10
    break_duration = 5

    with st.container(horizontal_alignment="center", width="stretch"):

        if "pomo_running" not in st.session_state:
            st.session_state.pomo_running = False

        if "pomo_start_time" not in st.session_state:
            st.session_state.pomo_start_time = None

        if "pomo_phase" not in st.session_state:
            st.session_state.pomo_phase = "pomodoro"

        if "pomo_paused" not in st.session_state:
            st.session_state.pomo_paused = duration

        pomo_timer_display = st.empty()

        if st.button("Start"):
            st.session_state.pomo_running = True
            st.session_state.pomo_phase = "pomodoro"
            st.session_state.pomo_start_time = time.time()

        if st.button("Pause or Resume"):
            if st.session_state.pomo_running:
                st.session_state.pomo_running = False
                if st.session_state.pomo_phase == "pomodoro":
                    elapsed = int(time.time() - st.session_state.pomo_start_time)
                    remaining = duration - elapsed
                    minutes = remaining // 60
                    seconds = remaining % 60
                    pomo_timer_display.header(f"{minutes:02d}:{seconds:02d}", text_alignment="center")

                else:
                    elapsed = int(time.time() - st.session_state.pomo_start_time)
                    remaining = break_duration - elapsed
                    minutes = remaining // 60
                    seconds = remaining % 60
                    pomo_timer_display.header(f"{minutes:02d}:{seconds:02d}", text_alignment="center")
                st.session_state.pomo_paused = remaining


            else:
                st.session_state.pomo_running = True
                if st.session_state.pomo_phase == "pomodoro":
                    st.session_state.pomo_start_time = (time.time() - (duration - st.session_state.pomo_paused))
                else:
                    st.session_state.pomo_start_time = (time.time() - (break_duration - st.session_state.pomo_paused))

        if st.button("Stop"):
            st.session_state.pomo_running = False

        if st.button("Reset"):
            st.session_state.pomo_running = False
            st.session_state.pomo_phase = "pomodoro"
            st.session_state.pomo_start_time = None
            st.session_state.pomo_paused = duration

        @st.fragment(run_every=1)
        def timerr():
            if st.session_state.pomo_running:

                elapsed = int(time.time() - st.session_state.pomo_start_time)
                if st.session_state.pomo_phase == "pomodoro":
                    remaining = duration - elapsed
                else:
                    remaining = break_duration - elapsed

                if remaining <= 0:
                    remaining = 0
                    st.session_state.pomo_running = False
                    st.balloons()
                    if st.session_state.pomo_phase == "pomodoro":
                        st.session_state.pomo_phase = "break"
                        st.session_state.pomo_paused = break_duration
                    else:
                        st.session_state.pomo_phase = "pomodoro"
                        st.session_state.pomo_paused = duration
                    st.session_state.pomo_start_time = time.time()
                    st.session_state.pomo_running = True
                minutes = remaining // 60
                seconds = remaining % 60
                pomo_timer_display.header(f"{minutes:02d}:{seconds:02d}",text_alignment="center")

        timerr()

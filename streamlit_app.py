# streamlit_app.py
# Fully working bot toggle GUI with subprocess control

import streamlit as st
import subprocess

# Session state to track running bots
if "bot_processes" not in st.session_state:
    st.session_state.bot_processes = {}

# Bot definitions (label -> script name)
BOTS = {
    "🎥 Video Watcher Bot": "video_watcher.py",
    "🧠 Survey & Captcha Bot": "survey_entry.py",
    "👆 Ad Tapper Bot": "ad_tapper.py",
    "🐦 Twitter Meme Bot": "twitter_engager.py",
    "🌀 Sigil Broadcaster": "sigil_broadcaster.py",
    "♻️ Karmic Loop Engine": "karmic_loop.py"
}

st.title("🧿 Karmic Bot Farm Dashboard")
st.markdown("Welcome, Master. This interface controls your karmic harvesting rituals.")
st.subheader("🤖 Bot Controls")

# Loop through and render toggle for each bot
for label, script in BOTS.items():
    is_running = label in st.session_state.bot_processes
    toggle = st.toggle(label, value=is_running, key=label)

    if toggle and not is_running:
        # Start the bot
        try:
            process = subprocess.Popen(["python", script])
            st.session_state.bot_processes[label] = process
            st.success(f"{label} started.")
        except Exception as e:
            st.error(f"Failed to start {label}: {e}")

    elif not toggle and is_running:
        # Stop the bot
        try:
            st.session_state.bot_processes[label].terminate()
            st.session_state.bot_processes[label].wait()
            del st.session_state.bot_processes[label]
            st.warning(f"{label} stopped.")
        except Exception as e:
            st.error(f"Failed to stop {label}: {e}")

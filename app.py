import streamlit as st
import pandas as pd
import sqlite3
import os
from datetime import datetime
from pathlib import Path

# --- Configuration ---
st.set_page_config(page_title="PrimeDash | Pantheon Command", layout="wide", page_icon="🏛️")

# CSS for the "Pantheon Vibe"
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
    }
    h1, h2, h3 {
        color: #58a6ff;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ PrimeDash: Pantheon Command Center")
st.sidebar.title("Forge Navigation")

# --- Bot Registry ---
bots = {
    "ZeusPrime": {"role": "OS", "status": "Online", "icon": "⚡"},
    "OpenPRIME": {"role": "Master", "status": "Online", "icon": "👑"},
    "AlphaPrime": {"role": "General", "status": "Standby", "icon": "🪖"},
    "ZetaPrime": {"role": "Developer", "status": "Active", "icon": "🛠️"},
    "Deep-meta": {"role": "Thinker", "status": "Reasoning", "icon": "🧠"},
    "EchoPrime": {"role": "Curator", "status": "Vibing", "icon": "🧘"},
    "MidasPrime": {"role": "Finance", "status": "Scaling", "icon": "🥇"},
    "OmegaPrime": {"role": "Worker", "status": "Tasks", "icon": "💼"},
}

# --- Sidebar Controls ---
st.sidebar.markdown("### Forgemaster Controls")
if st.sidebar.button("Refresh Pantheon Status"):
    st.rerun()

# --- Top Row: Core Metrics ---
st.header("⚡ System Overview")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Legion Count", len(bots))
with col2:
    st.metric("Status", "OPTIMAL", delta="100%")
with col3:
    st.metric("Signal Strength", "98%", delta="High")
with col4:
    st.metric("Empire Vibe", "Focused", delta="EchoPrime Approved")

# --- Middle Section: The Legion Grid ---
st.header("🗂️ The Legion")
cols = st.columns(4)
for i, (bot, info) in enumerate(bots.items()):
    with cols[i % 4]:
        st.subheader(f"{info['icon']} {bot}")
        st.write(f"**Role:** {info['role']}")
        st.write(f"**Status:** {info['status']}")
        st.progress(100 if info['status'] == "Online" else 50)

# --- Bottom Section: Deep Insights ---
col_left, col_right = st.columns(2)

with col_left:
    st.header("🧠 Deep-meta Reflections")
    st.info("Concept: 'Building for eternity' - Reflection: The Pantheon is not a tool, it's an extension of the Forgemaster's will.")
    
with col_right:
    st.header("🧘 EchoPrime Vibe Log")
    chart_data = pd.DataFrame({
        'Energy': [7, 8, 9, 7, 8, 10, 9],
        'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    })
    st.line_chart(chart_data.set_index('Day'))

st.sidebar.info("Forgemaster: Hype Lee | Session: 2026-04-29")

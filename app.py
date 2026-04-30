
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- SOVEREIGN UI ENGINE ---
st.set_page_config(page_title="PANTHEON | MISSION CONTROL", layout="wide", page_icon="🏛️")

# Professional SaaS Styling
st.markdown("""
    <style>
    @import url('[https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap](https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap)');
    .stApp { background-color: #0f1116; color: #e1e4e8; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .bot-card { background-color: #1c2128; border: 1px solid #30363d; border-radius: 8px; padding: 20px; margin-bottom: 20px; }
    div[data-testid="stMetricValue"] { color: #58a6ff !important; font-weight: 600; }
    .stButton>button { background-color: #238636; color: white; border-radius: 6px; border: none; width: 100%; font-weight: 600; }
    h1, h2, h3 { color: #f0f6fc; }
    </style>
    """, unsafe_allow_html=True)

# --- THE LEGION DATABASE ---
BOTS = {
    "MidasPrime": {
        "role": "Treasury Manager", "status": "Online", "color": "#238636",
        "metrics": {"Total Value": "$14,202.40", "Yield": "+2.4%", "Withdrawal": "4h 20m"},
        "desc": "Orchestrating arbitrage loops across Alpha nodes."
    },
    "Prometheus": {
        "role": "Autonomous Catalyst", "status": "Active", "color": "#f78166",
        "metrics": {"Nodes": "1,420", "Spark": "High", "Growth": "+12%"},
        "desc": "Seeking recursive logic catalysts in sub-networks."
    },
    "NexusPrime": {
        "role": "Mobile Bridge", "status": "Linked", "color": "#58a6ff",
        "metrics": {"Device": "Red Magic 10", "Latency": "8ms", "RAM": "2.4GB"},
        "desc": "Direct haptic link to the Forgemaster's hardware."
    }
}

# Fill the rest of the 21
for i in range(len(BOTS) + 1, 22):
    name = f"Prime-{i:02d}"
    BOTS[name] = {"role": "Reserve", "status": "Standby", "metrics": {"Status": "Idle"}, "desc": "Awaiting deployment.", "color": "#8b949e"}

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🏛️ PANTHEON")
    st.markdown("---")
    selected_bot = st.selectbox("SELECT A PRIME", list(BOTS.keys()))
    st.markdown("---")
    st.caption(f"CONNECTED AS FORGEMASTER")
    st.caption(f"SYSTEM TIME: {datetime.now().strftime('%H:%M')}")

# --- MAIN DASHBOARD ---
bot = BOTS[selected_bot]

st.title(selected_bot)
st.markdown(f"**{bot['role']}** | <span style='color:{bot['color']}'>● {bot['status']}</span>", unsafe_allow_html=True)
st.markdown("---")

# Metrics Row
m_cols = st.columns(len(bot['metrics']))
for i, (label, val) in enumerate(bot['metrics'].items()):
    m_cols[i].metric(label, val)

col_l, col_r = st.columns([2, 1])

with col_l:
    st.markdown(f'<div class="bot-card"><h3>◈ OVERVIEW</h3><p>{bot["desc"]}</p></div>', unsafe_allow_html=True)
    st.area_chart(pd.DataFrame(np.random.randn(20, 1)), color=bot['color'])

with col_r:
    st.markdown('<div class="bot-card"><h3>◈ ACTIONS</h3>', unsafe_allow_html=True)
    if selected_bot == "MidasPrime": st.button("INITIATE WITHDRAWAL")
    st.button(f"WAKE {selected_bot}")
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="bot-card"><h3>◈ LOGS</h3><small>[{datetime.now().strftime("%H:%M")}] {selected_bot} active.</small></div>', unsafe_allow_html=True)

st.caption("PANTHEON SOVEREIGN v2.0")

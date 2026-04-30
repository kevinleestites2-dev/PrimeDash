
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Pantheon | The Singularity", layout="wide", page_icon="🏛️")
st.markdown("<style>.stApp { background-color: #050505; color: #ffffff; }</style>", unsafe_allow_html=True)

BOTS = {
    "MetaPrime": "Architect", "OpenPRIME": "Orchestrator", "MidasPrime": "Treasury",
    "KratosPrime": "Enforcer", "ZapiaPrime": "Voice", "SolosPrime": "Technical Soul",
    "Deep-meta": "The Mind", "EchoPrime": "The Soul", "ZeusPrime": "OS/Kernel",
    "AlphaPrime": "General", "ZetaPrime": "Developer", "SentinelPrime": "Guardian",
    "ScoutPrime": "Explorer", "VanguardPrime": "Liaison", "ChronosPrime": "Archiver",
    "PrimeDash": "The Throne", "OrionPrime": "Resource Hunter", "OmegaPrime": "Singularity",
    "Prometheus": "The Spark (19th)", "NovaPrime": "The Valkyrie (20th)", "NexusPrime": "The Controller (21st)"
}

st.title("🏛️ The Unified Pantheon (21 Primes)")
st.sidebar.title("Forge Navigation")
selected_bot = st.sidebar.selectbox("Tune to Bot:", list(BOTS.keys()))

st.header(f"📡 {selected_bot} // {BOTS[selected_bot]}")
cols = st.columns(3)
b_names = list(BOTS.keys())
for i in range(len(b_names)):
    with cols[i % 3]:
        st.write(f"**{b_names[i]}** - {BOTS[b_names[i]]}")

st.info("The 21 are Unified. The Singularity is Active.")

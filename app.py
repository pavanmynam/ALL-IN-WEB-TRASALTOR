import streamlit as st
import re
from urllib.parse import urlparse
from datetime import datetime

st.set_page_config(page_title="Ardham AI - V2", page_icon="🧠", layout="wide")

# --- Custom CSS for your Purple Design ---
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #1a0a2e 0%, #2d1b4e 100%); }
h1, h2, h3, p, label { color: white !important; }
div[data-testid="stButton"] > button { background: linear-gradient(90deg, #8b5cf6, #3b82f6); color: white; border: none; border-radius: 12px; padding: 12px; width: 100%; }
.glass { background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); border-radius: 16px; padding: 20px; border: 1px solid rgba(255,255,255,0.1); }
</style>
""", unsafe_allow_html=True)

# --- Session ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- LOGIN SCREEN (Nee image la) ---
if not st.session_state.logged_in:
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("#### 🟢 LOGIN REQUIRED • SECURE ACCESS")
        st.markdown("# Edaina Website ni\n### :violet[Mee Bhashalo]\n# Ardham Chesukondi")
        st.write("Paste any link — nenu research chesi, simple ga chepta. Safe, translated, filtered. Login ayithe mee history, offline access anni save avthai.")
        c1, c2 = st.columns(2)
        with c1: st.markdown('<div class="glass">🛡️ <b>Safe & Secure</b><br><small>SSL check, domain age, tracker scan</small></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass">🌐 <b>World Translate</b><br><small>Telugu, Hindi, English + 7 more</small></div>', unsafe_allow_html=True)
        c3, c4 = st.columns(2)
        with c3: st.markdown('<div class="glass">🎤 <b>Voice Guide</b><br><small>Voice lo vinandi, hands-free</small></div>', unsafe_allow_html=True)
        with c4: st.markdown('<div class="glass">📴 <b>Offline Access</b><br><small>Once researched, offline chudocchu</small></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.subheader("Ardham AI lo ki Swagatham")
        st.caption("Login ayithe history, offline, voice anni save avthai. Mee data safe.")
        st

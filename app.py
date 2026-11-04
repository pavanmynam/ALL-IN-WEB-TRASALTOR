import streamlit as st
from urllib.parse import urlparse
import time

st.set_page_config(page_title="Ardham AI - Universal Explainer", page_icon="🧠", layout="wide")

# --- PREMIUM CSS - Nee image laga ---
st.markdown("""
<style>
/* Hide Streamlit default menu */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Background */
.stApp {
    background: #1A0A2E;
    background: linear-gradient(180deg, #1A0A2E 0%, #251240 100%);
}

/* Texts */
h1, h2, h3 { color: #FFFFFF !important; font-weight: 800 !important; }
p, span, label, small { color: #E5E7EB !important; }
.purple-text { color: #A78BFA !important; }

/* Glass Cards */
.glass-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 16px;
    padding: 18px 16px;
    margin-bottom: 14px;
    backdrop-filter: blur(8px);
}
.glass-card b { color: #fff; font-size: 14px; }
.glass-card small { color: #9CA3AF !important; font-size: 12px; }

/* Login Card */
.login-box {
    background: #241445;
    border: 1px solid #3B2A67;
    border-radius: 24px;
    padding: 28px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}

/* Buttons */
div[data-testid="stButton"] > button {
    border-radius: 12px !important;
    height: 48px;
    font-weight: 600;
    border: none;
}
div[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(90deg, #EF4444, #F87171) !important;
    color: white !important;
}

/* Input */
input {
    background: #FFFFFF !important;
    color: #111827 !important;
    border-radius: 12px !important;
    height: 48px !important;
}
</style>
""", unsafe_allow_html=True)

# Session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'phone' not in st.session_state:
    st.session_state.phone = ""

# ================= LOGIN SCREEN =================
if not st.session_state.logged_in:
    left, right = st.columns([1.15, 0.85], gap="large")

    with left:
        st.markdown("<div style='color:#22c55e;font-size:13px;font-weight:600;margin-bottom:20px'>🟢 LOGIN REQUIRED • SECURE ACCESS</div>", unsafe_allow_html=True)
        
        st.markdown("<h1 style='font-size:52px;line-height:1.1;margin-bottom:0'>Edaina Website ni</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:#6B7280 !important;font-size:22px;font-weight:400;margin-top:8px'>Mee Bhashalo</h2>", unsafe_allow_html=True)
        st.markdown("<h1 style='font-size:52px;line-height:1.1;margin-top:10px'>Ardham Chesukondi</h1>", unsafe_allow_html=True)
        
        st.markdown("<p style='color:#9CA3AF !important;margin-top:16px;font-size:14px'>Paste

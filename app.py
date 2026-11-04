import streamlit as st

st.set_page_config(page_title="Ardham AI", layout="wide")

st.markdown("""
<style>
.stApp { background: #1A0A2E; }
h1 { color: white !important; font-size: 3rem !important; }
.purple { color: #8B5CF6; }
.glass {
  background: rgba(255,255,255,0.07);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 16px;
  padding: 16px;
  margin-bottom: 12px;
}
.login-card {
  background: #241445;
  border-radius: 20px;
  padding: 24px;
  border: 1px solid #3a2a60;
}
</style>
""", unsafe_allow_html=True)

left, right = st.columns([1.1, 0.9])

with left:
    st.markdown("🟢 <span style='color:#22c55e;font-size:13px'>LOGIN REQUIRED • SECURE ACCESS</span>", unsafe_allow_html=True)
    st.markdown("# Edaina Website ni")
    st.markdown("<h3 class='purple'>Mee Bhashalo</h3>", unsafe_allow_html=True)
    st.markdown("# Ardham Chesukondi")
    st.caption("Paste any link — nenu research chesi, simple ga chepta. Safe, translated, filtered. Login ayithe mee history, offline access anni save avthai.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="glass">🛡️ <b>Safe & Secure</b><br><small>SSL check, domain age, tracker scan</small></div>', unsafe_allow_html=True)
        st.markdown('<div class="glass">🎙️ <b>Voice Guide</b><br><small>Voice lo vinandi, hands-free</small></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="glass">🌐 <b>World Translate</b><br><small>Telugu, Hindi, English + 7 more</small></div>', unsafe_allow_html=True)
        st.markdown('<div class="glass">📴 <b>Offline Access</b><br><small>Once researched, offline kuda chudocchu</small></div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown("### Ardham AI lo ki Swagatham")
    st.caption("Login ayithe history, offline, voice anni save avthai. Mee data safe.")
    
    st.button("🔵 Google tho Login Avvandi", use_container_width=True)
    st.markdown("<center style='color:#888;margin:10px'>— or —</center>", unsafe_allow_html=True)
    
    st.text_input("Phone", placeholder="98 765 43210", label_visibility="collapsed")
    col_a, col_b = st.columns([1,1])
    with col_a: st.button("OTP Pampinchu", use_container_width=True)
    with col_b: st.button("Login Avvandi →", type="primary", use_container_width=True)
    
    st.caption("✅ Secure • 🌐 Languages • ⚡ Fast AI")
    st.markdown('</div>', unsafe_allow_html=True)

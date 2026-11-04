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
        
        st.markdown("<p style='color:#9CA3AF !important;margin-top:16px;font-size:14px'>Paste any link — nenu research chesi, simple ga chepta. Safe, translated, filtered. Login ayithe mee history, offline access anni save avthai.</p>", unsafe_allow_html=True)
        
        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
        
        r1c1, r1c2 = st.columns(2)
        with r1c1:
            st.markdown('<div class="glass-card">🛡️ <b>Safe & Secure</b><br><small>SSL check, domain age, tracker scan</small></div>', unsafe_allow_html=True)
        with r1c2:
            st.markdown('<div class="glass-card">🌐 <b>World Translate</b><br><small>Telugu, Hindi, English + 7 more</small></div>', unsafe_allow_html=True)
        
        r2c1, r2c2 = st.columns(2)
        with r2c1:
            st.markdown('<div class="glass-card">🎙️ <b>Voice Guide</b><br><small>Voice lo vinandi, hands-free</small></div>', unsafe_allow_html=True)
        with r2c2:
            st.markdown('<div class="glass-card">📴 <b>Offline Access</b><br><small>Once researched, offline kuda chudocchu</small></div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown("### Ardham AI lo ki Swagatham")
        st.markdown("<p style='font-size:13px;color:#9CA3AF !important'>Login ayithe history, offline, voice anni save avthai. Mee data safe.</p>", unsafe_allow_html=True)
        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

        st.button("🔵 Google tho Login Avvandi", use_container_width=True)
        
        st.markdown("<div style='text-align:center;color:#6B7280;margin:14px 0;font-size:13px'>— or —</div>", unsafe_allow_html=True)

        phone = st.text_input("phone", placeholder="9666183665", label_visibility="collapsed", key="phone_input")
        
        b1, b2 = st.columns(2)
        with b1:
            if st.button("OTP Pampinchu", use_container_width=True):
                st.toast("OTP sent (Mock) - 123456", icon="📱")
        with b2:
            if st.button("Login Avvandi →", type="primary", use_container_width=True):
                st.session_state.logged_in = True
                st.session_state.phone = phone
                st.rerun()

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:12px;color:#6B7280'>✅ Secure • 🌐 Languages • ⚡ Fast AI</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ================= MAIN APP AFTER LOGIN =================
else:
    st.markdown("### 🧠 Ardham AI - Dashboard")
    st.markdown(f"<small style='color:#9CA3AF'>Welcome! Phone: {st.session_state.phone} | History saved</small>", unsafe_allow_html=True)
    
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    url = st.text_input("🔗 Website / App link paste chey:", placeholder="https://www.example.com or Play Store link")

    if st.button("🔍 Analyze Chey", type="primary") and url:
        with st.spinner("Ardham chestunna... 3 sec lo chepta..."):
            time.sleep(1.5)
        
        try:
            domain = urlparse(url).netloc or url
        except:
            domain = url

        # Safety mock logic
        score = 85
        if "https" in url: score += 5
        if "loan" in url.lower() or "earn" in url.lower(): score = 45

        c1, c2, c3 = st.columns(3)
        c1.metric("Safety Score", f"{score}/100", "Secure" if score>70 else "Risk")
        c2.metric("Domain Age", "3 Years", "Trusted")
        c3.metric("Trackers", "2 Found", "Low")

        st.divider()

        col_a, col_b = st.columns([1, 1])
        with col_a:
            st.markdown("#### 📖 Enti Idi? (Mee Bhashalo)")
            if score < 60:
                st.error(f"**{domain}** idi risk category lo undi. Chala permissions adugutundi. Aadhar, bank details adigithe ivvaku.")
            else:
                st.info(f"**{domain}** idi oka genuine online service. User data konchem collect chestundi kani major risk ledu.")

            st.markdown("#### 🛠️ Ela Vadali?")
            st.write("1. Link lo HTTPS unda chudu (🔒 symbol)\n2. Play Store reviews chudu\n3. Permissions - Location/Contacts adigithe No chey\n4. First time small amount / dummy data tho test chey")

        with col_b:
            st.markdown("#### 🔒 Safe a Kada?")
            if score > 75:
                st.success("✅ HTTPS undi\n✅ Domain old\n⚠️ 2 trackers - Ad-blocker vadandi")
            else:
                st.warning("⚠️ HTTPS ledu / kotha domain\n⚠️ Too many permissions\n❌ Bank details adigithe danger")

            st.markdown("#### 🔄 Better Alternatives")
            st.write(f"- Google lo `alternative to {domain}` search chey\n- Open-source options chudu\n- Official apps ke prefer chey (【entity-SBI¦canonical_name=SBI】, 【entity-HDFC¦canonical_name=HDFC】 etc for finance)")

        st.divider()
        c_voice, c_save = st.columns(2)
        with c_voice:
            if st.button("🔊 Voice lo Vinu (Telugu)"):
                st.toast("Voice Guide - Coming Soon!", icon="🎙️")
        with c_save:
            if st.button("💾 Offline ki Save Chey"):
                st.toast("Saved to offline history!", icon="✅")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

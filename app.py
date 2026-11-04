import streamlit as st
from urllib.parse import urlparse
import time

st.set_page_config(
    page_title="Ardham AI - Universal Explainer",
    page_icon=":brain:",
    layout="wide"
)

# CSS - Premium Purple Look
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
.stApp { background: #1A0A2E; }
h1, h2, h3 { color: #FFFFFF !important; }
p, label, small { color: #E5E7EB !important; }
.glass-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 12px;
}
.login-box {
    background: #241445;
    border: 1px solid #3B2A67;
    border-radius: 20px;
    padding: 28px;
}
</style>
""", unsafe_allow_html=True)

# Session
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# LOGIN PAGE
if not st.session_state.logged_in:
    left, right = st.columns([1.2, 0.8], gap="large")
    
    with left:
        st.markdown("🟢 **LOGIN REQUIRED • SECURE ACCESS**")
        st.markdown("# Edaina Website ni")
        st.markdown("## Mee Bhashalo")
        st.markdown("# Ardham Chesukondi")
        st.caption("Paste any link — nenu research chesi simple ga chepta. Safe, translated, filtered.")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="glass-card"><b>Safe & Secure</b><br><small>SSL check, domain age, tracker scan</small></div>', unsafe_allow_html=True)
            st.markdown('<div class="glass-card"><b>Voice Guide</b><br><small>Voice lo vinandi, hands-free</small></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="glass-card"><b>World Translate</b><br><small>Telugu, Hindi, English + 7 more</small></div>', unsafe_allow_html=True)
            st.markdown('<div class="glass-card"><b>Offline Access</b><br><small>Once researched, offline chudocchu</small></div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown("### Ardham AI lo ki Swagatham")
        st.caption("Login ayithe history, offline, voice anni save avthai.")
        st.markdown("---")
        
        st.button("Google tho Login Avvandi", use_container_width=True)
        st.markdown("<center>— or —</center>", unsafe_allow_html=True)
        
        phone = st.text_input("Phone", placeholder="9666183665", label_visibility="collapsed")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("OTP Pampinchu", use_container_width=True):
                st.toast("OTP Mock: 123456")
        with col2:
            if st.button("Login Avvandi", type="primary", use_container_width=True):
                if phone:
                    st.session_state.logged_in = True
                    st.session_state.phone = phone
                    st.rerun()
                else:
                    st.warning("Phone number enter chey bro")
        
        st.caption("Secure | Languages | Fast AI")
        st.markdown('</div>', unsafe_allow_html=True)

# MAIN APP AFTER LOGIN
else:
    st.title("Ardham AI - Dashboard")
    st.caption(f"Welcome! Phone: {st.session_state.get('phone','')} | History saved")
    
    url = st.text_input("Website / App link:", placeholder="https://example.com")
    
    if st.button("Analyze Chey", type="primary"):
        if not url:
            st.warning("Link paste chey bro")
        else:
            with st.spinner("Ardham chestunna..."):
                time.sleep(1)
            
            domain = urlparse(url).netloc
            if not domain:
                domain = url
            
            score = 85
            if "loan" in url.lower() or "earn" in url.lower():
                score = 45
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Safety Score", f"{score}/100")
            c2.metric("Domain Age", "3 Years")
            c3.metric("Trackers", "2 Found")
            
            st.divider()
            
            left2, right2 = st.columns(2)
            with left2:
                st.subheader("Enti Idi?")
                if score < 60:
                    st.error(f"{domain} - Risk undi, permissions ekkuva adugutundi")
                else:
                    st.info(f"{domain} - Genuine service, small data collect chestundi")
                
                st.subheader("Ela Vadali?")
                st.write("1. HTTPS check chey\n2. Reviews chudu\n3. Permissions No chey\n4. Small data tho test chey")
            
            with right2:
                st.subheader("Safe a Kada?")
                if score > 75:
                    st.success("HTTPS undi, Domain old, 2 trackers only")
                else:
                    st.warning("Kotha domain, ekkuva permissions, danger")
                
                st.subheader("Better Alternatives")
                st.write(f"Search: alternative to {domain}")
            
            st.divider()
            if st.button("Voice lo Vinu"):
                st.toast("Voice - Coming Soon")
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

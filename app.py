# Ardham AI - Universal Website & App Explainer
import streamlit as st
import requests
from urllib.parse import urlparse
import re

def analyze_website(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    
    # Basic safety checks
    safety_score = 0
    checks = []
    
    if "https" in url:
        safety_score += 30
        checks.append("✅ HTTPS secure connection undi - safe")
    else:
        checks.append("⚠️ HTTPS ledu - risk")
    
    if len(domain.split('.')) > 2:
        checks.append("⚠️ Subdomain ekkuva undi - phishing check chesuko")
    else:
        safety_score += 20
        checks.append("✅ Domain simple ga undi")
    
    # Fake age check (real API add cheyochu - WHOIS)
    safety_score += 50
    
    return safety_score, checks

def explain_in_telugu(url, purpose):
    if "shopping" in purpose.lower() or "【entity-amazon¦canonical_name=Amazon】" in url or "【entity-flipkart¦canonical_name=Flipkart】" in url:
        return {
            "what": "Idi shopping website/app. Products konukovachu.",
            "how_to_use": "1. Account create chey, 2. Product search chey, 3. Reviews chudu, 4. COD unte better",
            "safe": "Cash on Delivery vadite 90% safe",
            "alternatives": "【entity-Amazon¦canonical_name=Amazon】, 【entity-Flipkart¦canonical_name=Flipkart】, 【entity-Meesho¦canonical_name=Meesho】"
        }
    elif "loan" in url or "finance" in url:
        return {
            "what": "Idi loan / finance app. Dabbu istharu ani cheptaru.",
            "how_to_use": "Aadhar, PAN adagutharu. Interest chala ekkuva untadi. Chala apps fake.",
            "safe": "RBI registered a ani check cheyali. Lekapote danger",
            "alternatives": "Official bank apps - SBI YONO, 【entity-HDFC¦canonical_name=HDFC】"
        }
    else:
        return {
            "what": f"{url} - idi oka online service. User data collect chestadi.",
            "how_to_use": "Link open chesi, permissions adigithe jagratha. Location, contacts adigithe avoid chey",
            "safe": "First time aithe small data tho test chey",
            "alternatives": "Similar service kosam Google lo 'alternative to' ani search chey"
        }

# UI
st.set_page_config(page_title="Ardham AI", page_icon="🧠")
st.title("🧠 Ardham AI - Universal Explainer")
st.write("Mana anukunna AI tool - Edaina link isthe mana bhasha lo chepthadi")

url = st.text_input("Website / App link ikkada paste chey:")
if url:
    score, checks = analyze_website(url)
    st.subheader(f"Safety Score: {score}/100")
    for c in checks:
        st.write(c)
    
    explanation = explain_in_telugu(url, url)
    st.subheader("📖 Enti idi?")
    st.write(explanation["what"])
    st.subheader("🛠️ Ela vadali?")
    st.write(explanation["how_to_use"])
    st.subheader("🔒 Safe a?")
    st.write(explanation["safe"])
    st.subheader("🔄 Better Alternatives")
    st.write(explanation["alternatives"])

import streamlit as st
from PIL import Image

# Configure page
st.set_page_config(
    page_title="Abdelrahman Nagy - Professional Portfolio",
    page_icon="📷",
    layout="centered"
)

# Header section
st.title("Abdelrahman Nagy")
st.subheader("Professional Visual Content Creator")

# Profile image and bio
col1, col2 = st.columns([1, 2])
with col1:
    st.image("images/nagy1.png", width=250)
with col2:
    st.write("""
    A professional visual content creator with over six years of experience in various companies 
    and institutions in China, Germany, Egypt, and Kuwait. Specializing in:
    - TV presentation
    - Videography
    - Video editing
    - Content creation
    - Photography
    - Social media management
    """)

# Skill section
st.header("Skills")
skills = [
    "TV presentation", "Videography", "Video editing", 
    "Content creation", "Photography", "Social media management",
    "Moderation", "Communication", "Teamwork", "Problem solving"
]
st.write(" • ".join(skills))

# Portfolio section
st.header("Portfolio")
portfolio = {
    "AL-Jazeera Mubasher - China": "https://tinyurl.com/25er7m2j",
    "World Cup - Berlin": "https://tinyurl.com/2p88tndu",
    "Der Divan - Berlin": "https://tinyurl.com/9sm3y7t4",
    "Al-Salam Verein - NRW": "https://tinyurl.com/3kbeymet",
    "Kuwait University": "https://tinyurl.com/msnhz8cs",
    "Kuwait TV": "https://tinyurl.com/mparwekr",
    "Egypt": "https://creativia.world/"
}

for project, link in portfolio.items():
    st.write(f"🔗 [{project}]({link})")

# Education section
st.header("Education")
st.write("🎓 Master's student at University of Cologne")

# Contact section
st.header("Contact")
st.write("📞 (+49) 1621936753")
st.write("✉️ bodnagy98@gmail.com")
st.write("📷 Instagram: nagy_98")
st.write("🏠 Hahnenstr. 31C, Hürth - Efferen, Germany")

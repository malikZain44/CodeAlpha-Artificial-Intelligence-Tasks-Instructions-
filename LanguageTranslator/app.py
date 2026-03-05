import streamlit as st
from translator import translate_text
from speech import text_to_speech

# 1. PAGE CONFIG - Must be at the very top
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="wide"
)

# 2. LOAD CSS
def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("style.css file not found!")

load_css()

# 3. CENTER THE CONTENT
# Side columns (1.5) and Middle column (7) creates a centered look
empty_l, mid_col, empty_r = st.columns([1.5, 7, 1.5])

with mid_col:
    # MAIN CARD CONTAINER
    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    # HEADER
    st.markdown('<div class="title">🌍 AI Language Translator</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Fast, accurate, and professional AI-powered translations</div>', unsafe_allow_html=True)

    # INPUT BOX
    text = st.text_area("Enter your text below:", placeholder="Type or paste your content here...", height=150)

    # LANGUAGE SELECTION
    languages = {
        "English": "en", "Urdu": "ur", "French": "fr", 
        "German": "de", "Spanish": "es", "Hindi": "hi"
    }

    col1, col2 = st.columns(2)
    with col1:
        source_lang = st.selectbox("From (Source)", list(languages.keys()), index=0)
    with col2:
        target_lang = st.selectbox("To (Target)", list(languages.keys()), index=1)

    # TRANSLATION TRIGGER
    if st.button("🚀 Translate Text"):
        if not text.strip():
            st.warning("⚠️ Please enter some text to translate.")
        else:
            with st.spinner("Analyzing and translating..."):
                translated = translate_text(text, languages[source_lang], languages[target_lang])
                st.session_state['last_result'] = translated

    # RESULT DISPLAY
    if 'last_result' in st.session_state:
        st.markdown('<div class="result-label">Translation Result:</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box">{st.session_state["last_result"]}</div>', unsafe_allow_html=True)
        
        # SPEECH BUTTON
        if st.button("🔊 Play Translation"):
            with st.spinner("Generating audio..."):
                audio_data = text_to_speech(st.session_state['last_result'], languages[target_lang])
                st.audio(audio_data)

    st.markdown('</div>', unsafe_allow_html=True) # End of main-card

    # FOOTER
    st.markdown('<div class="footer">Developed with ❤️ using Streamlit & Advanced AI</div>', unsafe_allow_html=True)
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Mockup Portal Kesejahteraan Mahasiswa",
    layout="wide",
)

st.title("Mockup Portal Kesejahteraan Mahasiswa (ITB Minimal)")

# Baca HTML dari file
html_path = Path(__file__).parent / "index2.html"
html_content = html_path.read_text(encoding="utf-8")

# Tampilkan HTML dalam iframe
components.html(
    html_content,
    height=1100,        # atur sesuai kebutuhan
    scrolling=True      # penting biar bisa scroll jika konten tinggi
)

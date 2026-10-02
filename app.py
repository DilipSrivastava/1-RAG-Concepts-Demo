import streamlit as st
from pypdf import PdfReader
from src.document_loader import DocumentLoader
from src.document_chunker import DocumentChunker
from pathlib import Path


def load_css():
    css_file = Path(__file__).parent / "styles" / "style.css"

    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()
st.markdown(
    '<div class="main-title">AI Document Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Intelligent document analysis powered by AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <div class="step-header">
        <div class="step-title">Step 1: Document Loading</div>
    </div>
    ''',
    unsafe_allow_html=True
)


'''Which files This application will support.'''
uploaded_file = st.file_uploader(
    "Upload a document",
    type=[
        "pdf",
   ]
)

loader = DocumentLoader()
chunker = DocumentChunker()

if uploaded_file:
    st.success(
        f"Uploaded: {uploaded_file.name}"
    )
    if uploaded_file.type == "application/pdf":

        text = loader.load_pdf(uploaded_file) # Load text from the PDF file
        chunks = chunker.chunk_text(text) # Split the text into chunks
        print("========== CHUNKS ==========")
        for i, chunk in enumerate(chunks):
            print(f"\n--- Chunk {i + 1} ---")
            print(chunk)
        print("========== END CHUNKS ==========")
    else:
        st.error("Unsupported file type")
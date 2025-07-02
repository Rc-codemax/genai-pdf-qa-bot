import streamlit as st  # 📚 Streamlit for UI
from pypdf import PdfReader        # 📚 Extract text from PDFs

# ------------------------------------------------------------
# 📄 PDF → Q&A Bot (Enhanced UI v1)
# ------------------------------------------------------------
# Day‑2 of Week‑1
# This revision applies CRO feedback:
#   • Clear hero headline + benefit copy
#   • Trust/privacy messaging (local processing)
#   • Friendlier uploader micro‑copy
#   • Success toast with page count
#   • Question box visible but disabled until a PDF is present
#   • Spinner during PDF parsing
#   • All backend calls still stubbed for tomorrow
# ------------------------------------------------------------

# 🖥️ Basic page‑level config
st.set_page_config(
    page_title="📄 Ask Your PDF",   # Title in browser tab
    page_icon="📄",                # Favicon emoji
    layout="centered"              # Keep content narrow & centered
)

# 🏷️ Hero section -------------------------------------------------------
st.header("Ask Questions About Any PDF — Instantly")
st.caption(
    "Drop a white‑paper, contract, or textbook and get concise answers. "
    "All processing happens **locally** on your device — files never leave your computer."
)

st.markdown("---")  # Visual divider

# 1️⃣ PDF upload widget -----------------------------------------------
uploaded_file = st.file_uploader(
    "1️⃣ Drag & drop or click to select a PDF (max 200 MB)",  # Label with step indicator
    type=["pdf"],                                              # Accept only PDFs
    help="Your file is processed entirely in‑browser / on‑device."  # Tooltip / privacy note
)

# 2️⃣ If a file exists, extract text & preview -------------------------
if uploaded_file:
    # Show spinner while reading pages
    with st.spinner("Reading PDF…"):
        reader = PdfReader(uploaded_file)
        raw_text = "\n".join(page.extract_text() or "" for page in reader.pages)

    # Instant success feedback
    st.success(f"Loaded **{uploaded_file.name}** — {len(reader.pages)} pages ✅", icon="📄")

    # Preview the first 500 chars so user knows it worked
    st.subheader("📑 Document Preview (first 500 characters)")
    st.text_area(
        label="",  # No label inside textarea
        value=raw_text[:500] + (" …" if len(raw_text) > 500 else ""),
        height=200
    )

    st.markdown("---")

# 3️⃣ Question input ----------------------------------------------------
question = st.text_input(
    "2️⃣ Ask a question about your PDF",                      # Prompt label
    disabled=uploaded_file is None,                          # Enabled only after PDF upload
    placeholder="e.g., Summarize section 3 (enabled after upload)"
)

# 4️⃣ CTA button --------------------------------------------------------
if st.button("Get Answer", disabled=uploaded_file is None or not question.strip()):
    # Placeholder for tomorrow’s Retrieval‑QA pipeline
    st.info("🚧 Backend not connected yet — we'll wire this up tomorrow!")

# 5️⃣ Gentle nudge when no file is present -----------------------------
if uploaded_file is None:
    st.info("⬆️ Upload a PDF above to enable questions.", icon="ℹ️")

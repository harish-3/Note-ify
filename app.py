import streamlit as st
import os
from utils import extract_text_from_pdf, extract_text_from_docx
from gemini_chain import get_summary_and_flashcards

st.set_page_config(page_title="Note-ify", layout="centered")
st.title("📚 Note-ify (Gemini Edition)")
st.subheader("Summarize Notes & Generate Flashcards Using Gemini AI")

model_choice = st.selectbox("Choose Model:", ["Gemini 2.5(Most Accurate)", "Gemini 1.5(Most Faster)"], index=1)

uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])

if uploaded_file:
    file_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("🔍 Processing your document..."):
        if uploaded_file.name.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        else:
            text = extract_text_from_docx(file_path)

        if len(text.strip()) == 0:
            st.error("⚠️ No text found in the document.")
        else:
            # Select model based on user choice
            model_name = "gemini-2.5-pro-exp-03-25" if model_choice == "Gemini 2.5(Most Accurate)" else "gemini-1.5-flash"
            output = get_summary_and_flashcards(text, model_name)
            st.success("✅ Done! Here’s what we found:")

            if "## Summary:" in output and "## Flashcards:" in output:
                summary, flashcards = output.split("## Flashcards:")
                summary_text = summary.replace("## Summary:", "")
                st.session_state.summary_text = summary_text
                st.markdown("### 📌 Summary")
                st.markdown(summary_text)
                
                st.markdown("### 💡 Flashcards")
                for line in flashcards.strip().split("\n"):
                    if line.startswith("Q"):
                        st.markdown(f"**{line}**")
                    elif line.startswith("A"):
                        st.markdown(f"{line}")
            else:
                st.text(output)
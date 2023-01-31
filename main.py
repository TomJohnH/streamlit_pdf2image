import streamlit as st
import pdf2image
import zipfile
import os

pdf_uploaded = st.file_uploader("Select a file", type="pdf")
button = st.button("Confirm")
image_down = []
if button and pdf_uploaded is not None:

    if pdf_uploaded.type == "application/pdf":
        images = pdf2image.convert_from_bytes(pdf_uploaded.read())
        for i, page in enumerate(images):
            st.image(page, use_column_width=True)
            st.download_button("Download", data=page, file_name=f"Image_{i}.png")
            image_down.append(page)

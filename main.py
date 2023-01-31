import streamlit as st
import pdf2image
import zipfile
import os

pdf_uploaded = st.file_uploader("Select a file", type="pdf")
button = st.button("Confirm")
image_down = []
st.write("test1")
if button and pdf_uploaded is not None:
    st.write("test2")
    if pdf_uploaded.type == "application/pdf":
        st.write("test3")
        images = pdf2image.convert_from_bytes(pdf_uploaded.read())
        for i, page in enumerate(images):
            st.write(i)
            st.write(page)
            st.image(page, use_column_width=True)
            image_to_download = st.image(page, use_column_width=True)
            st.download_button(
                "Download", data=image_to_download, file_name=f"Image_{i}.png"
            )
            # image_down.append(page)

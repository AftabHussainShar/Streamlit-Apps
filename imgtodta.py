from cryptography.fernet import Fernet
import os
from matplotlib.pyplot import text
import streamlit as st
from stegano import lsb
import cv2
from PIL import Image


key = Fernet.generate_key()
f=Fernet(key)

def encrypt(uploaded_file):
    imageFile=uploaded_file
    imagestr = base64.b64encode(imageFile.read())

def decrypt(uploaded_file_2):

    imgFile.write(base64.b64decode(imagestr))
    return decrypted



st.set_page_config(
    page_title="IMAGE TO TEXT AND VOICE WEBAPP",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
)



@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def download_success():
    st.balloons()
    st.success('✅ Download Successful !!')




st.set_option('deprecation.showfileUploaderEncoding',False)
# st.image(main_image,use_column_width='auto')
st.title("✨ IMAGE TO TEXT AND VOICE WEBAPP 🖼 ")
st.subheader('Optical Character Recognition with Voice output')
st.text('Select source Language from the Sidebar.')

uploaded_file = st.file_uploader("Upload Image 🖼", type=["png","jpg","bmp","jpeg"])
Text=st.text_input("Enter Text to Hide")
upload_path = "uploads/"
download_path = "downloads/"

if st.button("Convert"):
    
    if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())

        with st.spinner(f"Sketching... 💫"):
            uploaded_image = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
            downloaded_image = os.path.abspath(os.path.join(download_path,str("enhanced_"+uploaded_file.name)))
            encrypt(uploaded_file)
          

            final_image = Image.open(downloaded_image)
            print("Opening ",final_image)
            st.markdown("---")
            st.image(final_image, caption='This is how your sketch image looks like 😉')
            with open(downloaded_image, "rb") as file:
                if uploaded_file.name.endswith('.jpg') or uploaded_file.name.endswith('.JPG'):
                    if st.download_button(
                                            label="Download Sketch Image 📷",
                                            data=file,
                                            file_name=str("Sketch_AFFI_"+uploaded_file.name),
                                            mime='image/jpg'
                                        ):
                        download_success()

                if uploaded_file.name.endswith('.jpeg') or uploaded_file.name.endswith('.JPEG'):
                    if st.download_button(
                                            label="Download Sketch Image 📷",
                                            data=file,
                                            file_name=str("Sketch_AFFI_"+uploaded_file.name),
                                            mime='image/jpeg'
                                        ):
                        download_success()

                if uploaded_file.name.endswith('.png') or uploaded_file.name.endswith('.PNG'):
                    if st.download_button(
                                            label="Download Sketch Image 📷",
                                            data=file,
                                            file_name=str("Sketch_AFFI_"+uploaded_file.name),
                                            mime='image/png'
                                        ):
                        download_success()

                if uploaded_file.name.endswith('.bmp') or uploaded_file.name.endswith('.BMP'):
                    if st.download_button(
                                            label="Download Sketch Image 📷",
                                            data=file,
                                            file_name=str("Sketch_AFFI_"+uploaded_file.name),
                                            mime='image/bmp'
                                        ):
                        download_success()
else:
    st.warning('⚠ Please upload your Image file 😯')
       


st.text('Select source Language from the Sidebar.')

uploaded_file_2 = st.file_uploader("Upload Image 🖼", type=["png","jpg","bmp","jpeg"],key="2")
if st.button("Reveal"):
    if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())

        with st.spinner(f"Sketching... 💫"):
            secret=lsb.reveal(uploaded_file_2)
            st.write(secret)

            

else:
    st.warning('⚠ Please upload your Image file 😯')






uploaded_file = st.file_uploader("Upload Image 🖼", type=["png","jpg","bmp","jpeg"])
Text=st.text_input("Enter Text to Hide")
upload_path = "uploads/"
download_path = "downloads/"

if st.button("Convert"):
    
    if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())

        with st.spinner(f"Sketching... 💫"):
            uploaded_image = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
            downloaded_image = os.path.abspath(os.path.join(download_path,str("enhanced_"+uploaded_file.name)))
            secret_2=lsb.hide(uploaded_image, "ILOVE YOU")
            secret_2.save(downloaded_image)

            final_image = Image.open(downloaded_image)
            print("Opening ",final_image)
            st.markdown("---")
            st.image(final_image, caption='This is how your sketch image looks like 😉')
            with open(downloaded_image, "rb") as file:
                if uploaded_file.name.endswith('.jpg') or uploaded_file.name.endswith('.JPG'):
                    if st.download_button(
                                            label="Download Sketch Image 📷",
                                            data=file,
                                            file_name=str("Sketch_AFFI_"+uploaded_file.name),
                                            mime='image/jpg'
                                        ):
                        download_success()

                if uploaded_file.name.endswith('.jpeg') or uploaded_file.name.endswith('.JPEG'):
                    if st.download_button(
                                            label="Download Sketch Image 📷",
                                            data=file,
                                            file_name=str("Sketch_AFFI_"+uploaded_file.name),
                                            mime='image/jpeg'
                                        ):
                        download_success()

                if uploaded_file.name.endswith('.png') or uploaded_file.name.endswith('.PNG'):
                    if st.download_button(
                                            label="Download Sketch Image 📷",
                                            data=file,
                                            file_name=str("Sketch_AFFI_"+uploaded_file.name),
                                            mime='image/png'
                                        ):
                        download_success()

                if uploaded_file.name.endswith('.bmp') or uploaded_file.name.endswith('.BMP'):
                    if st.download_button(
                                            label="Download Sketch Image 📷",
                                            data=file,
                                            file_name=str("Sketch_AFFI_"+uploaded_file.name),
                                            mime='image/bmp'
                                        ):
                        download_success()
else:
    st.warning('⚠ Please upload your Image file 😯')
       


st.text('Select source Language from the Sidebar.')

uploaded_file_2 = st.file_uploader("Upload Image 🖼", type=["png","jpg","bmp","jpeg"],key="2")
if st.button("Reveal"):
    if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())

        with st.spinner(f"Sketching... 💫"):
            secret=lsb.reveal(uploaded_file_2)
            st.write(secret)

            

else:
    st.warning('⚠ Please upload your Image file 😯')
    
st.markdown("<br><hr><center>Made with ❤️ by <a href='a03003132335@gmail.com?subject=IMAGE to SKETCH WebApp!&body=Please specify the issue you are facing with the app.'><strong>AFTAB HUSSAIN SHAR</strong></a></center><hr>", unsafe_allow_html=True)
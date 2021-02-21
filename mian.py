import streamlit as st
from skimage import io
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import Phone_camera as pc


model = load_model('garbage_recognition.h5')

@st.cache
def predictor(img):
    img = cv2.resize(img, (50, 50))
    pred = model.predict(np.array([img]))
    pred = np.where(pred > 0.6, 1, 0).flatten()
    if pred[0] == 1:
        return 'Garbage'
    else:
        return 'No Garbage'

def main():
    st.title("Garbage Recognition")
    choice = st.sidebar.selectbox("Choice",['Image', 'Web Camera', 'Phone Camera'])
    if choice == 'Image':
        st.subheader("Garbage recognition using images")
        try:
            file = st.file_uploader("Upload Image", type=['png', 'jpg'])
            if file is not None:
                img = io.imread(file)
                st.write(predictor(img))
                st.image(img, width=400)
        except:
            pass

    elif choice == 'Phone Camera':
        st.subheader("Garbage recognition using phone camera")
        try:
            link = st.text_input("link")
            link = 'https://'+link+':8080/video'
            st.write(link)
            pc.camera(url=link)
        except:
            pass

    elif choice == 'Web Camera':
        st.subheader("Garbage recognition using web camera")
        try:
            pc.camera(url=0)
        except:
            pass
    elif choice == 'Web Camera':
        st.subheader("Web Camera")
    elif choice == 'Phone Camera':
        st.subheader("Phone Camera")

if __name__ == '__main__':
    main()
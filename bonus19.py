import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")
with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    grey_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(grey_img)





# # Create a file uploader component allowing the user to upload a file
# uploaded_image = st.file_uploader("Upload Image")
#
# with st.expander("Start camera"):
#     camera_image = st.camera_input("Camera")
#
# if camera_image:
#     img = Image.open(camera_image)
#     gray_camera_img = img.convert('L')
#     st.image(gray_camera_img)
#
# # Check if the image exists meaning the user has uploaded a file
# if uploaded_image:
#     # Open the user uploaded image with PIL
#     img = Image.open(uploaded_image)
#     # Convert the image to grayscale
#     gray_uploaded_img = img.convert('L')
#     # Display the grayscale image on the webpage
#     st.image(gray_uploaded_img)
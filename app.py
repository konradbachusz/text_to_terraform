import streamlit as st
import utils
from PIL import Image

image = Image.open('static\graphic.png')
st.image(image)


prompt=st.text_input("Return Terraform code to create...", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, 
 placeholder=None, disabled=False)



if st.button('Terraform it!'):
     response=utils.get_terraform(prompt)
     st.success(response)



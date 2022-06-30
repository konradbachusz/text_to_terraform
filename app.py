import streamlit as st
import utils
from PIL import Image


#App image
image = Image.open('static\graphic.png')
st.image(image)

#Textbox for user prompt
prompt=st.text_input("Return Terraform code to create...", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, 
 placeholder=None, disabled=False)


#Button to get the prompt from Codex API
if st.button('Terraform it!'):

     response=utils.get_terraform(prompt)
     st.success(response)

#Text field to paste the code that needs validation
edited_response=st.text_area('Enter the code to test')

#Button to check if generated code is valid
if st.button('Validate terraform code'):
     utils.string_to_tf_file(edited_response)
     utils.terraform_fmt()

     validation_result=utils.validate_terraform()
     if  validation_result is True:

          st.success("Code valid")
     else:
          st.error("Code invalid")
          #Return error message
          st.header("Error Explanation")
          st.text(validation_result)

     #Remove temporart terraform file
     utils.remove_tf_file()



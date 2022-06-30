import streamlit as st
import utils
from PIL import Image


#App image
image = Image.open('static\graphic.png')
st.image(image)

#Textbox for user prompt
prompt=st.text_input("Return Terraform code to create...", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, 
 placeholder=None, disabled=False)


button1 = st.button('Terraform it!')

if st.session_state.get('button') != True:

     st.session_state['button'] = button1

if st.session_state['button'] == True:

     #response=utils.get_terraform(prompt)
     response="Terraform code"
     st.success(response)

     edited_response=st.text_area('Code to test')

     if st.button('Validate the above code'):
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
   

          utils.remove_tf_file()
          st.session_state['button'] = False



# text_to_terraform
![](https://github.com/konradbachusz/text_to_terraform/blob/main/static/graphic.PNG)
Tool that converts natural language to Terraform code

# Prerequisites
* Terraform 1.3.0: https://www.terraform.io/downloads
* Python 3.10.5: https://www.python.org/downloads/
* OpenAI Codex API: http://beta.openai.com/codex-waitlist

# Setup Instructions
1. Clone the repo 
2. **cd** into the repo
3. Run **pip install -r requirements.txt** (best to install it within a [Python venv](https://realpython.com/python-virtual-environments-a-primer/) )
4. Run **terraform init -backend=false**
5. Run **$env:OPENAI_API_KEY="<YOUR_OPENAI_API_KEY>"** (this command may vary depending on the operating system)
6. Run **streamlit run .\app.py** to open the web app locally
7. Enter the description of desired resources into the textbox under "Return Terraform code to create..."
   ![](https://github.com/konradbachusz/text_to_terraform/blob/main/static/prompt_screenshot.PNG)
8. Click on "Terraform it!" button
9.  The AI generated code will be shown below.
10. To validate the generated code, enter the code snippet into the text box below and click on "Validate terraform code"
    
   ![](https://github.com/konradbachusz/text_to_terraform/blob/main/static/testing_screenshot.PNG)

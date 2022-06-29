import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_terraform(prompt):
    """"""
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=("Terraform code to create,"+str(prompt)),
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response["choices"][0]["text"]




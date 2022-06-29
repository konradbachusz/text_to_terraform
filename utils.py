import os
import openai
import subprocess
from python_terraform import *
import os.path




openai.api_key = os.getenv("OPENAI_API_KEY")

def get_terraform(prompt):
    """This fuction takes text prompt as parameter and returns proposed Terraform code"""
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

def terraform_fmt():
    """This function formats the terraform code returned from Codex API"""
    Terraform(working_dir='.').fmt()
    return None



def validate_terraform():
    """This function performs basic validation of terraform code"""

    if os.path.isfile("main.tf"):
        result = subprocess.run(["terraform", "validate"], stdout=subprocess.PIPE)
        if "The configuration is valid" in str(result.stdout):
            output_correct=True
        else:
            output_correct=False
    
    else:
        output_correct=False
    
    return output_correct


def string_to_tf_file(response):
    """Function to save the response to a local terraform file"""
    text_file = open("main.tf", "wt")
    n = text_file.write(response)
    text_file.close()
    return None

def remove_tf_file():
    """Helper function to remove the temporary main.tf file"""
    if os.path.exists("main.tf"):
        os.remove("main.tf")
    else:
        print("The file does not exist")

responses=["hello","string_to_tf_file(response)","""Terraform code to create a kms encrypted s3 bucket

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region     = "us-east-1"
}

resource "aws_s3_bucket" "kms_encrypted_bucket" {
  bucket = "my-kms-encrypted-bucket"
  acl    = "private"

  server_side_encryption_configuration {{}
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "aws:kms"
      }
    }
  }
}""","""
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region     = "us-east-1"
}

resource "aws_s3_bucket" "kms_encrypted_bucket" {
  bucket = "my-kms-encrypted-bucket"
  acl    = "private"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "aws:kms"
      }
    }
  }
}""","test","""resource "aws_s3_bucket" "kms_encrypted_bucket" {
  bucket = "my-kms-encrypted-bucket"
  acl    = "private"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "aws:kms"
      }
    }
  }
}"""]
# while validate_terraform() is False:
#     for response in responses:
#         string_to_tf_file(response)
#         terraform_fmt()
#         print()

# print(validate_terraform())
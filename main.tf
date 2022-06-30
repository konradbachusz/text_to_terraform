#Test script needed for the set-up
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
} 
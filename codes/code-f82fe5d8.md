---
id: f82fe5d8-8d9e-4562-9778-4cc077492344
type: code
language: Terraform
verified: false
created_at: '2020-03-16T07:05:53.299842+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet f82fe5d8

**Language**: Terraform

```terraform
### AWS Config
provider "aws" {
  region = "us-east-1"
  profile = "${var.aws_profile}"
}

### Variable Definitions
variable "site_hash" {
  type = string
  description = "md5 hash"
}

variable "site_name" {
  type = string
  description = "site or project name"
}

variable "payload_file" {
  type = string
  description = "payload filename to upload to s3"
}

variable "aws_profile" {
  type = string
  description = "aws credentials profile"
}

### S3 Bucket -> Logs
resource "aws_s3_bucket" "logs" {
  bucket = "${var.site_hash}-${var.site_name}-site-logs"
  acl = "log-delivery-write"
  force_destroy = true
}

### S3 Bucket -> Website
resource "aws_s3_bucket" "http" {
  bucket = "${var.site_hash}-${var.site_name}"
  acl = "public-read"
  force_destroy = true

  logging {
    target_bucket = "${aws_s3_bucket.logs.bucket}"
    target_prefix = "${var.site_hash}-${var.site_name}"
  }

  # 2nd delivery method to upload payload
  provisioner "local-exec" {
    command = "aws s3 cp ${var.payload_file} s3://${aws_s3_bucket.http.bucket} --profile ${var.aws_profile}"
  }

policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAllHTTPConnections",
      "Principal": {
        "AWS": "*"
      },
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::${var.site_hash}-${var.site_name}/*"
    }
  ]
}
EOF
}

### Output
output "bucket_domain_name" {
  value = "s3://${aws_s3_bucket.http.bucket_domain_name}/${var.payload_file}"
  description = "FQDN of bucket"
} 

```

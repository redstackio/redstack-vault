---
id: 9df0cea1-61d6-4743-9c52-d86bbe1f5229
name: Terraform-Script-Provision-S3-Website
type: code
language: terraform
verified: true
created_at: '2019-10-10T18:18:30.601061+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
  - macOS
tags:
  - terraform
  - s3
  - infrastructure
validated: true
---

# Terraform-Script-Provision-S3-Website

## Code

```hcl
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

## Description

This Terraform script configures an AWS provider, defines variables for customization, creates a logging S3 bucket and a public website bucket with anonymous read policy, uploads a payload using a local-exec provisioner, and outputs the payload URL. It enables rapid staging of payloads in cloud environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| site_hash | MD5 hash for bucket uniqueness | 4a4a8f4331a58e913893a5d58b03221f |
| site_name | Site identifier | redstack |
| payload_file | Payload to upload | reverse_shell.exe |
| aws_profile | Credentials profile | hacker |

## Usage

Save as main.tf, load variables from terraform.tfvars, then run terraform init, plan, and apply. The script targets us-east-1; adjust region in provider block if needed. Use force_destroy=true for easy cleanup of non-empty buckets.

## Detection

- CloudTrail logs for S3 bucket creations with public policies.
- Alerts on local-exec provisioners uploading files in IaC runs.
- Monitor output values exposing public URLs in Terraform logs.

## Related

- [[procedures/Provision-AWS-S3-Website-and-Upload-Payload]]
- [[tools/terraform]]

---
id: e4672b45-de7e-4bd2-8d00-2f2b3f9182d3
name: Terraform-Variables-File-for-S3-Setup
type: code
language: terraform
verified: true
created_at: '2019-10-10T18:18:30.633982+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
  - macOS
tags:
  - terraform
  - variables
  - aws
validated: true
---

# Terraform-Variables-File-for-S3-Setup

## Code

```hcl
# terraform.tfvars
site_hash = "4a4a8f4331a58e913893a5d58b03221f"
site_name = "redstack"
payload_file = "reverse_shell.exe"
aws_profile = "hacker"
```

## Description

This variables file defines inputs for a Terraform script provisioning S3 buckets, ensuring unique naming and specifying the payload to upload. It promotes reusability across operations by parameterizing bucket names and file paths.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| site_hash | MD5 hash for unique bucket naming | 4a4a8f4331a58e913893a5d58b03221f |
| site_name | Project or site identifier | redstack |
| payload_file | Name of the file to upload to S3 | reverse_shell.exe |
| aws_profile | AWS CLI profile for authentication | hacker |

## Usage

Save as terraform.tfvars in the working directory alongside main.tf. Terraform automatically loads it during apply. Generate site_hash via md5sum on a unique string to avoid global naming conflicts.

## Detection

- Look for .tfvars files containing sensitive paths or hashes in environments.
- Monitor Terraform state files for S3 resource patterns.
- Detect variable values exposing operational details in logs.

## Related

- [[procedures/Provision-AWS-S3-Website-and-Upload-Payload]]
- [[tools/terraform]]

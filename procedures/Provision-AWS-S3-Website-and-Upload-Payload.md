---
id: 83634d12-6c01-4018-8622-3719e75fc0f2
name: Provision-AWS-S3-Website-and-Upload-Payload
type: procedure
verified: true
submitted: false
created_at: '2019-10-10T18:18:30.697830+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Stage Capabilities|TA0026 - Stage Capabilities]]'
techniques:
  - >-
    [[techniques/Upload, install, and configure software/tools|T1362 - Upload,
    install, and configure software/tools]]
sub_techniques: []
platforms:
  - Cloud
tags:
  - '[[tags/AWS]]'
  - '[[tags/Cloud]]'
  - '[[tags/Network]]'
commands:
  - '[[commands/terraform-initialize-project]]'
  - '[[commands/terraform-apply-provision-s3]]'
  - '[[commands/terraform-destroy-cleanup]]'
tools:
  - '[[tools/aws-cli]]'
  - '[[tools/terraform]]'
validated: true
---

# Provision-AWS-S3-Website-and-Upload-Payload

## Summary

This procedure uses Terraform to provision an AWS S3 bucket configured as a public website, upload a specified payload file to it, and set up a separate logging bucket to track access. It provides a quick way to host and deliver payloads from an internet-accessible location during red team engagements, outputting the direct URL to the payload for use in further attack steps.

## Description

In red team operations, hosting payloads on a controlled, public-facing website is essential for delivery via phishing, drive-by downloads, or other initial access vectors. This procedure automates the creation of an S3 bucket with public read access, enables static website hosting, applies an open policy for anonymous GetObject access, and uploads the payload using AWS CLI within the Terraform provisioner. A secondary logging bucket captures access logs to monitor target interactions, such as reverse shell downloads. The setup uses variables for reusability, ensuring unique bucket names via hashing to avoid conflicts. Upon completion, Terraform outputs the full URL (e.g., s3://bucket-domain/payload.exe). This approach minimizes manual AWS console interactions and ensures cleanup to avoid lingering resources and costs.

## Requirements

1. AWS account with IAM user credentials having S3 full access permissions (e.g., AmazonS3FullAccess policy).
2. AWS CLI installed and configured with a profile (e.g., 'hacker') containing access key and secret key.
3. Terraform installed (version 0.12+ recommended).
4. A payload file (e.g., reverse_shell.exe) ready in the working directory.
5. Network access to AWS APIs (no VPC restrictions).

## Defense

Defensive measures and detection strategies:

- Monitor AWS CloudTrail for S3 bucket creation, policy changes, and object uploads via unusual IAM users.
- Enable S3 access logging and integrate with SIEM for anomalous public bucket access patterns.
- Use AWS Config rules to alert on public S3 buckets and enforce least-privilege IAM policies.
- Scan for Terraform state files or .tfvars in compromised environments to detect infrastructure-as-code abuse.

## Objectives

1. Create a public S3 website hosting a payload for target delivery.
2. Enable logging to track payload access and confirm target engagement.
3. Provide a reusable URL for payload distribution in attack chains.
4. Ensure easy teardown to maintain operational security and minimize costs.

## Instructions

### Step 1: Set Up AWS Credentials and Working Directory

**Context**: Prepare the AWS CLI configuration with a dedicated profile for the red team operation and create a working directory containing the payload file, variables file, and Terraform script. This ensures isolated credentials and unique bucket naming to prevent conflicts.

Create the AWS credentials file at ~/.aws/credentials with the 'hacker' profile. Refer to the [[codes/AWS-Credentials-File-Example]] for the format. Then, in a new directory (e.g., workdir), place your payload.exe and create terraform.tfvars using [[codes/Terraform-Variables-File-for-S3-Setup]]. Finally, create main.tf using [[codes/Terraform-Script-Provision-S3-Website]].

### Step 2: Initialize Terraform Project

**Context**: Download and configure Terraform providers and modules for AWS, preparing the environment to apply the infrastructure configuration without manual dependency management.

**Command** ([[commands/terraform-initialize-project]]):
```bash
terraform init
```

This command fetches the AWS provider plugin and initializes the backend. Run it in the working directory containing main.tf and terraform.tfvars.

### Step 3: Apply Terraform Configuration to Provision Resources

**Context**: Execute the Terraform plan to create the S3 logging bucket, the public website bucket with policy, upload the payload, and output the access URL. This step incurs AWS costs for storage and requests.

**Command** ([[commands/terraform-apply-provision-s3]]):
```bash
terraform apply -auto-approve
```

Upon success, note the outputted bucket_domain_name, which provides the direct S3 URL to the payload (e.g., s3://hash-site.s3.amazonaws.com/payload.exe). Use this URL in delivery mechanisms like phishing links.

### Step 4: Monitor Logs and Verify Setup

**Context**: After provisioning, access the logging bucket via AWS console or CLI to confirm setup. Download logs periodically to track IP addresses accessing the payload, validating target interaction.

Use AWS CLI to list and download logs:
```bash
aws s3 ls s3://hash-site-logs/ --profile hacker
aws s3 cp s3://hash-site-logs/ ./logs/ --recursive --profile hacker
```

### Step 5: Clean Up Resources

**Context**: Destroy all provisioned resources to remove the public bucket, prevent data exposure, and stop billing. Download logs first if retention is needed.

**Command** ([[commands/terraform-destroy-cleanup]]):
```bash
terraform destroy -auto-approve
```

This removes both buckets and any uploaded objects. Verify destruction via AWS console.

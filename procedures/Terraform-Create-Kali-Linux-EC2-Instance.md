---
id: 126a4fb8-83a1-4a2d-80c2-2b8c629a4c9a
name: Terraform-Create-Kali-Linux-EC2-Instance
type: procedure
verified: true
submitted: true
created_at: '2019-10-11T16:41:20.166468+00:00'
updated_at: '2023-05-25T20:04:01.573232+00:00'
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
  - '[[tags/ec2]]'
  - terraform
commands:
  - '[[commands/terraform-init]]'
  - '[[commands/terraform-apply]]'
  - '[[commands/terraform-destroy]]'
tools:
  - '[[tools/aws-cli]]'
  - '[[tools/terraform]]'
validated: true
---

# Terraform-Create-Kali-Linux-EC2-Instance

## Summary

This procedure uses Terraform to provision a Kali Linux EC2 instance on AWS, including security group setup for open ports, SSH key configuration, and cloud-init for user creation and system updates. It enables rapid deployment of a pentesting environment with public IP access for red team operations.

## Description

In red team engagements, quickly staging a controlled Kali Linux instance in the cloud is essential for hosting tools, receiving reverse shells, or running ad-hoc services. This procedure automates the creation of an EC2 instance using Terraform, handling AWS resource provisioning such as key pairs, security groups allowing all ingress traffic (for flexibility in pentesting), and user data scripts to configure a 'hacker' user with sudo access, password authentication, and Kali repository updates. The instance is launched in a specified region with a default t2.small size, but variables allow customization. Prerequisites include AWS credentials configured for an IAM user with EC2 permissions. After deployment, connect via SSH using the provided public IP. Always destroy resources post-engagement to avoid costs.

## Requirements

1. AWS account with IAM user having EC2 full access permissions (e.g., AmazonEC2FullAccess policy).
2. AWS CLI installed and configured with access keys in the ~/.aws/credentials file under the 'hacker' profile.
3. Terraform installed on the local machine (hacker system).
4. Existing SSH public key (e.g., ~/.ssh/id_rsa.pub) for secure access.
5. Local working directory for Terraform files.

## Objectives

1. Provision a fully configured Kali Linux EC2 instance accessible via SSH.
2. Ensure open ports for reverse shells and pentesting tools.
3. Automate user setup and system hardening for immediate use.
4. Provide cleanup mechanism to tear down resources.

## Instructions

### Step 1: Set Up AWS Credentials

**Context**: Configure AWS CLI with the necessary profile for the 'hacker' account to authenticate Terraform operations. This ensures secure access to AWS resources without hardcoding keys in scripts.

Use the [[codes/AWS-Credentials-Hacker-Profile]] configuration:

```ini
# ~/.aws/credentials
[hacker]
aws_access_key_id = AKIA<REDACTED>SX65
aws_secret_access_key = pODU9<REDACTED>K4qW
```

> Edit the ~/.aws/credentials file to include your actual access key ID and secret access key under the [hacker] profile. Test with `aws sts get-caller-identity --profile hacker` to verify.

### Step 2: Create Working Directory and Terraform Script

**Context**: Prepare the local environment by creating a directory and the main Terraform configuration file. This script defines variables for region, AMI, profile, SSH key, and instance type, then provisions the security group, key pair, and EC2 instance with cloud-init for Kali setup.

Create a new directory named 'workdir' and inside it, create 'kali-linux.tf' with the content from [[codes/Terraform-Kali-EC2-Instance-Script]]. Update variables as needed (e.g., region, SSH key path, passwords in userdata).

> The script creates an open security group (all ports ingress/egress for pentesting flexibility), uploads the SSH public key, and runs cloud-init to add the 'hacker' user (password: iamhacker), enable password auth, and update to Kali rolling repos. Change default passwords to strong ones.

### Step 3: Initialize Terraform

**Context**: Download providers and modules required for the AWS Terraform configuration, preparing the workspace for planning and application.

**Command** ([[commands/terraform-init]]):
```bash
terraform init
```

> This command initializes the Terraform working directory, downloading the AWS provider plugin. Run it from within the 'workdir' containing kali-linux.tf.

### Step 4: Apply Terraform Configuration

**Context**: Execute the Terraform plan to create the EC2 instance, security group, and key pair. This provisions the resources in AWS and outputs the public IP for SSH connection.

**Command** ([[commands/terraform-apply]]):
```bash
terraform apply -auto-approve
```

> Review the execution plan if not using -auto-approve. Upon success, note the output 'kali-linux' which provides the SSH command (e.g., ssh hacker@<public_ip>). Connect using the 'hacker' user and password 'iamhacker' or SSH key.

### Step 5: Verify and Use Instance

**Context**: Confirm the instance is running and accessible, then use it for pentesting activities.

SSH to the instance:
```bash
ssh hacker@<PUBLIC_IP>
```

> Expected: Login successful, Kali environment ready with updates applied. Test sudo access and port openness (e.g., nc -lvp 4444 for reverse shells).

### Step 6: Destroy Resources

**Context**: Clean up all provisioned AWS resources to prevent ongoing costs and exposure.

**Command** ([[commands/terraform-destroy]]):
```bash
terraform destroy -auto-approve
```

> This removes the EC2 instance, key pair, and security group. Confirm with AWS console if needed.

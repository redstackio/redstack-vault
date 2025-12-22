---
type: command
executor: bash
data: >-
  aws ec2 import-key-pair --key-name "$_KEY_NAME" --public-key-material
  file://$_PUBLIC_KEY_PATH --region $_REGION
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - aws
  - ec2
  - ssh
  - access
verified: true
validated: true
---

# aws-ec2-import-key-pair

## Command

```bash
aws ec2 import-key-pair --key-name "$_KEY_NAME" --public-key-material file://$_PUBLIC_KEY_PATH --region $_REGION
```

## Description

Imports an SSH public key into AWS EC2 for use with instances, enabling secure access to newly launched clones.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_KEY_NAME | Name for the key pair (e.g., "AWS Audit") | Yes |
| $_PUBLIC_KEY_PATH | Path to public key file (PEM format, e.g., ~/.ssh/id_rsa.pub) | Yes |
| $_REGION | AWS region | Yes |

## Examples

### Basic Usage

```bash
aws ec2 import-key-pair --key-name "AWS Audit" --public-key-material file://~/.ssh/id_rsa.pub --region eu-west-1
```

## Expected Output

JSON with key details:
```
{
    "KeyName": "AWS Audit",
    "KeyFingerprint": "1f:51:ae..."
}
```
Success: Key imported without duplicate errors.

## Related

- [[procedures/Copy-EC2-Instance-via-AMI-Creation-in-AWS]]
- [[commands/aws-ec2-run-instances-from-ami]]

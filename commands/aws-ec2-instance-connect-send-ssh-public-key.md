---
id: 9df71556-f8d4-45ae-b6d2-928a6908253f
name: aws-ec2-instance-connect-send-ssh-public-key
type: command
executor: bash
data: >-
  aws ec2-instance-connect send-ssh-public-key --region $_REGION --instance-id
  $_INSTANCE_ID --availability-zone $_AVAILABILITY_ZONE --instance-os-user
  $_OS_USER --ssh-public-key file://$_KEY_FILE --profile $_PROFILE
output: null
created_at: '2023-04-06T03:56:09.629928+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
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

# aws-ec2-instance-connect-send-ssh-public-key

## Command

```bash
aws ec2-instance-connect send-ssh-public-key --region $_REGION --instance-id $_INSTANCE_ID --availability-zone $_AVAILABILITY_ZONE --instance-os-user $_OS_USER --ssh-public-key file://$_KEY_FILE --profile $_PROFILE
```

## Description

This command pushes a public SSH key to an EC2 instance via AWS Instance Connect, authorizing temporary SSH access (valid for 60 seconds) using the corresponding private key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --region $_REGION | AWS region of the instance (e.g., us-east-1) | Yes |
| --instance-id $_INSTANCE_ID | ID of the target EC2 instance (e.g., i-1234567890abcdef0) | Yes |
| --availability-zone $_AVAILABILITY_ZONE | AZ of the instance (e.g., us-east-1d) | Yes |
| --instance-os-user $_OS_USER | OS user to authenticate as (e.g., ubuntu, ec2-user) | Yes |
| --ssh-public-key file://$_KEY_FILE | Path to the public key file (e.g., file://shortkey.pub) | Yes |
| --profile $_PROFILE | AWS CLI profile name | Yes |

## Examples

### Basic Usage

```bash
aws ec2-instance-connect send-ssh-public-key --region us-east-1 --instance-id i-1234567890abcdef0 --availability-zone us-east-1d --instance-os-user ubuntu --ssh-public-key file://~/.ssh/id_rsa.pub --profile default
```

### Advanced Usage

```bash
aws ec2-instance-connect send-ssh-public-key --region eu-west-1 --instance-id i-0987654321fedcba0 --availability-zone eu-west-1a --instance-os-user ec2-user --ssh-public-key file://custom.pub --profile uploadcreds
```

## Expected Output

```
{
  "RequestId": "abc123-def456-ghi789",
  "Result": "Success"
}
```
A JSON response indicating success. Errors include permission denied or invalid instance ID.

## Related

- [[procedures/Push-SSH-Key-to-EC2-Instance-via-AWS-Instance-Connect]]
- [[commands/aws-ec2-describe-instances]]

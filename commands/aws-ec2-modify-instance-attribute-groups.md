---
type: command
executor: bash
data: >-
  aws ec2 modify-instance-attribute --instance-id $_INSTANCE_ID --groups
  "$_SECURITY_GROUP_ID" --region $_REGION
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - aws
  - ec2
  - modify
  - configuration
verified: true
validated: true
---

# aws-ec2-modify-instance-attribute-groups

## Command

```bash
aws ec2 modify-instance-attribute --instance-id $_INSTANCE_ID --groups "$_SECURITY_GROUP_ID" --region $_REGION
```

## Description

Modifies the security groups associated with an EC2 instance to adjust network access post-launch.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INSTANCE_ID | ID of the instance | Yes |
| $_SECURITY_GROUP_ID | New security group ID(s) | Yes |
| $_REGION | AWS region | Yes |

## Examples

### Basic Usage

```bash
aws ec2 modify-instance-attribute --instance-id "i-0546910a0c18725a1" --groups "sg-6d0d7f01" --region eu-west-1
```

## Expected Output

Empty JSON on success:
```
{}
```
Success: No error; verify with describe-instances.

## Related

- [[procedures/Copy-EC2-Instance-via-AMI-Creation-in-AWS]]
- [[commands/aws-ec2-describe-instance-by-id]]

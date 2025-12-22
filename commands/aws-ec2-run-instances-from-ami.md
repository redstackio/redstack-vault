---
type: command
executor: bash
data: >-
  aws ec2 run-instances --image-id $_AMI_ID --security-group-ids
  "$_SECURITY_GROUP_ID" --subnet-id $_SUBNET_ID --count 1 --instance-type
  $_INSTANCE_TYPE --key-name "$_KEY_NAME" --query "Instances[0].InstanceId"
  --region $_REGION
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - aws
  - ec2
  - launch
  - lateral-movement
verified: true
validated: true
---

# aws-ec2-run-instances-from-ami

## Command

```bash
aws ec2 run-instances --image-id $_AMI_ID --security-group-ids "$_SECURITY_GROUP_ID" --subnet-id $_SUBNET_ID --count 1 --instance-type $_INSTANCE_TYPE --key-name "$_KEY_NAME" --query "Instances[0].InstanceId" --region $_REGION
```

## Description

Launches one or more EC2 instances from a specified AMI, configuring network and access settings to match the source for lateral propagation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_AMI_ID | ID of the AMI to use (e.g., ami-0b77e2d906b00202d) | Yes |
| $_SECURITY_GROUP_ID | Security group ID (e.g., sg-6d0d7f01) | Yes |
| $_SUBNET_ID | Subnet ID (e.g., subnet-9eb001ea) | Yes |
| $_INSTANCE_TYPE | Instance type (e.g., t2.micro) | Yes |
| $_KEY_NAME | SSH key pair name | Yes |
| $_REGION | AWS region | Yes |
| --count | Number of instances | No (default 1) |

## Examples

### Basic Usage

```bash
aws ec2 run-instances --image-id ami-0b77e2d906b00202d --security-group-ids "sg-6d0d7f01" --subnet-id subnet-9eb001ea --count 1 --instance-type t2.micro --key-name "AWS Audit" --query "Instances[0].InstanceId" --region eu-west-1
```

## Expected Output

Instance ID string:
```
"i-0546910a0c18725a1"
```
Success: Valid instance ID returned; check status with describe.

## Related

- [[procedures/Copy-EC2-Instance-via-AMI-Creation-in-AWS]]
- [[commands/aws-ec2-describe-instance-by-id]]

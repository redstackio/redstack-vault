---
id: 197d4d94-5c10-4311-933f-d44d4fcf49cf
name: aws-ec2-associate-iam-instance-profile
type: command
executor: bash
data: >-
  aws ec2 associate-iam-instance-profile --instance-id $_INSTANCE_ID
  --iam-instance-profile Name=$PROFILE_NAME
output: null
created_at: '2023-04-06T03:56:13.529718+00:00'
updated_at: '2023-04-10T20:20:54.124879+00:00'
platforms:
  - AWS
tags:
  - cloud
  - aws
  - privilege-escalation
verified: true
validated: true
---

# aws-ec2-associate-iam-instance-profile

## Command

```bash
aws ec2 associate-iam-instance-profile --instance-id $_INSTANCE_ID --iam-instance-profile Name=$PROFILE_NAME
```

## Description

This AWS CLI command associates an IAM instance profile with a running or stopped EC2 instance, effectively updating the instance's IAM role and enabling elevated permissions via the Instance Metadata Service. Use this during privilege escalation when you have permissions to modify EC2 instance configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --instance-id $_INSTANCE_ID | The ID of the target EC2 instance (e.g., i-1234567890abcdef0) | Yes |
| --iam-instance-profile Name=$PROFILE_NAME | The name of the IAM instance profile to attach (must exist and be compatible) | Yes |

## Examples

### Basic Usage

```bash
aws ec2 associate-iam-instance-profile --instance-id i-1234567890abcdef0 --iam-instance-profile Name=MyElevatedProfile
```

### Advanced Usage

If replacing an existing profile, first disassociate the old one with `disassociate-iam-instance-profile`, then run this command.

```bash
aws ec2 associate-iam-instance-profile --instance-id i-1234567890abcdef0 --iam-instance-profile Name=AdminProfile --region us-east-1
```

## Expected Output

Successful execution returns JSON like:

```json
{
    "IamInstanceProfileAssociation": {
        "AssociationId": "eia-1234567890abcdef0",
        "InstanceId": "i-1234567890abcdef0",
        "IamInstanceProfile": {
            "Arn": "arn:aws:iam::123456789012:instance-profile/MyElevatedProfile"
        }
    }
}
```

Errors may include `UnauthorizedOperation` if permissions are insufficient or `InvalidInstanceID.NotFound` if the ID is wrong.

## Related

- [[procedures/AWS-EC2-Instance-Profile-Privilege-Escalation]]

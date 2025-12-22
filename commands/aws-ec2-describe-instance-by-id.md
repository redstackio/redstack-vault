---
type: command
executor: bash
data: aws ec2 describe-instances --instance-ids $_INSTANCE_ID --region $_REGION
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - aws
  - ec2
  - describe
  - verification
verified: true
validated: true
---

# aws-ec2-describe-instance-by-id

## Command

```bash
aws ec2 describe-instances --instance-ids $_INSTANCE_ID --region $_REGION
```

## Description

Retrieves detailed information about a specific EC2 instance, including state, IP, and configuration, to verify launch success.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INSTANCE_ID | ID of the instance (e.g., i-0546910a0c18725a1) | Yes |
| $_REGION | AWS region | Yes |

## Examples

### Basic Usage

```bash
aws ec2 describe-instances --instance-ids i-0546910a0c18725a1 --region eu-west-1
```

## Expected Output

JSON with instance details:
```
{
    "Reservations": [
        {
            "Instances": [
                {
                    "InstanceId": "i-0546910a0c18725a1",
                    "State": { "Name": "running" },
                    "PrivateIpAddress": "10.0.1.100"
                }
            ]
        }
    ]
}
```
Success: State running, no errors.

## Related

- [[procedures/Copy-EC2-Instance-via-AMI-Creation-in-AWS]]
- [[commands/aws-ec2-run-instances-from-ami]]

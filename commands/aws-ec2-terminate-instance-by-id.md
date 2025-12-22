---
type: command
executor: bash
data: aws ec2 terminate-instances --instance-ids $_INSTANCE_ID --region $_REGION
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - aws
  - ec2
  - terminate
  - cleanup
verified: true
validated: true
---

# aws-ec2-terminate-instance-by-id

## Command

```bash
aws ec2 terminate-instances --instance-ids $_INSTANCE_ID --region $_REGION
```

## Description

Permanently terminates an EC2 instance, deleting it and associated resources (except EBS if configured).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INSTANCE_ID | ID of the instance | Yes |
| $_REGION | AWS region | Yes |

## Examples

### Basic Usage

```bash
aws ec2 terminate-instances --instance-ids "i-0546910a0c18725a1" --region eu-west-1
```

## Expected Output

JSON with shutting-down state:
```
{
    "TerminatingInstances": [
        { "InstanceId": "i-0546910a0c18725a1", "CurrentState": { "Name": "shutting-down" } }
    ]
}
```
Success: Instance marked for termination.

## Related

- [[procedures/Copy-EC2-Instance-via-AMI-Creation-in-AWS]]
- [[commands/aws-ec2-stop-instance-by-id]]

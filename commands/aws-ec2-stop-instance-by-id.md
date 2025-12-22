---
type: command
executor: bash
data: aws ec2 stop-instances --instance-ids $_INSTANCE_ID --region $_REGION
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - aws
  - ec2
  - stop
  - cleanup
verified: true
validated: true
---

# aws-ec2-stop-instance-by-id

## Command

```bash
aws ec2 stop-instances --instance-ids $_INSTANCE_ID --region $_REGION
```

## Description

Stops a running EC2 instance, preserving data but halting execution to reduce costs or exposure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INSTANCE_ID | ID of the instance | Yes |
| $_REGION | AWS region | Yes |
| --force | Force stop if needed | No |

## Examples

### Basic Usage

```bash
aws ec2 stop-instances --instance-ids "i-0546910a0c18725a1" --region eu-west-1
```

## Expected Output

JSON with stopping state:
```
{
    "StoppingInstances": [
        { "InstanceId": "i-0546910a0c18725a1", "CurrentState": { "Name": "stopping" } }
    ]
}
```
Success: State changes to stopping.

## Related

- [[procedures/Copy-EC2-Instance-via-AMI-Creation-in-AWS]]
- [[commands/aws-ec2-describe-instance-by-id]]

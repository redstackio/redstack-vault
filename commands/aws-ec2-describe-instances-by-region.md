---
id: b3303536-82e1-43f5-b2a5-9213cba4fd1e
name: aws-ec2-describe-instances-by-region
type: command
executor: bash
data: aws ec2 describe-instances --region $_AWS_REGION
output: null
created_at: '2023-04-06T03:56:13.228129+00:00'
updated_at: '2023-04-10T20:20:35.851871+00:00'
platforms:
  - AWS
tags:
  - cloud
  - enumeration
  - aws
verified: true
validated: true
---

# aws-ec2-describe-instances-by-region

## Command

```bash
aws ec2 describe-instances --region $_AWS_REGION
```

## Description

This command queries the AWS EC2 service to retrieve detailed information about all EC2 instances in a specified region. It is used for discovery and mapping of cloud infrastructure, providing data on instance states, types, security groups, and more. Run this after obtaining AWS credentials to enumerate resources without direct console access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--region` | The AWS region to query (e.g., us-east-1, eu-west-1) | Yes |
| `$_AWS_REGION` | Placeholder for the region name | Yes |

## Examples

### Basic Usage

```bash
aws ec2 describe-instances --region us-east-1
```

### Advanced Usage

Add filters to narrow results, e.g., running instances only:
```bash
aws ec2 describe-instances --region us-east-1 --filters "Name=instance-state-name,Values=running"
```

## Expected Output

The command returns a JSON structure with reservations containing instance details. Successful output looks like:

```json
{
  "Reservations": [
    {
      "Instances": [
        {
          "InstanceId": "i-1234567890abcdef0",
          "InstanceType": "t2.micro",
          "State": { "Name": "running" },
          "SecurityGroups": [ { "GroupId": "sg-0123456789abcdef0" } ]
        }
      ]
    }
  ]
}
```

If no instances are found, an empty Reservations array is returned. Errors include permission denied (if lacking ec2:DescribeInstances) or invalid region.

## Related

- [[procedures/aws-region-information-gathering]]
- [[tools/aws-cli]]

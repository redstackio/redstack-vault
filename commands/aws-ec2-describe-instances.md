---
id: c0d77dd5-0f35-41a9-a2f8-fcfb32aae535
name: aws-ec2-describe-instances
type: command
executor: bash
data: >-
  aws ec2 describe-instances --instance-ids $_INSTANCE_IDS --region $_REGION
  --output json
output: null
created_at: '2023-04-06T03:56:13.251461+00:00'
updated_at: '2023-04-10T20:20:56.936765+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - aws
  - ec2
  - discovery
verified: true
validated: true
---

# aws-ec2-describe-instances

## Command

```bash
aws ec2 describe-instances --instance-ids $_INSTANCE_IDS --region $_REGION --output json
```

## Description

This command queries the AWS EC2 API to retrieve detailed metadata about one or more specified EC2 instances, such as their state, IP addresses, instance types, launch times, and security groups. Use it during cloud discovery phases to map infrastructure after obtaining instance IDs from broader listings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --instance-ids | Space-separated list of EC2 instance IDs to describe (e.g., i-1234567890abcdef0 i-0987654321fedcba0). Omit for all instances (requires broader permissions). | Yes |
| $_INSTANCE_IDS | Placeholder for the instance IDs list. | Yes |
| --region | AWS region to query (e.g., us-east-1). Defaults to configured region if omitted. | No |
| --output | Format of output (json, text, table). JSON is recommended for parsing. | No |
| --filters | Optional filters to narrow results (e.g., "Name=instance-state-name,Values=running"). | No |
| --dry-run | Simulate the request without executing (for permission testing). | No |

## Examples

### Basic Usage

Describe a single instance:
```bash
aws ec2 describe-instances --instance-ids i-1234567890abcdef0 --region us-east-1
```

### Advanced Usage

Describe running instances with filters and JSON output:
```bash
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --output json --region us-west-2
```

## Expected Output

A JSON object structured as follows, indicating successful retrieval:
```
{
    "Reservations": [
        {
            "Instances": [
                {
                    "InstanceId": "i-1234567890abcdef0",
                    "InstanceType": "t2.micro",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "PrivateIpAddress": "10.0.1.123",
                    "PublicIpAddress": "203.0.113.1",
                    "LaunchTime": "2023-01-01T12:00:00.000Z",
                    "SecurityGroups": [
                        {
                            "GroupId": "sg-0123456789abcdef0",
                            "GroupName": "default"
                        }
                    ],
                    "VpcId": "vpc-0123456789abcdef0"
                }
            ]
        }
    ]
}
```
If no instances match or access is denied, expect an empty Reservations array or an error like "An error occurred (UnauthorizedOperation)".

## Related

- [[procedures/Enumerate-AWS-EC2-Instances]]
- [[tools/AWS-CLI]]

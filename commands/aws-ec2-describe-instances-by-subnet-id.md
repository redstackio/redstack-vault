---
type: command
executor: bash
data: 'aws ec2 describe-instances --filters "Name=subnet-id,Values=$_SUBNET_ID"'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - AWS
tags:
  - aws-ec2
  - enumeration
  - lateral-movement
verified: true
validated: true
---

# AWS EC2 Describe Instances by Subnet ID

## Command

```bash
aws ec2 describe-instances --filters "Name=subnet-id,Values=$_SUBNET_ID"
```

## Description

This command invokes the AWS EC2 API to retrieve detailed information about all instances running in a specified subnet, useful for discovering resources during lateral movement in AWS environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SUBNET_ID | The unique identifier of the target subnet (format: subnet- followed by hexadecimal string) | Yes |
| --filters | Specifies the filter criteria; here, Name=subnet-id limits results to the provided subnet | Built-in |
| Name=subnet-id | The filter name for subnet association | Built-in |
| Values=$_SUBNET_ID | The value to match against the filter | Built-in |

## Examples

### Basic Usage

```bash
aws ec2 describe-instances --filters "Name=subnet-id,Values=subnet-0123456789abcdef0"
```

### Advanced Usage with Output Formatting

```bash
aws ec2 describe-instances --filters "Name=subnet-id,Values=subnet-0123456789abcdef0" --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name]' --output table
```

This variation uses --query to extract specific fields (InstanceId, InstanceType, State) and --output table for readable formatting.

## Expected Output

The command returns a JSON object with a 'Reservations' array containing instance details. Successful execution shows instances if present in the subnet.

Example output:

```json
{
    "Reservations": [
        {
            "Instances": [
                {
                    "InstanceId": "i-1234567890abcdef0",
                    "InstanceType": "t3.micro",
                    "LaunchTime": "2023-01-01T12:00:00Z",
                    "State": {
                        "Name": "running"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "RDS-Proxy"
                        }
                    ],
                    "VpcId": "vpc-abcdef0123456789",
                    "SubnetId": "subnet-0123456789abcdef0"
                }
            ]
        }
    ]
}
```

If no instances are found, "Reservations" will be an empty array. Errors may occur if credentials lack permissions (e.g., AccessDenied).

## Related

- [[procedures/List-EC2-Instances-in-Specific-Subnet-for-Lateral-Movement]]
- [[tools/AWS-CLI]]

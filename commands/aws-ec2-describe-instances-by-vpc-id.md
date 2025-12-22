---
id: 83a666bf-c0d4-4f52-a3b1-09c74c53afad
name: aws-ec2-describe-instances-by-vpc-id
type: command
executor: bash
data: 'aws ec2 describe-instances --filters "Name=vpc-id,Values=$_VPC_ID"'
output: null
created_at: '2023-04-06T03:56:14.507020+00:00'
updated_at: '2023-04-10T20:20:17.691315+00:00'
platforms:
  - AWS
tags:
  - discovery
  - cloud
verified: true
validated: true
---

# AWS EC2 Describe Instances by VPC ID

## Command

```bash
aws ec2 describe-instances --filters "Name=vpc-id,Values=$_VPC_ID"
```

## Description

This command queries the AWS EC2 API to retrieve details of all instances within a specified VPC. It is used for discovering potential pivot hosts in cloud environments during lateral movement scenarios, such as targeting RDS access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VPC_ID | The ID of the VPC to filter instances by (format: vpc- followed by alphanumeric string) | Yes |
| --filters | Specifies the filter criteria; here, filtering by vpc-id name | Built-in |
| --query | Optional: JMESPath query to customize output (e.g., --query 'Reservations[].Instances[?State.Name==`running`]') | No |
| --output | Optional: Format output (json, table, text) | No |

## Examples

### Basic Usage

```bash
aws ec2 describe-instances --filters "Name=vpc-id,Values=vpc-0123456789abcdef0"
```

### Advanced Usage with Filtering for Running Instances

```bash
aws ec2 describe-instances --filters "Name=vpc-id,Values=vpc-0123456789abcdef0" --query 'Reservations[].Instances[?State.Name==`running`].InstanceId' --output table
```

## Expected Output

Successful execution returns a JSON structure with reservations containing instance details:

```json
{
  "Reservations": [
    {
      "Instances": [
        {
          "InstanceId": "i-0123456789abcdef0",
          "InstanceType": "t2.micro",
          "State": { "Name": "running" },
          "PrivateIpAddress": "10.0.1.100",
          "LaunchTime": "2023-01-01T00:00:00.000Z"
        }
      ]
    }
  ]
}
```

Look for running instances to use as pivots.

## Related

- [[procedures/rds-lateral-movement-via-ec2-instances-in-vpc]]
- [[tools/aws-cli]]

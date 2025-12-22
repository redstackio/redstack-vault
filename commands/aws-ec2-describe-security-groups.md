---
id: ba3a870a-95bf-472d-8958-c577fb77796a
name: aws-ec2-describe-security-groups
type: command
executor: bash
data: aws ec2 describe-security-groups --group-ids $_GROUP_ID
output: null
created_at: '2023-04-06T03:56:13.989198+00:00'
updated_at: '2023-04-10T20:20:20.134934+00:00'
platforms:
  - AWS
tags:
  - discovery
  - aws-api
verified: true
validated: true
---

# aws-ec2-describe-security-groups

## Command

```bash
aws ec2 describe-security-groups --group-ids $_GROUP_ID
```

## Description

This AWS CLI command queries the EC2 API to retrieve detailed information about one or more specified security groups, including their inbound and outbound rules, descriptions, and associated VPCs. It is useful for reconnaissance in AWS environments to identify misconfigured access controls, particularly for services like RDS that rely on these groups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --group-ids $_GROUP_ID | Comma-separated list of security group IDs to describe (e.g., sg-0123456789abcdef0) | Yes |
| --filters (optional) | Key-value pairs to filter results (e.g., --filters "Name=group-name,Values=mygroup") | No |
| --dry-run (optional) | Validate input without executing | No |

## Examples

### Basic Usage

Describe a single security group:

```bash
aws ec2 describe-security-groups --group-ids sg-0123456789abcdef0
```

### Advanced Usage

Describe multiple groups with filtering:

```bash
aws ec2 describe-security-groups --group-ids sg-0123456789abcdef0,sg-0987654321fedcba0 --filters "Name=vpc-id,Values=vpc-12345678"
```

## Expected Output

A JSON response with security group details:

```json
{
  "SecurityGroups": [
    {
      "Description": "RDS access group",
      "GroupName": "rds-sg",
      "GroupId": "sg-0123456789abcdef0",
      "IpPermissions": [
        {
          "IpProtocol": "tcp",
          "FromPort": 3306,
          "ToPort": 3306,
          "IpRanges": [
            {"CidrIp": "0.0.0.0/0"}
          ]
        }
      ],
      "IpPermissionsEgress": [...],
      "OwnerId": "123456789012",
      "VpcId": "vpc-12345678"
    }
  ]
}
```
Success is a 200 OK response with populated SecurityGroups array; errors include InvalidGroup.NotFound for invalid IDs.

## Related

- [[procedures/Enumerate-RDS-Security-Groups]]
- [[tools/AWS-CLI]]

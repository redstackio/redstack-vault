---
id: 2b76d9c8-c1f5-468c-b6db-72bf98b02e70
name: aws-ec2-describe-vpc-peering-connections
type: command
executor: bash
data: >-
  aws ec2 describe-vpc-peering-connections --region $_AWS_REGION --vpc-id
  $_TARGET_VPC_ID
output: null
created_at: '2023-04-06T03:56:14.430969+00:00'
updated_at: '2023-10-10T20:20:49.230853+00:00'
platforms:
  - AWS
tags:
  - discovery
  - vpc-peering
  - aws
verified: true
validated: true
---

# AWS EC2 Describe VPC Peering Connections

## Command

```bash
aws ec2 describe-vpc-peering-connections --region $_AWS_REGION --vpc-id $_TARGET_VPC_ID
```

## Description

This AWS CLI command retrieves detailed information about VPC peering connections for a specified VPC, including connected VPC IDs, CIDR blocks, status, and tags. Use it during discovery to map network interconnections for lateral movement opportunities, such as pivoting to RDS instances in peered VPCs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --region $_AWS_REGION | AWS region (e.g., us-east-1) | Yes |
| --vpc-id $_TARGET_VPC_ID | ID of the target VPC (e.g., vpc-12345678) | Yes |
| --filters Name=tag:Key,Values=Value | Filter by tags | No |
| --query 'expression' | JMESPath query to customize output | No |
| --output text\|json\|table | Output format | No |

## Examples

### Basic Usage

```bash
aws ec2 describe-vpc-peering-connections --region us-east-1 --vpc-id vpc-0a1b2c3d4e5f67890
```

### Filtered Output

```bash
aws ec2 describe-vpc-peering-connections --query 'VpcPeeringConnections[].{ID:VpcPeeringConnectionId,Status:Status.Code}' --output table
```

## Expected Output

Successful execution returns JSON like:

```json
{
  "VpcPeeringConnections": [
    {
      "VpcPeeringConnectionId": "pcx-12345678",
      "Status": { "Code": "active" },
      "AccepterVpcInfo": { "VpcId": "vpc-abcdef01", "CidrBlock": "10.0.0.0/16" },
      "RequesterVpcInfo": { "VpcId": "vpc-01234567", "CidrBlock": "172.16.0.0/16" }
    }
  ]
}
```

Look for 'active' status and extract CIDRs for scanning.

## Related

- [[procedures/rds-lateral-movement-via-vpc-peering-connections]]
- [[tools/aws-cli]]

---
type: command
executor: bash
data: aws ec2 allocate-address --domain vpc --region $AWS_REGION
platforms:
  - Cloud
tags:
  - aws
  - ec2
  - elastic-ip
verified: true
validated: true
---

# aws-ec2-allocate-elastic-ip-in-vpc

## Command

```bash
aws ec2 allocate-address --domain vpc --region $AWS_REGION
```

## Description

Allocates a static Elastic IP address within a VPC for use with services like NAT Gateways. This ensures persistent public addressing for outbound traffic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --domain vpc | Specifies VPC-scoped allocation (EC2-Classic alternative) | Yes |
| --region $AWS_REGION | AWS region (e.g., us-east-1) | Yes |

## Examples

### Basic Usage

```bash
aws ec2 allocate-address --domain vpc --region us-east-1
```

### With Output to JSON

```bash
aws ec2 allocate-address --domain vpc --region us-east-1 --output json
```

## Expected Output

```
{
    "AllocationId": "eipalloc-0abcd1234efgh5678",
    "Domain": "vpc",
    "PublicIp": "203.0.113.25"
}
```

A successful allocation returns the ID and IP; use the AllocationId in subsequent commands like creating a NAT Gateway.

## Related

- [[procedures/Setup-AWS-NAT-Gateway-for-Private-Subnet-Internet-Access]]
- [[commands/aws-ec2-create-nat-gateway-in-subnet]]

---
type: command
executor: bash
data: >-
  aws ec2 create-nat-gateway --subnet-id $AWS_SUBNET_ID --allocation-id
  $AWS_ALLOCATION_ID --region $AWS_REGION
platforms:
  - Cloud
tags:
  - aws
  - ec2
  - nat-gateway
verified: true
validated: true
---

# aws-ec2-create-nat-gateway-in-subnet

## Command

```bash
aws ec2 create-nat-gateway --subnet-id $AWS_SUBNET_ID --allocation-id $AWS_ALLOCATION_ID --region $AWS_REGION
```

## Description

Creates a NAT Gateway in a specified public subnet, associating it with an Elastic IP for outbound internet access from private resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --subnet-id $AWS_SUBNET_ID | ID of the public subnet (e.g., subnet-0123456789abcdef0) | Yes |
| --allocation-id $AWS_ALLOCATION_ID | Elastic IP allocation ID from allocate-address | Yes |
| --region $AWS_REGION | AWS region (e.g., us-east-1) | Yes |

## Examples

### Basic Usage

```bash
aws ec2 create-nat-gateway --subnet-id subnet-0123456789abcdef0 --allocation-id eipalloc-0abcd1234efgh5678 --region us-east-1
```

### With Wait for Availability

```bash
aws ec2 create-nat-gateway --subnet-id subnet-0123456789abcdef0 --allocation-id eipalloc-0abcd1234efgh5678 --region us-east-1 && aws ec2 wait nat-gateway-available --nat-gateway-ids $(aws ec2 create-nat-gateway ... --query 'NatGateway.NatGatewayId' --output text)
```

## Expected Output

```
{
    "NatGateway": {
        "NatGatewayId": "nat-0123456789abcdef0",
        "SubnetId": "subnet-0123456789abcdef0",
        "State": "pending",
        "NatGatewayAddresses": [
            {
                "AllocationId": "eipalloc-0abcd1234efgh5678",
                "PublicIp": "203.0.113.25"
            }
        ]
    }
}
```

The gateway enters 'pending' state; poll with describe-nat-gateways until 'available'.

## Related

- [[procedures/Setup-AWS-NAT-Gateway-for-Private-Subnet-Internet-Access]]
- [[commands/aws-ec2-allocate-elastic-ip-in-vpc]]

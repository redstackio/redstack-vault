---
id: cmd-uuid-003
data: >-
  aws ec2 associate-address --instance-id i-1234567890abcdef0 --allocation-id
  eipalloc-12345678 --allow-reassociation
tags:
  - aws
  - ec2
type: command
output: null
executor: bash
platforms:
  - Linux
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.915Z'
verified: false
validated: true
submitted: true
---
# aws-associate-address

## Command

```bash
aws ec2 associate-address --instance-id i-1234567890abcdef0 --allocation-id eipalloc-12345678 --allow-reassociation
```

## Description

Associates an allocated Elastic IP with an EC2 instance, enabling traffic routing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --instance-id | EC2 instance ID | Yes |
| --allocation-id | Elastic IP allocation ID | Yes |
| --allow-reassociation | Permit reassociation if already linked | No |

## Examples

### Basic Usage

```bash
aws ec2 associate-address --instance-id i-1234567890abcdef0 --allocation-id eipalloc-12345678
```

### Advanced Usage

```bash
aws ec2 associate-address --instance-id i-1234567890abcdef0 --allocation-id eipalloc-12345678 --allow-reassociation
```

## Expected Output

JSON with AssociationId, e.g., {"AssociationId":"eipassoc-12345678"}.

## Related

- [[Related Procedure: Allocate-Reusable-AWS-Elastic-IP]]

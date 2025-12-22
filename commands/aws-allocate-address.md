---
id: cmd-uuid-002
data: aws ec2 allocate-address --domain vpc --address 52.XX.XX.XX
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
updated_at: '2025-12-14T04:51:10.918Z'
verified: false
validated: true
submitted: true
---
# aws-allocate-address

## Command

```bash
aws ec2 allocate-address --domain vpc --address 52.XX.XX.XX
```

## Description

Allocates a specific Elastic IP address from AWS's pool for use with EC2 instances in VPC mode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --domain vpc | Specifies VPC domain | Yes |
| --address | Specific IP to allocate | Yes (for dangling IPs) |

## Examples

### Basic Usage

```bash
aws ec2 allocate-address --domain vpc
```

### Advanced Usage

```bash
aws ec2 allocate-address --domain vpc --address 52.XX.XX.XX
```

## Expected Output

JSON with AllocationId, e.g., {"AllocationId":"eipalloc-12345678"}.

## Related

- [[Related Procedure: Allocate-Reusable-AWS-Elastic-IP]]

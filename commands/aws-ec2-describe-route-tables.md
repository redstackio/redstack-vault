---
id: bcd86bbe-5226-4a6c-8153-2e96e810098d
name: aws-ec2-describe-route-tables
type: command
executor: bash
data: >-
  aws ec2 describe-route-tables --vpc-id $_VPC_ID --query
  'RouteTables[*].[RouteTableId,Associations[].SubnetId,Routes[]]' --output
  table
output: null
created_at: '2023-04-06T03:56:14.203937+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
tags:
  - aws
  - vpc
  - routing
verified: true
validated: true
---

# aws-ec2-describe-route-tables

## Command

```bash
aws ec2 describe-route-tables --vpc-id $_VPC_ID --query 'RouteTables[*].[RouteTableId,Associations[].SubnetId,Routes[]]' --output table
```

## Description

This command queries AWS EC2 to list route tables in a specified VPC, including associations to subnets and existing routes. Use it to identify the route table for an RDS instance's subnet before modification, ensuring targeted changes for traffic redirection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --vpc-id $_VPC_ID | ID of the target VPC (e.g., vpc-0123456789abcdef0) | Yes |
| --query | JMESPath query to filter output (e.g., RouteTableId, Associations, Routes) | No |
| --output table | Format output as a table for readability | No |

## Examples

### Basic Usage

```bash
aws ec2 describe-route-tables --vpc-id vpc-0123456789abcdef0
```

### Advanced Usage

```bash
aws ec2 describe-route-tables --vpc-id vpc-0123456789abcdef0 --filters "Name=association.subnet-id,Values=subnet-0123456789abcdef0" --output json
```

## Expected Output

```
-----------------------------------------------
|             DescribeRouteTables              |
+----------------+--------------------+---------+
|  rtb-01234567  |  subnet-01234567  |  local  |
|                |                   |  igw    |
+----------------+--------------------+---------+
```

A table showing route table IDs, associated subnets, and routes (e.g., destination CIDR to target). Success: Lists tables without errors; verify RDS subnet association.

## Related

- [[procedures/Modify-AWS-VPC-Route-Tables-for-RDS-Traffic-Redirection]]
- [[commands/aws-ec2-create-route]]

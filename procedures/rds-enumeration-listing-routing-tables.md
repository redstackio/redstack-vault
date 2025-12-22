---
id: 6299d3b1-180a-4f2e-8adf-8d4726ee14c1
name: rds-enumeration-listing-routing-tables
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.361355+00:00'
updated_at: '2023-04-10T20:20:02.706751+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Network Service Scanning]]'
sub_techniques: []
tags:
  - enumeration
  - aws-ec2
  - routing-tables
  - discovery
  - cloud
commands:
  - '[[commands/aws-ec2-describe-route-tables]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# RDS Enumeration: Listing Routing Tables

## Summary

This procedure uses the AWS CLI to enumerate and list routing tables associated with Amazon EC2 instances in a Virtual Private Cloud (VPC). By describing route tables, attackers can map network topology, identify active subnets, and discover associated EC2 instances, aiding in further reconnaissance and targeting of cloud resources.

## Description

In AWS environments, routing tables control the flow of network traffic within a VPC by defining rules for directing packets to specific destinations, such as internet gateways, NAT gateways, or other VPCs. This procedure leverages the `aws ec2 describe-route-tables` command to retrieve details about these tables, including route table IDs, associated VPCs, subnets, and route destinations. This information reveals the structure of the network, such as public vs. private subnets and potential points of ingress/egress, which can be used to plan lateral movement or identify misconfigurations. The technique requires AWS credentials with EC2 read permissions (e.g., `ec2:DescribeRouteTables`) and is typically executed after obtaining initial access to AWS via compromised IAM roles or console credentials. It aligns with discovery tactics in cloud intrusions, where understanding infrastructure topology is key to escalating access or exfiltrating data.

## Requirements

1. AWS CLI installed and configured with credentials that have `ec2:DescribeRouteTables` permissions.
2. Access to a shell environment (e.g., Linux, macOS, or Windows with AWS CLI).
3. Network connectivity to AWS endpoints (no direct VPC access needed if using IAM credentials).
4. Optional: Specific VPC or route table IDs for filtered queries to reduce output noise.

## Defense

- Implement least-privilege IAM policies to restrict `ec2:DescribeRouteTables` access to only necessary roles.
- Enable AWS CloudTrail logging for EC2 API calls and monitor for unusual describe-route-tables invocations from unexpected IPs or users.
- Use VPC Flow Logs to detect anomalous network patterns that might indicate reconnaissance.
- Regularly audit routing table configurations via AWS Config rules to identify and remediate overly permissive setups.

## Objectives

1. Retrieve a list of VPC route tables and their configurations to map network topology.
2. Identify associated subnets and EC2 instances for targeting in subsequent attacks.
3. Uncover potential misconfigurations, such as routes to public internet gateways exposing private resources.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure your AWS credentials are set up correctly and have the required permissions. This prevents authentication errors during execution.

Run the following to test access:

**Command** ([[commands/aws-ec2-describe-route-tables]] with dry-run):
```bash
aws ec2 describe-route-tables --dry-run
```

> This checks permissions without querying actual data. If successful, it returns a success message; if not, update your IAM policy or credentials.

### Step 2: List All Route Tables

**Context**: Execute the main command to describe all route tables in the default region. This provides a broad view of the VPC's routing structure.

**Command** ([[commands/aws-ec2-describe-route-tables]]):
```bash
aws ec2 describe-route-tables
```

> The command outputs JSON with route table details, including IDs, VPC associations, and routes (e.g., destination CIDRs and targets like igw-xxx). Review for subnets linked to EC2 instances.

### Step 3: Filter Results for Specific VPC or Tables (Optional)

**Context**: If you know a VPC ID or route table ID, apply filters to focus on relevant data and avoid overwhelming output in large environments.

**Command** ([[commands/aws-ec2-describe-route-tables]] with filters):
```bash
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=vpc-12345678"
```

> Replace `vpc-12345678` with the target VPC ID. Expected output is filtered JSON showing only matching route tables, aiding in targeted enumeration.

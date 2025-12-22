---
id: ff123c96-1bc0-4fb0-9c37-edfd5a3e9ad0
name: enumerate-rds-subnets-via-ec2-describe-subnets
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.302623+00:00'
updated_at: '2023-04-10T20:20:22.878774+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
  - '[[techniques/Remote System Discovery|T1018 - Remote System Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/Listing-subnets]]'
  - '[[tags/RDS-Relational-Database-Service]]'
commands:
  - '[[commands/aws-ec2-describe-subnets]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# Enumerate RDS Subnets via EC2 Describe Subnets

## Summary

This procedure uses the AWS CLI to enumerate subnets associated with RDS instances in a target AWS environment. By querying EC2 subnet details, attackers can identify network segments hosting managed databases, enabling further discovery of potential targets for lateral movement or data exfiltration.

## Description

RDS (Relational Database Service) is AWS's managed database offering. In a compromised AWS account with sufficient permissions, attackers can leverage the `ec2 describe-subnets` API call to list all subnets within a VPC, including those used by RDS instances. This reveals CIDR blocks, availability zones, and tags that may indicate RDS usage (e.g., tags like 'Name: RDS-Subnet'). The technique aids in mapping the cloud infrastructure, identifying isolated database segments, and planning subsequent attacks such as attempting direct RDS access or pivoting to EC2 instances in the same subnet. It requires EC2 read permissions and is commonly used in cloud reconnaissance phases to understand resource distribution without triggering database-specific alerts.

## Requirements

1. AWS CLI installed and configured with access keys or IAM role providing `ec2:DescribeSubnets` permission.
2. Network access to AWS APIs (internet or VPC endpoint).
3. Target AWS account or assumed role with EC2 read access.

## Defense

Defensive measures and detection strategies:

- Implement least-privilege IAM policies to restrict `ec2:DescribeSubnets` to necessary roles only.
- Enable AWS CloudTrail logging for EC2 API calls and monitor for unusual describe-subnets queries from unexpected sources.
- Use VPC flow logs and GuardDuty to detect anomalous cloud API activity, such as repeated subnet enumerations.
- Segment RDS subnets with security groups and NACLs to limit lateral movement even if discovered.

## Objectives

1. Identify subnets used by RDS instances in the target AWS environment.
2. Gain a better understanding of the target environment's network topology for potential attack paths.
3. Locate potential database targets for further exploitation or exfiltration.

## Instructions

### Step 1: Verify AWS CLI Configuration and Permissions

**Context**: Ensure the AWS CLI is set up and you have the required permissions to query EC2 subnets. This step confirms access before enumeration to avoid permission errors.

Run a test command to verify configuration:

```bash
aws sts get-caller-identity
```

> This command returns your AWS account details and confirms authentication. If it fails, reconfigure credentials using `aws configure`.

**Expected Output**: JSON with Account, UserId, and Arn fields showing your identity.

### Step 2: Enumerate All Subnets in the VPC

**Context**: Use the AWS EC2 describe-subnets command to retrieve details on all subnets, focusing on those tagged or configured for RDS. This reveals CIDR blocks and zones where databases may reside.

**Command** ([[commands/aws-ec2-describe-subnets]]):

```bash
aws ec2 describe-subnets
```

> This retrieves a JSON list of subnets, including IDs, VPC IDs, CIDR blocks, availability zones, and tags. Filter output with `--filters` for RDS-specific tags (e.g., `--filters "Name=tag:Name,Values=RDS*"`) or specific VPCs using `--vpc-ids`. Pipe to `jq` for parsing: `aws ec2 describe-subnets | jq '.Subnets[] | {SubnetId, CidrBlock, AvailabilityZone, Tags}'`.

**Expected Output**: JSON array of subnet objects, e.g., {"Subnets": [{"SubnetId": "subnet-123", "CidrBlock": "10.0.1.0/24", "AvailabilityZone": "us-east-1a", "Tags": [{"Key": "Name", "Value": "RDS-Private-Subnet"}]}]}.

### Step 3: Analyze Output for RDS Indicators

**Context**: Parse the results to identify RDS-related subnets. Look for tags like 'RDS', 'Database', or private CIDRs not associated with public-facing resources.

Use `jq` or grep to filter:

```bash
aws ec2 describe-subnets | jq '.Subnets[] | select(.Tags[]?.Value | contains("RDS")) | {SubnetId, CidrBlock, Tags}'
```

> This filters subnets with 'RDS' in tags. Manually review for patterns indicating database usage, such as multi-AZ setups.

**Expected Output**: Filtered JSON showing RDS-tagged subnets, confirming potential targets.

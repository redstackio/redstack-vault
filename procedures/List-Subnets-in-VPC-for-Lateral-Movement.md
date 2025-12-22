---
id: 533dd375-ddfb-4cd5-b032-495d1726e51a
name: List-Subnets-in-VPC-for-Lateral-Movement
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.459826+00:00'
updated_at: '2023-04-10T20:20:10.789280+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Network Configuration Discovery|T1016 - System Network
    Configuration Discovery]]
sub_techniques: []
tags:
  - lateral-movement
  - vpc-subnets
  - aws-rds
  - discovery
  - aws-ec2
commands:
  - '[[commands/aws-ec2-describe-subnets-by-vpc-id]]'
platforms:
  - AWS
tools: []
validated: true
---

# List-Subnets-in-VPC-for-Lateral-Movement

## Summary

This procedure uses the AWS CLI to enumerate subnets within a specific Virtual Private Cloud (VPC) from a compromised EC2 instance, enabling attackers to map the network layout for lateral movement in an AWS environment, particularly targeting RDS resources.

## Description

In an AWS cloud environment, attackers who have gained initial access to an EC2 instance can pivot by discovering the underlying network structure. Listing subnets in a VPC reveals available CIDR blocks, availability zones, and subnet IDs, which can indicate potential targets like RDS databases or other services restricted to specific subnets. This technique is part of broader lateral movement strategies where access might be segmented across VPCs or subnets. By identifying accessible subnets, attackers can plan further actions such as port scanning or attempting connections to RDS endpoints. The procedure relies on the AWS EC2 API via CLI and assumes the compromised instance has the necessary IAM permissions (e.g., ec2:DescribeSubnets).

## Requirements

1. Compromised EC2 instance with AWS CLI installed and configured with credentials that have ec2:DescribeSubnets permission.
2. Knowledge of the target VPC ID (obtainable via other discovery procedures like describing VPCs).
3. Network connectivity within the VPC to execute AWS API calls.

## Defense

Defensive measures and detection strategies:

- Implement least-privilege IAM policies to restrict ec2:DescribeSubnets access to only necessary roles.
- Enable AWS CloudTrail logging for EC2 API calls and monitor for unusual describe-subnets queries from EC2 instances.
- Use VPC Flow Logs to detect anomalous internal network discovery patterns.
- Segment VPCs and subnets with security groups and NACLs to limit lateral movement.

## Objectives

1. Enumerate all subnets associated with a target VPC to map the network topology.
2. Identify potential pivot points for accessing RDS or other cloud resources in restricted subnets.
3. Facilitate further exploitation by revealing availability zones and CIDR blocks for targeting.

## Instructions

### Step 1: Prepare AWS CLI and Identify VPC

**Context**: Ensure AWS CLI is installed on the compromised EC2 instance and authenticated with appropriate credentials. Obtain the VPC ID through prior reconnaissance (e.g., via aws ec2 describe-vpcs).

Install AWS CLI if not present:
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Configure credentials if needed (assuming IAM role is attached to EC2):
```bash
aws configure list
```

### Step 2: List Subnets in the Target VPC

**Context**: Use the AWS EC2 describe-subnets command filtered by VPC ID to retrieve subnet details. This reveals the network segments available for pivoting, such as those hosting RDS instances.

**Command** ([[commands/aws-ec2-describe-subnets-by-vpc-id]]):
```bash
aws ec2 describe-subnets --filters "Name=vpc-id,Values=vpc-0123456789abcdef0"
```

> This command queries the EC2 API for subnets matching the specified VPC ID. Replace the VPC ID placeholder with the actual value. The output is JSON containing subnet details, which can be parsed for further analysis. If successful, it lists all subnets without errors; failures may indicate insufficient permissions or invalid VPC ID.

### Step 3: Parse and Analyze Output

**Context**: Review the JSON output to extract key information like subnet IDs, CIDR blocks, and availability zones. Pipe to jq for easier parsing if available.

Install jq if needed:
```bash
sudo yum install jq -y  # On Amazon Linux
```

Parse output:
```bash
aws ec2 describe-subnets --filters "Name=vpc-id,Values=vpc-0123456789abcdef0" | jq '.Subnets[] | {SubnetId, CidrBlock, AvailabilityZone}'
```

> Expected output includes a list of subnets with their configurations. Use this to identify subnets potentially hosting RDS (e.g., private subnets in specific AZs). Verify no access denied errors in the response.

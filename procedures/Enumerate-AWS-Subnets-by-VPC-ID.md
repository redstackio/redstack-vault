---
id: aebb8591-3729-45ae-9bf1-cf5648a617e5
name: Enumerate-AWS-Subnets-by-VPC-ID
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:14.330540+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Resource Development|TA0042 - Resource Development]]'
techniques:
  - >-
    [[techniques/Account-Discovery-Cloud-Account|T1087.004 - Account Discovery:
    Cloud Account]]
  - '[[techniques/Acquire-Infrastructure|T1583 - Acquire Infrastructure]]'
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/AWS]]'
  - '[[tags/VPC]]'
  - '[[tags/Subnets]]'
  - '[[tags/RDS]]'
commands:
  - '[[commands/aws-ec2-describe-subnets-by-vpc-id]]'
tools:
  - '[[tools/AWS-CLI]]'
platforms:
  - AWS
validated: true
---

# Enumerate-AWS-Subnets-by-VPC-ID

## Summary

This procedure uses the AWS CLI to enumerate subnets associated with a specific VPC ID in an AWS environment. It is a key reconnaissance technique for identifying network segmentation and potential targets like RDS instances within those subnets, enabling attackers to map cloud infrastructure for further exploitation.

## Description

In cloud environments like AWS, attackers with compromised credentials or IAM roles often begin by discovering the underlying infrastructure. This procedure focuses on querying the EC2 API to list subnets tied to a given VPC ID, revealing details such as CIDR blocks, availability zones, and subnet IDs. This information helps identify isolated network segments that may host sensitive resources like RDS databases. The technique assumes initial access to AWS services via CLI and is commonly used in lateral movement or persistence phases to scope the attack surface. By filtering on VPC ID, attackers can narrow down to specific virtual networks without enumerating the entire account, reducing detection risk while gathering actionable intel for targeting vulnerable resources.

## Requirements

1. Valid AWS credentials with permissions to call EC2 DescribeSubnets (e.g., ec2:DescribeSubnets policy attached to IAM user/role).
2. AWS CLI installed and configured with access keys or assumed role.
3. Known VPC ID to filter the query (obtainable via other enumeration like describe-vpcs).
4. Network access to AWS APIs (internet or VPC endpoint).

## Defense

- Implement least-privilege IAM policies to restrict DescribeSubnets API calls to necessary roles only.
- Enable AWS CloudTrail logging for EC2 API actions and monitor for unusual DescribeSubnets queries filtered by VPC.
- Use VPC flow logs and GuardDuty to detect anomalous infrastructure enumeration patterns.
- Segment VPCs with security groups and NACLs to limit lateral discovery even if subnets are enumerated.

## Objectives

1. Retrieve a list of subnets associated with the target VPC ID, including their configurations.
2. Identify potential network segments hosting RDS or other resources for targeted attacks.
3. Map availability zones and CIDR blocks to understand isolation and attack paths.

## Instructions

### Step 1: Query Subnets for the Specified VPC

**Context**: Use the AWS CLI to invoke the EC2 DescribeSubnets API with a filter for the target VPC ID. This step retrieves detailed subnet information without scanning the entire account, providing context on network layout for subsequent targeting of RDS instances or other services.

**Command** ([[commands/aws-ec2-describe-subnets-by-vpc-id]]):
```bash
aws ec2 describe-subnets --filters "Name=vpc-id,Values=$_VPC_ID"
```

> This command filters subnets by the provided VPC ID ($_VPC_ID should be replaced with the actual VPC identifier, e.g., vpc-12345678). It returns a JSON response listing matching subnets. Verify the output for subnet IDs, CIDR blocks, and availability zones to confirm discovery. If no subnets are returned, the VPC may be empty or the ID incorrect—cross-reference with VPC enumeration procedures.

### Step 2: Parse and Analyze Output

**Context**: Review the JSON output to extract key details like subnet IDs and CIDR ranges. This manual step helps identify subnets likely hosting RDS (e.g., private subnets in specific AZs) and prepares data for further queries like describe-instances or rds-describe-db-instances.

**Command** ([[commands/aws-ec2-describe-subnets-by-vpc-id]]):
```bash
aws ec2 describe-subnets --filters "Name=vpc-id,Values=$_VPC_ID" --query "Subnets[*].[SubnetId,CidrBlock,AvailabilityZone]" --output table
```

> Adding --query and --output table formats the response for quick analysis. Look for patterns like private CIDR blocks (e.g., 10.0.x.0/24) indicating internal resources. Success is indicated by a table of subnets; pipe to jq for JSON parsing if needed (e.g., | jq '.Subnets[] | {SubnetId, CidrBlock}').

---
type: procedure
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Cloud Service Discovery]]'
sub_techniques: []
tags:
  - enumeration
  - aws
  - vpc
  - rds
  - discovery
  - cloud
platforms:
  - AWS
commands:
  - '[[commands/aws-rds-describe-db-instances]]'
  - '[[commands/aws-ec2-describe-vpcs-by-id]]'
tools:
  - '[[tools/AWS-CLI]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
verified: true
validated: true
---

# Enumerate-AWS-RDS-VPCs

## Summary

This procedure discovers VPC information associated with Amazon RDS instances by first listing RDS databases to extract VPC IDs and then describing the corresponding VPCs using AWS CLI commands. It enables attackers to map out cloud infrastructure for further targeting, such as identifying network boundaries or potential lateral movement paths in an AWS environment.

## Description

In cloud environments like AWS, RDS instances are often deployed within specific VPCs, which define network isolation and access controls. Enumerating these VPCs reveals critical details like CIDR blocks, subnets, and tags that can inform subsequent attacks, such as attempting to access databases or pivoting to other resources. This technique requires AWS credentials with read access to RDS and EC2 services. It leverages the AWS CLI to query services non-interactively, making it suitable for automated reconnaissance scripts. Success provides a view of the target's cloud footprint, aiding in discovery of misconfigurations or exposed resources. Note that this assumes the attacker has obtained initial AWS access, such as via compromised IAM credentials.

## Requirements

1. Valid AWS credentials (IAM user/role) with permissions for `rds:DescribeDBInstances` and `ec2:DescribeVpcs` actions.
2. AWS CLI installed and configured with the target account's access key ID, secret access key, and default region (e.g., us-east-1).
3. Network access to AWS APIs (typically over HTTPS port 443).
4. Basic knowledge of AWS services and JSON output parsing.

## Defense

- Implement least privilege access for IAM policies, restricting Describe actions to necessary roles.
- Enable AWS CloudTrail logging for API calls and monitor for unusual DescribeVpcs or DescribeDBInstances queries from unexpected sources.
- Use AWS Organizations SCPs to deny discovery actions in sensitive accounts.
- Rotate credentials regularly and monitor for anomalous access patterns via GuardDuty or similar tools.

## Objectives

1. List all RDS instances in the target AWS account to identify associated VPCs.
2. Extract VPC IDs from RDS details and query VPC configurations for network mapping.
3. Gather infrastructure details like CIDR blocks and tags to plan further exploitation.

## Instructions

### Step 1: List RDS Instances to Identify VPCs

**Context**: Begin by querying RDS for all database instances to retrieve their VPC associations. This step uncovers DBInstanceIdentifiers and linked VPCSecurityGroups or DBSubnetGroup, from which VPC IDs can be parsed. Use this to build a list of relevant VPCs without directly querying EC2 yet.

**Command** ([[commands/aws-rds-describe-db-instances]]):
```bash
aws rds describe-db-instances --region $_AWS_REGION
```

> This command fetches a JSON list of RDS instances. Review the output for fields like "DBSubnetGroup": {"DBSubnetGroupName": "..."} or "VpcSecurityGroups" to note VPC-related identifiers. If no VPC is shown, the instance may be in the default VPC. Save the output to a file (e.g., rds_instances.json) for parsing VPC IDs in the next step. Expected: A JSON array of DB instances with details; success if at least one RDS instance is returned without permission errors.

### Step 2: Extract VPC IDs and Describe VPCs

**Context**: From the RDS output, manually or script-extract VPC IDs (often via DBSubnetGroup ARN patterns like arn:aws:rds:region:account:db-subnet-group:name, which links to VPC). Then, use the VPC ID to describe the full VPC configuration, revealing CIDR blocks, states, and tags for network reconnaissance.

**Command** ([[commands/aws-ec2-describe-vpcs-by-id]]):
```bash
aws ec2 describe-vpcs --filters "Name=vpc-id,Values=$_VPC_ID" --region $_AWS_REGION
```

> Replace $_VPC_ID with the extracted ID (e.g., vpc-12345678). This returns detailed VPC info. For multiple VPCs, loop over IDs or remove the filter for all VPCs (but this may return unrelated ones). Expected: JSON with "Vpcs" array containing CIDRBlock, State (available), IsDefault, and Tags. Parse for tags like "Name: production-vpc" to identify targets. If the VPC ID is invalid, the output will be empty—verify extraction from Step 1.

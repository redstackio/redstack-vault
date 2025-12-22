---
type: procedure
description: >-
  Uses AWS CLI to enumerate EC2 instances in a target subnet to identify pivot
  points, including potential RDS databases, for lateral movement in an AWS
  environment.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Remote Services]]'
sub_techniques: []
tags:
  - lateral-movement
  - aws-ec2
  - subnet-enumeration
  - rds
  - cloud
commands:
  - '[[commands/aws-ec2-describe-instances-by-subnet-id]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# List-EC2-Instances-in-Specific-Subnet-for-Lateral-Movement

## Summary

This procedure leverages the AWS CLI to query and list all EC2 instances running within a specified subnet, enabling attackers with compromised AWS credentials to map the network topology and identify potential targets for lateral movement, such as RDS database instances containing sensitive data.

## Description

In cloud environments like AWS, lateral movement often involves enumerating resources in specific VPC subnets to discover exploitable instances. An attacker who has obtained IAM credentials (e.g., via initial access to an EC2 instance or API key compromise) can use this technique to filter EC2 describe operations by subnet ID. This reveals instance details like IDs, types, states, and security groups, helping pinpoint RDS endpoints or other services for further pivoting, such as database credential extraction or remote execution. The procedure assumes the attacker has the necessary ec2:DescribeInstances permission and knows the target subnet ID, often obtained from prior reconnaissance like VPC enumeration.

## Requirements

1. AWS CLI installed and configured with access keys or role-based credentials that have ec2:DescribeInstances permission.
2. Knowledge of the target subnet ID (e.g., from previous VPC or subnet listing procedures).
3. Network access to AWS APIs (internet or VPC endpoint for private access).

## Defense

- Enforce least-privilege IAM policies to restrict DescribeInstances actions to specific subnets or resources.
- Enable AWS CloudTrail logging and monitor for unusual describe-instances API calls, especially filtered by subnet.
- Implement VPC network segmentation and security groups to limit visibility between subnets.
- Use AWS Config rules to alert on excessive enumeration activities.

## Objectives

1. Enumerate all EC2 instances in the specified subnet to map potential pivot points.
2. Identify RDS or other database instances for targeted lateral movement and data access.
3. Gather instance metadata to plan subsequent exploitation steps, such as SSH/RDP access or API pivoting.

## Instructions

### Step 1: Query EC2 Instances by Subnet ID

**Context**: This step uses the AWS CLI to filter and describe EC2 instances associated with a specific subnet, providing a list of running instances that could serve as lateral movement targets. The output includes critical details for further analysis, such as instance states and tags, allowing the attacker to prioritize active RDS resources.

**Command** ([[commands/aws-ec2-describe-instances-by-subnet-id]]):

```bash
aws ec2 describe-instances --filters "Name=subnet-id,Values=$_SUBNET_ID"
```

> Execute this command after substituting $_SUBNET_ID with the actual subnet identifier (e.g., subnet-0123456789abcdef0). The command queries the EC2 API and returns a JSON structure detailing reservations and instances. If the subnet contains RDS-related instances, look for tags like 'Database' or security groups allowing database ports (e.g., 3306 for MySQL). Verify success by checking for non-empty 'Reservations' array; if empty, the subnet may have no instances or permissions are insufficient.

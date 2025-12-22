---
id: 268328e1-6a95-4c0f-9183-20011e531eac
name: RDS-Security-Group-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.922701+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/RDS]]'
  - '[[tags/AWS]]'
  - '[[tags/Cloud Discovery]]'
commands:
  - '[[commands/aws-rds-describe-db-security-groups]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# RDS-Security-Group-Enumeration

## Summary

This procedure enumerates security groups associated with Amazon RDS database instances using the AWS CLI. It retrieves details such as security group names, descriptions, VPC IDs, and associated EC2 security groups, helping identify misconfigurations like overly permissive inbound rules that could expose databases to unauthorized access.

## Description

In cloud environments, attackers with compromised AWS credentials often perform discovery to map resources and identify weak points. This procedure focuses on RDS instances, which host relational databases, by querying their security groups. Security groups act as virtual firewalls, controlling inbound and outbound traffic. Enumerating them reveals rules that might allow excessive access, such as open ports from broad IP ranges (e.g., 0.0.0.0/0 on port 3306 for MySQL). The technique leverages the AWS RDS API via CLI to list these configurations without altering the environment. It is particularly useful in red team engagements simulating lateral movement in AWS or during audits to detect compliance issues. Prerequisites include AWS credentials with at least 'rds:DescribeDBSecurityGroups' permission. Expected outcomes include a JSON output detailing security group rules, which can be parsed for analysis.

## Requirements

1. AWS CLI installed and configured with credentials that have read access to RDS (e.g., IAM policy allowing 'rds:DescribeDBSecurityGroups' and 'rds:DescribeDBInstances').
2. Network access to AWS APIs (typically over HTTPS on port 443).
3. Knowledge of the target RDS DB instance identifier (DBInstanceIdentifier).
4. jq or similar tool for parsing JSON output (optional but recommended for filtering).

## Defense

- Implement least privilege IAM policies to restrict 'Describe' actions on RDS resources to authorized roles only.
- Use AWS Config rules to monitor and alert on permissive security group configurations (e.g., public access to databases).
- Enable AWS CloudTrail logging for RDS API calls and integrate with SIEM for anomaly detection, such as unusual enumeration from compromised credentials.
- Regularly audit security groups using AWS Trusted Advisor or automated scripts to enforce inbound rules limiting access to trusted CIDRs.

## Objectives

1. Retrieve detailed information about RDS DB security groups to identify potential misconfigurations.
2. Map associated EC2 security groups and VPCs for broader network discovery.
3. Support further analysis for vulnerabilities like open database ports or excessive permissions.

## Instructions

### Step 1: Verify AWS CLI Configuration and Permissions

**Context**: Ensure your AWS environment is set up correctly and you have the necessary permissions before querying RDS. This prevents errors due to misconfiguration.

Run the following to check your current AWS identity and test basic RDS access:

**Command** ([[commands/aws-sts-get-caller-identity]]):
```bash
aws sts get-caller-identity
```

> This command outputs your account details. If it fails, reconfigure credentials using `aws configure`. Expected output is a JSON with UserArn, Account, and UserId confirming access.

### Step 2: Enumerate RDS Security Groups

**Context**: Use the AWS CLI to describe security groups for a specific RDS DB instance. This step fetches the core data needed for analysis, including rules that could indicate exposure.

**Command** ([[commands/aws-rds-describe-db-security-groups]]):
```bash
aws rds describe-db-security-groups --db-instance-identifier $_DB_INSTANCE_ID --region $_REGION
```

> Replace $_DB_INSTANCE_ID with the target RDS instance name (e.g., mydbinstance) and $_REGION with the AWS region (e.g., us-east-1). This retrieves security group details. If no DBInstanceIdentifier is specified, it lists all, but for targeted enumeration, use the parameter. Expected output is a JSON array under 'DBSecurityGroups' with fields like DBSecurityGroupName, Description, VpcId, and EC2SecurityGroups (listing associated groups and rules).

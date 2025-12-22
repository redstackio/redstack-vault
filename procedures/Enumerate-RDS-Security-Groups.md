---
id: b0c79a94-571e-46cb-b350-62bba97dfd6e
name: Enumerate-RDS-Security-Groups
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.993100+00:00'
updated_at: '2023-05-25T20:09:40.796139+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - data-exfiltration
  - security-group-enumeration
  - aws-rds
commands:
  - '[[commands/aws-ec2-describe-security-groups]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Enumerate-RDS-Security-Groups

## Summary

This procedure uses the AWS CLI to query and retrieve detailed information about specified security groups associated with RDS instances, revealing inbound and outbound rules, IP permissions, and other configurations. It aids in assessing the security posture of RDS databases, identifying overly permissive rules that could enable unauthorized access, and planning targeted attacks such as lateral movement or data exfiltration in cloud environments.

## Description

In AWS, RDS instances are often protected by security groups that act as virtual firewalls, controlling traffic to and from the database. This procedure focuses on enumerating EC2 security groups (which can be associated with RDS via VPCs) to discover rules that allow access from unexpected sources, such as broad CIDR ranges or internal IPs. By querying the EC2 API, attackers with compromised credentials can map network access paths, identify misconfigurations like open ports (e.g., 3306 for MySQL), and exploit them for further compromise. This is particularly useful in post-exploitation scenarios where initial AWS access has been gained, allowing reconnaissance without direct RDS interaction. The output provides JSON data that can be parsed for vulnerabilities, such as unrestricted ingress on database ports.

## Requirements

1. AWS CLI installed and configured with credentials that have at least `ec2:DescribeSecurityGroups` permissions (e.g., via IAM role or access keys).
2. Network access to AWS APIs (internet or VPC endpoint for private environments).
3. Knowledge of the target security group ID (obtainable from prior enumeration like listing all groups).
4. jq or similar tool for parsing JSON output (optional but recommended for analysis).

## Defense

- Implement least-privilege IAM policies to restrict `DescribeSecurityGroups` API calls to authorized roles only.
- Enable AWS CloudTrail logging for EC2 and RDS APIs to monitor and alert on anomalous describe operations.
- Use security group rules with tight IP restrictions and regular audits via AWS Config or GuardDuty.
- Rotate credentials frequently and monitor for unusual API activity from compromised accounts.

## Objectives

1. Retrieve detailed configuration of specified RDS-associated security groups.
2. Identify permissive rules that expose database ports or allow unauthorized traffic.
3. Gather intelligence for planning attacks, such as exploiting open ingress rules for database access.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure your AWS environment is set up correctly to authenticate API calls. This step confirms access to EC2 services without errors.

Use the [[tools/AWS-CLI]] to check configuration:

```bash
aws sts get-caller-identity
```

> This command returns your AWS account details, user ARN, and session status. If it fails with authentication errors, reconfigure credentials using `aws configure`.

**Expected Output**: JSON with Account, UserId, and Arn fields confirming valid credentials.

### Step 2: Enumerate Security Group Details

**Context**: Query the EC2 API for the specified security group's rules, including inbound/outbound permissions, to map access controls.

Execute [[commands/aws-ec2-describe-security-groups]] with the target group ID:

```bash
aws ec2 describe-security-groups --group-ids $_GROUP_ID
```

> Replace $_GROUP_ID with the actual ID (e.g., sg-0123456789abcdef0). This retrieves comprehensive details like group name, description, VPC ID, and rule sets. Review IpPermissions for ingress (e.g., port 3306 from 0.0.0.0/0) and IpPermissionsEgress for outbound.

**Expected Output**: JSON array with SecurityGroup objects, including rules like {"IpProtocol": "tcp", "FromPort": 3306, "ToPort": 3306, "IpRanges": [{"CidrIp": "0.0.0.0/0"}]}. Success is indicated by HTTP 200 and populated data.

### Step 3: Analyze Output for Vulnerabilities

**Context**: Parse the JSON to identify risks, such as open ports or broad CIDR blocks, which could allow direct RDS access.

Pipe the output to jq for filtering (assuming jq is available):

```bash
aws ec2 describe-security-groups --group-ids $_GROUP_ID | jq '.SecurityGroups[0].IpPermissions[] | select(.FromPort == 3306)'
```

> This filters for MySQL port rules. Look for insecure configurations like public access or internal lateral movement paths. If no jq, manually inspect the JSON for IpRanges with 0.0.0.0/0 or unexpected sources.

**Expected Output**: Filtered JSON showing permissive rules, e.g., entries with wide CIDR ranges. No output indicates no matching rules or success in tight configurations.

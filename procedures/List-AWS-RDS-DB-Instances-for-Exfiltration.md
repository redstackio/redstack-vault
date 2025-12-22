---
id: 96f57a27-7aa5-49e7-9c14-218108ae37ab
name: List-AWS-RDS-DB-Instances-for-Exfiltration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.968596+00:00'
updated_at: '2023-04-10T20:19:50.611806+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud-Service-Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/AWS]]'
  - '[[tags/RDS]]'
  - '[[tags/Discovery]]'
  - '[[tags/Data exfiltration]]'
  - '[[tags/List instances in RDS]]'
  - '[[tags/RDS - Relational Database Service]]'
commands:
  - '[[commands/aws-rds-describe-db-instances]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# List-AWS-RDS-DB-Instances-for-Exfiltration

## Summary

This procedure enables an attacker with compromised AWS credentials to list all RDS DB instances in a target AWS account, revealing details such as engine types, endpoints, instance classes, and availability zones. This discovery step identifies potential targets for further exfiltration of sensitive data like user credentials or PII stored in the databases.

## Description

In a cloud compromise scenario, after obtaining AWS API credentials (e.g., via IAM role escalation or stolen access keys), an attacker uses the AWS CLI to query RDS resources. This reveals the infrastructure layout, allowing prioritization of high-value instances for subsequent attacks like SQL injection or unauthorized data dumps. The procedure assumes the attacker has sufficient permissions (e.g., rds:DescribeDBInstances) and focuses on enumeration as a precursor to exfiltration. It maps to MITRE ATT&CK for cloud environments where resource discovery facilitates lateral movement and data theft.

## Requirements

1. Valid AWS access key ID and secret access key with rds:DescribeDBInstances permission.
2. AWS CLI installed and configured on the attacker's system.
3. Network access to AWS endpoints (no VPC restrictions blocking CLI calls).

## Defense

- Implement least privilege access for IAM users/roles, restricting DescribeDBInstances to necessary personnel.
- Enable AWS CloudTrail logging for API calls and monitor for unusual RDS queries from unexpected IPs.
- Use AWS Config rules to alert on unauthorized RDS access and implement network segmentation with VPC endpoints.

## Objectives

1. Enumerate all RDS DB instances in the target AWS account to identify potential data stores.
2. Extract instance details like endpoints and engine types for targeting in exfiltration attempts.
3. Validate the output to confirm access to sensitive cloud resources.

## Instructions

### Step 1: Configure AWS CLI Credentials

**Context**: Ensure the AWS CLI is set up with the compromised credentials to authenticate API calls. This step verifies connectivity before querying RDS.

**Command** ([[commands/aws-configure-set-credentials]]):
```bash
aws configure set aws_access_key_id $_ACCESS_KEY_ID
aws configure set aws_secret_access_key $_SECRET_ACCESS_KEY
aws configure set default.region $_REGION
```

> This sets the credentials and default region (e.g., us-east-1). Expected output is no errors, confirming configuration. Test with `aws sts get-caller-identity` to verify identity.

### Step 2: List All RDS DB Instances

**Context**: Use the describe-db-instances command to retrieve a comprehensive list of RDS instances, including identifiers, statuses, and endpoints. This reveals the attack surface for data exfiltration.

**Command** ([[commands/aws-rds-describe-db-instances]]):
```bash
aws rds describe-db-instances
```

> Run this to output JSON with DB instance details. If no filters are used, it lists all instances. Expected output includes an array of DBInstances with fields like DBInstanceIdentifier, Engine, Endpoint.Address, and DBInstanceStatus.

### Step 3: Filter and Parse Output for Targets

**Context**: Apply filters to narrow results (e.g., by status or engine) and pipe to jq for readable extraction of key details like endpoints, which can be used for direct connections or further attacks.

**Command** ([[commands/aws-rds-describe-db-instances-with-filters]]):
```bash
aws rds describe-db-instances --filters "Name=status,Values=available" --query 'DBInstances[*].[DBInstanceIdentifier,Endpoint.Address,Engine]' --output table
```

> This filters for available instances and queries specific fields. Expected output is a table of instance IDs, endpoints, and engines, helping identify active databases for exfiltration.

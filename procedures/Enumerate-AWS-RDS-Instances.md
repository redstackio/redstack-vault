---
id: a5bd50e5-99d9-4e74-b856-92f73a249e21
name: Enumerate-AWS-RDS-Instances
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.879764+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/AWS-RDS]]'
  - '[[tags/Cloud-Discovery]]'
commands:
  - '[[commands/aws-rds-describe-db-instances]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-AWS-RDS-Instances

## Summary

This procedure uses the AWS CLI to query and list all RDS database instances in a specified AWS region, revealing details such as instance identifiers, engine types, status, endpoints, and other configuration information. It is useful for attackers with compromised AWS credentials to map the cloud environment and identify potential database targets for further exploitation, such as unauthorized access or data exfiltration.

## Description

In an AWS environment, RDS (Relational Database Service) instances host managed databases like MySQL, PostgreSQL, or SQL Server. Enumerating these instances provides an attacker with visibility into the target's database infrastructure, including availability, connectivity endpoints, and versions that may indicate vulnerabilities. This technique leverages the AWS RDS API via the CLI to perform discovery without direct network access to the instances themselves. It is typically executed after initial credential compromise and is part of broader cloud reconnaissance. The output is in JSON format, which can be parsed for automated follow-on actions like targeting specific instances with weak configurations.

## Requirements

1. Valid AWS credentials (access key and secret key) with at least `rds:DescribeDBInstances` permissions.
2. Network access to AWS endpoints (internet or VPC connectivity).
3. AWS CLI installed and configured with the target account credentials using `aws configure`.
4. Specify the AWS region where RDS instances exist (default is the configured region).

## Defense

- Monitor AWS CloudTrail logs for `DescribeDBInstances` API calls, alerting on unusual volumes or from unexpected IP addresses.
- Implement IAM least privilege policies, restricting `rds:DescribeDBInstances` to only necessary roles and auditing permission elevations.
- Use AWS Config rules to detect over-permissive IAM policies and enable guardrails like AWS Organizations SCPs to limit RDS actions.

## Objectives

1. Discover all RDS instances in the target AWS region to map database assets.
2. Extract key details like endpoints and engine versions for vulnerability assessment.
3. Identify active or misconfigured instances as potential entry points for lateral movement or data theft.

## Instructions

### Step 1: Configure AWS CLI and Verify Access

**Context**: Ensure the AWS CLI is set up with credentials that have RDS read permissions. This step verifies connectivity and lists available regions if needed.

Run the AWS CLI configuration command if not already done:

```bash
aws configure
```

> Enter your access key, secret key, default region (e.g., us-east-1), and output format (json).

Then, test access with a basic RDS command:

**Command** ([[commands/aws-rds-describe-db-instances]]):
```bash
aws rds describe-db-instances --max-records 1
```

> This fetches a limited set of instances to confirm permissions without retrieving all data. If successful, proceed; if denied, check IAM policies.

### Step 2: Enumerate All RDS Instances in the Region

**Context**: Query the full list of RDS instances to gather comprehensive details. Use filters if targeting specific instances, but start with a broad query for discovery.

**Command** ([[commands/aws-rds-describe-db-instances]]):
```bash
aws rds describe-db-instances
```

> This command returns JSON output with an array of DBInstance objects. Each includes fields like DBInstanceIdentifier, Engine, DBInstanceStatus, Endpoint.Address, AllocatedStorage, and DBInstanceClass. Pipe to `jq` for parsing if needed (e.g., `| jq '.DBInstances[].DBInstanceIdentifier'`).

If filtering by instance name:

```bash
aws rds describe-db-instances --db-instance-identifier $_DB_INSTANCE_ID
```

> Replace $_DB_INSTANCE_ID with a known identifier from prior recon. This narrows results to one instance.

### Step 3: Apply Filters for Targeted Enumeration

**Context**: Use filters to refine results based on criteria like status or engine type, helping prioritize active or vulnerable instances.

**Command** ([[commands/aws-rds-describe-db-instances]]):
```bash
aws rds describe-db-instances --filters Name=db-instance-id,Values=$_DB_INSTANCE_ID Name=engine,Values=mysql
```

> This example filters for MySQL instances matching a specific ID. Common filters include 'status' (e.g., available), 'engine' (e.g., postgres), or 'db-cluster-id' for Aurora. Review the full list with `aws rds describe-db-instances help`.

### Step 4: Parse and Export Results

**Context**: Process the JSON output to extract actionable intelligence, such as saving endpoints for connection testing.

Use `jq` to filter key fields:

```bash
aws rds describe-db-instances | jq '.DBInstances[] | {Identifier: .DBInstanceIdentifier, Endpoint: .Endpoint.Address, Engine: .Engine, Status: .DBInstanceStatus}'
```

> Export to a file for further analysis: `> rds_enum.json`. Look for public endpoints or outdated engines indicating risks.

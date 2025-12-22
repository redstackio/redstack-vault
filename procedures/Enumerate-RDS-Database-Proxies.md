---
id: b310c5d2-3a71-405e-b7ba-ced1a12d5fb5
name: Enumerate-RDS-Database-Proxies
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.943596+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/RDS]]'
  - '[[tags/AWS]]'
  - '[[tags/Cloud-Discovery]]'
commands:
  - '[[commands/aws-rds-describe-db-proxies]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-RDS-Database-Proxies

## Summary

This procedure uses the AWS CLI to list all RDS database proxies in the target AWS account, providing details such as proxy endpoints, engine families, VPC security groups, and connected database instances. It aids in discovering the database infrastructure for offensive reconnaissance to identify potential attack vectors like credential brute-forcing or vulnerability exploitation, or for defensive auditing to detect unauthorized proxies.

## Description

RDS Database Proxies act as intermediaries for database connections in AWS, enhancing security and scalability. Enumerating them reveals the structure of the database environment, including proxy names, statuses, endpoints, and associated resources. In an offensive context, this information helps attackers map the target infrastructure, pinpoint weakly secured proxies, or identify misconfigurations that could lead to lateral movement or data access. Defensively, regular enumeration can baseline normal configurations and alert on anomalies like unexpected proxies. The procedure relies on AWS credentials with read access to RDS and assumes the AWS CLI is configured with the appropriate profile and region.

## Requirements

1. AWS CLI installed and configured with credentials that have at least `rds:DescribeDBProxies` permissions (e.g., via IAM policy attached to the user/role).
2. Network access to AWS APIs (typically over HTTPS on port 443).
3. Target AWS region specified if not using the default.
4. Basic familiarity with JSON output parsing for analysis.

## Defense

- Implement least-privilege IAM policies to restrict `DescribeDBProxies` actions to authorized users only.
- Enable AWS CloudTrail logging for RDS API calls to monitor and audit enumeration attempts.
- Use AWS Config rules to detect and alert on unauthorized RDS proxy creations or accesses.
- Segment network access with VPC endpoints or security groups to limit API exposure.

## Objectives

1. Retrieve a comprehensive list of all RDS database proxies in the account.
2. Identify key details like endpoints and security groups for further targeting or auditing.
3. Validate proxy configurations to spot potential security gaps.

## Instructions

### Step 1: Configure AWS CLI and Verify Access

**Context**: Ensure the AWS CLI is set up with valid credentials and test basic RDS access to avoid errors during enumeration.

Run the AWS CLI configure command if not already done, or verify with a simple RDS list command.

**Command** ([[commands/aws-rds-describe-db-instances]]):
```bash
aws rds describe-db-instances --max-records 1
```

> This tests permissions without listing all proxies. Expected output is a JSON array with at least one DB instance if access is granted; errors indicate permission issues.

### Step 2: Enumerate All RDS Database Proxies

**Context**: Execute the core enumeration to fetch details on all proxies, which provides visibility into the database proxy setup.

Use the describe-db-proxies command to list all proxies in the current region.

**Command** ([[commands/aws-rds-describe-db-proxies]]):
```bash
aws rds describe-db-proxies
```

> This returns a JSON object containing an array of proxy details, including `DBProxyName`, `Status`, `Endpoint`, `EngineFamily`, `VpcSecurityGroupIds`, and `Associated DB instances`. If no proxies exist, an empty array is returned. Pipe to `jq` for better readability: `aws rds describe-db-proxies | jq '.DBProxies[] | {DBProxyName, Endpoint, VpcSecurityGroupIds}'`.

### Step 3: Analyze Output for Specific Proxies (Optional)

**Context**: If targeting a specific proxy, refine the query; otherwise, review the full list for anomalies.

For a named proxy, add the `--db-proxy-name` parameter.

**Command** ([[commands/aws-rds-describe-db-proxies]]):
```bash
aws rds describe-db-proxies --db-proxy-name my-proxy-name
```

> Narrows output to the specified proxy's details. Success is confirmed by non-empty JSON with matching proxy info.

---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - AWS
  - CloudTrail
  - Discovery
  - List-Trails
commands:
  - '[[commands/aws-cloudtrail-list-trails]]'
platforms:
  - AWS
tools: []
validated: true
---

# List-AWS-CloudTrail-Trails

## Summary

This procedure uses the AWS CLI to list all CloudTrail trails in the targeted AWS account, enabling discovery of logging configurations that record API calls and user activities. It provides attackers with insights into account actions, potential misconfigurations, and targets for further exploitation in cloud environments.

## Description

CloudTrail is AWS's service for logging API calls and account activity. Listing trails reveals the names, ARNs, home regions, and other details of active logging trails, which can expose historical actions, identify high-value resources, or highlight gaps in monitoring. This technique is useful during initial reconnaissance in compromised AWS accounts to map the environment and plan lateral movement or persistence. It requires AWS credentials with read access to CloudTrail but does not retrieve actual log events—only trail metadata. In an attack scenario, this helps identify if sensitive actions like IAM changes or S3 access are being logged, informing stealthier subsequent operations.

## Requirements

1. AWS CLI installed and configured with valid credentials (e.g., access key and secret key) that have permissions to call `cloudtrail:ListTrails` (typically `ReadOnlyAccess` or specific CloudTrail read policies).
2. Network access to AWS endpoints (no VPC restrictions blocking CLI calls).
3. Configured AWS profile if using multiple accounts (e.g., via `aws configure`).

## Defense

- Implement least privilege by restricting `cloudtrail:ListTrails` to only necessary roles and monitoring its usage via CloudTrail itself.
- Enable AWS CloudTrail organization-wide with multi-region logging and integrate with Amazon GuardDuty or SIEM for anomaly detection on trail enumeration attempts.
- Use IAM policies to deny listing trails for untrusted principals and rotate credentials regularly.

## Objectives

1. Enumerate all CloudTrail trails to understand logging coverage in the AWS account.
2. Identify trail configurations (e.g., S3 buckets, regions) for potential log access or manipulation.
3. Gather intelligence on past API activities to select targets for escalation or exfiltration.

## Instructions

### Step 1: Execute Trail Listing

**Context**: This step queries the AWS CloudTrail service to retrieve a list of all configured trails. It provides metadata like trail names and ARNs, which can be used to further query logs or assess logging gaps. Run this from a machine with AWS CLI access after assuming a role or using credentials in the target account.

**Command** ([[commands/aws-cloudtrail-list-trails]]):
```bash
aws cloudtrail list-trails
```

> This command returns a JSON response with trail details. If multiple trails exist, review the output for names and home regions. For large accounts, consider pagination with `--max-items` or `--starting-token` if needed, though the default handles most cases. Success is indicated by a non-empty `Trails` array in the JSON.

### Step 2: Parse and Analyze Output

**Context**: Review the JSON output to extract actionable intelligence, such as trail ARNs for subsequent log retrieval (e.g., via `get-trail-status` or S3 access). Pipe to `jq` for filtering if available.

**Command** ([[commands/aws-cloudtrail-list-trails]]):
```bash
aws cloudtrail list-trails | jq '.Trails[] | {Name: .Name, HomeRegion: .HomeRegion}'
```

> Filters the output to show trail names and regions. Look for trails logging management events or data events on critical services like IAM or S3. If no trails are returned, logging may be disabled, indicating a defense weakness.

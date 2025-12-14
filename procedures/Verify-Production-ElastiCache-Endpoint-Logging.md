---
tags:
  - aws
  - elasticache
  - cloudtrail
  - logging
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-elasticache-describe-users]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1087.004]]'
updated_at: '2025-12-14T17:32:28.935Z'
skill_level: intermediate
impact_level: low
detection_risk: high
sub_techniques: []
id: 9ca99723-2dd8-4b35-b780-596d28242475
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Verify-Production-ElastiCache-Endpoint-Logging

## Summary

This procedure tests a standard production AWS ElastiCache API call to confirm it generates logs in CloudTrail, establishing the baseline for detecting normal activity versus stealthy operations.

## Description

In an AWS environment with CloudTrail enabled, execute an ElastiCache API operation using AWS CLI with a privileged IAM role. The call will succeed and produce a log event in CloudTrail after a short delay, allowing verification of logging functionality. This step is crucial for contrasting with non-logged endpoints in subsequent reconnaissance.

## Requirements

1. AWS CLI installed and configured with IAM credentials having ElastiCache read permissions
2. CloudTrail trail configured and active for the region
3. Access to CloudTrail logs (via console or S3)

## Defense

Defensive measures and detection strategies:

- Ensure all API endpoints are monitored via CloudTrail
- Implement alerts for ElastiCache API calls
- Regularly audit IAM permissions and log completeness

## Objectives

1. Confirm production API logging behavior
2. Validate IAM permissions for ElastiCache operations
3. Baseline for identifying logging gaps

## Instructions

### Step 1: Execute Production API Call

**Context**: Run a describe-users command to trigger a logged event.

**Command** ([[commands/aws-elasticache-describe-users]]):
```bash
aws elasticache describe-users
```

> This command queries ElastiCache users and generates a CloudTrail event. Expected output: JSON with user ARNs and details if permitted.

### Step 2: Verify CloudTrail Log

**Context**: Check for the log entry to confirm detection.

**Command** (Manual check via AWS Console or CLI):
```bash
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventSource,AttributeValue=elasticache.amazonaws.com
```

> Wait 5-10 minutes; expected output: Event list including the describe-users call.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1087.004]] Cloud Account

### Sub-Techniques

- None

## Commands Used

- [[commands/aws-elasticache-describe-users]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- elasticache
- cloudtrail

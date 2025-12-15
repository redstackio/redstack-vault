---
id: proc-uuid-001
tags:
  - aws
  - ssm
  - cloudtrail
  - logging
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-ssm-describe-instance-properties-production]]'
  - '[[commands/export-aws-profile-admin]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1087.004]]'
updated_at: '2025-12-14T17:32:20.870Z'
skill_level: intermediate
impact_level: low
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Demonstrate Normal CloudTrail Logging with SSM API

## Summary

This procedure executes a standard AWS SSM API call on production endpoints to verify that CloudTrail logs the event normally, providing a baseline for comparison with unlogged non-production calls.

## Description

In an AWS environment with SSM and CloudTrail enabled, use AWS CLI to invoke an SSM action like DescribeInstanceProperties. The call generates a log in CloudTrail after a delay, allowing detection of API activity. This step is crucial for confirming logging behavior before testing evasion techniques on non-production endpoints. Prerequisites include AWS CLI installed, configured profiles, and access to us-west-2 region.

## Requirements

1. AWS CLI v2 installed and configured with IAM credentials.
2. CloudTrail trail active in the target region.
3. IAM role with SSM read permissions (e.g., admin profile).
4. Access to AWS Management Console for log verification.

## Defense

Defensive measures and detection strategies:

- Monitor CloudTrail for SSM API events using AWS GuardDuty or CloudWatch alarms.
- Enforce least-privilege IAM policies to limit SSM actions.

## Objectives

1. Confirm standard logging for SSM calls.
2. Baseline response times and log delays.
3. Identify detectable permission failures.

## Instructions

### Step 1: Set Admin Profile

**Context**: Prepare AWS CLI with elevated permissions for the test call.

**Command** ([[commands/export-aws-profile-admin]]):
```bash
export AWS_PROFILE=admin
```

> Sets the environment to use an admin IAM profile. Expected output: Environment variable updated (no visible output).

### Step 2: Execute SSM API Call

**Context**: Invoke DescribeInstanceProperties to trigger logging.

**Command** ([[commands/aws-ssm-describe-instance-properties-production]]):
```bash
aws ssm describe-instance-properties --region us-west-2
```

> Calls the SSM API on production endpoint. Expected output: JSON response with instance properties or success message; check CloudTrail after 5-10 minutes for log entry.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1087.004]] Cloud Account

### Sub-Techniques


## Commands Used

- [[commands/export-aws-profile-admin]]
- [[commands/aws-ssm-describe-instance-properties-production]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- ssm
- baseline

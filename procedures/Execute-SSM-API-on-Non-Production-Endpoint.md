---
id: proc-uuid-002
tags:
  - aws
  - ssm
  - evasion
  - non-production
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/aws-ssm-describe-instance-properties-nonprod]]'
  - '[[commands/export-aws-profile-admin]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:32:20.868Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Execute SSM API on Non-Production Endpoint

## Summary

This procedure calls an SSM API using a non-production endpoint URL, which fails to log to CloudTrail, enabling silent testing of IAM permissions based on response differences.

## Description

Non-production endpoints in AWS SSM, such as redacted URLs like ██████, do not forward API calls to CloudTrail due to design choices or internal dependencies (e.g., on EC2 actions). Using --endpoint-url in AWS CLI, adversaries can probe permissions: success or AccessDeniedException reveals privilege levels without logs. This evades detection reliant on failed call logs. Limited to no customer data access.

## Requirements

1. AWS CLI configured with test profiles (privileged and unprivileged).
2. Knowledge of non-production endpoint URLs (internal or discovered).
3. CloudTrail access to confirm absence of logs.
4. us-west-2 region permissions.

## Defense

Defensive measures and detection strategies:

- Block or monitor custom --endpoint-url usage in AWS CLI via proxy or endpoint policies.
- Implement SSM endpoint validation to reject non-production URLs.
- Use AWS Config to audit IAM policy attachments.

## Objectives

1. Perform undetectable permission checks.
2. Compare responses across privilege levels.
3. Confirm logging evasion.

## Instructions

### Step 1: Set Test Profile

**Context**: Use a profile to simulate compromised credentials.

**Command** ([[commands/export-aws-profile-admin]]):
```bash
export AWS_PROFILE=admin
```

> Configures CLI for privileged testing. Expected output: Silent success.

### Step 2: Call Non-Production Endpoint

**Context**: Execute the API to test silent enumeration.

**Command** ([[commands/aws-ssm-describe-instance-properties-nonprod]]):
```bash
aws ssm describe-instance-properties --region us-west-2 --endpoint-url ██████
```

> Probes the endpoint. Expected output: Success response for permitted, AccessDeniedException for denied; no CloudTrail log after 5-10 minutes.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools

### Sub-Techniques


## Commands Used

- [[commands/export-aws-profile-admin]]
- [[commands/aws-ssm-describe-instance-properties-nonprod]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- enumeration
- silent

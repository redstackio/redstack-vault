---
id: proc-verify-logging-001
tags:
  - aws
  - cloudtrail
  - logging
  - verification
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-devicefarm-get-account-settings-production]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1087.004]]'
updated_at: '2025-12-14T17:32:20.650Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Verify-Normal-CloudTrail-Logging-with-Production-Endpoint

## Summary

This procedure tests a standard AWS Device Farm API call using production endpoints to confirm that it generates logs in CloudTrail, providing a baseline for identifying logging gaps in non-production interfaces.

## Description

In an AWS environment, production API endpoints for services like Device Farm log all calls to CloudTrail for auditing and detection. This procedure simulates a legitimate operation with privileged IAM credentials to verify logging behavior, which is crucial for contrasting with silent non-production endpoints. It requires AWS CLI access and involves waiting for log propagation.

## Requirements

1. AWS CLI installed and configured with IAM credentials having Device Farm read permissions (e.g., devicefarm:GetAccountSettings)
2. Access to us-west-2 region
3. Ability to query CloudTrail logs via AWS console or CLI
4. Wait time of 5-10 minutes for log appearance

## Defense

Defensive measures and detection strategies:

- Enable comprehensive CloudTrail logging across all regions and services
- Monitor for anomalous Device Farm API calls in logs
- Implement IAM policies with least privilege to limit permission testing

## Objectives

1. Confirm production endpoint logging to CloudTrail
2. Validate IAM permissions for Device Farm operations
3. Establish baseline for logging evasion detection

## Instructions

### Step 1: Execute Production API Call

**Context**: Run the AWS CLI command to fetch Device Farm account settings, which triggers a logged event if permissions allow.

**Command** ([[commands/aws-devicefarm-get-account-settings-production]]):
```bash
aws devicefarm get-account-settings --region us-west-2
```

> This command queries the production endpoint. Expected output is a JSON object with account details. If successful, it confirms permissions and initiates logging.

### Step 2: Verify CloudTrail Log

**Context**: Check for the log entry to ensure normal behavior.

**Command** (AWS CLI for logs, optional):
```bash
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventSource,AttributeValue=devicefarm.amazonaws.com --region us-west-2
```

> Wait 5-10 minutes post-execution. Successful log verification shows an event with eventName: GetAccountSettings.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1087.004]] Cloud Account

### Sub-Techniques


## Commands Used

- [[commands/aws-devicefarm-get-account-settings-production]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- cloudtrail
- logging

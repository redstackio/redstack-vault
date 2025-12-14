---
id: proc-test-silent-001
tags:
  - aws
  - devicefarm
  - non-production
  - logging-bypass
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-devicefarm-get-account-settings-non-production]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1087.004]]'
  - '[[Disable or Modify Cloud Firewall]]'
updated_at: '2025-12-14T17:32:20.645Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
  - '[[Disable or Modify Cloud Firewall]]'
---
# Test-Non-Production-Endpoint-for-Silent-API-Calls

## Summary

This procedure exploits non-production API endpoints in AWS Device Farm to perform operations that enforce IAM permissions but do not log to CloudTrail, enabling silent testing of access rights.

## Description

Non-production endpoints in AWS Device Farm, accessible via the --endpoint-url flag in AWS CLI, behave like production ones for permission checks but skip CloudTrail logging. This allows adversaries to probe IAM capabilities without detection, ideal for reconnaissance in compromised credential scenarios. The procedure uses a known redacted endpoint and requires waiting to confirm log absence.

## Requirements

1. AWS CLI with IAM credentials potentially lacking or having Device Farm permissions
2. Knowledge of non-production endpoint URL (e.g., redacted as https://nonprod.devicefarm.us-west-2.amazonaws.com)
3. Access to CloudTrail for negative verification
4. Extended wait time (5-10+ minutes) to rule out delayed logging

## Defense

Defensive measures and detection strategies:

- Audit and disable or monitor non-production endpoints
- Implement endpoint-specific logging or WAF rules
- Use AWS Config to detect unusual endpoint overrides in CLI usage
- Correlate IAM activity with other logs (e.g., S3 access logs)

## Objectives

1. Perform API call without CloudTrail logging
2. Observe IAM permission enforcement on non-production endpoint
3. Confirm evasion of standard monitoring

## Instructions

### Step 1: Override Endpoint and Execute Call

**Context**: Use the --endpoint-url to target the non-production interface, testing if the call succeeds or fails based on permissions.

**Command** ([[commands/aws-devicefarm-get-account-settings-non-production]]):
```bash
aws devicefarm get-account-settings --region us-west-2 --endpoint-url https://nonprod.devicefarm.us-west-2.amazonaws.com
```

> Response is JSON if permitted or an error like AccessDenied. This tests permissions silently.

### Step 2: Confirm No Logging

**Context**: Monitor CloudTrail to ensure no event is recorded.

**Command** (AWS CLI for logs):
```bash
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventSource,AttributeValue=devicefarm.amazonaws.com --region us-west-2
```

> After 5-10 minutes or longer, absence of GetAccountSettings event confirms the bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1087.004]] Cloud Account
- [[Disable or Modify Cloud Firewall]] Disable or Modify Tools (for logging impairment)

### Sub-Techniques


## Commands Used

- [[commands/aws-devicefarm-get-account-settings-non-production]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- devicefarm
- silent-testing

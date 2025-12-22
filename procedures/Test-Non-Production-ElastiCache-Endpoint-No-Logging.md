---
tags:
  - aws
  - elasticache
  - logging-bypass
  - evasion
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/aws-elasticache-describe-users-nonprod]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable Cloud Logs]]'
updated_at: '2025-12-14T17:32:28.930Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e9ad5b17-91ab-4798-b42e-481504c9b89a
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable Cloud Logs]]'
---
# Test-Non-Production-ElastiCache-Endpoint-No-Logging

## Summary

This procedure exploits a non-production ElastiCache endpoint by overriding the API URL in AWS CLI calls, confirming that permission checks occur without CloudTrail logging, enabling undetected testing.

## Description

The non-production endpoint for ElastiCache enforces IAM policies but skips CloudTrail integration. Using the --endpoint-url flag, API calls like describe-users are processed silently, returning success or AccessDenied based on credentials. This reveals logging deficiencies without accessing data.

## Requirements

1. Knowledge of the non-production endpoint URL (e.g., ███████)
2. AWS CLI with IAM credentials
3. CloudTrail access for verification of absence

## Defense

Defensive measures and detection strategies:

- Monitor for unusual endpoint overrides in network traffic
- Audit all ElastiCache endpoints for logging parity
- Implement proxy logging for API calls

## Objectives

1. Bypass CloudTrail logging via custom endpoint
2. Validate IAM enforcement without detection
3. Identify stealthy reconnaissance opportunities

## Instructions

### Step 1: Execute API Call with Custom Endpoint

**Context**: Override the endpoint to test non-logged behavior.

**Command** ([[commands/aws-elasticache-describe-users-nonprod]]):
```bash
aws elasticache describe-users --endpoint-url ███████
```

> Command processes via non-production endpoint; expected output: JSON or AccessDenied, no CloudTrail event.

### Step 2: Confirm No Logging

**Context**: Verify absence of logs to confirm evasion.

**Command** (Check CloudTrail):
```bash
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventSource,AttributeValue=elasticache.amazonaws.com --start-time $(date -u -d '5 minutes ago' +%Y-%m-%dT%H:%M:%SZ)
```

> Expected output: No events for the call.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Disable Cloud Logs]] Disable or Modify Tools

### Sub-Techniques

- None

## Commands Used

- [[commands/aws-elasticache-describe-users-nonprod]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- evasion
- logging-bypass

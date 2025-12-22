---
tags:
  - aws
  - datazone
  - endpoint-bypass
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/aws-datazone-list-domains-nonprod]]'
techniques:
  - '[[Disable Cloud Logs]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8310fbc1-3d7b-4934-be0d-93e9747b56dd
created_at: '2025-12-14T17:32:39.039Z'
updated_at: '2025-12-14T17:32:39.039Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable Cloud Logs]]'
---
# Test-Non-Production-Datazone-Endpoint

## Summary

This procedure tests a non-production API endpoint for AWS Datazone using the --endpoint-url flag to perform calls without CloudTrail logging, enabling stealthy operations.

## Description

Non-production endpoints (e.g., 44 redacted URLs with test or employee aliases) enforce IAM but skip logging. Using AWS CLI, override the endpoint to invoke list-domains, revealing permissions via responses without audit trails. This exploits design for internal testing; prerequisites include known non-prod URLs and configured CLI.

## Requirements

1. AWS CLI with IAM credentials.
2. Redacted non-production endpoint URL (e.g., from reconnaissance).
3. Basic understanding of AWS API structures.

## Defense

Defensive measures and detection strategies:

- Disable or monitor access to non-production endpoints.
- Implement endpoint URL validation in IAM policies.
- Use AWS Config to track endpoint usage anomalies.

## Objectives

1. Bypass CloudTrail logging.
2. Maintain IAM enforcement for realistic testing.
3. Observe API responses without detection.

## Instructions

### Step 1: Invoke API on Non-Prod Endpoint

**Context**: Use the endpoint override to target unlogged URL.

**Command** ([[commands/aws-datazone-list-domains-nonprod]]):
```bash
aws datazone list-domains --endpoint-url <redacted>
```

> The --endpoint-url parameter routes the call to non-prod (redacted). Expected output: JSON domains list or AccessDeniedException; no CloudTrail event.

### Step 2: Analyze Response

**Context**: Evaluate for permission insights.

**Command** (No command; analysis):

> Compare to production response for differences.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Disable Cloud Logs]]

### Sub-Techniques


## Commands Used

- [[commands/aws-datazone-list-domains-nonprod]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- evasion
- non-production

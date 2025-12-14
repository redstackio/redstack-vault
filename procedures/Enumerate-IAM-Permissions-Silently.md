---
id: proc-uuid-3
tags:
  - iam
  - discovery
  - aws
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-forecast-list-datasets-nonprod]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:39.606Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate-IAM-Permissions-Silently

## Summary

This procedure uses unlogged non-production endpoints to test multiple AWS Forecast API operations, mapping IAM permissions based on success/failure responses without triggering CloudTrail alerts.

## Description

With compromised credentials, systematically call various Forecast APIs (e.g., list-datasets, create-forecast) via non-production endpoints. Responses indicate permission levels, enabling attackers to discover access rights stealthily across services.

## Requirements

1. List of target API operations for Forecast
2. Scriptable AWS CLI or automation for iteration
3. Redacted non-production endpoint access

## Defense

Defensive measures and detection strategies:

- Block non-production endpoint calls via VPC endpoints or proxies
- Use AWS Config to monitor IAM policy changes
- Implement anomaly detection on API call volumes

## Objectives

1. Map IAM permissions for Forecast operations
2. Avoid detection through logging bypass
3. Expand reconnaissance to other unlogged endpoints

## Instructions

### Step 1: Iterate Over API Operations

**Context**: Test permissions by varying operations on non-production endpoint.

**Command** ([[commands/aws-forecast-list-datasets-nonprod]] adapted):
```bash
aws forecast describe-forecast --region us-west-2 --endpoint-url ███████ --forecast-arn arn:aws:forecast:us-west-2:123456789012:forecast/example
```

> Success grants permission; AccessDenied reveals denial. Log responses manually.

### Step 2: Analyze Responses for Permission Mapping

**Context**: Compile results to infer full access scope.

No specific command; parse outputs for patterns like "User is not authorized".

> Build a permission matrix from multiple tests.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/aws-forecast-list-datasets-nonprod]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- iam
- discovery

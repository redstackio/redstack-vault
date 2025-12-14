---
tags:
  - aws
  - datazone
  - cloudtrail
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-datazone-list-domains]]'
techniques:
  - '[[T1087.004]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d8f1d95d-0158-484b-a0cc-4233233500bd
created_at: '2025-12-14T17:32:39.045Z'
updated_at: '2025-12-14T17:32:39.045Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Verify-Normal-Datazone-API-Logging

## Summary

This procedure establishes a baseline by executing a standard AWS Datazone API call on the production endpoint to confirm that it generates CloudTrail logs, highlighting normal logging behavior before testing evasion techniques.

## Description

In an AWS environment with Datazone and CloudTrail enabled, this step verifies that legitimate API interactions are auditable. It uses the AWS CLI to invoke the list-domains operation, which should succeed or fail based on IAM permissions and log the event. This is crucial for contrasting with unlogged non-production calls, allowing attackers to identify logging gaps. Prerequisites include AWS CLI setup with valid credentials and CloudTrail trails configured for the region.

## Requirements

1. AWS CLI installed and configured with IAM credentials having Datazone access.
2. CloudTrail enabled and delivering logs to a trail or S3 bucket.
3. Access to AWS console or CLI for log monitoring.

## Defense

Defensive measures and detection strategies:

- Ensure all API endpoints, including non-production, route through logged services.
- Monitor for anomalous API call patterns via CloudTrail Insights or GuardDuty.
- Implement least-privilege IAM policies to limit Datazone access.

## Objectives

1. Confirm production endpoint logging functionality.
2. Baseline API response for permission checks.
3. Prepare for comparison with unlogged endpoints.

## Instructions

### Step 1: Execute Production API Call

**Context**: Perform the list-domains operation on the default production endpoint to trigger logging.

**Command** ([[commands/aws-datazone-list-domains]]):
```bash
aws datazone list-domains
```

> This command queries the Datazone service for domains. Expected output includes a JSON list of domains if permitted, or an AccessDeniedException if not; a CloudTrail event is generated asynchronously.

### Step 2: Note Response for Baseline

**Context**: Record the API response to compare with non-production tests.

**Command** (No specific command; manual observation):

> Observe the output for success/failure indicators tied to IAM permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1087.004]]

### Sub-Techniques


## Commands Used

- [[commands/aws-datazone-list-domains]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- datazone
- logging

---
tags:
  - aws
  - endpoint-bypass
  - stealth
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/aws-docdb-elastic-list-cluster-snapshots-non-production]]'
platforms:
  - AWS
techniques:
  - '[[Disable Cloud Logs]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a887bcea-e782-4f3d-804f-151b3e873602
created_at: '2025-12-14T17:32:29.155Z'
updated_at: '2025-12-14T17:32:29.155Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable Cloud Logs]]'
---
# Invoke-Non-Production-Endpoint

## Summary

This procedure targets a non-production API endpoint for AWS DocumentDB Elastic using AWS CLI, demonstrating that calls are processed with IAM checks but not logged to CloudTrail, enabling stealthy operations.

## Description

Non-production endpoints for DocumentDB Elastic, intended for internal or testing use, accept standard IAM-authenticated requests but lack CloudTrail integration. By overriding the endpoint URL, attackers can perform API actions without audit trails, ideal for evading monitoring during reconnaissance. The procedure replicates a list operation and confirms the logging gap.

## Requirements

1. Knowledge of non-production endpoint URL (e.g., from documentation or discovery)
2. AWS CLI with IAM credentials
3. DocumentDB Elastic service availability
4. CloudTrail access for verification of absence

## Defense

Defensive measures and detection strategies:

- Restrict IAM policies to production endpoints only
- Monitor for unusual endpoint URL overrides in network traffic
- Implement endpoint-specific logging proxies or WAF rules

## Objectives

1. Bypass CloudTrail logging while retaining API functionality
2. Test IAM authorization on non-production paths
3. Validate stealth for subsequent enumeration

## Instructions

### Step 1: Override Endpoint and Invoke API

**Context**: Direct the request to the non-production endpoint to avoid logging.

**Command** ([[commands/aws-docdb-elastic-list-cluster-snapshots-non-production]]):
```bash
aws docdb-elastic list-cluster-snapshots --endpoint-url ██████
```

> The --endpoint-url parameter routes to the non-production endpoint. Response mirrors production (success/failure via IAM), but no CloudTrail event is generated.

### Step 2: Confirm No Logging

**Context**: Verify the absence of logs to ensure evasion.

**Command** (Check CloudTrail):
```bash
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ListClusterSnapshots
```

> After 5-10 minutes, no matching event confirms the bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Disable Cloud Logs]]

### Sub-Techniques


## Commands Used

- [[commands/aws-docdb-elastic-list-cluster-snapshots-non-production]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- logging-bypass
- evasion

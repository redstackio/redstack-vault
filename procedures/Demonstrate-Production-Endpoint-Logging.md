---
tags:
  - aws
  - cloudtrail
  - logging
  - baseline
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-docdb-elastic-list-cluster-snapshots-production]]'
platforms:
  - AWS
techniques:
  - '[[T1087.004]]'
skill_level: intermediate
impact_level: low
detection_risk: high
sub_techniques: []
id: 41e62d70-1b4a-4bf1-a466-d48dacb65223
created_at: '2025-12-14T17:32:29.158Z'
updated_at: '2025-12-14T17:32:29.158Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Demonstrate-Production-Endpoint-Logging

## Summary

This procedure verifies that API calls to the production endpoint of AWS DocumentDB Elastic are properly logged in CloudTrail, serving as a baseline to contrast with unlogged non-production endpoints.

## Description

In an AWS environment with DocumentDB Elastic and CloudTrail enabled, execute a standard API operation using AWS CLI on the production endpoint. The call will be authorized via IAM and logged for auditing. This step is crucial to highlight the logging discrepancy exploited in permission enumeration attacks, where adversaries confirm detection mechanisms before attempting stealthy tests.

## Requirements

1. AWS CLI installed and configured with IAM credentials
2. Access to DocumentDB Elastic service (read permissions for list actions)
3. CloudTrail trail configured to capture management events for docdb-elastic
4. Ability to query CloudTrail logs (via Console, CLI, or Athena)

## Defense

Defensive measures and detection strategies:

- Enable comprehensive CloudTrail logging for all AWS services
- Monitor for anomalous API call volumes or patterns in logs
- Use AWS Config to enforce endpoint usage policies

## Objectives

1. Establish baseline logging behavior for production APIs
2. Validate IAM permissions for DocumentDB Elastic actions
3. Confirm CloudTrail integration for detection

## Instructions

### Step 1: Execute API Call on Production Endpoint

**Context**: Invoke the list-cluster-snapshots operation to trigger a logged event.

**Command** ([[commands/aws-docdb-elastic-list-cluster-snapshots-production]]):
```bash
aws docdb-elastic list-cluster-snapshots
```

> This command lists cluster snapshots using the default production endpoint. Expect a JSON response with snapshot details if permitted, or an AccessDenied error. The event will be logged in CloudTrail.

### Step 2: Verify CloudTrail Log

**Context**: Check for the log entry to confirm detection.

**Command** (AWS CLI for lookup events, if needed):
```bash
aws logs filter-log-events --log-group-name /aws/events --filter-pattern "eventName = ListClusterSnapshots"
```

> Wait 5-10 minutes post-execution. Successful logging shows an event with source as docdb-elastic.amazonaws.com and the invoked action.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1087.004]]

### Sub-Techniques


## Commands Used

- [[commands/aws-docdb-elastic-list-cluster-snapshots-production]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- cloudtrail
- logging

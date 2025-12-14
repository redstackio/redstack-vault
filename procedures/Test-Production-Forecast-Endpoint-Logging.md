---
id: proc-uuid-1
tags:
  - aws
  - cloudtrail
  - logging
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-forecast-list-datasets-production]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:39.612Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Test-Production-Forecast-Endpoint-Logging

## Summary

This procedure tests the standard production API endpoint of AWS Forecast to confirm that API calls are properly logged to CloudTrail, providing a baseline for identifying logging gaps in non-production endpoints.

## Description

In an AWS environment with compromised IAM credentials, execute a Forecast API operation like list-datasets on the production endpoint. This generates an auditable event in CloudTrail after a short delay, allowing defenders to monitor access. The procedure requires AWS CLI access and verifies logging behavior in us-west-2 region.

## Requirements

1. AWS CLI installed and configured with IAM credentials
2. Access to CloudTrail console or query tools for log verification
3. AWS Forecast service availability in the target region

## Defense

Defensive measures and detection strategies:

- Enable comprehensive CloudTrail logging for all regions and services
- Monitor for unusual Forecast API calls via CloudWatch alarms
- Implement IAM least-privilege policies to limit Forecast access

## Objectives

1. Confirm production endpoint logging functionality
2. Baseline for comparison with non-production tests
3. Identify if credentials have Forecast permissions

## Instructions

### Step 1: Execute Production API Call

**Context**: Call the list-datasets operation to trigger a loggable event.

**Command** ([[commands/aws-forecast-list-datasets-production]]):
```bash
aws forecast list-datasets --region us-west-2
```

> This command lists datasets if permitted or returns AccessDenied. Expect a JSON response; log appears in CloudTrail within 5-10 minutes.

### Step 2: Verify CloudTrail Logging

**Context**: Check for the event to confirm detection.

**Command** (Custom CloudTrail query):
```bash
aws logs filter-log-events --log-group-name CloudTrail --filter-pattern "eventName=list-datasets"
```

> Query recent logs; success if event is found with details like userIdentity and eventTime.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/aws-forecast-list-datasets-production]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- cloudtrail
- logging

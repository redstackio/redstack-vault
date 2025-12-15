---
id: proc-uuid-2
tags:
  - aws
  - cloudtrail
  - evasion
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/aws-forecast-list-datasets-nonprod]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Impair Defenses]]'
updated_at: '2025-12-14T17:32:39.609Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Impair Defenses]]'
---
# Test-Non-Production-Forecast-Endpoint-Logging

## Summary

This procedure exploits non-production API endpoints in AWS Forecast that bypass CloudTrail logging, allowing API calls to go undetected while still enforcing IAM permissions.

## Description

By overriding the endpoint URL to a non-production variant (redacted), attackers can test Forecast operations without audit trails. This reveals permissions via responses but evades logging, useful for stealthy reconnaissance in compromised AWS accounts.

## Requirements

1. Knowledge of non-production endpoint URLs (e.g., internal testing endpoints)
2. AWS CLI with IAM credentials
3. Extended wait time for log checks (10+ minutes)

## Defense

Defensive measures and detection strategies:

- Audit and disable access to non-production endpoints
- Implement endpoint-specific logging or WAF rules
- Regularly review IAM policies for Forecast access

## Objectives

1. Confirm logging evasion on non-production endpoints
2. Validate IAM permission enforcement despite no logs
3. Highlight insufficient logging vulnerability

## Instructions

### Step 1: Override Endpoint and Execute Call

**Context**: Use --endpoint-url to target non-production service.

**Command** ([[commands/aws-forecast-list-datasets-nonprod]]):
```bash
aws forecast list-datasets --region us-west-2 --endpoint-url ███████
```

> Response mirrors production (success/failure); no CloudTrail event generated.

### Step 2: Monitor for Absence of Logs

**Context**: Verify no detection after delay.

**Command** (CloudTrail query):
```bash
aws logs filter-log-events --log-group-name CloudTrail --filter-pattern "eventName=list-datasets" --start-time $(date -d '10 minutes ago' +%s)000
```

> No matching events indicate successful bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Impair Defenses]]

### Sub-Techniques


## Commands Used

- [[commands/aws-forecast-list-datasets-nonprod]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- evasion
- logging

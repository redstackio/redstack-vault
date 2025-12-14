---
tags:
  - aws
  - datazone
  - permission-enumeration
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/export-aws-profile]]'
  - '[[commands/aws-datazone-list-domains]]'
platforms:
  - AWS
  - Cloud
techniques:
  - '[[T1087.004]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8092bd67-a7df-4cc3-a740-565d0378c6f0
created_at: '2025-12-14T17:32:39.225Z'
updated_at: '2025-12-14T17:32:39.225Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Test Non-Production Endpoint with Limited Credentials

## Summary

This procedure uses limited permission credentials to probe a non-production AWS Datazone endpoint, eliciting detailed AccessDenied responses that reveal permission levels without CloudTrail logging.

## Description

Switch to a 'noperm' AWS profile with restricted access and call the list-domains API on the non-prod endpoint. The response includes specific details like user ARN and denied actions, allowing enumeration of exact permissions. Since non-prod endpoints do not log to CloudTrail, this occurs silently, aiding adversaries in assessing compromised credential capabilities.

## Requirements

1. AWS CLI configured with 'noperm' profile having no Datazone permissions
2. Valid non-production endpoint URL from prior discovery
3. AWS credentials file with both profiles

## Defense

Defensive measures and detection strategies:

- Ensure all endpoints, including non-prod, forward logs to CloudTrail
- Implement permission boundaries to limit error verbosity in responses
- Monitor for repeated AccessDenied patterns from limited accounts

## Objectives

1. Expose detailed permission denials
2. Enumerate access without alerting monitoring
3. Confirm logging bypass for stealth

## Instructions

### Step 1: Set Limited Profile

**Context**: Switch AWS CLI authentication to restricted credentials.

**Command** ([[commands/export-aws-profile]]):
```bash
export AWS_PROFILE=noperm
```

> Sets environment for noperm profile; no output.

### Step 2: Probe API for Denial Details

**Context**: Execute the API call to trigger and capture permission-specific error.

**Command** ([[commands/aws-datazone-list-domains]]):
```bash
aws datazone list-domains --endpoint-url [redacted]
```

> Expects detailed error: 'An error occurred (AccessDeniedException) when calling the ListDomains operation: User: arn:aws:sts::[redacted]:assumed-role/noperm/noperm is not authorized to perform: datazone:ListDomains on resource: arn:aws:datazone:us-east-1:[redacted]:domain/*'; verify no CloudTrail entry.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1087.004]]

### Sub-Techniques


## Commands Used

- [[commands/export-aws-profile]]
- [[commands/aws-datazone-list-domains]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- [[aws]]
- [[datazone]]
- [[permission-enumeration]]

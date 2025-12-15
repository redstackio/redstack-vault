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
id: 25440659-c242-4c7f-9771-25ea46f65661
created_at: '2025-12-14T17:32:39.227Z'
updated_at: '2025-12-14T17:32:39.227Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Test Non-Production Endpoint with Admin Credentials

## Summary

This procedure tests a non-production AWS Datazone endpoint using admin credentials to confirm accessibility and lack of detailed logging in CloudTrail, producing only generic errors.

## Description

Using AWS CLI with an admin profile, call the list-domains API on a discovered non-prod endpoint. This step verifies the endpoint is reachable but returns a generic 'Invalid endpoint or operation type' error, without generating CloudTrail logs, unlike production endpoints. It sets the stage for permission probing by confirming silent execution.

## Requirements

1. AWS CLI installed and configured with 'admin' profile having broad Datazone permissions
2. Discovered non-production endpoint URL
3. Network access to AWS

## Defense

Defensive measures and detection strategies:

- Enable comprehensive CloudTrail logging for all API endpoints, including non-prod
- Monitor for unusual endpoint URLs in API calls via WAF or API gateway logs
- Restrict non-prod endpoints to internal VPC access only

## Objectives

1. Confirm endpoint responds without logging
2. Validate admin access yields generic errors
3. Avoid detection during initial probing

## Instructions

### Step 1: Set Admin Profile

**Context**: Configure AWS CLI to use administrative credentials for the test.

**Command** ([[commands/export-aws-profile]]):
```bash
export AWS_PROFILE=admin
```

> This sets the environment variable to authenticate with admin permissions; no output expected.

### Step 2: Call List-Domains API

**Context**: Invoke the Datazone API on the non-prod endpoint to test response.

**Command** ([[commands/aws-datazone-list-domains]]):
```bash
aws datazone list-domains --endpoint-url [redacted]
```

> Overrides the default endpoint to the non-prod URL; expects 'An error occurred (AccessDeniedException) when calling the ListDomains operation: Invalid endpoint or operation type' with no CloudTrail log.

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

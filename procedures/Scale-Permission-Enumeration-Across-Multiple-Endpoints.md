---
tags:
  - aws
  - datazone
  - permission-enumeration
  - scaling
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
id: 7a2ec186-eb86-42ba-a126-496a8a361c3a
created_at: '2025-12-14T17:32:39.222Z'
updated_at: '2025-12-14T17:32:39.222Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Scale Permission Enumeration Across Multiple Endpoints

## Summary

This procedure extends permission testing to additional non-production AWS Datazone endpoints, confirming consistent silent enumeration behavior across a broader set.

## Description

After initial testing, repeat the admin and limited credential probes on multiple discovered endpoints (e.g., redacted as ██████████, ████, █████, ████, ████████). Each test alternates profiles to compare responses, verifying the lack of CloudTrail logging universally, which amplifies the reconnaissance potential in AWS environments.

## Requirements

1. List of multiple non-production endpoint URLs
2. AWS CLI with admin and noperm profiles
3. Scripting for automation if scaling beyond manual tests

## Defense

Defensive measures and detection strategies:

- Deploy global fixes to enable CloudTrail logging on all endpoints
- Use AWS Config to audit endpoint configurations regularly
- Alert on API calls to non-standard endpoints

## Objectives

1. Validate vulnerability across endpoints
2. Gather comprehensive permission insights
3. Demonstrate scalability of silent enumeration

## Instructions

### Step 1: Alternate Profiles for Each Endpoint

**Context**: For each endpoint, set admin profile and test.

**Command** ([[commands/export-aws-profile]]):
```bash
export AWS_PROFILE=admin
```

**Command** ([[commands/aws-datazone-list-domains]]):
```bash
aws datazone list-domains --endpoint-url [redacted-endpoint]
```

> Generic error expected per endpoint.

### Step 2: Test with Limited Credentials

**Context**: Switch to noperm and repeat for detailed responses.

**Command** ([[commands/export-aws-profile]]):
```bash
export AWS_PROFILE=noperm
```

**Command** ([[commands/aws-datazone-list-domains]]):
```bash
aws datazone list-domains --endpoint-url [redacted-endpoint]
```

> Detailed AccessDenied per endpoint; confirm no logs.

### Step 3: Post-Fix Verification

**Context**: After mitigation, retest all endpoints.

Repeat steps with updated AWS deployment; expect logged errors or denials.

> Expected output: No vulnerable silent behavior remains.

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
- [[scaling]]

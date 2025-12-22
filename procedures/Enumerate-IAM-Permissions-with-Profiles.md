---
tags:
  - aws
  - iam
  - enumeration
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/export-aws-profile-admin]]'
  - '[[commands/aws-datazone-list-domains-nonprod]]'
  - '[[commands/export-aws-profile-noperm]]'
  - '[[commands/aws-datazone-list-domains-nonprod]]'
techniques:
  - '[[T1087.004]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 097d221e-c1d2-4acb-a3e8-aae91b199b04
created_at: '2025-12-14T17:32:39.031Z'
updated_at: '2025-12-14T17:32:39.031Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Enumerate-IAM-Permissions-with-Profiles

## Summary

This procedure uses multiple IAM profiles to test Datazone permissions on non-production endpoints, revealing access levels through response differences without logging.

## Description

With stolen credentials, switch AWS CLI profiles (e.g., admin vs. noperm) and invoke list-domains on unlogged endpoints. Success indicates permissions; errors like AccessDeniedException denote denials. This enables invisible reconnaissance in AWS; 44 endpoints amplify scope.

## Requirements

1. Multiple IAM profiles configured in AWS CLI (~/.aws/config).
2. Non-production endpoint URL.
3. Credentials for each profile.

## Defense

Defensive measures and detection strategies:

- Rotate credentials frequently and monitor for unusual profile switches.
- Use AWS IAM Access Analyzer to detect over-permissions.
- Block non-prod endpoint access via VPC endpoints or WAF.

## Objectives

1. Map permissions silently.
2. Identify exploitable access with stolen creds.
3. Evade log-based credential abuse detection.

## Instructions

### Step 1: Switch to Privileged Profile

**Context**: Set admin profile for positive test.

**Command** ([[commands/export-aws-profile-admin]]):
```bash
export AWS_PROFILE=admin
```

> Sets environment; follow with API call.

**Command** ([[commands/aws-datazone-list-domains-nonprod]]):
```bash
aws datazone list-domains --endpoint-url <redacted>
```

> Expected: Success or InternalServerError; no log.

### Step 2: Switch to Unprivileged Profile

**Context**: Test denial for contrast.

**Command** ([[commands/export-aws-profile-noperm]]):
```bash
export AWS_PROFILE=noperm
```

> Sets noperm profile.

**Command** ([[commands/aws-datazone-list-domains-nonprod]]):
```bash
aws datazone list-domains --endpoint-url <redacted>
```

> Expected: AccessDeniedException for datazone:ListDomains; no log.

### Step 3: Compare Responses

**Context**: Analyze for enumeration.

**Command** (Manual):

> Note differences to infer permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1087.004]]

### Sub-Techniques


## Commands Used

- [[commands/export-aws-profile-admin]]
- [[commands/aws-datazone-list-domains-nonprod]]
- [[commands/export-aws-profile-noperm]]
- [[commands/aws-datazone-list-domains-nonprod]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- iam
- profile-switch
- enumeration

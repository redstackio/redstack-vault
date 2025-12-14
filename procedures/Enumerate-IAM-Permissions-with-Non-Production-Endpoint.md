---
tags:
  - aws
  - iam
  - permission-enumeration
  - discovery
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/export-aws-profile-admin]]'
  - '[[commands/aws-elasticache-describe-cache-subnet-groups-admin]]'
  - '[[commands/export-aws-profile-noperm]]'
  - '[[commands/aws-elasticache-describe-cache-subnet-groups-noperm]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1087.004]]'
updated_at: '2025-12-14T17:32:28.927Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 6f97e296-d0dc-4955-b82a-72d1e607d625
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Enumerate-IAM-Permissions-with-Non-Production-Endpoint

## Summary

This procedure uses the non-logging ElastiCache endpoint to test IAM permissions across privileged and non-privileged profiles, allowing silent discovery of access rights without CloudTrail alerts.

## Description

By switching AWS profiles and issuing API calls to the non-production endpoint, adversaries can probe for permissions on actions like describe-cache-subnet-groups. Success indicates access, failure shows denial, all without logs, aiding in reconnaissance for further compromise.

## Requirements

1. AWS credentials file with multiple profiles (e.g., admin, noperm)
2. Non-production endpoint URL (e.g., ████████, ███)
3. Basic ElastiCache knowledge

## Defense

Defensive measures and detection strategies:

- Enforce least privilege on IAM roles
- Monitor for profile switches and endpoint anomalies
- Enable comprehensive logging across all endpoints

## Objectives

1. Discover effective IAM permissions stealthily
2. Map access levels without detection
3. Facilitate targeted escalation

## Instructions

### Step 1: Switch to Privileged Profile and Test

**Context**: Use admin profile to confirm successful access without logging.

**Command** ([[commands/export-aws-profile-admin]]):
```bash
export AWS_PROFILE=admin
```

Followed by [[commands/aws-elasticache-describe-cache-subnet-groups-admin]]:
```bash
aws elasticache describe-cache-subnet-groups --endpoint-url ████████
```

> Expected output: {"CacheSubnetGroups": []} (empty on success).

### Step 2: Switch to Non-Privileged Profile and Test

**Context**: Use noperm profile to confirm denial without logging.

**Command** ([[commands/export-aws-profile-noperm]]):
```bash
export AWS_PROFILE=noperm
```

Followed by [[commands/aws-elasticache-describe-cache-subnet-groups-noperm]]:
```bash
aws elasticache describe-cache-subnet-groups --endpoint-url ███
```

> Expected output: AccessDenied error with policy details.

### Step 3: Verify No Logs

**Context**: Confirm stealth by checking CloudTrail.

**Command** (Lookup events):
```bash
aws cloudtrail lookup-events --start-time $(date -u -d '10 minutes ago' +%Y-%m-%dT%H:%M:%SZ)
```

> Expected: No events for these calls.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1087.004]] Cloud Account

### Sub-Techniques

- None

## Commands Used

- [[commands/export-aws-profile-admin]]
- [[commands/aws-elasticache-describe-cache-subnet-groups-admin]]
- [[commands/export-aws-profile-noperm]]
- [[commands/aws-elasticache-describe-cache-subnet-groups-noperm]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- iam
- permission-enumeration
- discovery

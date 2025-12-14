---
tags:
  - aws
  - cloudtrail
  - iam
  - datazone
  - permission-enumeration
  - logging-bypass
  - defense-evasion
type: attack_chain
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
  - '[[Defense Evasion]]'
commands:
  - '[[commands/aws-datazone-list-domains]]'
  - '[[commands/aws-datazone-list-domains-nonprod]]'
  - '[[commands/export-aws-profile-admin]]'
  - '[[commands/export-aws-profile-noperm]]'
platforms:
  - AWS
complexity: medium
procedures:
  - '[[procedures/Verify-Normal-Datazone-API-Logging]]'
  - '[[procedures/Monitor-CloudTrail-for-Standard-Call]]'
  - '[[procedures/Test-Non-Production-Datazone-Endpoint]]'
  - '[[procedures/Verify-Absence-of-CloudTrail-Log]]'
  - '[[procedures/Enumerate-IAM-Permissions-with-Profiles]]'
step_count: 5
techniques:
  - '[[T1087.004]]'
  - '[[Disable Cloud Logs]]'
description: >-
  Attack chain exploiting unlogged non-production API endpoints in AWS Datazone
  to silently enumerate IAM permissions without CloudTrail detection.
skill_level: intermediate
impact_level: high
id: 3c60fae8-a083-4e15-aa62-44f20ebb6f6d
created_at: '2025-12-14T17:32:39.047Z'
updated_at: '2025-12-14T17:32:39.047Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[T1087.004]]'
  - '[[Disable Cloud Logs]]'
---
# Silent IAM Permission Enumeration via Non-Production AWS Datazone Endpoints

Multi-stage attack chain demonstrating how adversaries with stolen IAM credentials can silently test and enumerate permissions for the AWS Datazone service by targeting non-production API endpoints that bypass CloudTrail logging. This allows evasion of detection mechanisms that monitor for credential abuse via logs, enabling stealthy reconnaissance of access levels without alerting security teams.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15-20 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Verify Normal Logging] --> B[Monitor CloudTrail]
    B --> C[Test Non-Production Endpoint]
    C --> D[Confirm No Log]
    D --> E[Enumerate Permissions]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/AWS-CLI]]

### Target Environment

- AWS Cloud platform
- AWS Datazone service enabled
- CloudTrail configured for API logging
- IAM profiles with varying permissions (e.g., admin and noperm)

### Initial Access Requirements

- Stolen or compromised IAM credentials
- AWS CLI configured with access to the target account
- Knowledge of non-production endpoint URLs (e.g., test or employee-specific aliases, redacted in reports)

## Detailed Attack Procedures

### Step 1: Verify Normal Logging
procedure: [[procedures/Verify-Normal-Datazone-API-Logging]]

**Objective**: Confirm that standard production API calls to AWS Datazone are logged in CloudTrail as expected.

**Instructions**: Use [[commands/aws-datazone-list-domains]] to perform a baseline API call on the production endpoint:

```bash
aws datazone list-domains
```

This lists domains if permitted and generates a detectable log entry.

**Expected Output**: List of domains or AccessDeniedException; CloudTrail event appears within 5-10 minutes.

**Success Indicators**:
- API response received
- CloudTrail log entry confirmed in subsequent monitoring

### Step 2: Monitor CloudTrail
procedure: [[procedures/Monitor-CloudTrail-for-Standard-Call]]

**Objective**: Validate that the production API call is captured in CloudTrail logs.

**Instructions**: Wait 5-10 minutes after the production call, then query CloudTrail using AWS console or CLI to check for the event (e.g., eventName: ListDomains, source: datazone.amazonaws.com).

**Expected Output**: Log entry showing the API call details, including user identity and timestamp.

**Success Indicators**:
- Log entry present in CloudTrail trail
- No anomalies in log delivery

### Step 3: Test Non-Production Endpoint
procedure: [[procedures/Test-Non-Production-Datazone-Endpoint]]

**Objective**: Execute the same API call against a non-production endpoint to bypass logging.

**Instructions**: Use [[commands/aws-datazone-list-domains-nonprod]] with the --endpoint-url flag pointing to a redacted non-production URL (e.g., containing test aliases or employee names):

```bash
aws datazone list-domains --endpoint-url <redacted>
```

This performs the call without integrating with CloudTrail.

**Expected Output**: Success or AccessDeniedException based on permissions; no log generated.

**Success Indicators**:
- API response received without errors
- IAM enforcement still active (e.g., permission-based responses)

### Step 4: Verify Absence of Log
procedure: [[procedures/Verify-Absence-of-CloudTrail-Log]]

**Objective**: Confirm that the non-production call evades CloudTrail logging.

**Instructions**: Wait 5-10 minutes post-call, then re-query CloudTrail for any new events related to Datazone ListDomains.

**Expected Output**: No corresponding log entry for the non-production call.

**Success Indicators**:
- Absence of log after monitoring period
- Production logs remain unaffected

### Step 5: Enumerate Permissions
procedure: [[procedures/Enumerate-IAM-Permissions-with-Profiles]]

**Objective**: Use different IAM profiles to silently assess permission levels via response differences.

**Instructions**: Switch to admin profile with [[commands/export-aws-profile-admin]]:

```bash
export AWS_PROFILE=admin
aws datazone list-domains --endpoint-url <redacted>
```

Then switch to noperm with [[commands/export-aws-profile-noperm]]:

```bash
export AWS_PROFILE=noperm
aws datazone list-domains --endpoint-url <redacted>
```

Observe success vs. AccessDeniedException without logs.

**Expected Output**: Admin: successful list or error; Noperm: AccessDeniedException; no CloudTrail entries.

**Success Indicators**:
- Permission status revealed via responses
- No detection in logs

## Attack Chain Summary

### Key Achievements

1. Confirmed normal logging baseline for production endpoints.
2. Demonstrated logging bypass using non-production URLs.
3. Enabled silent permission testing with stolen credentials.
4. Evaded CloudTrail-based detection for credential enumeration.
5. Highlighted 44 vulnerable endpoints for potential abuse.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1087.004]]
- [[Disable Cloud Logs]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Defense Evasion]]

---
*Last updated: 2023-10-01T00:00:00Z*

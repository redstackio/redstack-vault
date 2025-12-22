---
tags:
  - gcp
  - token-analysis
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/kubectl]]'
  - '[[tools/Image-Editing-Software]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Discovery]]'
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-set-instance-metadata]]'
  - '[[commands/curl-query-token-info]]'
  - '[[commands/kubectl-get-pods]]'
  - '[[commands/kubectl-create-pod]]'
  - '[[commands/kubectl-delete-pod]]'
  - '[[commands/kubectl-exec-pod]]'
  - '[[commands/kubectl-describe-pod]]'
  - '[[commands/kubectl-get-secret]]'
  - '[[commands/kubectl-exec-pod-with-token]]'
  - '[[commands/kubectl-exec-pod-with-token-namespace]]'
  - '[[commands/id]]'
  - '[[commands/ls]]'
  - '[[commands/exit]]'
platforms:
  - GCP
techniques:
  - '[[Unsecured Credentials]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6bf9d5d0-5ef7-46d2-b7b9-5f161a733bf6
created_at: '2025-12-11T06:10:23.727Z'
updated_at: '2025-12-11T06:10:23.727Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1552]]'
---
# Test and Analyze Leaked GCP Tokens

## Summary

This procedure tests the capabilities of leaked GCP tokens by attempting metadata modifications and querying token scopes to understand permissions for escalation.

## Description

Using leaked access tokens from metadata, attempt to interact with GCP APIs to gauge scope and identify paths for further attacks, such as adding SSH keys (which failed here due to permissions).

## Requirements

1. Leaked GCP access token
2. [[tools/curl]] installed
3. Internet access to GCP APIs

## Defense

Defensive measures and detection strategies:

- Restrict service account scopes
- Monitor API calls for anomalous token usage
- Use workload identity to limit metadata exposure

## Objectives

1. Verify token validity and scopes
2. Test for write permissions
3. Plan next escalation steps

## Instructions

### Step 1: Attempt Metadata Modification

**Context**: Test if token can add SSH keys.

Execute [[commands/curl-set-instance-metadata]]:

```bash
curl -X POST "https://www.googleapis.com/compute/v1/projects/███/setCommonInstanceMetadata" -H "Authorization: Bearer ██████████████" -H "Content-Type: application/json" --data '{"items": [{"key": "0xACB", "value": "test"}]}'
```

> Expected: 403 Forbidden error.

### Step 2: Query Token Scopes

**Context**: Check token permissions.

Execute [[commands/curl-query-token-info]]:

```bash
curl "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=██████████████████"
```

> Expected: JSON with scopes like cloud-platform.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]
- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques



## Commands Used

- [[commands/curl-set-instance-metadata]]
- [[commands/curl-query-token-info]]

## Tools Used

- [[tools/curl]]

## Tags

- [[gcp]]
- [[token-analysis]]

---
tags:
  - credential-access
  - kubernetes
type: procedure
tools:
  - '[[tools/BinaryEdge]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-kubernetes-api-access]]'
  - '[[commands/curl-create-kubernetes-job]]'
  - '[[commands/curl-get-kubernetes-secrets]]'
  - '[[commands/curl-binaryedge-query]]'
platforms:
  - Kubernetes
techniques:
  - '[[Unsecured Credentials]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 41b39949-6d67-452a-84eb-152c8aea76a7
created_at: '2025-12-11T06:10:10.579Z'
updated_at: '2025-12-11T06:10:10.579Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1552]]'
---
# Extract Internal Credentials from Kubernetes

## Summary

This procedure extracts sensitive credentials stored in Kubernetes secrets using administrative API access.

## Description

Kubernetes secrets often contain credentials for internal services. With admin access, attackers can list and decode these for lateral movement.

## Requirements

1. Admin-level API access
2. Ability to query secrets endpoint
3. Base64 decoding tool

## Defense

Defensive measures and detection strategies:

- Encrypt secrets at rest
- Audit secret access logs

## Objectives

1. List available secrets
2. Decode and exfiltrate credentials
3. Access internal instances

## Instructions

### Step 1: List Secrets

**Command** ([[commands/curl-get-kubernetes-secrets]]):
```bash
curl -k https://TARGET_IP:6443/api/v1/namespaces/default/secrets
```

> This returns a list of secrets in JSON format.

### Step 2: Decode Credentials

**Context**: Extract and base64-decode data fields.

```bash
echo "BASE64_DATA" | base64 -d
```

> Reveals plaintext credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques



## Commands Used

- [[commands/curl-get-kubernetes-secrets]]

## Tools Used

- [[commands/curl-binaryedge-query]]

## Tags

- [[credential-access]]
- [[commands/curl-kubernetes-api-access]]

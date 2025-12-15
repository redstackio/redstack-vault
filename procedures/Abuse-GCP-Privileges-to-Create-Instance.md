---
id: proc-7
name: Abuse-GCP-Privileges-to-Create-Instance
tags:
  - gcp
  - resource-abuse
  - crypto-mining
type: procedure
tools:
  - '[[tools/gcloud]]'
  - '[[tools/jq]]'
tactics:
  - '[[Command and Control]]'
commands:
  - '[[commands/export-cloudsdk-admin-token]]'
  - '[[commands/gcloud-compute-create-miner]]'
verified: false
platforms:
  - GCP
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:30:18.561Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Command and Control]]'
mitre_techniques:
  - '[[T1078.004]]'
---
# Abuse-GCP-Privileges-to-Create-Instance

## Summary

Authenticates gcloud with the privileged master token and creates a new Compute Engine instance, demonstrating project compromise (e.g., for crypto-mining).

## Description

The master node's service account has roles like Compute Admin, allowing instance creation. This procedure sets the token and spins up a VM, proving full GCP takeover from initial pod access.

## Requirements

1. admin.token from master
2. gcloud installed
3. Zone and image details (e.g., europe-west1-b, ubuntu-2204-lts)

## Defense

- Limit master service account scopes
- Enable GCP Guardrails for resource creation
- Alert on unusual instance spins from service accounts

## Objectives

1. Authenticate as privileged GCP account
2. Create unauthorized VM
3. Enable persistent access or abuse

## Instructions

### Step 1: Set Admin Token

**Context**: Export token for gcloud auth.

**Command** ([[commands/export-cloudsdk-admin-token]]):
```bash
export CLOUDSDK_AUTH_ACCESS_TOKEN=$(jq .access_token -r ./admin.token)
```

> Sets env. Expected output: Token exported.

### Step 2: Create Compute Instance

**Context**: Use privileges to launch VM.

**Command** ([[commands/gcloud-compute-create-miner]]):
```bash
gcloud compute instances create miner --image-family=ubuntu-2204-lts --zone=europe-west1-b --image-project=ubuntu-os-cloud
```

> Creates instance. Expected output: 'Created miner.'

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control]] Command and Control

### Techniques

- [[T1078.004]] Valid Accounts: Cloud Accounts

### Sub-Techniques

- None

## Commands Used

- [[commands/export-cloudsdk-admin-token]]
- [[commands/gcloud-compute-create-miner]]

## Tools Used

- [[tools/gcloud]]
- [[tools/jq]]

## Tags

- gcp
- resource-abuse
- crypto-mining

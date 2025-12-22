---
id: cmd-10
data: >-
  gcloud storage cat
  gs://kops-state-test/kops.k8s.local/pki/private/kubernetes-ca/keyset.yaml | yq
  e '.spec.keys[0].publicMaterial' - | base64 -d > keys/ca.pem
tags:
  - gcs
  - extract
type: command
output: ca.pem file
executor: bash
platforms:
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.528Z'
verified: false
validated: true
submitted: true
---
# gcloud-storage-cat-public-cert

## Command

```bash
gcloud storage cat gs://kops-state-test/kops.k8s.local/pki/private/kubernetes-ca/keyset.yaml | yq e '.spec.keys[0].publicMaterial' - | base64 -d > keys/ca.pem
```

## Description

Retrieves, parses, and decodes the public CA certificate from kOps state bucket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gs://...` | GCS path | Yes |
| `yq e ...` | Extract public | Yes |
| `base64 -d` | Decode | Yes |
| `> keys/ca.pem` | Output | Yes |

## Examples

### Basic Usage

```bash
gcloud storage cat ... | yq ... | base64 -d > cert.pem
```

### Advanced Usage

Similar to private key extraction.

## Expected Output

X.509 cert in ca.pem.

## Related

- [[commands/gcloud-storage-cat-private-key]]

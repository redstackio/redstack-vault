---
id: cmd-9
data: >-
  gcloud storage cat
  gs://kops-state-test/kops.k8s.local/pki/private/kubernetes-ca/keyset.yaml | yq
  e '.spec.keys[0].privateMaterial' - | base64 -d > keys/ca.key
tags:
  - gcs
  - extract
type: command
output: ca.key file
executor: bash
platforms:
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.531Z'
verified: false
validated: true
submitted: true
---
# gcloud-storage-cat-private-key

## Command

```bash
gcloud storage cat gs://kops-state-test/kops.k8s.local/pki/private/kubernetes-ca/keyset.yaml | yq e '.spec.keys[0].privateMaterial' - | base64 -d > keys/ca.key
```

## Description

Retrieves, parses, and decodes the private CA key from kOps state bucket.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gs://...` | GCS object path | Yes |
| `yq e ...` | YAML extract | Yes |
| `base64 -d` | Decode | Yes |
| `> keys/ca.key` | Output | Yes |

## Examples

### Basic Usage

```bash
gcloud storage cat gs://bucket/path | yq ... | base64 -d > key
```

### Advanced Usage

```bash
gcloud storage cp gs://... keyset.yaml && yq ... > key
```

## Expected Output

PEM private key in ca.key.

## Related

- [[commands/gcloud-storage-cat-public-cert]]

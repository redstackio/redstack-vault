---
id: cmd-24
data: >-
  gcloud compute instances create miner --image-family=ubuntu-2204-lts
  --zone=europe-west1-b --image-project=ubuntu-os-cloud
tags:
  - compute
  - abuse
type: command
output: Instance created
executor: bash
platforms:
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.479Z'
verified: false
validated: true
submitted: true
---
# gcloud-compute-create-miner

## Command

```bash
gcloud compute instances create miner --image-family=ubuntu-2204-lts --zone=europe-west1-b --image-project=ubuntu-os-cloud
```

## Description

Creates a new GCP Compute Engine instance using privileged auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `miner` | Instance name | Yes |
| `--image-family` | OS family | Yes |
| `--zone` | Zone | Yes |
| `--image-project` | Project for image | Yes |

## Examples

### Basic Usage

```bash
gcloud compute instances create vm --image-family=ubuntu-2204-lts --zone=us-central1-a
```

### Advanced Usage

```bash
gcloud ... create --machine-type=n1-standard-1 --scopes=cloud-platform
```

## Expected Output

'Created [https://.../projects/.../zones/.../instances/miner].'

## Related

- [[commands/export-cloudsdk-admin-token]]

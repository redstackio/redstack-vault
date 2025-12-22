---
id: cmd-uuid-5
data: >-
  curl
  https://www.googleapis.com/storage/v1/b?access_token=xxx&project=gitlab-ci-155816
tags:
  - bucket-enum
  - storage
type: command
output: >-
  JSON array of buckets including gitlab-ci-usage-outputs and
  gitlab-runner-secrets with details like id, name, location
executor: bash
platforms:
  - Linux
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.510Z'
verified: false
validated: true
submitted: true
---
# curl-list-gcp-buckets

## Command

```bash
curl https://www.googleapis.com/storage/v1/b?access_token=xxx&project=gitlab-ci-155816
```

## Description

List all buckets in the specified Google Cloud Storage project using stolen token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `access_token=xxx` | Service account token | Yes |
| `project=gitlab-ci-155816` | Project ID | Yes |

## Examples

### Basic Usage

```bash
curl https://www.googleapis.com/storage/v1/b?access_token=xxx&project=gitlab-ci-155816
```

## Expected Output

JSON array of buckets including gitlab-ci-usage-outputs and gitlab-runner-secrets with details like id, name, location.

## Related

- [[Related Procedure: Enumerate-and-Access-GCP-Storage-Buckets]]

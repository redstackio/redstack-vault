---
id: cmd-uuid-6
data: >-
  curl
  https://www.googleapis.com/storage/v1/b/gitlab-runner-secrets/o?access_token=xxxx
tags:
  - object-enum
  - storage
type: command
output: 'JSON list of objects, including package_signing.gpg'
executor: bash
platforms:
  - Linux
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.508Z'
verified: false
validated: true
submitted: true
---
# curl-list-bucket-objects

## Command

```bash
curl https://www.googleapis.com/storage/v1/b/gitlab-runner-secrets/o?access_token=xxxx
```

## Description

List objects in the gitlab-runner-secrets bucket using access token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `b=gitlab-runner-secrets` | Bucket name | Yes |
| `o` | List objects flag | Yes |
| `access_token=xxxx` | Token | Yes |

## Examples

### Basic Usage

```bash
curl https://www.googleapis.com/storage/v1/b/gitlab-runner-secrets/o?access_token=xxxx
```

## Expected Output

JSON list of objects, including package_signing.gpg.

## Related

- [[Related Procedure: Enumerate-and-Access-GCP-Storage-Buckets]]

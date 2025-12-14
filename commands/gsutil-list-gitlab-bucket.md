---
id: c1b2c3d4-e5f6-7890-abcd-ef1234567894
data: 'gsutil ls gs://gitlab'
tags:
  - gcs
  - access-denied
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.448Z'
verified: false
validated: true
submitted: true
---
# gsutil-list-gitlab-bucket

## Command

```bash
gsutil ls gs://gitlab
```

## Description

Attempts to list the main GitLab production bucket to confirm it is not public, serving as a negative control in the attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ls | List bucket objects | Yes |
| gs://gitlab | Target production bucket | Yes |

## Examples

### Basic Usage

```bash
gsutil ls gs://gitlab
```

### Advanced Usage

```bash
gsutil ls -p gs://gitlab  # With project flag if authenticated
```

## Expected Output

403 error: 'does not have storage.objects.list access', indicating restricted access.

## Related

- [[commands/gsutil-list-review-bucket]]
- [[procedures/Enumerate-Additional-Public-GCS-Buckets]]

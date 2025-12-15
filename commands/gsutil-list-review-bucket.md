---
id: c1b2c3d4-e5f6-7890-abcd-ef1234567893
data: 'gsutil ls gs://about.gitlab-review.app'
tags:
  - gcs
  - additional-bucket
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.454Z'
verified: false
validated: true
submitted: true
---
# gsutil-list-review-bucket

## Command

```bash
gsutil ls gs://about.gitlab-review.app
```

## Description

Lists objects in another public GCS bucket related to GitLab app reviews, expanding the attack surface.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ls | List bucket objects | Yes |
| gs://about.gitlab-review.app | Target review bucket | Yes |

## Examples

### Basic Usage

```bash
gsutil ls gs://about.gitlab-review.app
```

### Advanced Usage

```bash
gsutil ls -r gs://about.gitlab-review.app  # Recursive list
```

## Expected Output

Enumeration of directories like gs://about.gitlab-review.app/1006-qa-fix-color-on-links-for-campus-page/, showing app update contents.

## Related

- [[commands/gsutil-list-main-bucket]]
- [[procedures/Enumerate-Additional-Public-GCS-Buckets]]

---
id: c1b2c3d4-e5f6-7890-abcd-ef1234567891
data: 'gsutil ls gs://about.gitlab.com/'
tags:
  - gcs
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.464Z'
verified: false
validated: true
submitted: true
---
# gsutil-list-main-bucket

## Command

```bash
gsutil ls gs://about.gitlab.com/
```

## Description

Lists all objects in the public GCS bucket gs://about.gitlab.com/, demonstrating anonymous access to sensitive contents as part of proof-of-concept exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ls | List bucket objects | Yes |
| gs://about.gitlab.com/ | Target public bucket path | Yes |

## Examples

### Basic Usage

```bash
gsutil ls gs://about.gitlab.com/
```

### Advanced Usage

```bash
gsutil ls -l gs://about.gitlab.com/  # With details
```

## Expected Output

Enumeration of bucket contents including directories and files like gs://about.gitlab.com/javascripts/, gs://about.gitlab.com/all-releases.xml, etc., without authentication errors.

## Related

- [[commands/gsutil-list-javascripts-dir]]
- [[procedures/List-GCS-Bucket-Contents-with-gsutil]]

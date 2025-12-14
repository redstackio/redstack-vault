---
id: cmd-6
data: gcloud auth revoke
tags:
  - auth
  - gcloud
type: command
output: Revoked credentials
executor: bash
platforms:
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.540Z'
verified: false
validated: true
submitted: true
---
# gcloud-auth-revoke

## Command

```bash
gcloud auth revoke
```

## Description

Revokes current gcloud authentication credentials to prepare for token-based auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
gcloud auth revoke
```

### Advanced Usage

```bash
gcloud auth revoke --all
```

## Expected Output

'Revoked user credentials for project.'

## Related

- [[commands/export-cloudsdk-token]]

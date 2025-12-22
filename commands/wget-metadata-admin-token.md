---
id: cmd-21
data: >-
  wget --header 'Metadata-Flavor: Google'
  http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token
  -O admin.token
tags:
  - metadata
  - admin-token
type: command
output: Admin token JSON
executor: bash
platforms:
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.493Z'
verified: false
validated: true
submitted: true
---
# wget-metadata-admin-token

## Command

```bash
wget --header 'Metadata-Flavor: Google' http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token -O admin.token
```

## Description

Fetches the privileged service account token from master node metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header` | Metadata flavor | Yes |
| `-O` | Output file | Yes |

## Examples

### Basic Usage

```bash
wget ... -O admin.token
```

## Expected Output

JSON with broader-scoped token.

## Related

- [[commands/kubectl-cp-admin-token]]

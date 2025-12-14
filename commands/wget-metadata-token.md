---
id: cmd-3
data: >-
  wget --header 'Metadata-Flavor: Google'
  http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token
  -O default.token
tags:
  - metadata
  - token
type: command
output: JSON file saved
executor: bash
platforms:
  - GCP
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.550Z'
verified: false
validated: true
submitted: true
---
# wget-metadata-token

## Command

```bash
wget --header 'Metadata-Flavor: Google' http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token -O default.token
```

## Description

Downloads the GCP instance's default service account access token from the metadata server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--header` | Auth header for metadata | Yes |
| `-O` | Output file | Yes |
| URL | Metadata endpoint | Yes |

## Examples

### Basic Usage

```bash
wget --header 'Metadata-Flavor: Google' http://metadata.google.internal/.../token -O token.json
```

### Advanced Usage

```bash
wget --quiet --header 'Metadata-Flavor: Google' ... -O token.json
```

## Expected Output

JSON with access_token, token_type, expires_in.

## Related

- [[commands/export-cloudsdk-token]]

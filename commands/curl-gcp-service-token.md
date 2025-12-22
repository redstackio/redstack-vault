---
type: command
executor: bash
data: >-
  curl
  "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token"
  -H "Metadata-Flavor: Google"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - gcp
  - token
verified: true
validated: true
---

# curl-gcp-service-token

## Command

```bash
curl "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token" -H "Metadata-Flavor: Google"
```

## Description

Fetches the OAuth2 access token for the default service account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H "Metadata-Flavor: Google" | Metadata auth header | Yes |

## Examples

### Basic

```bash
curl "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token" -H "Metadata-Flavor: Google"
```

## Expected Output

```
{"access_token":"ya29...","expires_in":3600,"token_type":"Bearer"}
```

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]

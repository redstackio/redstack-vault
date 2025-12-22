---
type: command
executor: bash
data: >-
  curl
  "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/email"
  -H "Metadata-Flavor: Google"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - gcp
  - metadata
verified: true
validated: true
---

# curl-gcp-service-email

## Command

```bash
curl "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/email" -H "Metadata-Flavor: Google"
```

## Description

Retrieves the email of the default GCP service account from instance metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H "Metadata-Flavor: Google" | Auth header for metadata | Yes |

## Examples

### Basic

```bash
curl "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/email" -H "Metadata-Flavor: Google"
```

## Expected Output

```
123456-compute@developer.gserviceaccount.com
```

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]

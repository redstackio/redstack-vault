---
data: >-
  curl
  "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=██████████████████"
tags:
  - gcp
  - token
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: dea34d36-7492-4b99-8f11-5510c6b49dec
created_at: '2025-12-11T06:10:23.367Z'
updated_at: '2025-12-11T06:10:23.367Z'
verified: false
validated: true
submitted: true
---
# curl-query-token-info

## Command

```bash
curl "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=██████████████████"
```

## Description

Queries GCP token information to check scopes and validity of a leaked access token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `access_token` | Leaked access token to inspect | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=token-value"
```

## Expected Output

JSON with token details including scopes like https://www.googleapis.com/auth/cloud-platform.

## Related

- [[commands/curl-set-instance-metadata]]
- [[procedures/Test-and-Analyze-Leaked-GCP-Tokens]]

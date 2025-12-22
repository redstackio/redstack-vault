---
id: e3a0d731-2c84-41eb-814f-abe566c12ad2
name: gcp-check-token-scope
type: command
executor: bash
data: >-
  curl
  "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=$_ACCESS_TOKEN"
output: null
created_at: '2023-04-06T03:56:38.401259+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - GCP
tags:
  - gcp
  - token
  - oauth
verified: true
validated: true
---

# gcp-check-token-scope

## Command

```bash
curl "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=$_ACCESS_TOKEN"
```

## Description

Queries Google's OAuth2 tokeninfo endpoint to retrieve details about a GCP access token, including scopes, issuer, and expiration, to validate its permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ACCESS_TOKEN | The GCP service account access token to inspect | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=ya29.a0AfH6SMC..."
```

## Expected Output

```json
{
  "issued_to": "101302079XXXXX",
  "audience": "10130207XXXXX",
  "scope": "https://www.googleapis.com/auth/compute https://www.googleapis.com/auth/devstorage.read_write",
  "expires_in": 2443,
  "access_type": "offline"
}
```

Look for 'scope' containing 'auth/compute' for metadata manipulation capabilities.

## Related

- [[procedures/Exploit-SSRF-to-Add-SSH-Key-to-GCP-Instance]]

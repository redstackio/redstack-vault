---
id: cmd-001
data: >-
  curl -X GET https://api.netlify.com/api/v1/accounts -H "Authorization: Bearer
  ████" -s | jq
tags:
  - api
  - auth
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.728Z'
verified: false
validated: true
submitted: true
---
# curl-verify-netlify-token

## Command

```bash
curl -X GET https://api.netlify.com/api/v1/accounts -H "Authorization: Bearer ████" -s | jq
```

## Description

This command verifies a Netlify authentication token by querying the accounts endpoint, retrieving details on accessible accounts and roles.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP GET method | Yes |
| `-H "Authorization: Bearer ████"` | Adds Bearer token for authentication; replace ████ with actual token | Yes |
| `-s` | Silent mode to suppress progress meter | No |
| `| jq` | Pipes output to jq for JSON formatting | No |
| `https://api.netlify.com/api/v1/accounts` | Endpoint to fetch account information | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://api.netlify.com/api/v1/accounts -H "Authorization: Bearer your-token-here" -s | jq
```

### Advanced Usage

```bash
curl -X GET https://api.netlify.com/api/v1/accounts -H "Authorization: Bearer ████" -s | jq '.[0] | {name, roles}'
```

## Expected Output

JSON response with account details: {"name": "Mozilla IT Web SRE", "slug": "mozilla-it", "roles": ["Owner", "Developer", "Billing Admin"]}. Errors if token invalid (401 Unauthorized).

## Related

- [[Related Procedure: Verify-Token-Validity-via-Netlify-API]]

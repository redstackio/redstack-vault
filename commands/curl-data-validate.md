---
data: >-
  curl -H "Authorization: Bearer overly_permissive_key"
  https://api.stripo.com/v1/storage/user-info | jq '.data'
tags:
  - data-validation
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.767Z'
id: e1e1c1ae-30b8-438b-8b5c-49277cb4a7d6
verified: false
validated: true
submitted: true
---
# curl-data-validate

## Command

```bash
curl -H "Authorization: Bearer overly_permissive_key" https://api.stripo.com/v1/storage/user-info | jq '.data'
```

## Description

Fetches and parses user data to validate exposure, using jq for JSON filtering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Auth header | Yes |
| `Bearer overly_permissive_key` | Token | Yes |
| `https://api.stripo.com/v1/storage/user-info` | User info endpoint | Yes |
| `jq '.data'` | JSON parser | Yes (if installed) |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer key" https://api.example.com/user-info | jq '.data'
```

### Advanced Usage

```bash
curl -H "Authorization: Bearer key" https://api.example.com/user-info | jq '.data | .email'
```

## Expected Output

Filtered sensitive data, e.g., {"email": "user@example.com"}.

## Related

- [[Related Procedure: Access Unencrypted Sensitive Data Storage]]

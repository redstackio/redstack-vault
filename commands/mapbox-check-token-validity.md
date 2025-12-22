---
id: a80ae606-f145-4113-b676-51150da2c02f
name: mapbox-check-token-validity
type: command
executor: bash
data: 'curl "https://api.mapbox.com/tokens/v2?access_token=$_TOKEN"'
output: null
created_at: '2023-04-06T03:55:53.473413+00:00'
updated_at: '2023-04-06T03:55:53.486070+00:00'
platforms:
  - Linux
  - macOS
tags:
  - api
  - credential
  - validation
verified: true
validated: true
---

# mapbox-check-token-validity

## Command

```bash
curl "https://api.mapbox.com/tokens/v2?access_token=$_TOKEN"
```

## Description

This command queries the Mapbox Tokens API to validate a suspected API token and retrieve its metadata, such as scopes and associated user. Use it after discovering a potential leak to confirm usability before exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TOKEN | The Mapbox API token to validate (starts with 'pk.' or 'sk.') | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.mapbox.com/tokens/v2?access_token=pk.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

### Advanced Usage

Add -s for silent output or pipe to jq for parsing: `curl ... | jq '.tokens[0].scopes'`.

## Expected Output

Successful response is JSON detailing the token:

```json
{
  "tokens": [
    {
      "id": "token_id",
      "url": "https://account.mapbox.com/access-tokens/token_id",
      "scopes": ["styles:read", "tiles:read"],
      "token": "pk.eyJ...",
      "created": "2023-01-01T00:00:00.000Z",
      "owner": "username"
    }
  ]
}
```

Invalid tokens return: {"message":"Invalid token"} with HTTP 401.

## Related

- [[procedures/Mapbox-API-Token-Leakage]]
- [[commands/mapbox-get-account-tokens]]

---
id: 3165dca3-4a69-4174-a578-c12dc51b22cb
name: mapbox-get-account-tokens
type: command
executor: bash
data: 'curl "https://api.mapbox.com/tokens/v2/$_USERNAME?access_token=$_TOKEN"'
output: null
created_at: '2023-04-06T03:55:53.473448+00:00'
updated_at: '2023-04-06T03:55:53.486141+00:00'
platforms:
  - Linux
  - macOS
tags:
  - api
  - credential
  - enumeration
verified: true
validated: true
---

# mapbox-get-account-tokens

## Command

```bash
curl "https://api.mapbox.com/tokens/v2/$_USERNAME?access_token=$_TOKEN"
```

## Description

Retrieves a list of all API tokens associated with a Mapbox account, requiring a secret token ('sk.') with 'tokens:read' scope. Useful for expanding access after validating a single leaked token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Mapbox account username | Yes |
| $_TOKEN | Valid secret API token for authentication | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.mapbox.com/tokens/v2/exampleuser?access_token=sk.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

### Advanced Usage

With output formatting: `curl ... | jq '.tokens[] | {id, scopes}'`.

## Expected Output

JSON array of account tokens:

```json
{
  "tokens": [
    {
      "id": "token1",
      "scopes": ["styles:write"],
      "token": "pk.eyJ...",
      "created": "2023-01-01T00:00:00.000Z"
    },
    {
      "id": "token2",
      "scopes": ["geocoding:read"],
      "token": "sk.eyJ..."
    }
  ]
}
```

Failure (insufficient scope): {"message":"Forbidden"} with HTTP 403.

## Related

- [[procedures/Mapbox-API-Token-Leakage]]
- [[commands/mapbox-check-token-validity]]

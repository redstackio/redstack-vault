---
id: cmd-curl-internal-check
data: 'curl -s ''http://4290d4225642/api/v4/internal/check?secret_token=██████████'''
tags:
  - internal-api
  - auth
type: command
output: >-
  {"api_version":"v4","gitlab_version":"12.0.3","gitlab_rev":"08a51a9db93","redis":true}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.757Z'
verified: false
validated: true
submitted: true
---
# curl-internal-check

## Command

```bash
curl -s 'http://4290d4225642/api/v4/internal/check?secret_token=██████████'
```

## Description

Quietly sends a request to the internal GitLab API to check authentication with the secret token after overwrite.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Silent mode | Yes |
| secret_token=██████████ | Known token from overwrite | Yes |

## Examples

### Basic Usage

```bash
curl -s 'http://target/api/v4/internal/check?secret_token=known_hash'
```

## Expected Output

JSON with version and status info.

## Related

- [[procedures/Access-Internal-APIs-with-Overwritten-Secrets]]

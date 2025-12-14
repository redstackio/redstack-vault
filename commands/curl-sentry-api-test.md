---
data: >-
  curl -X GET -H "Authorization: Bearer
  5841673fc43843db98088d579568271bcee388b21d91455b9c1fb151bab260b9"
  https://sentry.io/api/0/projects/
tags:
  - api
  - sentry
type: command
executor: bash
platforms:
  - Linux
  - Cloud
id: ea0e63d5-3657-4794-b35b-ecb11d0ed641
created_at: '2025-12-14T17:31:42.933Z'
updated_at: '2025-12-14T17:31:42.933Z'
verified: false
validated: true
submitted: true
---
# curl-sentry-api-test

## Command

```bash
curl -X GET -H "Authorization: Bearer 5841673fc43843db98088d579568271bcee388b21d91455b9c1fb151bab260b9" https://sentry.io/api/0/projects/
```

## Description

Tests a Sentry Bearer token by requesting a list of projects from the API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET method | Yes |
| `-H "Authorization: Bearer ..."` | Auth header with token | Yes |
| `https://sentry.io/api/0/projects/` | Endpoint for projects | Yes |

## Examples

### Basic Usage

```bash
curl -X GET -H "Authorization: Bearer 5841673fc43843db98088d579568271bcee388b21d91455b9c1fb151bab260b9" https://sentry.io/api/0/projects/
```

### Advanced Usage

```bash
curl -X GET -H "Authorization: Bearer TOKEN" -H "User-Agent: Mozilla/5.0" https://sentry.io/api/0/projects/ | jq '.'
```

## Expected Output

JSON array of projects: e.g., [{"id": "123", "name": "Project Name", ...}]

## Related

- [[commands/docker-inspect-image-file]]

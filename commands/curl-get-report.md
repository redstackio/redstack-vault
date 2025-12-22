---
id: cmd-curl-get-report
data: >-
  curl -X GET 'https://hackerone.com/reports/1139535' -H 'Authorization: Bearer
  YOUR_TOKEN'
tags:
  - api
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.184Z'
verified: false
validated: true
submitted: true
---
# curl-get-report

## Command

```bash
curl -X GET 'https://hackerone.com/reports/1139535' -H 'Authorization: Bearer YOUR_TOKEN'
```

## Description

This command retrieves details of a specific HackerOne report via its API, useful for reconnaissance of data structures and identifying immutable fields during MAID assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `https://hackerone.com/reports/1139535` | Target report endpoint | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://hackerone.com/reports/1139535' -H 'Authorization: Bearer YOUR_TOKEN'
```

### Advanced Usage

```bash
curl -X GET 'https://hackerone.com/reports/1139535' -H 'Authorization: Bearer YOUR_TOKEN' -o report.json
```

## Expected Output

JSON response with report details, e.g., {"id": 1139535, "state": "resolved", ...}, allowing inspection of data fields.

## Related

- [[Related Procedure|procedures/Modify-Assumed-Immutable-Data-via-API-Manipulation]]
- [[commands/curl-patch-report]]

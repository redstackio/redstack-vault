---
data: >-
  curl -H "Authorization: Token token=YOUR_TOKEN"
  https://api.hackerone.com/v1/reports
tags:
  - api
  - get
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.209Z'
id: 1aee572e-fa74-428c-b458-3e8c9c61d0d4
verified: false
validated: true
submitted: true
---
# curl-api-read-reports

## Command

```bash
curl -H "Authorization: Token token=YOUR_TOKEN" https://api.hackerone.com/v1/reports
```

## Description

Retrieves a list of reports from HackerOne's API using token authentication. Use this to test read access and confirm token validity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Adds Authorization header with token | Yes |
| `YOUR_TOKEN` | Replace with actual API token secret | Yes |
| URL | Endpoint for reports | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Token token=abc123" https://api.hackerone.com/v1/reports
```

### Advanced Usage

```bash
curl -H "Authorization: Token token=YOUR_TOKEN" -X GET https://api.hackerone.com/v1/reports?page=1
```

## Expected Output

JSON array of report objects, e.g., {"data": [{"id": 123, "title": "Test Report"}]} with HTTP 200 status.

## Related

- [[Related Procedure: Perform-API-Operations-with-Curl]]

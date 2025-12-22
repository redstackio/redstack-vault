---
data: >-
  curl "https://api.hackerone.com/v1/hackers/payments/earnings" -X GET -u
  "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
tags:
  - api
  - hackerone
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.461Z'
id: 3d7495ff-c85d-4ef3-838c-19445331d093
verified: false
validated: true
submitted: true
---
# curl-hackerone-fetch-earnings

## Command

```bash
curl "https://api.hackerone.com/v1/hackers/payments/earnings" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

## Description

Retrieves the earnings history for the HackerOne user, bypassing ban via old token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Basic auth | Yes |
| URL | Earnings endpoint | Yes |
| `-H` | JSON accept | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.hackerone.com/v1/hackers/payments/earnings" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

## Expected Output

JSON list of earnings entries with amounts and dates.

## Related

- [[commands/curl-hackerone-fetch-balance]]
- [[procedures/Exploit-HackerOne-API-with-Old-Token]]

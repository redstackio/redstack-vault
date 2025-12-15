---
data: >-
  curl "https://api.hackerone.com/v1/hackers/reports" -X POST -u
  "testhackerone-creative:pYnONekvxUTvHbKF7Jp64qh9STIhhdXvKmefWOeR8YU=" -H
  'Content-Type: application/json' -H 'Accept: application/json' -d @- <<EOD {
  "data": { "type": "report", "attributes": { "team_handle":
  "HackerOne-test_h1b", "title": "string", "vulnerability_information": "test
  tst tst", "impact": "tst tst", "severity_rating": "none", "weakness_id": 1 } }
  } EOD
tags:
  - api
  - auth-bypass
  - hackerone
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.305Z'
id: ee0fdc62-093e-4552-b3a2-d699cec95a19
verified: false
validated: true
submitted: true
---
# curl-hackerone-report-submission

## Command

```bash
curl "https://api.hackerone.com/v1/hackers/reports" -X POST -u "testhackerone-creative:pYnONekvxUTvHbKF7Jp64qh9STIhhdXvKmefWOeR8YU=" -H 'Content-Type: application/json' -H 'Accept: application/json' -d @- <<EOD { "data": { "type": "report", "attributes": { "team_handle": "HackerOne-test_h1b", "title": "string", "vulnerability_information": "test tst tst", "impact": "tst tst", "severity_rating": "none", "weakness_id": 1 } } } EOD
```

## Description

This command submits a vulnerability report to a HackerOne program via their REST API, using basic auth with an API key to bypass UI bans. Use it when testing auth restrictions or simulating report spam.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-u "user:token"` | Basic auth credentials (username:API key) | Yes |
| `-H 'Content-Type: application/json'` | Sets request body MIME type | Yes |
| `-H 'Accept: application/json'` | Requests JSON response | Yes |
| `-d @- <<EOD ... EOD` | JSON payload with report data (team_handle, title, etc.) | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.hackerone.com/v1/hackers/reports" -X POST -u "user:token" -H 'Content-Type: application/json' -d '{"data":{"type":"report","attributes":{"team_handle":"test","title":"Test"}}}' 
```

### Advanced Usage

```bash
curl "https://api.hackerone.com/v1/hackers/reports" -X POST -u "testhackerone-creative:pYnONekvxUTvHbKF7Jp64qh9STIhhdXvKmefWOeR8YU=" -H 'Content-Type: application/json' -H 'Accept: application/json' -d @- <<EOD { "data": { "type": "report", "attributes": { "team_handle": "sony", "title": "Advanced Test", "vulnerability_information": "Detailed info", "impact": "High impact", "severity_rating": "high", "weakness_id": 1 } } } EOD
```

## Expected Output

Successful execution returns a 201 Created response with JSON containing the new report's ID and details, e.g., {"data":{"id":"123","type":"report",...}}. Failures may show 401/403 errors if auth fails.

## Related

- [[Related Procedure: Submit-Report-via-HackerOne-API]]

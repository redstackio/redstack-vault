---
data: >-
  curl
  "https://wakatime.com/api/v1/users/current/summaries?start=today&end=today&api_key=waka_edf47c40-cabf-46e7-9f88-f1b44f00431f"
tags:
  - api-testing
  - credential-validation
type: command
output: >-
  JSON response with user summary data if key is valid, or 401 Unauthorized if
  invalid
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.409Z'
id: 5c11c024-9bfe-4438-8b94-7241161f2e8d
verified: false
validated: true
submitted: true
---
# curl-test-wakatime-api-key

## Command

```bash
curl "https://wakatime.com/api/v1/users/current/summaries?start=today&end=today&api_key=waka_edf47c40-cabf-46e7-9f88-f1b44f00431f"
```

## Description

This command sends an HTTP GET request to the WakaTime API endpoint using the exposed API key to test for valid authentication and retrieve user summary data. It helps validate if the key grants unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` (implied) | Full API endpoint with parameters | Yes |
| `api_key=...` | The exposed API key in query string | Yes |

## Examples

### Basic Usage

```bash
curl "https://wakatime.com/api/v1/users/current/summaries?start=today&end=today&api_key=waka_edf47c40-cabf-46e7-9f88-f1b44f00431f"
```

### Advanced Usage

```bash
curl -v "https://wakatime.com/api/v1/users/current/summaries?start=today&end=today&api_key=waka_edf47c40-cabf-46e7-9f88-f1b44f00431f" > response.json
```

Uses -v for verbose output and saves response to file.

## Expected Output

Successful: HTTP 200 with JSON like {"data": [{"grand_total": {"total_seconds": 3600}}]}
Failed: HTTP 401 Unauthorized

## Related

- [[Related Procedure: Validate-Exposed-API-Key-on-WakaTime]]

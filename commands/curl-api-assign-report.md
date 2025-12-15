---
data: >-
  curl -X POST -H "Authorization: Token token=YOUR_TOKEN" -d
  '{"report_id":123,"state":"triage"}'
  https://api.hackerone.com/v1/reports/123/state_changes
tags:
  - api
  - post
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.207Z'
id: 5b149b7e-85fe-4c8e-b911-512d6c27192e
verified: false
validated: true
submitted: true
---
# curl-api-assign-report

## Command

```bash
curl -X POST -H "Authorization: Token token=YOUR_TOKEN" -d '{"report_id":123,"state":"triage"}' https://api.hackerone.com/v1/reports/123/state_changes
```

## Description

Assigns a new state to a HackerOne report via API, testing write permissions and triggering backend notifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H` | Authorization header | Yes |
| `-d` | JSON payload with report_id and state | Yes |
| `123` | Target report ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Authorization: Token token=abc123" -d '{"report_id":123,"state":"triage"}' https://api.hackerone.com/v1/reports/123/state_changes
```

### Advanced Usage

```bash
curl -X POST -H "Authorization: Token token=YOUR_TOKEN" -d '{"report_id":123,"state":"resolved","comment":"Fixed"}' https://api.hackerone.com/v1/reports/123/state_changes
```

## Expected Output

JSON confirmation, e.g., {"message": "State changed successfully"} with HTTP 201 status.

## Related

- [[Related Procedure: Perform-API-Operations-with-Curl]]

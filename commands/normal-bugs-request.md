---
id: cmd-001
data: >-
  curl -X GET
  "https://hackerone.com/bugs?subject=anontest5667&report_id=99698&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1"
  -H "Cookie: your_session_cookie"
tags:
  - recon
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:30.185Z'
verified: false
validated: true
submitted: true
---
# normal-bugs-request

## Command

```bash
curl -X GET "https://hackerone.com/bugs?subject=anontest5667&report_id=99698&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1" -H "Cookie: your_session_cookie"
```

## Description

Sends a standard GET request to the HackerOne /bugs endpoint to load bug reports, triggering an internal XHR to fetch report JSON. Use this to baseline normal behavior.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `subject` | Team or user handle (e.g., anontest5667) | Yes |
| `report_id` | Integer ID of the report (e.g., 99698) | Yes |
| `view` | View mode (e.g., new) | No |
| `substates[]` | Filter states (e.g., new) | No |
| `Cookie` | Session cookie for auth | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://hackerone.com/bugs?subject=anontest5667&report_id=99698" -H "Cookie: your_session_cookie"
```

### Advanced Usage

```bash
curl -X GET "https://hackerone.com/bugs?subject=anontest5667&report_id=99698&view=new&limit=25" -H "Cookie: your_session_cookie" -v
```

## Expected Output

HTML response for the bugs page (200 OK), with dev tools showing XHR GET to /reports/99698.json containing report JSON data.

## Related

- [[commands/query-appended-report-id]]
- [[procedures/Observe-Normal-Bugs-Endpoint-Behavior]]

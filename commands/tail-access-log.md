---
id: cmd-tail-log-001
data: tail -f access.log
tags:
  - logging
  - monitoring
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.730Z'
verified: false
validated: true
submitted: true
---
# tail-access-log

## Command

```bash
tail -f access.log
```

## Description

Monitors the access log in real-time to capture callback requests containing new authorization codes from silent generation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| access.log | Path to Nginx or web server log | Yes |

## Examples

### Basic Usage

```bash
tail -f /var/log/nginx/access.log
```

## Expected Output

Lines like: <IP> - - [date] "GET /callback?state=...&code=..." 200 ...

## Related

- [[commands/html-silent-authorize]]
- [[procedures/Silent-Authorization-Code-Generation-for-Persistence]]

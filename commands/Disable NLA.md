---
id: 8cc728eb-2c14-4607-a410-f373d501f74d
name: Disable NLA
type: command
executor: bash
data: 'PS > (Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices
  -ComputerName "PC01" -Filter "TerminalName=''RDP-tcp''").UserAuthenticationRequired

  PS > (Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices
  -ComputerName "PC01" -Filter "TerminalName=''RDP-tcp''").SetUserAuthenticationRequired(0)'
output: null
created_at: '2023-04-06T03:56:31.036805+00:00'
updated_at: '2023-04-10T20:37:56.779209+00:00'
---

# Disable NLA

```bash
PS > (Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices -ComputerName "PC01" -Filter "TerminalName='RDP-tcp'").UserAuthenticationRequired
PS > (Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices -ComputerName "PC01" -Filter "TerminalName='RDP-tcp'").SetUserAuthenticationRequired(0)
```

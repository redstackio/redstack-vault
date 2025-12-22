---
id: ab08ca26-a6bf-4964-8e7b-0220395d5f5d
name: enable-powershell-remoting-and-trusted-hosts-script
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:31.140832+00:00'
updated_at: '2023-04-10T20:37:59.144920+00:00'
platforms:
  - Windows
tags:
  - winrm
  - setup
validated: true
---

# enable-powershell-remoting-and-trusted-hosts-script

## Code

```ps1
Enable-PSRemoting -Force
net start winrm

# Add the machine to the trusted hosts
Set-Item wsman:\localhost\client\trustedhosts *
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "10.10.10.10"
```

## Description

This script enables PowerShell remoting by configuring WinRM on the target and setting trusted hosts on the client side to allow remote connections from specified IPs. It combines setup steps for both ends of the connection, useful for initial configuration in lab or compromised environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 10.10.10.10 | Specific IP to trust (replace with target IP) | 192.168.1.100 |

## Usage

Run the first two lines on the target machine as admin to enable remoting. Run the Set-Item lines on the attacker machine to configure trust. Use in initial access scenarios before creating PSSessions; integrate into procedures like lateral movement after credential theft.

## Detection

- Event ID 4103/4104 in PowerShell logs for remoting config changes.
- WinRM service startup in System logs (Event ID 7045).
- Network traffic on 5985/5986 to untrusted IPs.
- Sysmon process creation for powershell.exe with WinRM args.

## Related

- [[procedures/windows-powershell-remoting-with-pssession]]
- [[commands/set-trusted-hosts]]

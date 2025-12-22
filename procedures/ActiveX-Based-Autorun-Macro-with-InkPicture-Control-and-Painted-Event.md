---
id: 0df27b77-592c-4f56-a5d3-d4394d2569d5
type: procedure
name: ActiveX-Based-Autorun-Macro-with-InkPicture-Control-and-Painted-Event
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.734272+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/User Execution|TA0002.001 - User Execution: Malicious File]]'
  - >-
    [[techniques/Signed Binary Proxy Execution|T1218 - Signed Binary Proxy
    Execution]]
sub_techniques: []
tags:
  - >-
    [[tags/DOCM - ActiveX-based (InkPicture control, Painted event) Autorun
    macro]]
  - '[[tags/Office - Attacks]]'
  - macro
  - activex
  - powershell
commands:
  - '[[commands/add-microsoft-inkpicture-control]]'
tools: []
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# ActiveX-Based-Autorun-Macro-with-InkPicture-Control-and-Painted-Event

## Summary

This procedure creates an ActiveX-based autorun macro in a Microsoft Office .docm document using the InkPicture control and its Painted event to trigger the download and execution of a malicious file via PowerShell. The macro activates when the user interacts with the control by drawing or writing, bypassing typical macro warnings and enabling stealthy payload delivery.

## Description

The technique embeds malicious VBA code within the Painted event of the Microsoft InkPicture ActiveX control in a Word document (.docm). When the document is opened and macros are enabled, the control appears as an interactive drawing area. User interaction (e.g., drawing with a mouse or stylus) fires the Painted event, which executes a PowerShell command to download a file from a remote host and run it. This leverages signed binaries like PowerShell for execution while evading detection through user-initiated triggering rather than automatic Document_Open events. It targets Windows environments with Microsoft Office and is effective against users who enable macros or have them auto-enabled via policy. The approach combines ActiveX exploitation with scripting for initial access or persistence in phishing campaigns.

## Requirements

1. Microsoft Word installed on a Windows system with ActiveX controls enabled.
2. Macro security set to allow signed or all macros (or user must enable them manually).
3. Access to a remote server hosting the malicious payload file (e.g., file.exe).
4. Victim must open the .docm file and interact with the InkPicture control by drawing.

## Defense

- Disable or restrict ActiveX controls in Office applications via Group Policy or registry settings (e.g., set HKCU\Software\Microsoft\Office\<version>\Common\Security\DisableAllActiveX=true).
- Enable macro disabling by default and use Protected View for documents from untrusted sources.
- Implement PowerShell logging (Module, ScriptBlock, and Transcription) to detect anomalous downloads and executions.
- Deploy endpoint detection rules for Office macros spawning PowerShell processes or network connections from Office apps.
- User training to avoid enabling macros or interacting with unknown documents.

## Objectives

1. Embed a malicious macro in a .docm file that triggers on user interaction via the InkPicture control.
2. Download and execute a remote payload using PowerShell to establish a foothold.
3. Evade detection by relying on user action rather than automatic execution.

## Instructions

### Step 1: Insert Microsoft InkPicture Control

**Context**: Add the ActiveX InkPicture control to the Word document to enable interactive drawing, which will later trigger the malicious event. This step sets up the user interface for the attack.

**Command** ([[commands/add-microsoft-inkpicture-control]]):

Navigate to Insert > More Controls > Microsoft InkPicture Control.

> This adds the control as an object in the document. Resize and position it as needed. The control allows drawing, simulating a normal annotation feature to lure user interaction.

**Expected Output**: The InkPicture control appears in the document as a drawable area. No errors if ActiveX is enabled.

### Step 2: Implement Painted Event Handler

**Context**: Attach the malicious VBA code to the InkPicture1_Painted event. This code will execute when the user finishes drawing, downloading and running the payload.

**Code** ([[codes/VBA-InkPicture-Painted-Event-Download-Execute]]):

Embed the following VBA code in the document's VBA editor (Alt+F11), associating it with the InkPicture control's Painted event.

> Access the VBA editor, select the InkPicture control in the document, and add the subroutine to its Painted event. Replace the <host> placeholder with your payload server URL. Save the document as .docm to preserve macros.

**Expected Output**: The code integrates without syntax errors. Test by drawing in the control to verify PowerShell execution (monitor network traffic for download).

### Step 3: Test and Deploy

**Context**: Verify the macro functions and distribute the document via phishing or other vectors.

**Instructions**: Enable macros in Word, open the .docm file, draw in the InkPicture control, and confirm the payload downloads/executes. Use a listener or log to validate.

> If successful, the file.exe downloads to the temp directory and runs. Monitor for antivirus alerts or PowerShell execution logs.

**Expected Output**: Payload file downloaded and executed without crashing Word. Network request to <host> succeeds.

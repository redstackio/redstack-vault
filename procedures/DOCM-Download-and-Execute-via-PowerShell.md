---
id: f367fa63-92bf-42df-af9f-9c0d14d956a1
name: DOCM-Download-and-Execute-via-PowerShell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.397035+00:00'
updated_at: '2023-04-10T20:36:56.212263+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Office Application Startup|T1137 - Office Application Startup]]'
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/DOCM - Download and Execute]]'
  - '[[tags/Office - Attacks]]'
commands: []
platforms:
  - Windows
tools: []
validated: true
---

# DOCM-Download-and-Execute-via-PowerShell

## Summary

This procedure details how to create a malicious DOCM (Word document with macros) that, upon opening and enabling macros, downloads and executes a PowerShell payload from a remote server. It leverages VBA macros in Microsoft Office to invoke PowerShell, bypassing some macro security restrictions and enabling initial access or further payload execution in phishing or social engineering scenarios.

## Description

The attack crafts a DOCM file containing VBA code that triggers on document open. When the victim enables macros, the VBA executes a hidden PowerShell command to download and invoke a script from an attacker-controlled URL. This technique exploits Office's macro functionality for execution and evasion, often delivered via email attachments. It requires the victim to interact by enabling content, making it effective against users without strict macro policies. The payload download uses .NET WebClient with proxy support and SSL bypass, allowing execution in corporate environments with proxies. Success leads to arbitrary code execution on the victim's machine, potentially establishing persistence or exfiltrating data.

## Requirements

1. Microsoft Word installed on the attacker's machine for creating the DOCM file.
2. Victim must have Microsoft Word with macro support enabled (or be tricked into enabling macros).
3. Network access from the victim's machine to the attacker's payload server (e.g., HTTP/HTTPS endpoint).
4. Attacker-controlled server hosting the PowerShell payload script.

## Defense

- Disable macros by default in Microsoft Office via Group Policy or application settings (e.g., Block all macros except digitally signed).
- Implement email security gateways to scan and block macro-enabled attachments (e.g., using Microsoft Defender or Proofpoint).
- Monitor for anomalous PowerShell execution, such as hidden windows (-w hidden) or downloads from untrusted URLs via endpoint detection tools (e.g., EDR like CrowdStrike).
- Educate users on phishing risks and the dangers of enabling macros in unsolicited documents.
- Enable Office macro logging and auditing to detect VBA execution patterns.

## Objectives

1. Deliver initial access via social engineering (phishing email with DOCM attachment).
2. Achieve code execution on the victim's machine without additional binaries.
3. Download and run further payloads for persistence, lateral movement, or data exfiltration.

## Instructions

### Step 1: Prepare the Payload Server

**Context**: Set up a simple HTTP server to host the PowerShell payload script that will be downloaded. This ensures the VBA can fetch and execute it seamlessly.

Use a tool like Python's built-in HTTP server or Apache to host a file named 'exploit.ps1' containing your desired payload (e.g., reverse shell or keylogger).

**Expected Output**: Server logs showing the file is accessible at the specified URL (e.g., http://your-ip:port/exploit.ps1).

### Step 2: Create a New DOCM Document

**Context**: Open Microsoft Word and create a macro-enabled document to embed the VBA code. This serves as the delivery vehicle.

1. Launch Microsoft Word.
2. Go to File > New > Blank Document.
3. Save the document as a macro-enabled file: File > Save As > Choose location > File name (e.g., 'Invoice.do cm') > File type: Word Macro-Enabled Document (*.docm).

**Expected Output**: A new .docm file ready for macro insertion.

### Step 3: Insert the VBA Macro Code

**Context**: Access the VBA editor to add the macro that will execute the PowerShell download. This code runs automatically on document open.

1. Press Alt + F11 to open the VBA editor.
2. In the Project Explorer, right-click 'ThisDocument' under your project > Insert > Module (or use the existing ThisDocument for auto-open).
3. Paste the VBA code into the code window (reference [[codes/Office-VBA-Macro-for-PowerShell-Download-Execution]] for the exact snippet).
4. Customize the URL in the payload variable to point to your server (e.g., replace 'http://10.10.10.10:4242/exploit' with your endpoint).
5. Save the VBA project (Ctrl + S).

**Expected Output**: No errors in the VBA editor; the code compiles successfully.

### Step 4: Test the Macro Locally

**Context**: Verify the macro works by simulating the victim's actions in a controlled environment.

1. Close and reopen the DOCM file.
2. If prompted, click 'Enable Content' or 'Enable Macros'.
3. Monitor your payload server for the download request and check the victim's machine for PowerShell execution (e.g., via Process Explorer).

**Expected Output**: PowerShell executes the downloaded script; server logs show a GET request for 'exploit.ps1'.

### Step 5: Deliver the DOCM File

**Context**: Package and send the file to the target via phishing or other vectors to initiate the attack.

1. Attach the DOCM to an email with a enticing subject (e.g., 'Urgent Invoice Review').
2. Obfuscate if needed (e.g., rename to .zip temporarily, but ensure it extracts to .docm).
3. Send and monitor for opens via email tracking or beacon in the payload.

**Expected Output**: Victim opens the file and enables macros, triggering the download.

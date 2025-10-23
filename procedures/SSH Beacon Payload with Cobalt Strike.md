---
id: fb83012d-6421-452b-b035-ca57dec1aad1
name: SSH Beacon Payload with Cobalt Strike
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.364916+00:00'
updated_at: '2023-04-10T20:36:20.000747+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
- '[[Remote Services|T1021 - Remote Services]]'
sub_techniques:
- '[[Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]]'
tags:
- '[[Cobalt Strike]]'
- '[[Payloads]]'
- '[[SSH Beacon]]'
commands:
- '[[Deploy Beacon]]'
---

# SSH Beacon Payload with Cobalt Strike

## Summary

The SSH Beacon payload is a remote access tool that allows an attacker to establish an SSH connection with a compromised system. This payload can be used to maintain persistence on a target system, exfiltrate data, or execute arbitrary commands. The payload is delivered using Cobalt Strike, a popul

## Description

# Description

The SSH Beacon payload is a remote access tool that allows an attacker to establish an SSH connection with a compromised system. This payload can be used to maintain persistence on a target system, exfiltrate data, or execute arbitrary commands. The payload is delivered using Cobalt Strike, a popular post-exploitation tool used by red teams and penetration testers.

Technical Explanation: The SSH Beacon payload is a custom implementation of the OpenSSH client that is used to establish an SSH connection with a remote server. The payload is configured to connect to a command and control (C2) server controlled by the attacker. Once the connection is established, the attacker can execute commands on the compromised system or transfer files to and from the system.

Business Value: The SSH Beacon payload can be used by attackers to maintain a persistent presence on a compromised system, allowing them to exfiltrate sensitive data or execute additional attacks. By using Cobalt Strike to deliver the payload, attackers can evade detection by traditional security controls.

 

## Requirements

1. Valid credentials or a vulnerability to exploit for initial access to the target system

1. Cobalt Strike post-exploitation tool

 

## Defense

1. Implement strong authentication mechanisms, such as multi-factor authentication, to prevent unauthorized access to systems

1. Monitor network traffic for suspicious SSH connections, especially to external servers

1. Implement network segmentation to limit the impact of a compromised system

 

## Objectives

1. Establish a persistent presence on a compromised system

1. Exfiltrate sensitive data from the compromised system

1. Execute arbitrary commands on the compromised system

 

# Instructions

1. Use the 'ssh' command to spawn an SSH client and attempt to login to a specified target. The command takes the following arguments:
- target:port: The IP address or hostname of the target machine and the port number (if different from default 22).
- user: The username to use for the SSH login.
- pass: The password to use for the SSH login.

Use the 'ssh-key' command to spawn an SSH client and attempt to login to a specified target using a private key. The command takes the following arguments:
- target:port: The IP address or hostname of the target machine and the port number (if different from default 22).
- user: The username to use for the SSH login.
- /path/to/key.pem: The path to the private key file to use for the SSH login.

 



**Code**: [[# deploy a beacon
beacon> help ssh
Use: ssh [targe]]



> The 'ssh' and 'ssh-key' commands are used to login to a remote machine via SSH. The 'ssh' command uses a username and password to authenticate while the 'ssh-key' command uses a private key file for authentication. Both commands take the target machine's IP address or hostname and an optional port number (if different from the default SSH port 22).



**Command** ([[Deploy Beacon]]):

```bash
beacon> help ssh
Use: ssh [target:port] [user] [pass]
Spawn an SSH client and attempt to login to the specified target

beacon> help ssh-key
Use: ssh [target:port] [user] [/path/to/key.pem]
Spawn an SSH client and attempt to login to the specified target

# beacon's commands
upload                    Upload a file
download                  Download a file
socks                     Start SOCKS4a server to relay traffic
sudo                      Run a command via sudo
rportfwd                  Setup a reverse port forward
shell                     Execute a command via the shell
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Remote Access Tools|T1219 - Remote Access Tools]]
- [[Remote Services|T1021 - Remote Services]]

### Sub-Techniques

- [[Remote Desktop Protocol|T1021.001 - Remote Desktop Protocol]]

## Commands Used

- [[Deploy Beacon]]

## Tags

- [[Cobalt Strike]]
- [[Payloads]]
- [[SSH Beacon]]



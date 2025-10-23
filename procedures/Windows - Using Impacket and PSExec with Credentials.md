---
id: 7eef8430-26db-4727-bfb4-fefd63bb0458
name: Windows - Using Impacket and PSExec with Credentials
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.914397+00:00'
updated_at: '2023-04-10T20:37:58.700527+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
- '[[Remote Services|T1021 - Remote Services]]'
- '[[Scheduled Task|T1053 - Scheduled Task]]'
- '[[Service Execution|T1035 - Service Execution]]'
tags:
- '[[Impacket]]'
- '[[PSExec]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Connect to IPC$ tree and open pipe]]'
- '[[Execute command on remote machine and save output to CSV]]'
- '[[Execute custombin.exe remotely using psexec.py]]'
- '[[Execute RemComSvcCustom.exe]]'
---

# Windows - Using Impacket and PSExec with Credentials

## Summary

This procedure involves using Impacket and PSExec to execute commands on a remote Windows system with valid credentials. The attacker can use this method to gain access to the remote system and execute commands with the privileges of the user account used to authenticate. Impacket is a collection o

## Description

# Description

This procedure involves using Impacket and PSExec to execute commands on a remote Windows system with valid credentials. The attacker can use this method to gain access to the remote system and execute commands with the privileges of the user account used to authenticate. Impacket is a collection of Python classes for working with network protocols, while PSExec is a command-line tool that allows for the execution of commands on remote systems. By using these tools together, the attacker can establish a connection to the remote system and execute commands as if they were physically present on the system.

From an offensive perspective, this technique is useful for lateral movement and privilege escalation. The attacker can use this method to move laterally across the network and gain access to other systems. Additionally, the attacker can use this method to escalate privileges on the remote system by executing commands with higher privileges than the authenticated user.

From a technical perspective, the attacker first establishes a connection to the remote system using Impacket. Once the connection is established, the attacker can then use PSExec to execute commands on the remote system. The commands are executed with the privileges of the authenticated user, allowing the attacker to gain access to the remote system and execute commands as if they were physically present on the system.

From a business value perspective, this technique can be used to assess the security posture of an organization by identifying vulnerabilities in the authentication mechanism and lateral movement paths. Additionally, this technique can be used to simulate an attack and identify areas where security controls can be improved.

 

## Requirements

1. Valid credentials for the remote Windows system

1. Access to a system with Impacket and PSExec installed

 

## Defense

1. Use strong and unique passwords for all user accounts

1. Enforce two-factor authentication for all user accounts

1. Monitor network traffic for signs of lateral movement and privilege escalation

 

## Objectives

1. Gain access to a remote Windows system with valid credentials

1. Execute commands on the remote system with the privileges of the authenticated user

1. Move laterally across the network

 

# Instructions

1. Use Psexec CSV command to execute a command on multiple machines simultaneously by reading the machine names from a CSV file.

 



**Code**: [[psexeccsv]]



> The Psexec CSV command takes a CSV file as input, with the first column containing the machine names and the second column containing the command to be executed. This command is useful when you need to execute the same command on multiple machines at once. The CSV file should be saved in the same directory as the Psexec executable. The Psexec CSV command can be executed from the command prompt or from a batch file.



**Command** ([[Execute command on remote machine and save output to CSV]]):

```bash
psexec.exe \\remote_machine cmd.exe /c dir > output.csv
```



2. Use this command to upload a service binary to the ADMIN$ share of a remote machine.

 



**Code**: [[ADMIN$]]



> The ADMIN$ share is a hidden share that is created on Windows machines for administrative purposes. This command can be used to upload a service binary to this share, which can then be executed on the remote machine to perform administrative tasks. To use this command, you will need to have administrative privileges on the remote machine. The service binary should be compiled for the correct architecture of the remote machine and should be tested thoroughly before uploading.

3. To execute a custom binary on a remote machine using psexec, use the -remote-binary-name flag followed by the name of the binary file. Additionally, use the -service-name flag followed by the name of the service to be created on the remote machine. The command should be in the following format:

psexec.py [username:password]@[target_ip] -service-name [custom_service_name] -remote-binary-name [custom_binary_name]

 



**Code**: [[psexec.py Administrator:Password123@IP -service-na]]



> - [username:password]: The credentials used to authenticate and execute the command on the remote machine.
- [target_ip]: The IP address of the remote machine where the command is to be executed.
- [custom_service_name]: The name of the service to be created on the remote machine.
- [custom_binary_name]: The name of the binary file to be executed on the remote machine.



**Command** ([[Execute custombin.exe remotely using psexec.py]]):

```bash
psexec.py Administrator:Password123@IP -service-name customservicename -remote-binary-name custombin.exe
```



4. To execute a custom file, use the '-file' parameter followed by the path of the file to be executed.

 



**Code**: [[-file /tmp/RemComSvcCustom.exe]]



> This command allows the user to execute a custom file on the remote machine. The '-file' parameter is used to specify the path of the file to be executed. The path can be an absolute or relative path. The file can be an executable, batch file, script or any other file that can be executed on the remote machine. This command is useful when the user needs to execute a specific file on the remote machine that is not present in the default location.



**Command** ([[Execute RemComSvcCustom.exe]]):

```bash
-file /tmp/RemComSvcCustom.exe
```



5. To establish a connection to the Remote Communication Channel, follow these steps:
1. Call the connectTree method on the socket object and pass in the name of the tree to connect to, which is 'IPC$' in this case.
2. Call the openPipe method on the object and pass in the socket, tree ID, the name of the pipe to open, which is '\\RemCom_communicaton', and a flag value of 0x12019f.


 



**Code**: [[162    tid = s.connectTree('IPC$')
163    fid_main]]



> The connectTree method is used to establish a connection to a named pipe on the remote system. The name of the pipe is passed in as an argument. The openPipe method is used to open a named pipe that has already been created on the remote system. The socket object and tree ID are passed in as arguments, along with the name of the pipe to open and a flag value that specifies the desired access rights and sharing mode for the pipe.



**Command** ([[Connect to IPC$ tree and open pipe]]):

```bash
tid = s.connectTree('IPC$')
fid_main = self.openPipe(s,tid,r'\\RemCom_communicaton',0x12019f)
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Pass the Hash|T1075 - Pass the Hash]]
- [[Remote Services|T1021 - Remote Services]]
- [[Scheduled Task|T1053 - Scheduled Task]]
- [[Service Execution|T1035 - Service Execution]]

## Commands Used

- [[Connect to IPC$ tree and open pipe]]
- [[Execute command on remote machine and save output to CSV]]
- [[Execute custombin.exe remotely using psexec.py]]
- [[Execute RemComSvcCustom.exe]]

## Tags

- [[Impacket]]
- [[PSExec]]
- [[Windows - Using credentials]]



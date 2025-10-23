---
id: 1d5706bb-b899-46cc-a6d5-cf1ce92b19fd
name: Windows Credentials Impacket Commands
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.853585+00:00'
updated_at: '2023-04-10T20:37:57.917393+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Pass the Hash|T1075 - Pass the Hash]]'
tags:
- '[[Impacket]]'
- '[[Windows - Using credentials]]'
commands:
- '[[Add Local Account Token Filter Policy]]'
- '[[Enable FilterAdministratorToken]]'
- '[[Execute atexec.py tool]]'
- '[[Execute dcomexec.py]]'
- '[[Execute wmiexec.py with username and NTLM hash]]'
- '[[Execute wmiexec.py with username and password]]'
- '[[psexec.py execution]]'
- '[[SMBExec.py Connection]]'
---

# Windows Credentials Impacket Commands

## Summary

This procedure involves using various Impacket commands to execute remote commands, schedule tasks, and execute commands via DCOM and WMI. These commands require valid credentials to be inputted and allow the attacker to execute commands on the victim's machine. This can be used to perform actions 

## Description

# Description

This procedure involves using various Impacket commands to execute remote commands, schedule tasks, and execute commands via DCOM and WMI. These commands require valid credentials to be inputted and allow the attacker to execute commands on the victim's machine. This can be used to perform actions such as lateral movement, privilege escalation, and data exfiltration. Impacket is a collection of Python classes for working with network protocols and can be used for both offensive and defensive purposes. The business value of this procedure is that it can help identify weaknesses in an organization's security posture and allow for the implementation of stronger security measures.

 

## Requirements

1. Valid credentials with sufficient permissions

1. Access to the victim's network

1. Impacket installed on the attacker's machine

 

## Defense

1. Implement strong password policies and regular password rotations

1. Use multi-factor authentication to prevent credential theft

1. Monitor network traffic for suspicious activity

 

## Objectives

1. Execute remote commands on a victim's machine

1. Perform lateral movement

1. Escalate privileges

1. Exfiltrate data

 

# Instructions

1. Execute commands on a remote machine using the PSEXEC equivalent. The command requires the following arguments: 
1. DOMAIN: The domain of the remote machine 
2. username: The username to use for authentication 
3. password: The password to use for authentication 
4. IP address: The IP address of the remote machine

 



**Code**: [[psexec.py DOMAIN/username:password@10.10.10.10]]



> This command allows the user to execute commands on a remote machine using the RemComSvc binary. The command requires the user to provide the domain, username, password, and IP address of the remote machine. Once authenticated, the user can execute commands on the remote machine as if they were physically present. This is useful for remote administration and troubleshooting purposes.



**Command** ([[psexec.py execution]]):

```bash
DOMAIN/username:password@10.10.10.10
```



2. The SMBExec command is used to execute commands on a remote Windows machine using SMB protocol. The command requires the domain, username, password and IP address of the target machine. Once the command is executed, it establishes a connection with the target machine and allows the user to execute commands in the context of the target machine.

 



**Code**: [[smbexec.py DOMAIN/username:password@10.10.10.10]]



> The SMBExec command is typically used by system administrators to remotely manage Windows machines. It is a powerful tool that allows administrators to execute commands on remote machines without having to physically access them. The command works by establishing a connection with the target machine using SMB protocol and then executing the specified commands in the context of the target machine. The command requires the domain, username, password and IP address of the target machine. The domain, username and password are used to authenticate the user on the target machine and the IP address is used to establish a connection with the target machine. Once the connection is established, the user can execute any command on the target machine that they have permissions to execute.



**Command** ([[SMBExec.py Connection]]):

```bash
smbexec.py DOMAIN/username:password@10.10.10.10
```



3. To use this command, replace 'DOMAIN', 'username', 'password', and '10.10.10.10' with the appropriate values for your target machine. Then, execute the command to run the specified command on the target machine through the Task Scheduler service.

 



**Code**: [[atexec.py DOMAIN/username:password@10.10.10.10]]



> This command allows an attacker to execute a command on a target machine through the Task Scheduler service. The attacker can specify the command to be executed and the output of the command will be returned to the attacker. This technique can be used to bypass endpoint protection solutions that may be monitoring for traditional command execution methods.



**Command** ([[Execute atexec.py tool]]):

```bash
atexec.py DOMAIN/username:password@10.10.10.10
```



4. The DCOMExec command is used to execute commands on remote Windows systems using DCOM. This command requires authentication credentials to be provided in the format of DOMAIN/username:password@ip_address. Once authenticated, DCOMExec provides a semi-interactive shell that allows for the execution of commands on the remote system.

 



**Code**: [[dcomexec.py DOMAIN/username:password@10.10.10.10]]



> The 'DOMAIN' field should be replaced with the name of the domain that the remote system is a part of. The 'username' and 'password' fields should be replaced with valid credentials for a user account that has administrative privileges on the remote system. The 'ip_address' field should be replaced with the IP address of the remote system. Once authenticated, the user can execute commands on the remote system using the semi-interactive shell provided by DCOMExec.



**Command** ([[Execute dcomexec.py]]):

```bash
dcomexec.py DOMAIN/username:password@10.10.10.10
```



5. To use WMIExec, you need to specify the target machine's IP address or hostname, the domain/username and password hash (if applicable) to authenticate to the target machine. Once authenticated, you can execute commands on the target machine remotely. If you do not specify the password hash, you will be prompted to enter the password manually.

 



**Code**: [[wmiexec.py DOMAIN/username:password@10.10.10.10
wm]]



> WMIExec is a tool used for remote command execution on Windows machines using Windows Management Instrumentation (WMI). It is useful for lateral movement and privilege escalation within a Windows network. WMIExec uses ports tcp/135 and tcp/445 to establish a connection with the target machine, and then communicates with the Winmgmt Windows service over a dynamically allocated high port such as tcp/50911. This tool can be used to execute commands on the target machine remotely, and can be helpful in situations where interactive shells are not possible or allowed.



**Command** ([[Execute wmiexec.py with username and password]]):

```bash
wmiexec.py DOMAIN/username:password@10.10.10.10
```





**Command** ([[Execute wmiexec.py with username and NTLM hash]]):

```bash
wmiexec.py DOMAIN/username@10.10.10.10 -hashes aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
```



6. This command adds a registry key that enables Non-RID 500 local admin accounts to perform Wmi or PsExec operations on a Windows system. The command adds the LocalAccountTokenFilterPolicy key to the System subkey of the Windows registry and sets its value to 1. This allows local administrators who are not members of the built-in Administrators group (RID 500) to perform certain administrative tasks on remote systems.

 



**Code**: [[reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVer]]



> The /v switch specifies the name of the registry value to be added, modified or deleted. In this case, the value is LocalAccountTokenFilterPolicy. The /t switch specifies the type of the registry value to be added. In this case, the type is REG_DWORD (32-bit DWORD value). The /f switch forces the command to overwrite any existing registry value without prompting for confirmation. The /d switch specifies the data to be added to the registry value. In this case, the data is 1, which enables the LocalAccountTokenFilterPolicy.



**Command** ([[Add Local Account Token Filter Policy]]):

```bash
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /f /d 1
```



7. Run the following command in Command Prompt or PowerShell:

 



**Code**: [[reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVer]]



> This command adds a registry key that enables the Filter Administrator Token feature in Windows. This feature prevents the built-in Administrator account (RID 500) from being able to remotely execute commands using tools like WmiExec or PsExec. By default, the built-in Administrator account has full access to the system, which makes it a prime target for attackers. Enabling this feature helps to mitigate the risk of lateral movement by attackers who have already compromised the built-in Administrator account on a system.



**Command** ([[Enable FilterAdministratorToken]]):

```bash
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v FilterAdministratorToken /t REG_DWORD /f /d 1
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Pass the Hash|T1075 - Pass the Hash]]

## Commands Used

- [[Add Local Account Token Filter Policy]]
- [[Enable FilterAdministratorToken]]
- [[Execute atexec.py tool]]
- [[Execute dcomexec.py]]
- [[Execute wmiexec.py with username and NTLM hash]]
- [[Execute wmiexec.py with username and password]]
- [[psexec.py execution]]
- [[SMBExec.py Connection]]

## Tags

- [[Impacket]]
- [[Windows - Using credentials]]



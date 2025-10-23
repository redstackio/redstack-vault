---
id: 809678dd-9196-48b8-8341-c5551f277757
name: Linux Privilege Escalation via SUID
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:18.794497+00:00'
updated_at: '2023-04-10T20:34:26.771390+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Setuid and Setgid|T1166 - Setuid and Setgid]]'
tags:
- '[[Linux - Privilege Escalation]]'
- '[[SUID]]'
commands:
- '[[List Sudo Permissions]]'
---

# Linux Privilege Escalation via SUID

## Summary

Linux systems often have executables with the SUID bit set, which allows them to run with the permissions of the file owner. This can be abused by attackers to escalate their privileges on the system. An attacker may use techniques such as changing the UID, confirming user execution, or viewing sud

## Description

# Description

Linux systems often have executables with the SUID bit set, which allows them to run with the permissions of the file owner. This can be abused by attackers to escalate their privileges on the system. An attacker may use techniques such as changing the UID, confirming user execution, or viewing sudo permissions to identify and exploit vulnerable SUID executables. Privilege escalation via SUID can allow attackers to gain access to sensitive data or perform unauthorized actions on the system.

 

## Requirements

1. Access to a Linux system with SUID executables

 

## Defense

1. Regularly review and audit SUID executables to ensure they are necessary and secure

1. Restrict access to SUID executables to only authorized users and groups

1. Implement least privilege principles to limit the impact of a successful SUID privilege escalation attack

 

## Objectives

1. Gain elevated privileges on the target Linux system

1. Access sensitive data or perform unauthorized actions on the system

 

# Instructions

1. To set the SUID bit on a file, use the chmod command followed by the number 4 as the first digit of the file permissions. For example, to set the SUID bit on a file named "myfile", use the command: chmod 4755 myfile.

 



**Code**: [[root]]



> The SUID bit is a special permission bit that is used to allow users to execute a file with the permissions of the file owner instead of the user who is running the file. This can be useful for allowing non-root users to execute specific commands with elevated privileges.

2. usermod -u [new_uid] [username]

 



**Code**: [[root]]



> This command is used to change the UID (user identification number) of a user. The [new_uid] argument specifies the new UID that you want to set for the user, and the [username] argument specifies the name of the user whose UID you want to change. Note that changing the UID of a user can have unintended consequences and should be done with caution.

3. This command confirms that the action was executed by the user.

 



**Code**: [[bob]]



> The 'data' field contains the name of the user who executed the action. The 'text' field provides additional confirmation that the action was executed by the user. No additional arguments are required for this command.

4. The SUID bit (set user ID bit) is a special permission bit that allows a user to execute a file with the permissions of the file owner rather than the user who runs the file. To set the SUID bit, use the chmod command with the numeric value 4 followed by the file name. For example, chmod 4755 file.txt.

 



**Code**: [[s]]



> The SUID bit is commonly used for programs that need to perform actions that require elevated privileges, such as changing passwords or managing system resources. However, it can also be a security risk if not used properly, as it can allow unauthorized access to sensitive information or system resources.

5. To view the permissions of sudo, use the 'ls' command followed by the path to sudo binary and the '-alh' options.

 



**Code**: [[╭─swissky@lab ~  
╰─$ ls /usr/bin/sudo -alh       ]]



> The 'ls' command is used to list the files and directories within a specified directory. The '-a' option shows all files and directories, including hidden ones. The '-l' option displays the files and directories in a long format, including the permissions, owner, group, size, and modification date. The '-h' option displays the file sizes in a human-readable format. The 'sudo' binary is located in the '/usr/bin/' directory, and the '-alh' options are used to display its permissions in a human-readable format.



**Command** ([[List Sudo Permissions]]):

```bash
ls /usr/bin/sudo -alh
```



## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Setuid and Setgid|T1166 - Setuid and Setgid]]

## Commands Used

- [[List Sudo Permissions]]

## Tags

- [[Linux - Privilege Escalation]]
- [[SUID]]



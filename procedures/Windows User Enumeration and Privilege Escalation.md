---
id: 9adb8704-13aa-4ef7-ad3e-b48371008d10
name: Windows User Enumeration and Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.643074+00:00'
updated_at: '2023-04-10T20:37:41.733300+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[System Owner/User Discovery|T1033 - System Owner/User Discovery]]'
sub_techniques:
- '[[Domain Account|T1087.002 - Domain Account]]'
- '[[Local Account|T1087.001 - Local Account]]'
tags:
- '[[User Enumeration]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Check User Groups]]'
- '[[Check User Privileges]]'
- '[[Create new users]]'
- '[[Discover Domain Controllers]]'
- '[[Get Domain Controller Information]]'
- '[[Get Primary Domain Controller]]'
- '[[List Local Groups]]'
- '[[Net Accounts Configuration]]'
---

# Windows User Enumeration and Privilege Escalation

## Summary

Windows User Enumeration and Privilege Escalation is a technique used to identify user accounts and their privileges on a Windows system. This technique is commonly used by attackers to gain access to sensitive information or to escalate privileges on a compromised system. The technique involves th

## Description

# Description

Windows User Enumeration and Privilege Escalation is a technique used to identify user accounts and their privileges on a Windows system. This technique is commonly used by attackers to gain access to sensitive information or to escalate privileges on a compromised system. The technique involves the use of various commands to extract information about users and their privileges on the system. This information can then be used to identify potential targets for privilege escalation or to identify weak points in the system's security.

From a technical standpoint, this technique involves the use of several commands to extract information about users and their privileges. These commands include 'Get Current Username', 'User Privilege List', 'List All Users Information', 'Net Accounts Information', 'User Details', 'Local Groups List', 'Administrators Group Details', and 'Domain Controller Information'.

From a business perspective, this technique can be used to identify potential security weaknesses in a Windows environment. By identifying weak points in the system's security, organizations can take steps to improve their security posture and prevent attacks from being successful.

 

## Requirements

1. Authenticated access to a Windows system

1. Access to the command line interface

 

## Defense

1. Implement the principle of least privilege to limit the exposure of user accounts

1. Use strong passwords and enforce password policies to prevent unauthorized access

1. Monitor user activity and logins to detect and respond to suspicious behavior

 

## Objectives

1. Identify user accounts and their privileges on a Windows system

1. Identify potential targets for privilege escalation

1. Identify weak points in the system's security

 

# Instructions

1. This command retrieves the current username of the user executing the command. The command works on both Windows and Linux systems.

To execute the command, simply copy and paste it into a command prompt or terminal and press enter.

 



**Code**: [[echo %USERNAME% || whoami
$env:username]]



> The command uses two different methods to retrieve the current username. The first method, 'echo %USERNAME%', is specific to Windows and retrieves the username from an environment variable. The second method, 'whoami' is a universal command that retrieves the current user's name from the system. The command then outputs the username in two different formats, separated by the '||' operator. The first format is the Windows environment variable format, while the second format is the PowerShell variable format.

2. To list the user's privilege, run the following commands:
1. whoami /priv
2. whoami /groups

 



**Code**: [[whoami /priv
whoami /groups]]



> The 'whoami' command is used to display the current user's security context. The '/priv' option lists the user's privilege information, such as the user's ability to perform certain actions on the system. The '/groups' option lists the groups to which the user belongs. This command is useful for troubleshooting user access issues and determining which privileges a user has on a system.



**Command** ([[Check User Privileges]]):

```bash
whoami /priv
```





**Command** ([[Check User Groups]]):

```bash
whoami /groups
```



3. This command will list all the users on the system along with their enabled status and last logon time. It will also list the names of all the directories under C:\Users. To run this command, open PowerShell and copy-paste the above command.

 



**Code**: [[net user
whoami /all
Get-LocalUser | ft Name,Enabl]]



> The 'net user' command lists all the users on the system along with some basic information like their account status and password expiration date. The 'whoami /all' command lists the current user's group membership and other information. The 'Get-LocalUser' command lists all the local users on the system along with their enabled status and last logon time. The 'Get-ChildItem' command lists the names of all the directories under C:\Users. The 'select Name' part of the command selects only the 'Name' property of the directories.

4. The 'net accounts' command is used to display the current logon requirements for the system. This includes password length, age, complexity, and lockout settings. This information can be useful for determining the strength of the current password policy and can be used to plan a brute force attack.

 



**Code**: [[net accounts]]



> The 'net accounts' command takes no arguments and simply displays the current logon requirements for the system. The output will include information such as the minimum password length, password complexity requirements, and the number of failed logon attempts allowed before a user is locked out of their account. It is important to note that this command requires administrative privileges to run.



**Command** ([[Net Accounts Configuration]]):

```bash
Maximum password age: 90 days
Minimum password age: 1 days
Minimum password length: 7 characters
Length of password history maintained: 24 passwords
Lockout threshold: 5 invalid logon attempts
Lockout duration: 30 minutes
Logon hours allowed: All
```



5. To get details about a user, run the following commands in PowerShell:
1. net user administrator
2. net user admin
3. net user %USERNAME%

 



**Code**: [[net user administrator
net user admin
net user %US]]



> This command will provide you with details about the specified users, including their full name, description, account type, and when their password was last set. The first two commands will give you details about the built-in Windows users 'administrator' and 'admin', while the third command will give you details about the current user.



**Command** ([[Create new users]]):

```bash
net user administrator
net user admin
net user %USERNAME%
```



6. To list all local groups, run the following command:

 



**Code**: [[net localgroup
Get-LocalGroup | ft Name]]



> This command will display a list of all the local groups on the system. The 'net localgroup' command is a legacy command used to manage local groups on older versions of Windows, while the 'Get-LocalGroup' command is used on newer versions of Windows. The 'ft Name' parameter is used to only display the name of the local groups in a table format.



**Command** ([[List Local Groups]]):

```bash
net localgroup
```



7. To use this command, open PowerShell and run the command as is. It will display the members of the Administrators group along with their PrincipalSource.

 



**Code**: [[net localgroup administrators
Get-LocalGroupMember]]



> This command is useful to get details about the members of a specific group. In this case, it displays the members of the Administrators group along with their PrincipalSource. The 'net localgroup administrators' command lists the members of the Administrators group, and the 'Get-LocalGroupMember' command gets the members of the Administrateurs group (the French equivalent of Administrators) and formats the output to display the member's name and PrincipalSource. This command can be modified to get details about other groups by changing the group name in the command.

8. To get information about the Domain Controllers in a domain, run the following commands:

 



**Code**: [[nltest /DCLIST:DomainName
nltest /DCNAME:DomainNam]]



> This command provides information about the domain controllers in a domain. The /DCLIST command lists all the domain controllers in the domain. The /DCNAME command displays the name of the domain controller that authenticated the user. The /DSGETDC command displays detailed information about the domain controller that authenticated the user. The DomainName parameter specifies the name of the domain for which you want to retrieve the information.



**Command** ([[Discover Domain Controllers]]):

```bash
nltest /DCLIST:DomainName
```





**Command** ([[Get Primary Domain Controller]]):

```bash
nltest /DCNAME:DomainName
```





**Command** ([[Get Domain Controller Information]]):

```bash
nltest /DSGETDC:DomainName
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[System Owner/User Discovery|T1033 - System Owner/User Discovery]]

### Sub-Techniques

- [[Domain Account|T1087.002 - Domain Account]]
- [[Local Account|T1087.001 - Local Account]]

## Commands Used

- [[Check User Groups]]
- [[Check User Privileges]]
- [[Create new users]]
- [[Discover Domain Controllers]]
- [[Get Domain Controller Information]]
- [[Get Primary Domain Controller]]
- [[List Local Groups]]
- [[Net Accounts Configuration]]

## Tags

- [[User Enumeration]]
- [[Windows - Privilege Escalation]]



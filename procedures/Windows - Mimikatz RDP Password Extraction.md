---
id: ff0152e4-76ed-437d-98ac-f780ed474c15
name: Windows - Mimikatz RDP Password Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.450645+00:00'
updated_at: '2023-04-10T20:37:15.859080+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[RDP Passwords]]'
- '[[Windows - Mimikatz]]'
commands:
- '[[Extract Logon Passwords]]'
---

# Windows - Mimikatz RDP Password Extraction

## Summary

Mimikatz is a powerful post-exploitation tool used by attackers to extract sensitive information from Windows systems. In this case, Mimikatz is used to extract RDP passwords from memory. RDP passwords are often stored in memory in plain text, which makes them vulnerable to Mimikatz. Attackers can 

## Description

# Description

Mimikatz is a powerful post-exploitation tool used by attackers to extract sensitive information from Windows systems. In this case, Mimikatz is used to extract RDP passwords from memory. RDP passwords are often stored in memory in plain text, which makes them vulnerable to Mimikatz. Attackers can use these passwords to gain unauthorized access to systems and steal sensitive information.

Technical Explanation: Mimikatz is a tool that extracts plaintext passwords, hash, PIN code and kerberos tickets from memory. In this case, Mimikatz extracts RDP passwords from memory. The tool uses a variety of techniques to bypass Windows security mechanisms and extract passwords from memory.

Business Value: Attackers can use Mimikatz to extract RDP passwords from memory and gain unauthorized access to systems. This can lead to theft of sensitive information, financial loss, and damage to reputation.

 

## Requirements

1. Access to the target system

1. Mimikatz tool installed on the attacker's system

 

## Defense

1. Implement strong password policies and enforce regular password changes

1. Monitor and analyze system logs for suspicious activity

1. Use endpoint protection software to detect and prevent Mimikatz usage

 

## Objectives

1. Extract RDP passwords from memory

1. Gain unauthorized access to systems

 

# Instructions

1. To extract passwords manually, run the following commands:
1. procdump64.exe -ma 988 -accepteula C:\svchost.dmp
2. strings -el svchost* | grep Password123 -C3

The first command will create a memory dump of the process with PID 988 and save it as svchost.dmp in the C drive. The second command will search for the string "Password123" in the svchost files and display 3 lines of context before and after each match.

 



**Code**: [[procdump64.exe -ma 988 -accepteula C:\svchost.dmp
]]



> The above commands can be used to manually extract passwords from a system. The first command creates a memory dump of the process with PID 988, which can then be analyzed for any passwords or sensitive information. The second command searches for the string "Password123" in the svchost files and displays 3 lines of context before and after each match, making it easier to identify any relevant information.

2. To extract passwords using Mimikatz, follow these steps:
1. Open a command prompt as an administrator
2. Navigate to the directory where Mimikatz is located
3. Run the command: mimikatz.exe privilege::debug ts::logonpasswords
4. The passwords will be displayed in the command prompt

 



**Code**: [[privilege::debug
ts::logonpasswords]]



> This command uses Mimikatz to extract passwords from a Windows system. The 'privilege::debug' command is used to enable debug privileges, which are required for accessing certain system information. The 'ts::logonpasswords' command is used to extract passwords from the system's memory. It is important to note that this command should only be used for ethical hacking or penetration testing purposes, and should not be used to gain unauthorized access to systems.



**Command** ([[Extract Logon Passwords]]):

```bash
privilege::debug
ts::logonpasswords
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Extract Logon Passwords]]

## Tags

- [[RDP Passwords]]
- [[Windows - Mimikatz]]



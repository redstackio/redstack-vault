---
id: 1adbc996-425b-4da4-ad87-6dd4a011328e
name: Windows - Mimikatz Password Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.087804+00:00'
updated_at: '2023-04-10T20:37:17.332944+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Execute commands]]'
- '[[Windows - Mimikatz]]'
commands:
- '[[Extract Logon Passwords and Wdigest]]'
- '[[Extract logon passwords using Mimikatz]]'
---

# Windows - Mimikatz Password Extraction

## Summary

Mimikatz is a powerful post-exploitation tool that can be used to extract Windows logon passwords from memory. This tool is commonly used by attackers to escalate privileges and move laterally within a network. Mimikatz works by exploiting weaknesses in the Windows authentication process and extrac

## Description

# Description

Mimikatz is a powerful post-exploitation tool that can be used to extract Windows logon passwords from memory. This tool is commonly used by attackers to escalate privileges and move laterally within a network. Mimikatz works by exploiting weaknesses in the Windows authentication process and extracting plaintext passwords from memory. This technique can be used to extract passwords for any user who has logged into the compromised system, including domain administrators.

From a technical standpoint, Mimikatz works by patching certain Windows system functions to capture plaintext passwords as they are passed between system components. Once the passwords are captured, they can be displayed in plain text or saved to a file for later use.

The business value of Mimikatz password extraction is that it allows an attacker to gain access to sensitive data and systems within a network. By extracting passwords for high-privilege accounts, an attacker can move laterally within a network and gain access to additional systems and data.

 

## Requirements

1. Local or remote access to a Windows system

1. Administrator-level privileges on the target system

1. Mimikatz tool installed on the attacker's system

 

## Defense

1. Implement strict password policies and require regular password changes

1. Monitor for suspicious activity, such as unusual logon times or failed logon attempts

1. Use multi-factor authentication to reduce the impact of password theft

 

## Objectives

1. Extract Windows logon passwords from memory

1. Escalate privileges and move laterally within a network

1. Gain access to sensitive data and systems within a network

 

# Instructions

1. To extract logon passwords using Mimikatz, follow these steps:
1. Open a PowerShell prompt in the directory where Mimikatz is located
2. Enter the command shown in the 'data' field
3. Press Enter to execute the command
4. The extracted passwords will be displayed in the PowerShell prompt

 



**Code**: [[PS C:\temp\mimikatz> .\mimikatz "privilege::debug"]]



> This command uses Mimikatz, a post-exploitation tool, to extract Windows logon passwords from memory. The 'privilege::debug' command enables debugging privileges for Mimikatz, which is required to extract certain types of passwords. The 'sekurlsa::logonpasswords' command instructs Mimikatz to extract logon passwords from memory. The 'exit' command exits Mimikatz after the passwords have been extracted.



**Command** ([[Extract logon passwords using Mimikatz]]):

```powershell
PS C:\temp\mimikatz> .\mimikatz "privilege::debug" "sekurlsa::logonpasswords" exit
```



2. To extract logon passwords using Mimikatz, follow these steps:
1. Open Mimikatz console by navigating to the folder where Mimikatz is located and running the command '.\mimikatz'.
2. Enable debug privileges by running the command 'privilege::debug'.
3. Enable logging by running the command 'log'.
4. Extract logon passwords by running the command 'sekurlsa::logonpasswords'.
5. Extract passwords stored in WDigest by running the command 'sekurlsa::wdigest'.

 



**Code**: [[PS C:\temp\mimikatz> .\mimikatz
mimikatz # privile]]



> Mimikatz is a popular tool used for extracting various types of credentials and other sensitive information from Windows systems. The commands listed above are used to extract logon passwords and passwords stored in WDigest from the system. Once the tool is run, it will display the extracted passwords in the console output. It is important to note that the use of Mimikatz may be detected by antivirus software and other security tools, and its use may be a violation of organizational security policies.



**Command** ([[Extract Logon Passwords and Wdigest]]):

```bash
.\mimikatz
privilege::debug
log
sekurlsa::logonpasswords
sekurlsa::wdigest
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Extract Logon Passwords and Wdigest]]
- [[Extract logon passwords using Mimikatz]]

## Tags

- [[Execute commands]]
- [[Windows - Mimikatz]]



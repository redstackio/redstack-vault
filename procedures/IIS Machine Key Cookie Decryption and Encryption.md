---
id: deb02ce8-fbfa-4c76-a86d-e07523becf5d
name: IIS Machine Key Cookie Decryption and Encryption
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:53.446569+00:00'
updated_at: '2023-04-06T03:55:53.464965+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]'
sub_techniques:
- '[[Pass the Ticket|T1550.003 - Pass the Ticket]]'
tags:
- '[[API Key Leaks]]'
- '[[Edit cookies with the machine key]]'
- '[[Exploit]]'
- '[[IIS Machine Keys]]'
commands:
- '[[Decrypt cookie using AspDotNetWrapper.exe]]'
- '[[Edit Decrypted.txt and encrypt cookie using AspDotNetWrapper.exe]]'
---

# IIS Machine Key Cookie Decryption and Encryption

## Summary

This procedure allows an attacker to decrypt and encrypt cookie data using the IIS machine key. By decrypting the cookie, the attacker can view the contents of the cookie, and by encrypting it, they can modify the contents. This can be used to gain unauthorized access to a web application, escalate

## Description

# Description

This procedure allows an attacker to decrypt and encrypt cookie data using the IIS machine key. By decrypting the cookie, the attacker can view the contents of the cookie, and by encrypting it, they can modify the contents. This can be used to gain unauthorized access to a web application, escalate privileges, or conduct other malicious activities. The IIS machine key is used to encrypt and decrypt sensitive data in ASP.NET applications, and it is often stored in a configuration file on the server.

 

## Requirements

1. Access to the IIS machine key configuration file

1. The AspDotNetWrapper.exe tool

 

## Defense

1. Store the machine key configuration file in a secure location with limited access

1. Enable ViewState encryption to protect sensitive data in cookies

1. Implement secure cookie handling practices, such as HttpOnly and Secure flags, to prevent cookie theft

 

## Objectives

1. Decrypt and view the contents of a cookie

1. Encrypt a modified cookie to gain unauthorized access to a web application

1. Escalate privileges or conduct other malicious activities

 

# Instructions

1. The AspDotNetWrapper.exe tool is used to decrypt and encrypt cookies. To decrypt a cookie, use the --decrypt flag and provide the path to the machine key configuration file with the --keypath flag. The --cookie flag is used to specify the cookie to decrypt. The --purpose flag should be set to owin.cookie, and the --valalgo and --decalgo flags should be set to hmacsha512 and aes, respectively. To encrypt a modified cookie, edit the Decrypted.txt file and use the --decryptDataFilePath flag with the path to the edited file.

 



**Code**: [[# decrypt cookie
$ AspDotNetWrapper.exe --keypath ]]



> The AspDotNetWrapper.exe tool is used to decrypt and encrypt cookies using the IIS machine key. The --keypath flag is used to specify the path to the machine key configuration file. The --cookie flag is used to specify the cookie to decrypt. The --purpose flag should be set to owin.cookie, and the --valalgo and --decalgo flags should be set to hmacsha512 and aes, respectively. To encrypt a modified cookie, edit the Decrypted.txt file and use the --decryptDataFilePath flag with the path to the edited file.



**Command** ([[Decrypt cookie using AspDotNetWrapper.exe]]):

```bash
$ AspDotNetWrapper.exe --keypath C:\MachineKey.txt --cookie XXXXXXX_XXXXX-XXXXX --decrypt --purpose=owin.cookie --valalgo=hmacsha512 --decalgo=aes
```





**Command** ([[Edit Decrypted.txt and encrypt cookie using AspDotNetWrapper.exe]]):

```bash
$ AspDotNetWrapper.exe --decryptDataFilePath C:\DecryptedText.txt
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

### Sub-Techniques

- [[Pass the Ticket|T1550.003 - Pass the Ticket]]

## Commands Used

- [[Decrypt cookie using AspDotNetWrapper.exe]]
- [[Edit Decrypted.txt and encrypt cookie using AspDotNetWrapper.exe]]

## Tags

- [[API Key Leaks]]
- [[Edit cookies with the machine key]]
- [[Exploit]]
- [[IIS Machine Keys]]



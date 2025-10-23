---
id: 80a89b42-3f49-4cb0-b3ed-0cd36610209b
name: Password Extraction from SYSVOL and Group Policy Preferences
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.506016+00:00'
updated_at: '2023-04-10T20:26:19.557166+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Password Filter DLL|T1174 - Password Filter DLL]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Passwords in SYSVOL & Group Policy Preferences]]'
commands:
- '[[Decrypt password using openssl]]'
---

# Password Extraction from SYSVOL and Group Policy Preferences

## Summary

Password Extraction from SYSVOL and Group Policy Preferences is a technique used to extract passwords from Group Policy Objects (GPOs) stored in SYSVOL. Attackers can search for cpassword values in GPOs or decrypt the password encrypted with AES-256-CBC. This technique can be used to obtain privile

## Description

# Description

Password Extraction from SYSVOL and Group Policy Preferences is a technique used to extract passwords from Group Policy Objects (GPOs) stored in SYSVOL. Attackers can search for cpassword values in GPOs or decrypt the password encrypted with AES-256-CBC. This technique can be used to obtain privileged account passwords, which can be used to move laterally within the network and escalate privileges. This technique is commonly used in combination with other Active Directory attacks to achieve domain dominance.

 

## Requirements

1. Authenticated access to the domain

1. Access to SYSVOL

1. Access to Group Policy Objects

1. Tools to search for cpassword values or decrypt passwords

 

## Defense

1. Implement strong password policies and ensure that passwords are not stored in Group Policy Preferences

1. Monitor SYSVOL and Group Policy Objects for changes and unauthorized access

1. Use tools such as Microsoft's LAPS to manage local administrator passwords

 

## Objectives

1. Extract passwords from SYSVOL and Group Policy Preferences

1. Obtain privileged account passwords

1. Move laterally within the network

1. Escalate privileges

 

# Instructions

1. To search for passwords in SYSVOL, use the following commands:

1. Navigate to the SYSVOL directory: 'cd \\&lt;DOMAIN&gt;\SYSVOL\&lt;DOMAIN&gt;\Policies\'

2. Search for the password in all files within the directory: 'findstr /si password *.*'

3. Review the results to identify any passwords that may have been stored in SYSVOL.

 



**Code**: [[\\&lt;DOMAIN&gt;\SYSVOL\&lt;DOMAIN&gt;\Policies\]]



> This command allows you to search for passwords that may have been inadvertently stored within SYSVOL, which is accessible to all authenticated users in the domain. The 'cd' command is used to navigate to the SYSVOL directory, and the 'findstr' command is used to search for the keyword 'password' in all files within the directory. The '/si' switch ensures that the search is case-insensitive, and the '*' wildcard is used to search all file types. The results of the search will be displayed in the command prompt, allowing you to identify any passwords that may have been stored within SYSVOL.

2. This command searches for the string 'cpassword' in all Group Policy Object files (.xml) located in the sysvol folder of the specified domain (FQDN).

 



**Code**: [[findstr /S /I cpassword \\\\FQDN\\sysvol\\FQDN\\po]]



> The 'findstr' command is used to search for a specific string in files. The '/S' switch makes the command search for the string in all subdirectories of the specified path. The '/I' switch makes the search case-insensitive. The '\\\\' is used to escape the backslashes in the path. The '<FQDN>' should be replaced with the fully qualified domain name of the domain you want to search in.

3. To use this command, replace 'password_in_base64' with the base64-encoded password that you want to decrypt. Then, replace the 32-byte AES key '4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b' and the initialization vector '0000000000000000' with the values provided by Microsoft in the MSDN - 2.2.1.1.4 Password Encryption.

 



**Code**: [[echo 'password_in_base64' | base64 -d | openssl en]]



> This command can be used to decrypt a password that is stored in a Group Policy Object (GPO) in SYSVOL. The password is encrypted using the AES-256-CBC algorithm, and the 32-byte key and initialization vector (IV) are provided by Microsoft in the MSDN - 2.2.1.1.4 Password Encryption. By using this command, you can decrypt the password and use it to gain access to the GPO.



**Command** ([[Decrypt password using openssl]]):

```bash
echo 'password_in_base64' | base64 -d | openssl enc -d -aes-256-cbc -K 4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b -iv 0000000000000000
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Password Filter DLL|T1174 - Password Filter DLL]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

## Commands Used

- [[Decrypt password using openssl]]

## Tags

- [[Active Directory Attacks]]
- [[Passwords in SYSVOL & Group Policy Preferences]]



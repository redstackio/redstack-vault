---
id: edfd5c34-1644-474b-bb90-5db50f3d02fb
name: Windows - SAM and SYSTEM Hash Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.814296+00:00'
updated_at: '2023-04-10T20:37:44.204630+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Password Filter DLL|T1174 - Password Filter DLL]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[SAM and SYSTEM files]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Convert SAM file to NT format using John]]'
- '[[Dump password hashes from SYSTEM and SAM files]]'
- '[[Dump SAM database]]'
- '[[Extract password hashes from SYSTEM and SAM files using samdump2]]'
---

# Windows - SAM and SYSTEM Hash Extraction

## Summary

The SAM and SYSTEM registry hive files contain sensitive information, such as user account passwords, that can be extracted and cracked to escalate privileges. This procedure involves dumping the SAM and SYSTEM registry hive files, extracting the password hashes, and then cracking them using a tool

## Description

# Description

The SAM and SYSTEM registry hive files contain sensitive information, such as user account passwords, that can be extracted and cracked to escalate privileges. This procedure involves dumping the SAM and SYSTEM registry hive files, extracting the password hashes, and then cracking them using a tool such as John the Ripper. 

This technique can be used by an attacker who has already gained access to a system with low privileges and is looking to escalate their privileges to gain access to more sensitive information or perform more damaging actions. From a technical perspective, this procedure involves using tools to dump and extract the password hashes from the SAM and SYSTEM registry hive files. From a business perspective, this procedure highlights the importance of securing sensitive information such as user account passwords to prevent unauthorized access and privilege escalation.

## Requirements

1. Access to the target system

1. Tools such as Pwdump and John the Ripper

## Defense

1. Regularly monitor and audit registry access and changes

1. Implement strong password policies and multi-factor authentication

1. Use endpoint detection and response (EDR) tools to detect and respond to suspicious activity

## Objectives

1. Escalate privileges to gain access to more sensitive information or perform more damaging actions

1. Extract and crack password hashes from the SAM and SYSTEM registry hive files

# Instructions

1. To access the SAM registry hive files, navigate to the following directories:
- %SYSTEMROOT%\repair\SAM
- %SYSTEMROOT%\System32\config\RegBack\SAM
- %SYSTEMROOT%\System32\config\SAM
- %SYSTEMROOT%\repair\system
- %SYSTEMROOT%\System32\config\SYSTEM
- %SYSTEMROOT%\System32\config\RegBack\system

You can use tools like Regedit or PowerShell to view or edit the contents of the SAM registry hive files. However, it is important to note that modifying the contents of the SAM registry hive files can result in system instability or even prevent the system from booting up.

**Code**: [[# Usually %SYSTEMROOT% = C:\Windows
%SYSTEMROOT%\r]]

> The SAM registry hive files contain sensitive information such as user account passwords and security policies. These files are critical components of the Windows operating system and should only be accessed or modified by experienced users with a specific need to do so. Any changes to the contents of the SAM registry hive files should be done with caution and proper backup procedures should be in place.

2. Pwdump is a command-line utility that retrieves the password hashes from the Security Account Manager (SAM) database of a Windows system. To use pwdump, open a command prompt and navigate to the directory where the tool is located. Then, type 'pwdump <options> <SAM file path>' and press Enter. The tool will generate a file containing the password hashes in a format that can be used by John the Ripper.

**Code**: [[pwdump]]

> The pwdump command is used to extract password hashes from the SAM database of a Windows system. These hashes can then be used to crack passwords using tools like John the Ripper. The command takes various options, such as '-u' to only dump the hashes for a specific user, and '-s' to dump the hashes for a remote system. The 'SAM file path' argument specifies the location of the SAM database on the system being analyzed.

3. samdump2 is a command-line utility that can be used to dump the password hashes from a Windows SAM database.

**Code**: [[samdump2]]

> The SAM database is a part of the Windows registry that contains information about user accounts on the local system. The samdump2 command can be used to extract password hashes from this database, which can be useful for password auditing and cracking. The command can be run with various options to extract different types of hashes, such as LM hashes, NTLM hashes, and cached domain credentials. The output can be saved to a file for further analysis or cracking with password cracking tools such as John the Ripper or Hashcat.

**Command** ([[Dump SAM database]]):

```bash
samdump2 /path/to/SAM/file > samdump.txt
```

4. To extract the SAM and SYSTEM hashes from a Windows machine, run the following commands:
1. pwdump SYSTEM SAM > /root/sam.txt
2. samdump2 SYSTEM SAM -o sam.txt

**Code**: [[pwdump SYSTEM SAM > /root/sam.txt
samdump2 SYSTEM ]]

> The 'pwdump' command extracts the password hashes from the SAM database on a Windows machine. The 'SYSTEM' and 'SAM' arguments specify the location of the SAM database. The output is redirected to a file named 'sam.txt' in the '/root' directory.
The 'samdump2' command is used to extract the same hashes, but in a different format. The 'SYSTEM' and 'SAM' arguments again specify the location of the SAM database. The '-o' argument specifies the output file name as 'sam.txt'.
Both commands are commonly used by security professionals to extract password hashes for further analysis or cracking.

**Command** ([[Dump password hashes from SYSTEM and SAM files]]):

```bash
pwdump SYSTEM SAM > /root/sam.txt
```

**Command** ([[Extract password hashes from SYSTEM and SAM files using samdump2]]):

```bash
samdump2 SYSTEM SAM -o sam.txt
```

5. Run the 'john' command with the '-format=NT' option followed by the path to the NT hash file (/root/sam.txt). This will attempt to crack the NT hash and reveal the plaintext password.

**Code**: [[john -format=NT /root/sam.txt]]

> The 'john' command is a password cracking tool that uses various techniques to crack passwords. The '-format=NT' option specifies the format of the hash file to be cracked. '/root/sam.txt' is the path to the NT hash file. The output of this command will be the plaintext password if it is successfully cracked.

**Command** ([[Convert SAM file to NT format using John]]):

```bash
john -format=NT /root/sam.txt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Password Filter DLL|T1174 - Password Filter DLL]]

## Commands Used

- [[Convert SAM file to NT format using John]]
- [[Dump password hashes from SYSTEM and SAM files]]
- [[Dump SAM database]]
- [[Extract password hashes from SYSTEM and SAM files using samdump2]]

## Tags

- [[EoP - Looting for passwords]]
- [[SAM and SYSTEM files]]
- [[Windows - Privilege Escalation]]

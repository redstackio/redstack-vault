---
id: e6dca8f4-f55f-4938-8e81-46e48015cddc
name: NTDS Hash Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.962770+00:00'
updated_at: '2023-04-10T20:25:54.914723+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dumping AD Domain Credentials]]'
- '[[Extract hashes from ntds.dit]]'
commands:
- '[[Dump domain controller hashes using secretsdump.py]]'
- '[[Dump NTDS.dit Password Hashes using secretsdump.py]]'
- '[[Dump NTLM hashes using secretsdump.py]]'
---

# NTDS Hash Extraction

## Summary

NTDS Hash Extraction is a technique used to extract password hashes from the Active Directory database file ntds.dit. This file contains the hashed passwords of all AD users and computers. By extracting these hashes, an attacker can attempt to crack them offline and gain access to user accounts. Th

## Description

# Description

NTDS Hash Extraction is a technique used to extract password hashes from the Active Directory database file ntds.dit. This file contains the hashed passwords of all AD users and computers. By extracting these hashes, an attacker can attempt to crack them offline and gain access to user accounts. This technique is commonly used in post-exploitation scenarios where the attacker has already gained administrative access to a domain controller.

Technical Explanation: This technique involves dumping the ntds.dit file from a domain controller and then using a tool like "NTDSXtract" to extract the password hashes. The extracted hashes can then be used with a password cracking tool like "John the Ripper" to attempt to crack the passwords.

Business Value: This technique can be used by attackers to gain access to sensitive information stored in Active Directory, such as intellectual property, financial data, and personal information of employees and customers.

## Requirements

1. Administrative access to a domain controller

1. Ability to dump ntds.dit file

1. NTDSXtract tool

1. Password cracking tool (e.g. John the Ripper)

## Defense

1. Limit access to domain controllers to only authorized personnel

1. Encrypt the ntds.dit file to prevent unauthorized access

1. Implement strong password policies to make cracking hashes more difficult

## Objectives

1. Extract password hashes from ntds.dit

1. Crack password hashes offline

1. Gain access to user accounts

# Instructions

1. hashcat -m <hash mode> <hash file> <wordlist>

**Code**: [[LOCAL]]

> This command is used to extract the hashes from a given hash file using a specified hash mode and a wordlist. The hash mode (-m) refers to the type of hash algorithm used in the file. The hash file is the file containing the hashes that need to be extracted. The wordlist is a text file containing a list of words that will be used to try and crack the hashes.

2. To dump NTDS secrets, run the following command:

**Code**: [[secretsdump.py -system /root/SYSTEM -ntds /root/nt]]

> This command uses the secretsdump.py tool to dump the NTDS secrets from the SYSTEM and ntds.dit files stored in the /root directory. The 'LOCAL' argument specifies that the command should be run locally on the machine. The output of this command will contain the password hashes of all users in the domain, which can be used for further attacks such as password cracking or pass-the-hash attacks.

**Command** ([[Dump NTDS.dit Password Hashes using secretsdump.py]]):

```bash
secretsdump.py -system /root/SYSTEM -ntds /root/ntds.dit LOCAL
```

3. To use this tool, replace <IP> with the IP address of the target machine and <NTLM hash> with the NTLM hash of a domain user with administrative privileges.

**Code**: [[./secretsdump.py -dc-ip <IP> AD\administrator@doma]]

> The first command will dump the password hashes of all users in the domain, along with their last password change time and account status. The second command will dump only the password hashes of the domain controller. The -use-vss option is used to create a snapshot of the target machine's volume shadow copies and dump the password hashes from there (if available), which can be useful for avoiding detection. The -pwd-last-set option is used to include the last password change time for each user. The -user-status option is used to include the status of each user account (e.g. enabled, disabled, locked out). The -just-dc option is used to dump only the password hashes of the domain controller, which can be faster and less noisy than dumping all domain user hashes. The PENTESTLAB/dc\$@<IP> argument specifies the target domain controller.

**Command** ([[Dump NTLM hashes using secretsdump.py]]):

```bash
./secretsdump.py -dc-ip <IP> AD\administrator@domain -use-vss -pwd-last-set -user-status
```

**Command** ([[Dump domain controller hashes using secretsdump.py]]):

```bash
./secretsdump.py -hashes <NTLM hash> -just-dc PENTESTLAB/dc\$@<IP>
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Dump domain controller hashes using secretsdump.py]]
- [[Dump NTDS.dit Password Hashes using secretsdump.py]]
- [[Dump NTLM hashes using secretsdump.py]]

## Tags

- [[Active Directory Attacks]]
- [[Dumping AD Domain Credentials]]
- [[Extract hashes from ntds.dit]]

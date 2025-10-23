---
id: 3a4b625e-a607-40f8-a616-6fe8924f1a65
name: NTDS Reversible Encryption Dumping
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.151456+00:00'
updated_at: '2023-04-10T20:26:12.774399+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques:
- '[[Security Account Manager|T1003.002 - Security Account Manager]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dumping AD Domain Credentials]]'
- '[[NTDS Reversible Encryption]]'
---

# NTDS Reversible Encryption Dumping

## Summary

NTDS Reversible Encryption is a feature in Active Directory that allows users to store their passwords in a reversible format. This feature is disabled by default, but attackers can enable it through various means, such as exploiting weak group policies or using a tool like Mimikatz. Once enabled, 

## Description

# Description

NTDS Reversible Encryption is a feature in Active Directory that allows users to store their passwords in a reversible format. This feature is disabled by default, but attackers can enable it through various means, such as exploiting weak group policies or using a tool like Mimikatz. Once enabled, an attacker can dump the NTDS.dit file, which contains the hashed passwords of all domain users, and then use a cracking tool to obtain the plaintext passwords.

This procedure can be used by attackers to gain access to sensitive information or systems within an organization. It requires a good understanding of Active Directory and the ability to execute commands on a domain controller.

 

## Requirements

1. Access to a domain controller

1. Privileged credentials or the ability to execute commands with administrative privileges

1. Knowledge of Active Directory and the NTDS.dit file structure

1. A tool for dumping the NTDS.dit file, such as PowerSploit or NTDSUtil

1. A cracking tool, such as Hashcat or John the Ripper

 

## Defense

1. Disable NTDS Reversible Encryption in group policies or at the domain level

1. Monitor for changes to group policies related to NTDS Reversible Encryption

1. Implement multi-factor authentication to reduce the risk of privileged credential theft

 

## Objectives

1. Dump the NTDS.dit file to obtain hashed passwords of all domain users

1. Use a cracking tool to obtain plaintext passwords

1. Gain access to sensitive information or systems within the organization

 

# Instructions

1. This command retrieves all Active Directory users who have the "Store passwords using reversible encryption" option enabled.

 



**Code**: [[Get-ADUser -Filter 'userAccountControl -band 128' ]]



> The "-Filter" parameter specifies the filter to apply when retrieving the users. In this case, the filter is set to "userAccountControl -band 128", which retrieves all users whose userAccountControl attribute has the 128 bit set. This bit corresponds to the "Store passwords using reversible encryption" option. The "-Properties" parameter specifies the user attributes to retrieve. In this case, we retrieve the userAccountControl attribute to check if the reversible encryption option is enabled. The output of the command will be a list of all users with reversible encryption enabled.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

### Sub-Techniques

- [[Security Account Manager|T1003.002 - Security Account Manager]]

## Tags

- [[Active Directory Attacks]]
- [[Dumping AD Domain Credentials]]
- [[NTDS Reversible Encryption]]



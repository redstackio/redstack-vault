---
id: 06f21c46-686a-4db0-a4b8-deec197b1290
name: Dumping AD Domain Credentials using Mimikatz sekurlsa
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.072472+00:00'
updated_at: '2023-04-10T20:25:44.028685+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dumping AD Domain Credentials]]'
- '[[Using Mimikatz sekurlsa]]'
commands:
- '[[Dumping krbtgt credentials using sekurlsa]]'
- '[[Dumping LSA secrets using lsadump]]'
---

# Dumping AD Domain Credentials using Mimikatz sekurlsa

## Summary

Dumping AD domain credentials using Mimikatz sekurlsa is a common technique used by attackers to obtain password hashes and LSA secrets from a Windows system. This technique is used to escalate privileges, move laterally across the network, and ultimately gain access to sensitive data.

Mimikatz is

## Description

# Description

Dumping AD domain credentials using Mimikatz sekurlsa is a common technique used by attackers to obtain password hashes and LSA secrets from a Windows system. This technique is used to escalate privileges, move laterally across the network, and ultimately gain access to sensitive data.

Mimikatz is a powerful post-exploitation tool that allows attackers to extract plaintext passwords, hashes, and other credentials from memory. The sekurlsa module in Mimikatz is specifically designed to dump credentials from the Windows LSA subsystem. This technique is widely used by attackers and is considered a high-risk threat to organizations.

Dumping AD domain credentials using Mimikatz sekurlsa can be devastating for organizations as it can lead to complete compromise of the network, data exfiltration, and loss of reputation.

 

## Requirements

1. Local administrator access on the Windows system

1. Mimikatz tool installed on the system

 

## Defense

1. Implementing the principle of least privilege can limit the impact of this attack

1. Regularly monitoring and analyzing system logs can help detect this attack

1. Enforcing strong password policies and multi-factor authentication can help prevent password theft and reduce the risk of this attack

 

## Objectives

1. Obtain password hashes and LSA secrets from a Windows system

1. Escalate privileges and move laterally across the network

1. Gain access to sensitive data

 

# Instructions

1. To retrieve the password hashes for krbtgt and dump LSA secrets, run the following commands:

 



**Code**: [[sekurlsa::krbtgt
lsadump::lsa /inject /name:krbtgt]]



> The 'sekurlsa::krbtgt' command is used to retrieve the password hashes for krbtgt, which is a privileged account used by Kerberos to encrypt and decrypt authentication tickets. The 'lsadump::lsa /inject /name:krbtgt' command is used to dump LSA secrets, which are used to store sensitive information such as passwords and keys. These commands can be useful for performing pass-the-hash attacks or for gaining access to other systems that use the same password as krbtgt.



**Command** ([[Dumping krbtgt credentials using sekurlsa]]):

```bash
sekurlsa::krbtgt
```





**Command** ([[Dumping LSA secrets using lsadump]]):

```bash
lsadump::lsa /inject /name:krbtgt
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Dumping krbtgt credentials using sekurlsa]]
- [[Dumping LSA secrets using lsadump]]

## Tags

- [[Active Directory Attacks]]
- [[Dumping AD Domain Credentials]]
- [[Using Mimikatz sekurlsa]]



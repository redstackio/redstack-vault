---
id: 2f9d6500-e41a-427b-b0ae-1282a6d6563e
name: Forest Trust Ticket Dumping
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.296686+00:00'
updated_at: '2023-04-10T20:26:22.966685+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Dumping trust passwords (trust keys)]]'
- '[[Forest to Forest Compromise - Trust Ticket]]'
commands:
- '[[Find TRUST_NAME$ machine account hash]]'
---

# Forest Trust Ticket Dumping

## Summary

Forest Trust Ticket Dumping is a technique used in Active Directory attacks to gain access to resources in a trusted forest. This technique involves extracting trust account hashes from a compromised domain controller using tools such as Mimikatz. Once the hashes have been extracted, an attacker ca

## Description

# Description

Forest Trust Ticket Dumping is a technique used in Active Directory attacks to gain access to resources in a trusted forest. This technique involves extracting trust account hashes from a compromised domain controller using tools such as Mimikatz. Once the hashes have been extracted, an attacker can use them to generate a trust ticket, which can be used to establish a trust relationship with the target forest.

From a technical perspective, this technique involves accessing the LSASS process on a compromised domain controller and using Mimikatz to extract the trust account hashes. Once the hashes have been extracted, an attacker can use them to generate a trust ticket and establish a trust relationship with the target forest. This technique is particularly effective in multi-forest environments where trust relationships are commonly used.

From a business perspective, this technique can be used to gain access to sensitive resources in a trusted forest, such as financial data or intellectual property. It is important for organizations to be aware of this technique and take steps to mitigate the risk of forest trust ticket dumping.

 

## Requirements

1. Access to a compromised domain controller

1. Tools such as Mimikatz to extract trust account hashes

 

## Defense

1. Implement strong password policies and regularly rotate passwords for trust accounts

1. Monitor for suspicious activity, such as abnormal access to trust accounts or changes to trust relationships

1. Implement network segmentation to limit the impact of a forest trust ticket dumping attack

 

## Objectives

1. Gain access to resources in a trusted forest

1. Establish a trust relationship with a target forest

 

# Instructions

1. To extract trust account hashes, run the following command:

lsadump::trust /patch

This will display a list of all the trust accounts and their corresponding hashes.

 



**Code**: [[lsadump::trust /patch

or find the TRUST_NAME$ mac]]



> The lsadump::trust command is used to extract trust account hashes from a Windows system. Trust accounts are used to establish a trust relationship between two domains or between a domain and a non-Windows Kerberos realm. These accounts are created automatically when a trust relationship is established and are used to authenticate users between the two domains. By extracting the trust account hashes, an attacker can use them to perform pass-the-hash attacks and gain access to other systems in the network.

The /patch option is used to extract the trust account hashes from the system's registry. Alternatively, an attacker can also find the TRUST_NAME$ machine account hash by running the following command:

reg query HKLM\SAM\SAM\Domains\Account\Aliases /s | findstr /i trust

This command will search for the TRUST_NAME$ machine account hash in the system's registry.



**Command** ([[Find TRUST_NAME$ machine account hash]]):

```bash
lsadump::trust /patch
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[Find TRUST_NAME$ machine account hash]]

## Tags

- [[Active Directory Attacks]]
- [[Dumping trust passwords (trust keys)]]
- [[Forest to Forest Compromise - Trust Ticket]]



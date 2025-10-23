---
id: 3e174a7f-c32d-4fda-9589-e6ae6c8a5b76
name: Establishing and Enumerating PAM Trust between lab.local and bastion.local
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.399531+00:00'
updated_at: '2023-04-10T20:26:01.490587+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Privileged Access Management (PAM) Trust]]'
commands:
- '[[Create trust between bastion.local and lab.local]]'
- '[[Create trust between lab.local and bastion.local]]'
---

# Establishing and Enumerating PAM Trust between lab.local and bastion.local

## Summary

Establishing and enumerating Privileged Access Management (PAM) trust between lab.local and bastion.local is an attack technique that allows an attacker to gain access to sensitive information and systems. This technique involves establishing a trust relationship between two Active Directory domain

## Description

# Description

Establishing and enumerating Privileged Access Management (PAM) trust between lab.local and bastion.local is an attack technique that allows an attacker to gain access to sensitive information and systems. This technique involves establishing a trust relationship between two Active Directory domains, in this case lab.local and bastion.local. Once the trust is established, the attacker can enumerate and access privileged accounts and resources in both domains. This attack can be used to move laterally within a network and gain access to high-value targets.

From a technical perspective, this attack involves sending specially crafted requests to the domain controllers of both domains to establish a trust relationship. Once the trust is established, the attacker can use tools like Mimikatz to enumerate and access privileged accounts and resources in both domains. This attack can be difficult to detect, as it does not involve the use of malware or other malicious tools.

The business value of this attack is significant, as it can allow an attacker to gain access to sensitive information and systems. This can result in data theft, financial loss, and damage to the organization's reputation.

 

## Requirements

1. Access to the network

1. Credentials with sufficient privileges to establish trust

1. Tools like Mimikatz for enumeration and access

 

## Defense

1. Limit the use of privileged accounts

1. Monitor for suspicious activity on domain controllers

1. Implement network segmentation to limit lateral movement

 

## Objectives

1. Establish a trust relationship between lab.local and bastion.local

1. Enumerate and access privileged accounts and resources in both domains

 

# Instructions

1. Execute the commands on the forest and bastion servers respectively to establish PAM trust between lab.local and bastion.local

 



**Code**: [[# execute on our forest
netdom trust lab.local /do]]



> The above commands use the netdom tool to establish PAM trust between two domains, lab.local and bastion.local. The /ForestTransitive parameter ensures that the trust is transitive across the entire forest. The /EnableSIDHistory parameter allows users to access resources in both domains with their existing permissions. The /EnablePIMTrust parameter enables privileged identity management trust, which allows administrators to manage privileged access across the domains. The /Quarantine parameter is set to No, which means that the trust relationship will not be quarantined if any issues arise. These commands need to be executed on the forest and bastion servers respectively.



**Command** ([[Create trust between lab.local and bastion.local]]):

```bash
netdom trust lab.local /domain:bastion.local /ForestTransitive:Yes 
netdom trust lab.local /domain:bastion.local /EnableSIDHistory:Yes 
netdom trust lab.local /domain:bastion.local /EnablePIMTrust:Yes 
netdom trust lab.local /domain:bastion.local /Quarantine:No
```





**Command** ([[Create trust between bastion.local and lab.local]]):

```bash
netdom trust bastion.local /domain:lab.local /ForestTransitive:Yes
```



2. This command is used to detect if the current forest is a PAM trust. It also enumerates shadow security principals and checks if the current forest is managed by a bastion forest.

 



**Code**: [[# Detect if current forest is PAM trust
Import ADM]]



> The first command uses the Get-ADTrust cmdlet to filter and retrieve all trusts that are forest transitive and have SID filtering quarantined set to false. The second command uses the Get-ADObject cmdlet to retrieve all shadow security principals and their associated members and msDS-ShadowPrincipalSid attribute values. The third command uses the Get-ADTrust cmdlet to filter and retrieve all trusts that are forest transitive. The Trust_Attribute_PIM_Trust and Trust_Attribute_Treat_As_External attributes are used to determine if the current forest is managed by a bastion forest.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[Create trust between bastion.local and lab.local]]
- [[Create trust between lab.local and bastion.local]]

## Tags

- [[Active Directory Attacks]]
- [[Privileged Access Management (PAM) Trust]]



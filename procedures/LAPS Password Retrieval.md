---
id: 567a9adf-4611-4e29-a402-62117cc8edb2
name: LAPS Password Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.530170+00:00'
updated_at: '2023-04-10T20:25:56.012388+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Grant LAPS Access]]'
- '[[Reading LAPS Password]]'
commands:
- '[[Add user1 to LAPS ADM group and LAPS READ group]]'
---

# LAPS Password Retrieval

## Summary

LAPS (Local Administrator Password Solution) is a Microsoft tool used to manage local administrator passwords on domain-joined computers. This procedure is used to retrieve the LAPS password for a specific computer. An attacker can use this password to gain access to the local administrator account

## Description

# Description

LAPS (Local Administrator Password Solution) is a Microsoft tool used to manage local administrator passwords on domain-joined computers. This procedure is used to retrieve the LAPS password for a specific computer. An attacker can use this password to gain access to the local administrator account on the compromised computer. This can be useful for lateral movement and privilege escalation.

To retrieve the LAPS password, the attacker needs to add their user account to the LAPS group for the targeted computer. Once added, the attacker can use the LAPS UI or PowerShell commands to retrieve the password. This procedure assumes that the attacker has already gained access to the domain and has the necessary privileges to add their user account to the LAPS group.

The business value of this procedure is that it allows an attacker to gain administrative access to a compromised computer, which can lead to further compromise of the network. It highlights the importance of proper access control and privilege management within an organization.

## Requirements

1. Domain access and privileges to add user account to LAPS group

1. Access to LAPS UI or PowerShell commands

## Defense

1. Limit access to the LAPS group to only necessary accounts

1. Monitor for changes to LAPS group membership

1. Implement multi-factor authentication to prevent unauthorized access to the domain

## Objectives

1. Retrieve the LAPS password for a specific computer

1. Gain access to the local administrator account on the compromised computer

# Instructions

1. To add a user to the LAPS ADM and LAPS READ groups, run the following commands:

**Code**: [[Add-DomainGroupMember -Identity 'LAPS ADM' -Member]]

> This command adds a user to two non-admin groups named LAPS ADM and LAPS READ. These groups are used for managing Local Administrator Password Solution (LAPS) in a Windows domain. The command requires the user's credentials and the domain name to be provided. Once a user is added to these groups, they can read the LAPS admin password for the computers in the domain.

**Command** ([[Add user1 to LAPS ADM group and LAPS READ group]]):

```bash
Add-DomainGroupMember -Identity 'LAPS ADM' -Members 'user1' -Credential $cred -Domain "domain.local"
Add-DomainGroupMember -Identity 'LAPS READ' -Members 'user1' -Credential $cred -Domain "domain.local"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Add user1 to LAPS ADM group and LAPS READ group]]

## Tags

- [[Active Directory Attacks]]
- [[Grant LAPS Access]]
- [[Reading LAPS Password]]

---
id: 47e95144-9812-403c-9c1d-5d1f8a073d9f
name: Azure AD Connect - Password Extraction via AD Sync Account DCSync
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:16.153460+00:00'
updated_at: '2023-04-10T20:19:33.225115+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques:
- '[[Security Account Manager|T1003.002 - Security Account Manager]]'
tags:
- '[[Azure AD Connect]]'
- '[[Azure AD Connect - Password extraction]]'
- '[[Cloud - Azure]]'
commands:
- '[[Clone adconnectdump repository]]'
---

# Azure AD Connect - Password Extraction via AD Sync Account DCSync

## Summary

Azure AD Connect is a tool used to synchronize on-premises Active Directory objects with Azure Active Directory. An attacker with access to the AD Sync account can use DCSync to extract password hashes from the on-premises Active Directory. This can be used to perform offline brute force attacks ag

## Description

# Description

Azure AD Connect is a tool used to synchronize on-premises Active Directory objects with Azure Active Directory. An attacker with access to the AD Sync account can use DCSync to extract password hashes from the on-premises Active Directory. This can be used to perform offline brute force attacks against the password hashes, which can result in the compromise of user accounts. This technique can be used to escalate privileges and move laterally within the network. 

Technical Explanation: AD Sync Account DCSync is a method of replicating password hashes from a domain controller to a non-domain controller. This technique can be used to extract password hashes from the on-premises Active Directory. Once the password hashes are extracted, they can be used to perform offline brute force attacks against the password hashes.

Business Value: An attacker can use this technique to gain access to sensitive data and elevate privileges within the network.

## Requirements

1. Access to the AD Sync account

1. Access to the on-premises Active Directory

## Defense

1. Limit access to the AD Sync account to only those who require it

1. Implement strong password policies to make brute force attacks more difficult

1. Monitor for unusual activity, such as large numbers of failed login attempts

## Objectives

1. Extract password hashes from the on-premises Active Directory

1. Perform offline brute force attacks against the password hashes

1. Compromise user accounts

1. Escalate privileges and move laterally within the network

# Instructions

1. To perform a DCSync attack using the AD Sync account, first clone the adconnectdump repository using the provided git command. Then, navigate to the adconnectdump directory and run the following command: ./adconnectdump.py -u <username> -d <domain> -p <password> --ntds <path_to_ntds.dit_file> --ldap-ip <domain_controller_ip_address> --ldap-port <ldap_port_number>. Replace the placeholders with the appropriate values for your environment. This will extract the NTLM hashes from the ntds.dit file using the AD Sync account credentials stored in the ADSync.mdf file.

**Code**: [[git clone https://github.com/fox-it/adconnectdump
]]

> This command is used to perform a DCSync attack using the AD Sync account. The adconnectdump tool is used to extract the NTLM hashes from the ntds.dit file on a domain controller. The AD Sync account credentials are stored in the ADSync.mdf file, which is located in the C:\Program Files\Microsoft Azure AD Sync\Data directory. The -u, -d, and -p flags are used to specify the username, domain, and password for the AD Sync account. The --ntds flag is used to specify the path to the ntds.dit file on the domain controller. The --ldap-ip and --ldap-port flags are used to specify the IP address and port number of the domain controller's LDAP service.

**Command** ([[Clone adconnectdump repository]]):

```bash
git clone https://github.com/fox-it/adconnectdump
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

### Sub-Techniques

- [[Security Account Manager|T1003.002 - Security Account Manager]]

## Commands Used

- [[Clone adconnectdump repository]]

## Tags

- [[Azure AD Connect]]
- [[Azure AD Connect - Password extraction]]
- [[Cloud - Azure]]

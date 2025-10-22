---
id: 0928b1c7-8972-4021-9755-8547049a79ad
name: Password Spraying with Pre-Generated Passwords
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.304382+00:00'
updated_at: '2023-04-10T20:25:55.299475+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Password spraying]]'
- '[[Spray a pre-generated passwords list]]'
commands:
- '[[Brute Force SMB Login]]'
- '[[Invoke Domain Password Spray]]'
- '[[Invoke Domain Password Spray with User and Password Lists]]'
---

# Password Spraying with Pre-Generated Passwords

## Summary

Password spraying is an attack technique that involves attempting a single password against multiple accounts before moving on to the next password. In this procedure, a pre-generated list of passwords is used to attempt to gain access to a target Active Directory environment. This attack can be ca

## Description

# Description

Password spraying is an attack technique that involves attempting a single password against multiple accounts before moving on to the next password. In this procedure, a pre-generated list of passwords is used to attempt to gain access to a target Active Directory environment. This attack can be carried out manually or automated using tools such as SMB Password Spraying, Domain Password Spray Attack, or SMB Auto Brute Force. A successful password spray attack can result in the compromise of multiple user accounts, which can then be used to gain further access to the network.

## Requirements

1. Valid user account credentials

1. Access to a target Active Directory environment

1. Pre-generated list of passwords

1. Password spraying tool

## Defense

1. Enforce strong password policies and multi-factor authentication to prevent successful password spraying attacks

1. Monitor for failed login attempts and anomalous activity

1. Use network segmentation and access controls to limit the impact of a successful password spray attack

## Objectives

1. Gain access to a target Active Directory environment

1. Compromise multiple user accounts

# Instructions

1. To use this command, run `crackmapexec` followed by the target IP range and the username to spray against. Use the `-p` flag followed by the path to the `mp64.bin` binary and the desired password mask to generate passwords to spray. This command is useful for testing the strength of SMB passwords on a network.

**Code**: [[crackmapexec smb 10.0.0.1/24 -u Administrator -p `]]

> The `crackmapexec` command is used to enumerate and attack network services. The `-u` flag specifies the username to spray against. The `-p` flag specifies the password mask to use when generating passwords to spray. The `mp64.bin` binary is a tool used to generate password masks. The password mask used in this example is `Pass@wor?l?a`, which will generate passwords with the format `Pass@wor1a`, `Pass@wor2a`, etc. This command should only be used on networks that you have permission to test.

2. To perform a Domain Password Spray Attack, use the `Invoke-DomainPasswordSpray` command with the following arguments:
- `UserList`: A list of usernames to spray the password against.
- `Domain`: The domain name to spray the password against.
- `PasswordList`: A list of passwords to spray against the users.
- `OutFile`: The file where the results will be saved.

Example:
```
Invoke-DomainPasswordSpray -UserList users.txt -Domain domain-name -PasswordList passlist.txt -OutFile sprayed-creds.txt
```

**Code**: [[# https://github.com/dafthack/DomainPasswordSpray
]]

> This command is used to perform a Domain Password Spray attack, which is an attack method where an attacker attempts to guess a password by spraying a single password against multiple user accounts. This technique is used to bypass account lockout policies and avoid detection. It is important to note that this attack should only be performed with proper authorization and in a controlled environment to avoid causing harm to the targeted system.

**Command** ([[Invoke Domain Password Spray]]):

```bash
Invoke-DomainPasswordSpray -Password Summer2021!
```

**Command** ([[Invoke Domain Password Spray with User and Password Lists]]):

```bash
Invoke-DomainPasswordSpray -UserList users.txt -Domain domain-name -PasswordList passlist.txt -OutFile sprayed-creds.txt
```

3. This command is used to automate the process of brute force attacks on SMB protocol. It takes a list of usernames and passwords as input and tries to authenticate with the target system. If the authentication is successful, it returns the valid credentials.

**Code**: [[Invoke-SMBAutoBrute -UserList "C:\ProgramData\admi]]

> -UserList: This parameter specifies the path of the file containing the list of usernames to be used for brute force attack.
-PasswordList: This parameter specifies the path of the file containing the list of passwords to be used for brute force attack.
-LockoutThreshold: This parameter specifies the maximum number of failed attempts before the account gets locked out.
-ShowVerbose: This parameter specifies whether to show verbose output or not. If specified, it will show detailed output of the brute force attack.

**Command** ([[Brute Force SMB Login]]):

```bash
 -UserList "C:\ProgramData\admins.txt" -PasswordList "Password1, Welcome1, 1qazXDR%+" -LockoutThreshold 5 -ShowVerbose
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[Brute Force SMB Login]]
- [[Invoke Domain Password Spray]]
- [[Invoke Domain Password Spray with User and Password Lists]]

## Tags

- [[Active Directory Attacks]]
- [[Password spraying]]
- [[Spray a pre-generated passwords list]]

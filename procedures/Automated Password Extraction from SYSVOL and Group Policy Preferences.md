---
id: df411125-df65-4113-8d37-1c4545ae30dd
name: Automated Password Extraction from SYSVOL and Group Policy Preferences
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:03.542823+00:00'
updated_at: '2023-04-10T20:26:15.107671+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Credential Dumping|T1003 - Credential Dumping]]'
- '[[Credentials from Password Stores|T1555 - Credentials from Password Stores]]'
- '[[Network Share Discovery|T1135 - Network Share Discovery]]'
sub_techniques:
- '[[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]'
- '[[Security Account Manager|T1003.002 - Security Account Manager]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Automate the SYSVOL and passwords research]]'
- '[[Passwords in SYSVOL & Group Policy Preferences]]'
commands:
- '[[Enumerate Group Policy Preferences (GPP) Passwords]]'
- '[[Enumerate Shares on Windows]]'
- '[[Enumerate SMB Shares]]'
- '[[Extract GPP Password]]'
- '[[Extract GPP Password]]'
- '[[Extract GPP Password]]'
- '[[Extracting GPP Autologin Password]]'
- '[[Extracting GPP Password]]'
---

# Automated Password Extraction from SYSVOL and Group Policy Preferences

## Summary

Automated Password Extraction from SYSVOL and Group Policy Preferences is a technique used by attackers to obtain plaintext passwords stored in the SYSVOL folder and Group Policy Preferences (GPP) of a Windows Active Directory domain. This technique automates the process of finding and extracting p

## Description

# Description

Automated Password Extraction from SYSVOL and Group Policy Preferences is a technique used by attackers to obtain plaintext passwords stored in the SYSVOL folder and Group Policy Preferences (GPP) of a Windows Active Directory domain. This technique automates the process of finding and extracting passwords from these locations, making it easier for attackers to gain access to sensitive information. The automated process involves using tools like CrackMapExec and Get Group Policy Preferences Password to extract passwords from the target environment. The extracted passwords can be used for lateral movement, privilege escalation, and persistence.

## Requirements

1. Valid credentials with sufficient privileges to access SYSVOL and Group Policy Preferences

1. Access to the target network

## Defense

1. Limit access to SYSVOL and Group Policy Preferences to authorized personnel only

1. Implement strong password policies and regularly rotate passwords for service accounts and privileged users

1. Monitor for suspicious activity and use of tools like CrackMapExec and Get Group Policy Preferences Password

## Objectives

1. Extract plaintext passwords from SYSVOL and Group Policy Preferences

1. Use the extracted passwords for lateral movement, privilege escalation, and persistence

# Instructions

1. To enumerate shares and credentials, use any of the following commands:
1. scanner/smb/smb_enumshares
2. post/windows/gather/enum_shares
3. post/windows/gather/credentials/gpp

To execute the command, use the `run` command followed by the name of the command.

**Code**: [[scanner/smb/smb_enumshares
post/windows/gather/enu]]

> These commands are used to enumerate shares and credentials on a target system. The `scanner/smb/smb_enumshares` command is used to enumerate shares on a target system using the Server Message Block (SMB) protocol. The `post/windows/gather/enum_shares` command is used to enumerate shares on a Windows system. The `post/windows/gather/credentials/gpp` command is used to enumerate Group Policy Preferences (GPP) credentials on a Windows system. These commands can be useful for reconnaissance and privilege escalation on a target system.

**Command** ([[Enumerate SMB Shares]]):

```bash
scanner/smb/smb_enumshares
```

**Command** ([[Enumerate Shares on Windows]]):

```bash
post/windows/gather/enum_shares
```

**Command** ([[Enumerate Group Policy Preferences (GPP) Passwords]]):

```bash
post/windows/gather/credentials/gpp
```

2. Use the CrackMapExec (CME) tool to perform SMB authentication against a target host with the specified IP address. Use the -u flag to specify the username and -H flag to specify the NTLM hash of the user's password. Use the -M flag to specify the module to execute. In this case, use the gpp_autologin module to extract the password from Group Policy Preferences (GPP) Autologin XML files, or use the gpp_password module to extract the password from GPP Password XML files.

**Code**: [[cme smb 10.10.10.10 -u Administrator -H 89[...]9d ]]

> CrackMapExec is a powerful penetration testing tool that can be used to perform a variety of tasks related to SMB authentication and exploitation. The tool supports multiple modules that can be used to extract information from target systems, including Group Policy Preferences (GPP) Autologin and Password XML files. These files often contain sensitive information, such as plaintext passwords, that can be used to escalate privileges and gain access to additional systems on the network.

**Command** ([[Extracting GPP Autologin Password]]):

```bash
cme smb 10.10.10.10 -u Administrator -H 89[...]9d -M gpp_autologin
```

**Command** ([[Extracting GPP Password]]):

```bash
cme smb 10.10.10.10 -u Administrator -H 89[...]9d -M gpp_password
```

3. This command is used to retrieve the Group Policy Preferences (GPP) password. The command can be executed in three different ways, using a NULL session, cleartext credentials, or pass-the-hash. The instructions for each method are as follows:

**Code**: [[# with a NULL session
Get-GPPPassword.py -no-pass ]]

> 1. NULL session: In this method, the command is executed without providing any credentials. The command will try to connect to the domain controller specified in the command and retrieve the GPP password.
2. Cleartext credentials: In this method, the command is executed by providing the domain, username, password, and domain controller information. The command will use these credentials to connect to the domain controller and retrieve the GPP password.
3. Pass-the-hash: In this method, the command is executed by providing the domain, username, password hashes, and domain controller information. The command will use the password hashes to connect to the domain controller and retrieve the GPP password.

**Command** ([[Extract GPP Password]]):

```bash
Get-GPPPassword.py -no-pass 'DOMAIN_CONTROLLER'
```

**Command** ([[Extract GPP Password]]):

```bash
Get-GPPPassword.py 'DOMAIN'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'
```

**Command** ([[Extract GPP Password]]):

```bash
Get-GPPPassword.py -hashes 'LMhash':'NThash' 'DOMAIN'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Credential Dumping|T1003 - Credential Dumping]]
- [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]
- [[Network Share Discovery|T1135 - Network Share Discovery]]

### Sub-Techniques

- [[Credentials from Web Browsers|T1555.003 - Credentials from Web Browsers]]
- [[Security Account Manager|T1003.002 - Security Account Manager]]

## Commands Used

- [[Enumerate Group Policy Preferences (GPP) Passwords]]
- [[Enumerate Shares on Windows]]
- [[Enumerate SMB Shares]]
- [[Extract GPP Password]]
- [[Extract GPP Password]]
- [[Extract GPP Password]]
- [[Extracting GPP Autologin Password]]
- [[Extracting GPP Password]]

## Tags

- [[Active Directory Attacks]]
- [[Automate the SYSVOL and passwords research]]
- [[Passwords in SYSVOL & Group Policy Preferences]]

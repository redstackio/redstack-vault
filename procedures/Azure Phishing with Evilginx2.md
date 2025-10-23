---
id: 56a08750-4e44-4cb1-a933-6cf32ecfa858
name: Azure Phishing with Evilginx2
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:56:15.096096+00:00'
updated_at: '2023-05-24T03:35:02.230319+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Phishing|T1566 - Phishing]]'
platforms:
- Cloud
tags:
- '[[Cloud - Azure]]'
- '[[o365]]'
- '[[Office 365]]'
- '[[Phishing]]'
- '[[Phishing with Evilginx2]]'
commands:
- '[[Configure evilginx2]]'
---

# Azure Phishing with Evilginx2

**Status**: ✓ Verified

## Summary

Azure Phishing with Evilginx2 is a social engineering technique used to trick users into giving up their Azure credentials. The attack involves setting up a phishing website that looks like the Azure login page using Evilginx2. Once the victim enters their credentials, the attacker can use them to 

## Description

# Description

Azure Phishing with Evilginx2 is a social engineering technique used to trick users into giving up their Azure credentials. The attack involves setting up a phishing website that looks like the Azure login page using Evilginx2. Once the victim enters their credentials, the attacker can use them to access the victim's Azure account. This attack can be used to gain initial access to an organization's Azure environment or to steal sensitive information stored in the victim's account.

Evilginx2 is a man-in-the-middle attack framework used to intercept and steal credentials. It is designed to bypass two-factor authentication and other security measures by using a fake login page that looks identical to the real one. Evilginx2 can be used to target a wide range of online services, including Azure.

The business value of this attack lies in its ability to gain access to sensitive information stored in Azure. Attackers can use this information to conduct further attacks, steal intellectual property, or sell the information on the black market.

 

## Requirements

1. Access to Evilginx2 framework

1. Victim must fall for the phishing website and enter their Azure credentials

 

## Defense

1. Educate users on how to identify and avoid phishing attacks

1. Implement multi-factor authentication to prevent attackers from using stolen credentials

1. Monitor Azure logs for suspicious activity

 

## Objectives

1. To gain access to an organization's Azure environment

1. To steal sensitive information stored in a victim's Azure account

 

# Instructions

1. To set up a phishing attack with Evilginx2, follow these steps:

 



**Code**: [[PS C:\Tools> evilginx2 -p C:\Tools\evilginx2\phish]]



> 1. Run the command `evilginx2 -p C:\Tools\evilginx2\phishlets` in PowerShell.
2. Configure the domain and IP address using the `config domain` and `config ip` commands respectively.
3. Set up the phishing hostname using the `phishlets hostname` command with the desired hostname.
4. Use the `phishlets get-hosts` command to get the hosts for the phishing attack.
5. Create a DNS entry for `login.login.username.corp` and `www.login.username.corp`, type A, pointing to your machine.
6. Copy the certificate using the `Copy-Item` command and enable the phishing using the `phishlets enable` command.
7. Use the `lures create` and `lures get-url` commands to get the phishing URL.



**Command** ([[Configure evilginx2]]):

```bash
evilginx2 -p C:\Tools\evilginx2\phishlets
```





## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Phishing|T1566 - Phishing]]

## Commands Used

- [[Configure evilginx2]]

## Tags

- [[Cloud - Azure]]
- [[o365]]
- [[Office 365]]
- [[Phishing]]
- [[Phishing with Evilginx2]]



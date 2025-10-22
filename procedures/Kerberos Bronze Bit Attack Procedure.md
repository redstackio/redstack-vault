---
id: 5d7b2e79-66dd-4843-9900-40c3c541ceda
name: Kerberos Bronze Bit Attack Procedure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:07.926451+00:00'
updated_at: '2023-04-10T20:35:58.868283+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos Tickets]]'
sub_techniques:
- '[[AS-REP Roasting|T1558.004 - AS-REP Roasting]]'
- '[[Kerberoasting|T1558.003 - Kerberoasting]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos Bronze Bit Attack - CVE-2020-17049]]'
commands:
- '[[Kerberos Session Error]]'
---

# Kerberos Bronze Bit Attack Procedure

## Summary

The Kerberos Bronze Bit Attack is a technique used to bypass Kerberos authentication and gain unauthorized access to an Active Directory environment. This attack exploits a vulnerability (CVE-2020-17049) in the Microsoft implementation of Kerberos. By setting the Bronze Bit to 1 in a Kerberos ticke

## Description

# Description

The Kerberos Bronze Bit Attack is a technique used to bypass Kerberos authentication and gain unauthorized access to an Active Directory environment. This attack exploits a vulnerability (CVE-2020-17049) in the Microsoft implementation of Kerberos. By setting the Bronze Bit to 1 in a Kerberos ticket, an attacker can force the domain controller to downgrade encryption to a weaker standard, allowing them to decrypt the ticket and gain access to the targeted system. From there, the attacker can move laterally through the network and exfiltrate sensitive data.

From a technical perspective, the Kerberos Bronze Bit Attack works by manipulating the Kerberos ticket-granting ticket (TGT) to downgrade the encryption standard used to protect the ticket. This allows the attacker to decrypt the TGT and gain access to the targeted system. This attack requires the attacker to have valid domain credentials, which can be obtained through other techniques such as phishing or password spraying.

Business value of this attack is that it can be used to gain access to sensitive data, intellectual property, and other confidential information. This can result in financial loss, reputational damage, and legal consequences for the targeted organization.

## Requirements

1. Valid domain credentials

1. Access to a vulnerable Microsoft implementation of Kerberos

## Defense

1. Implementing the latest security patches and updates can mitigate the vulnerability exploited by this attack

1. Implementing strong password policies, multi-factor authentication, and regular user awareness training can reduce the risk of attackers obtaining valid domain credentials

1. Monitoring network traffic and user activity can help detect and prevent this type of attack

## Objectives

1. Gain unauthorized access to an Active Directory environment

1. Move laterally through the network

1. Exfiltrate sensitive data

# Instructions

1. To resolve this issue, you need to reset the computer account password for the domain controller. To do this, follow these steps: 
1. Open Active Directory Users and Computers.
2. On the View menu, make sure that the Advanced Features option is selected.
3. Locate the domain controller computer account that you want to reset.
4. Right-click the domain controller computer account, and then click Reset Account.
5. In the Reset Account dialog box, click Yes.
6. Quit Active Directory Users and Computers, and then restart the domain controller.

**Code**: [[[-] Kerberos SessionError: KRB_AP_ERR_MODIFIED(Mes]]

> This error occurs when the Kerberos authentication process detects that the message stream has been modified. This can happen due to a variety of reasons, including incorrect system time, incorrect service principal name (SPN), or an attacker's attempt to tamper with the authentication process. Resetting the computer account password for the domain controller is a common solution to this issue.

**Command** ([[Kerberos Session Error]]):

```bash
[-] Kerberos SessionError: KRB_AP_ERR_MODIFIED(Message stream modified)
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

- [[Kerberos Session Error]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos Bronze Bit Attack - CVE-2020-17049]]

---
id: e95a740b-a420-4f9e-941e-da55e7bba3e8
name: DNS Rebinding Protection Bypass via CNAME
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.629968+00:00'
updated_at: '2023-04-10T20:22:11.420472+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Dynamic Resolution|T1568 - Dynamic Resolution]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
sub_techniques:
- '[[Domain Generation Algorithms|T1568.002 - Domain Generation Algorithms]]'
tags:
- '[[CNAME]]'
- '[[DNS Rebinding]]'
- '[[Protection Bypasses]]'
commands:
- '[[DNS CNAME Lookup]]'
---

# DNS Rebinding Protection Bypass via CNAME

## Summary

DNS Rebinding Protection Bypass via CNAME is a technique that allows an attacker to bypass DNS rebinding protections by resolving a domain name to an IP address that is not covered by the same-origin policy. This attack can be used to exploit vulnerable web applications and gain unauthorized access

## Description

# Description

DNS Rebinding Protection Bypass via CNAME is a technique that allows an attacker to bypass DNS rebinding protections by resolving a domain name to an IP address that is not covered by the same-origin policy. This attack can be used to exploit vulnerable web applications and gain unauthorized access to sensitive information. The attacker can use this technique to bypass security controls and access resources that are not normally accessible from the internet.

To execute this attack, the attacker first needs to identify a vulnerable web application that is protected by DNS rebinding. The attacker then creates a malicious website that will be used to launch the attack. The attacker then sends a phishing email to the victim, enticing them to click on a link that will take them to the malicious website. Once the victim visits the malicious website, the attacker can use DNS rebinding to bypass the protection and gain access to the vulnerable web application.

The business value of this attack is that an attacker can gain unauthorized access to sensitive information, such as financial data, trade secrets, and personal information. This can result in significant financial losses, legal liabilities, and reputational damage for the victim organization.

## Requirements

1. Access to a vulnerable web application that is protected by DNS rebinding

1. A malicious website to launch the attack

1. A phishing email to lure the victim to the malicious website

## Defense

1. Implement network segmentation to prevent attackers from accessing sensitive information

1. Implement DNS rebinding protections to prevent this attack

1. Train employees to recognize and avoid phishing emails

## Objectives

1. Bypass DNS rebinding protection on a vulnerable web application

1. Gain unauthorized access to sensitive information

# Instructions

1. Execute the command in a terminal to check if the server is vulnerable to DNS rebinding via CNAME.

**Code**: [[$ dig cname.example.com +noall +answer
; <<>> DiG ]]

> The command uses the dig utility to query the DNS server for the CNAME record of the target domain. If the server returns the expected result, the service is vulnerable to DNS rebinding via CNAME. If the server returns an error message, the server has most likely implemented protections to prevent DNS rebinding attacks.

**Command** ([[DNS CNAME Lookup]]):

```bash
$ dig cname.example.com +noall +answer
; <<>> DiG 9.11.3-1ubuntu1.15-Ubuntu <<>> example.com +noall +answer
;; global options: +cmd
cname.example.com.            381     IN      CNAME   target.local.
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Dynamic Resolution|T1568 - Dynamic Resolution]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

### Sub-Techniques

- [[Domain Generation Algorithms|T1568.002 - Domain Generation Algorithms]]

## Commands Used

- [[DNS CNAME Lookup]]

## Tags

- [[CNAME]]
- [[DNS Rebinding]]
- [[Protection Bypasses]]

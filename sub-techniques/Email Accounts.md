---
id: 61b19700-6285-466f-85ef-ac6cbe5b2ac3
name: Email Accounts
type: sub-technique
mitre_id: T1586.002
mitre_url: null
created_at: '2023-04-06T00:31:25.971330+00:00'
updated_at: '2023-04-06T00:31:25.971330+00:00'
parent_technique: '[[Compromise Accounts|T1586 - Compromise Accounts]]'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Email Accounts

**MITRE ID**: T1586.002

**Parent Technique**: [[Compromise Accounts|T1586 - Compromise Accounts]]

This is a sub-technique of T1586 - Compromise Accounts.

## Summary

Adversaries may compromise email accounts that can be used during targeting. Adversaries can use compromised email accounts to further their operations, such as leveraging them to conduct [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Phishing](https://attack.mitre.org/tec

## Description

Adversaries may compromise email accounts that can be used during targeting. Adversaries can use compromised email accounts to further their operations, such as leveraging them to conduct [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Phishing](https://attack.mitre.org/techniques/T1566). Utilizing an existing persona with a compromised email account may engender a level of trust in a potential victim if they have a relationship, or knowledge of, the compromised persona. Compromised email accounts can also be used in the acquisition of infrastructure (ex: [Domains](https://attack.mitre.org/techniques/T1583/001)).

A variety of methods exist for compromising email accounts, such as gathering credentials via [Phishing for Information](https://attack.mitre.org/techniques/T1598), purchasing credentials from third-party sites, or by brute forcing credentials (ex: password reuse from breach credential dumps).(Citation: AnonHBGary) Prior to compromising email accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation.

Adversaries can use a compromised email account to hijack existing email threads with targets of interest.

## Tactics

This sub-technique is used in the following tactics:

- [[Resource Development|TA0042 - Resource Development]]

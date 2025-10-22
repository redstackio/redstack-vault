---
id: 6e0d77ab-018c-4eb3-8370-7561bb2581e7
name: Compromise Accounts
type: technique
mitre_id: T1586
mitre_url: null
created_at: '2023-04-06T00:31:26.476519+00:00'
updated_at: '2023-04-06T00:31:27.840561+00:00'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Compromise Accounts

**MITRE ID**: T1586

## Description

Adversaries may compromise accounts with services that can be used during targeting. For operations incorporating social engineering, the utilization of an online persona may be important. Rather than creating and cultivating accounts (i.e. [Establish Accounts](https://attack.mitre.org/techniques/T1585)), adversaries may compromise existing accounts. Utilizing an existing persona may engender a level of trust in a potential victim if they have a relationship, or knowledge of, the compromised persona. 

A variety of methods exist for compromising accounts, such as gathering credentials via [Phishing for Information](https://attack.mitre.org/techniques/T1598), purchasing credentials from third-party sites, or by brute forcing credentials (ex: password reuse from breach credential dumps).(Citation: AnonHBGary) Prior to compromising accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation.

Personas may exist on a single site or across multiple sites (ex: Facebook, LinkedIn, Twitter, Google, etc.). Compromised accounts may require additional development, this could include filling out or modifying profile information, further developing social networks, or incorporating photos.

Adversaries may directly leverage compromised email accounts for [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Phishing](https://attack.mitre.org/techniques/T1566).

## Tactics

- [[Resource Development|TA0042 - Resource Development]]

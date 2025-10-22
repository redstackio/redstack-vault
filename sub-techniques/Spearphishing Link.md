---
id: c1f06a44-14d9-4833-95ca-440687127b1d
name: Spearphishing Link
type: sub-technique
mitre_id: T1598.003
mitre_url: null
created_at: '2023-04-06T00:31:25.809324+00:00'
updated_at: '2023-04-06T00:31:25.809324+00:00'
parent_technique: '[[Phishing for Information|T1598 - Phishing for Information]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Spearphishing Link

**MITRE ID**: T1598.003

**Parent Technique**: [[Phishing for Information|T1598 - Phishing for Information]]

This is a sub-technique of T1598 - Phishing for Information.

## Summary

Adversaries may send spearphishing messages with a malicious link to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for info

## Description

Adversaries may send spearphishing messages with a malicious link to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)) and/or sending multiple, seemingly urgent messages.

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, the malicious emails contain links generally accompanied by social engineering text to coax the user to actively click or copy and paste a URL into a browser.(Citation: TrendMictro Phishing)(Citation: PCMag FakeLogin) The given website may be a clone of a legitimate site (such as an online or corporate login portal) or may closely resemble a legitimate site in appearance and have a URL containing elements from the real site. 

From the fake website, information is gathered in web forms and sent to the adversary. Adversaries may also use information from previous reconnaissance efforts (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)) to craft persuasive and believable lures.

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]

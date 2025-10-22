---
id: a7a8e90b-8325-4566-8b16-d1ec8ce757ed
name: Spearphishing Attachment
type: sub-technique
mitre_id: T1598.002
mitre_url: null
created_at: '2023-04-06T00:31:26.537369+00:00'
updated_at: '2023-04-06T00:31:26.537369+00:00'
parent_technique: '[[Phishing for Information|T1598 - Phishing for Information]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Spearphishing Attachment

**MITRE ID**: T1598.002

**Parent Technique**: [[Phishing for Information|T1598 - Phishing for Information]]

This is a sub-technique of T1598 - Phishing for Information.

## Summary

Adversaries may send spearphishing messages with a malicious attachment to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing fo

## Description

Adversaries may send spearphishing messages with a malicious attachment to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)) and/or sending multiple, seemingly urgent messages.

All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries attach a file to the spearphishing email and usually rely upon the recipient populating information then returning the file.(Citation: Sophos Attachment)(Citation: GitHub Phishery) The text of the spearphishing email usually tries to give a plausible reason why the file should be filled-in, such as a request for information from a business associate. Adversaries may also use information from previous reconnaissance efforts (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)) to craft persuasive and believable lures.

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]

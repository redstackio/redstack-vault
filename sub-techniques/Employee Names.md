---
id: 09de19ea-8c29-4292-9c8b-c30bf06883c1
name: Employee Names
type: sub-technique
mitre_id: T1589.003
mitre_url: null
created_at: '2023-04-06T00:31:26.366859+00:00'
updated_at: '2023-04-06T00:31:26.366859+00:00'
parent_technique: '[[Gather Victim Identity Information|T1589 - Gather Victim Identity
  Information]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Employee Names

**MITRE ID**: T1589.003

**Parent Technique**: [[Gather Victim Identity Information|T1589 - Gather Victim Identity Information]]

This is a sub-technique of T1589 - Gather Victim Identity Information.

## Summary

Adversaries may gather employee names that can be used during targeting. Employee names be used to derive email addresses as well as to help guide other reconnaissance efforts and/or craft more-believable lures.

Adversaries may easily gather employee names, since they may be readily available and e

## Description

Adversaries may gather employee names that can be used during targeting. Employee names be used to derive email addresses as well as to help guide other reconnaissance efforts and/or craft more-believable lures.

Adversaries may easily gather employee names, since they may be readily available and exposed via online or other accessible data sets (ex: [Social Media](https://attack.mitre.org/techniques/T1593/001) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation: OPM Leak) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Phishing for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Phishing](https://attack.mitre.org/techniques/T1566) or [Valid Accounts](https://attack.mitre.org/techniques/T1078)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]

---
id: 6a5b39fd-3f15-4349-9410-5b46dc56109d
name: Search Victim-Owned Websites
type: technique
mitre_id: T1594
mitre_url: null
created_at: '2023-04-06T00:31:25.607815+00:00'
updated_at: '2023-04-06T03:56:21.759464+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
procedures:
- '[[Passive Recon and Information Gathering]]'
---

# Search Victim-Owned Websites

**MITRE ID**: T1594

## Description

Adversaries may search websites owned by the victim for information that can be used during targeting. Victim-owned websites may contain a variety of details, including names of departments/divisions, physical locations, and data about key employees such as names, roles, and contact info (ex: [Email Addresses](https://attack.mitre.org/techniques/T1589/002)). These sites may also have details highlighting business operations and relationships.(Citation: Comparitech Leak)

Adversaries may search victim-owned websites to gather actionable information. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Trusted Relationship](https://attack.mitre.org/techniques/T1199) or [Phishing](https://attack.mitre.org/techniques/T1566)).

## Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

## Related Procedures (1)

- [[Passive Recon and Information Gathering]]

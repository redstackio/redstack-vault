---
id: b5cba0b6-570b-4868-a042-2989b598426b
name: Search Closed Sources
type: technique
mitre_id: T1597
mitre_url: null
created_at: '2023-04-06T00:31:26.676018+00:00'
updated_at: '2023-04-06T00:31:27.853423+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Search Closed Sources

**MITRE ID**: T1597

## Description

Adversaries may search and gather information about victims from closed sources that can be used during targeting. Information about victims may be available for purchase from reputable private sources and databases, such as paid subscriptions to feeds of technical/threat intelligence data.(Citation: D3Secutrity CTI Feeds) Adversaries may also purchase information from less-reputable sources such as dark web or cybercrime blackmarkets.(Citation: ZDNET Selling Data)

Adversaries may search in different closed databases depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Valid Accounts](https://attack.mitre.org/techniques/T1078)).

## Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

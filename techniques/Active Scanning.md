---
id: acbcd1fd-7d81-46c0-bcc8-2c7e37a0911b
name: Active Scanning
type: technique
mitre_id: T1595
mitre_url: null
created_at: '2023-04-06T00:31:26.263056+00:00'
updated_at: '2023-04-06T03:56:25.846335+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
procedures:
- '[[Active Directory Recon - Using AD Module]]'
- '[[Active Directory Recon with PowerView]]'
- '[[Azure O365 Email Enumeration]]'
- '[[Azure Reconnaissance]]'
- '[[Network Discovery - Spyse Reverse IP Lookup]]'
- '[[Passive Recon and Information Gathering]]'
- '[[Subdomain Enumeration and Takeover using SubOver]]'
- '[[Subdomain Enumeration with Knockpy and EyeWitness]]'
---

# Active Scanning

**MITRE ID**: T1595

## Description

Adversaries may execute active reconnaissance scans to gather information that can be used during targeting. Active scans are those where the adversary probes victim infrastructure via network traffic, as opposed to other forms of reconnaissance that do not involve direct interaction.

Adversaries may perform different forms of active scanning depending on what information they seek to gather. These scans can also be performed in various ways, including using native features of network protocols such as ICMP.(Citation: Botnet Scan)(Citation: OWASP Fingerprinting) Information from these scans may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190)).

## Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

## Related Procedures (8)

- [[Active Directory Recon - Using AD Module]]
- [[Active Directory Recon with PowerView]]
- [[Azure O365 Email Enumeration]]
- [[Azure Reconnaissance]]
- [[Network Discovery - Spyse Reverse IP Lookup]]
- [[Passive Recon and Information Gathering]]
- [[Subdomain Enumeration and Takeover using SubOver]]
- [[Subdomain Enumeration with Knockpy and EyeWitness]]

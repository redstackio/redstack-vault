---
id: df01b4ea-e6d8-458f-875c-58fe12f6412b
name: Phishing for Information
type: technique
mitre_id: T1598
mitre_url: null
created_at: '2023-04-06T00:31:26.948069+00:00'
updated_at: '2023-04-06T03:56:31.671023+00:00'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
procedures:
- '[[OAuth Misconfiguration and CSRF Vulnerability]]'
---

# Phishing for Information

**MITRE ID**: T1598

## Description

Adversaries may send phishing messages to elicit sensitive information that can be used during targeting. Phishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Phishing for information is different from [Phishing](https://attack.mitre.org/techniques/T1566) in that the objective is gathering data from the victim rather than executing malicious code.

All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass credential harvesting campaigns.

Adversaries may also try to obtain information directly through the exchange of emails, instant messages, or other electronic conversation means.(Citation: ThreatPost Social Media Phishing)(Citation: TrendMictro Phishing)(Citation: PCMag FakeLogin)(Citation: Sophos Attachment)(Citation: GitHub Phishery) Phishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)) and/or sending multiple, seemingly urgent messages.

## Tactics

- [[Reconnaissance|TA0043 - Reconnaissance]]

## Related Procedures (1)

- [[OAuth Misconfiguration and CSRF Vulnerability]]

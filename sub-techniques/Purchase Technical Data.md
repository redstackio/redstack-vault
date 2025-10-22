---
id: 295ba21e-6de2-431e-a6d9-0b9d9518510e
name: Purchase Technical Data
type: sub-technique
mitre_id: T1597.002
mitre_url: null
created_at: '2023-04-06T00:31:25.484570+00:00'
updated_at: '2023-04-06T00:31:25.484570+00:00'
parent_technique: '[[Search Closed Sources|T1597 - Search Closed Sources]]'
tactics:
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
---

# Purchase Technical Data

**MITRE ID**: T1597.002

**Parent Technique**: [[Search Closed Sources|T1597 - Search Closed Sources]]

This is a sub-technique of T1597 - Search Closed Sources.

## Summary

Adversaries may purchase technical information about victims that can be used during targeting. Information about victims may be available for purchase within reputable private sources and databases, such as paid subscriptions to feeds of scan databases or other data aggregation services. Adversarie

## Description

Adversaries may purchase technical information about victims that can be used during targeting. Information about victims may be available for purchase within reputable private sources and databases, such as paid subscriptions to feeds of scan databases or other data aggregation services. Adversaries may also purchase information from less-reputable sources such as dark web or cybercrime blackmarkets.

Adversaries may purchase information about their already identified targets, or use purchased data to discover opportunities for successful breaches. Threat actors may gather various technical details from purchased data, including but not limited to employee contact information, credentials, or specifics regarding a victim’s infrastructure.(Citation: ZDNET Selling Data) Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Valid Accounts](https://attack.mitre.org/techniques/T1078)).

## Tactics

This sub-technique is used in the following tactics:

- [[Reconnaissance|TA0043 - Reconnaissance]]

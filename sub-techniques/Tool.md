---
id: be210e61-be87-4c33-b170-ff1ed567c754
name: Tool
type: sub-technique
mitre_id: T1588.002
mitre_url: null
created_at: '2023-04-06T00:31:26.669195+00:00'
updated_at: '2023-04-06T00:31:26.669195+00:00'
parent_technique: '[[Obtain Capabilities|T1588 - Obtain Capabilities]]'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Tool

**MITRE ID**: T1588.002

**Parent Technique**: [[Obtain Capabilities|T1588 - Obtain Capabilities]]

This is a sub-technique of T1588 - Obtain Capabilities.

## Summary

Adversaries may buy, steal, or download software tools that can be used during targeting. Tools can be open or closed source, free or commercial. A tool can be used for malicious purposes by an adversary, but (unlike malware) were not intended to be used for those purposes (ex: [PsExec](https://atta

## Description

Adversaries may buy, steal, or download software tools that can be used during targeting. Tools can be open or closed source, free or commercial. A tool can be used for malicious purposes by an adversary, but (unlike malware) were not intended to be used for those purposes (ex: [PsExec](https://attack.mitre.org/software/S0029)). Tool acquisition can involve the procurement of commercial software licenses, including for red teaming tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154). Commercial software may be obtained through purchase, stealing licenses (or licensed copies of the software), or cracking trial versions.(Citation: Recorded Future Beacon 2019)

Adversaries may obtain tools to support their operations, including to support execution of post-compromise behaviors. In addition to freely downloading or purchasing software, adversaries may steal software and/or software licenses from third-party entities (including other adversaries).

## Tactics

This sub-technique is used in the following tactics:

- [[Resource Development|TA0042 - Resource Development]]

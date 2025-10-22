---
id: 9d13d291-3f89-40b5-97cf-7a87682e711a
name: Indicator Removal from Tools
type: sub-technique
mitre_id: T1027.005
mitre_url: null
created_at: '2023-04-06T00:31:26.732258+00:00'
updated_at: '2023-04-06T00:31:26.732258+00:00'
parent_technique: '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[GUID / UUID Version Identification]]'
---

# Indicator Removal from Tools

**MITRE ID**: T1027.005

**Parent Technique**: [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

This is a sub-technique of T1027 - Obfuscated Files or Information.

## Summary

Adversaries may remove indicators from tools if they believe their malicious tool was detected, quarantined, or otherwise curtailed. They can modify the tool by removing the indicator and using the updated version that is no longer detected by the target's defensive systems or subsequent targets tha

## Description

Adversaries may remove indicators from tools if they believe their malicious tool was detected, quarantined, or otherwise curtailed. They can modify the tool by removing the indicator and using the updated version that is no longer detected by the target's defensive systems or subsequent targets that may use similar systems.

A good example of this is when malware is detected with a file signature and quarantined by anti-virus software. An adversary who can determine that the malware was quarantined because of its file signature may modify the file to explicitly avoid that signature, and then re-use the malware.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[GUID / UUID Version Identification]]

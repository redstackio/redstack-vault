---
id: e71407fb-6e9d-4987-adff-b5f67643bc9b
name: Exfiltration to Code Repository
type: sub-technique
mitre_id: T1567.001
mitre_url: null
created_at: '2023-04-06T00:31:26.526624+00:00'
updated_at: '2023-04-06T00:31:26.526624+00:00'
parent_technique: '[[Exfiltration Over Web Service|T1567 - Exfiltration Over Web Service]]'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
procedures:
- '[[DNS Poisoning and Credential Dumping via mitm6 Relay Attack]]'
---

# Exfiltration to Code Repository

**MITRE ID**: T1567.001

**Parent Technique**: [[Exfiltration Over Web Service|T1567 - Exfiltration Over Web Service]]

This is a sub-technique of T1567 - Exfiltration Over Web Service.

## Summary

Adversaries may exfiltrate data to a code repository rather than over their primary command and control channel. Code repositories are often accessible via an API (ex: https://api.github.com). Access to these APIs are often over HTTPS, which gives the adversary an additional level of protection.

Ex

## Description

Adversaries may exfiltrate data to a code repository rather than over their primary command and control channel. Code repositories are often accessible via an API (ex: https://api.github.com). Access to these APIs are often over HTTPS, which gives the adversary an additional level of protection.

Exfiltration to a code repository can also provide a significant amount of cover to the adversary if it is a popular service already used by hosts within the network. 

## Tactics

This sub-technique is used in the following tactics:

- [[Exfiltration|TA0010 - Exfiltration]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[DNS Poisoning and Credential Dumping via mitm6 Relay Attack]]

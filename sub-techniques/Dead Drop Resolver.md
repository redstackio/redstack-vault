---
id: 94bbd023-94e2-4b3d-a36e-ceca8c39941a
name: Dead Drop Resolver
type: sub-technique
mitre_id: T1102.001
mitre_url: null
created_at: '2023-04-06T00:31:27.212676+00:00'
updated_at: '2023-04-06T00:31:27.212676+00:00'
parent_technique: '[[Web Service|T1102 - Web Service]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
procedures:
- '[[MYSQL Injection Out-of-Band Data Exfiltration]]'
---

# Dead Drop Resolver

**MITRE ID**: T1102.001

**Parent Technique**: [[Web Service|T1102 - Web Service]]

This is a sub-technique of T1102 - Web Service.

## Summary

Adversaries may use an existing, legitimate external Web service to host information that points to additional command and control (C2) infrastructure. Adversaries may post content, known as a dead drop resolver, on Web services with embedded (and often obfuscated/encoded) domains or IP addresses. O

## Description

Adversaries may use an existing, legitimate external Web service to host information that points to additional command and control (C2) infrastructure. Adversaries may post content, known as a dead drop resolver, on Web services with embedded (and often obfuscated/encoded) domains or IP addresses. Once infected, victims will reach out to and be redirected by these resolvers.

Popular websites and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

Use of a dead drop resolver may also protect back-end C2 infrastructure from discovery through malware binary analysis while also enabling operational resiliency (since this infrastructure may be dynamically changed).

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[MYSQL Injection Out-of-Band Data Exfiltration]]

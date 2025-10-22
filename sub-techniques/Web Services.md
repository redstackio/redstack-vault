---
id: 0e24e28e-265c-44f3-bd6d-738efcd0e8a6
name: Web Services
type: sub-technique
mitre_id: T1584.006
mitre_url: null
created_at: '2023-04-06T00:31:26.719373+00:00'
updated_at: '2023-04-06T00:31:26.719373+00:00'
parent_technique: '[[Compromise Infrastructure|T1584 - Compromise Infrastructure]]'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Web Services

**MITRE ID**: T1584.006

**Parent Technique**: [[Compromise Infrastructure|T1584 - Compromise Infrastructure]]

This is a sub-technique of T1584 - Compromise Infrastructure.

## Summary

Adversaries may compromise access to third-party web services that can be used during targeting. A variety of popular websites exist for legitimate users to register for web-based services, such as GitHub, Twitter, Dropbox, Google, etc. Adversaries may try to take ownership of a legitimate user's ac

## Description

Adversaries may compromise access to third-party web services that can be used during targeting. A variety of popular websites exist for legitimate users to register for web-based services, such as GitHub, Twitter, Dropbox, Google, etc. Adversaries may try to take ownership of a legitimate user's access to a web service and use that web service as infrastructure in support of cyber operations. Such web services can be abused during later stages of the adversary lifecycle, such as during Command and Control ([Web Service](https://attack.mitre.org/techniques/T1102)) or [Exfiltration Over Web Service](https://attack.mitre.org/techniques/T1567).(Citation: Recorded Future Turla Infra 2020) Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. By utilizing a web service, particularly when access is stolen from legitimate users, adversaries can make it difficult to physically tie back operations to them.

## Tactics

This sub-technique is used in the following tactics:

- [[Resource Development|TA0042 - Resource Development]]

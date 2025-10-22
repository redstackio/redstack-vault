---
id: 80f5ca86-609f-46e4-9797-b216d0dae6ec
name: Upload Tool
type: sub-technique
mitre_id: T1608.002
mitre_url: null
created_at: '2023-04-06T00:31:26.095699+00:00'
updated_at: '2023-04-06T00:31:26.095699+00:00'
parent_technique: '[[Stage Capabilities|T1608 - Stage Capabilities]]'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Upload Tool

**MITRE ID**: T1608.002

**Parent Technique**: [[Stage Capabilities|T1608 - Stage Capabilities]]

This is a sub-technique of T1608 - Stage Capabilities.

## Summary

Adversaries may upload tools to third-party or adversary controlled infrastructure to make it accessible during targeting. Tools can be open or closed source, free or commercial. Tools can be used for malicious purposes by an adversary, but (unlike malware) were not intended to be used for those pur

## Description

Adversaries may upload tools to third-party or adversary controlled infrastructure to make it accessible during targeting. Tools can be open or closed source, free or commercial. Tools can be used for malicious purposes by an adversary, but (unlike malware) were not intended to be used for those purposes (ex: [PsExec](https://attack.mitre.org/software/S0029)). Adversaries may upload tools to support their operations, such as making a tool available to a victim network to enable [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105) by placing it on an Internet accessible web server.

Tools may be placed on infrastructure that was previously purchased/rented by the adversary ([Acquire Infrastructure](https://attack.mitre.org/techniques/T1583)) or was otherwise compromised by them ([Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)).(Citation: Dell TG-3390) Tools can also be staged on web services, such as an adversary controlled GitHub repo, or on Platform-as-a-Service offerings that enable users to easily provision applications.(Citation: Dragos Heroku Watering Hole)(Citation: Malwarebytes Heroku Skimmers)(Citation: Intezer App Service Phishing)

Adversaries can avoid the need to upload a tool by having compromised victim machines download the tool directly from a third-party hosting location (ex: a non-adversary controlled GitHub repo), including the original hosting site of the tool.

## Tactics

This sub-technique is used in the following tactics:

- [[Resource Development|TA0042 - Resource Development]]

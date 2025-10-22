---
id: bba999ac-e747-46b2-9dbf-eab4f9431c36
name: Outlook Forms
type: sub-technique
mitre_id: T1137.003
mitre_url: null
created_at: '2023-04-06T00:31:26.702665+00:00'
updated_at: '2023-04-06T00:31:26.702665+00:00'
parent_technique: '[[Office Application Startup|T1137 - Office Application Startup]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Outlook Forms

**MITRE ID**: T1137.003

**Parent Technique**: [[Office Application Startup|T1137 - Office Application Startup]]

This is a sub-technique of T1137 - Office Application Startup.

## Summary

Adversaries may abuse Microsoft Outlook forms to obtain persistence on a compromised system. Outlook forms are used as templates for presentation and functionality in Outlook messages. Custom Outlook forms can be created that will execute code when a specifically crafted email is sent by an adversar

## Description

Adversaries may abuse Microsoft Outlook forms to obtain persistence on a compromised system. Outlook forms are used as templates for presentation and functionality in Outlook messages. Custom Outlook forms can be created that will execute code when a specifically crafted email is sent by an adversary utilizing the same custom Outlook form.(Citation: SensePost Outlook Forms)

Once malicious forms have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious forms will execute when an adversary sends a specifically crafted email to the user.(Citation: SensePost Outlook Forms)

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]

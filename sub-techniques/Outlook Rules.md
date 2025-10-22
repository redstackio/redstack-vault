---
id: 19f9c172-a78a-4726-ab3b-da3d0d0afb98
name: Outlook Rules
type: sub-technique
mitre_id: T1137.005
mitre_url: null
created_at: '2023-04-06T00:31:25.961954+00:00'
updated_at: '2023-04-06T00:31:25.961954+00:00'
parent_technique: '[[Office Application Startup|T1137 - Office Application Startup]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Outlook Rules

**MITRE ID**: T1137.005

**Parent Technique**: [[Office Application Startup|T1137 - Office Application Startup]]

This is a sub-technique of T1137 - Office Application Startup.

## Summary

Adversaries may abuse Microsoft Outlook rules to obtain persistence on a compromised system. Outlook rules allow a user to define automated behavior to manage email messages. A benign rule might, for example, automatically move an email to a particular folder in Outlook if it contains specific words

## Description

Adversaries may abuse Microsoft Outlook rules to obtain persistence on a compromised system. Outlook rules allow a user to define automated behavior to manage email messages. A benign rule might, for example, automatically move an email to a particular folder in Outlook if it contains specific words from a specific sender. Malicious Outlook rules can be created that can trigger code execution when an adversary sends a specifically crafted email to that user.(Citation: SilentBreak Outlook Rules)

Once malicious rules have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious rules will execute when an adversary sends a specifically crafted email to the user.(Citation: SilentBreak Outlook Rules)

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]

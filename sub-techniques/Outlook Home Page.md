---
id: b86d7226-b73c-4314-be42-279ce67a57b6
name: Outlook Home Page
type: sub-technique
mitre_id: T1137.004
mitre_url: null
created_at: '2023-04-06T00:31:26.842186+00:00'
updated_at: '2023-04-06T00:31:26.842186+00:00'
parent_technique: '[[Office Application Startup|T1137 - Office Application Startup]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Outlook Home Page

**MITRE ID**: T1137.004

**Parent Technique**: [[Office Application Startup|T1137 - Office Application Startup]]

This is a sub-technique of T1137 - Office Application Startup.

## Summary

Adversaries may abuse Microsoft Outlook's Home Page feature to obtain persistence on a compromised system. Outlook Home Page is a legacy feature used to customize the presentation of Outlook folders. This feature allows for an internal or external URL to be loaded and presented whenever a folder is 

## Description

Adversaries may abuse Microsoft Outlook's Home Page feature to obtain persistence on a compromised system. Outlook Home Page is a legacy feature used to customize the presentation of Outlook folders. This feature allows for an internal or external URL to be loaded and presented whenever a folder is opened. A malicious HTML page can be crafted that will execute code when loaded by Outlook Home Page.(Citation: SensePost Outlook Home Page)

Once malicious home pages have been added to the user’s mailbox, they will be loaded when Outlook is started. Malicious Home Pages will execute when the right Outlook folder is loaded/reloaded.(Citation: SensePost Outlook Home Page)

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]

---
id: f367fa63-92bf-42df-af9f-9c0d14d956a1
name: DOCM Download and Execute via PowerShell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.397035+00:00'
updated_at: '2023-04-10T20:36:56.212263+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Office Application Startup|T1137 - Office Application Startup]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[DOCM - Download and Execute]]'
- '[[Office - Attacks]]'
---

# DOCM Download and Execute via PowerShell

## Summary

This procedure involves crafting a malicious Microsoft Office document (DOCM) that, when opened, downloads and executes a PowerShell payload. The DOCM file is typically delivered via a phishing email or other social engineering tactics. Upon opening the document, the user is prompted to enable macr

## Description

# Description

This procedure involves crafting a malicious Microsoft Office document (DOCM) that, when opened, downloads and executes a PowerShell payload. The DOCM file is typically delivered via a phishing email or other social engineering tactics. Upon opening the document, the user is prompted to enable macros, which then triggers the PowerShell payload to download and execute. This attack can be used to gain initial access to a network or to execute further malicious activity. From a technical standpoint, this attack leverages the scripting capabilities of Microsoft Office and the powerful execution capabilities of PowerShell. From a business perspective, this attack can lead to data theft, system compromise, and reputational damage.

## Requirements

1. Victim must have Microsoft Office installed

1. Victim must enable macros in the malicious document

1. Network access to download the PowerShell payload

## Defense

1. Disable macros in Microsoft Office by default

1. Use email filtering and user education to prevent phishing attacks

1. Monitor network traffic for suspicious activity, such as downloads of PowerShell payloads

## Objectives

1. Gain initial access to a network

1. Execute further malicious activity

# Instructions

1. This script executes a PowerShell payload when the document is opened.

**Code**: [[Sub Execute()
Dim payload
payload = "powershell.ex]]

> The `Execute` sub-routine defines a payload that executes a PowerShell command. The `Document_Open` sub-routine calls the `Execute` sub-routine when the document is opened. The PowerShell command downloads and executes a payload from the specified URL. The command uses a Web Proxy to download the payload and bypasses SSL certificate validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Office Application Startup|T1137 - Office Application Startup]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[DOCM - Download and Execute]]
- [[Office - Attacks]]

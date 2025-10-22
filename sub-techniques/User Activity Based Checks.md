---
id: 594ba7c5-1d24-4fbc-bade-d2d9595149a3
name: User Activity Based Checks
type: sub-technique
mitre_id: T1497.002
mitre_url: null
created_at: '2023-04-06T00:31:26.569969+00:00'
updated_at: '2023-04-06T00:31:26.569969+00:00'
parent_technique: '[[Virtualization/Sandbox Evasion|T1497 - Virtualization/Sandbox
  Evasion]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
---

# User Activity Based Checks

**MITRE ID**: T1497.002

**Parent Technique**: [[Virtualization/Sandbox Evasion|T1497 - Virtualization/Sandbox Evasion]]

This is a sub-technique of T1497 - Virtualization/Sandbox Evasion.

## Summary

Adversaries may employ various user activity checks to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a 

## Description

Adversaries may employ various user activity checks to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use the information learned from [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497) during automated discovery to shape follow-on behaviors.(Citation: Deloitte Environment Awareness)

Adversaries may search for user activity on the host based on variables such as the speed/frequency of mouse movements and clicks (Citation: Sans Virtual Jan 2016) , browser history, cache, bookmarks, or number of files in common directories such as home or the desktop. Other methods may rely on specific user interaction with the system before the malicious code is activated, such as waiting for a document to close before activating a macro (Citation: Unit 42 Sofacy Nov 2018) or waiting for a user to double click on an embedded image to activate.(Citation: FireEye FIN7 April 2017) 

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

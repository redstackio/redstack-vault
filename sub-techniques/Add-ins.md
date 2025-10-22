---
id: 14c2af19-c581-4901-bf5b-0373a488df38
name: Add-ins
type: sub-technique
mitre_id: T1137.006
mitre_url: null
created_at: '2023-04-06T00:31:25.888132+00:00'
updated_at: '2023-04-06T00:31:25.888132+00:00'
parent_technique: '[[Office Application Startup|T1137 - Office Application Startup]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Add-ins

**MITRE ID**: T1137.006

**Parent Technique**: [[Office Application Startup|T1137 - Office Application Startup]]

This is a sub-technique of T1137 - Office Application Startup.

## Summary

Adversaries may abuse Microsoft Office add-ins to obtain persistence on a compromised system. Office add-ins can be used to add functionality to Office programs. (Citation: Microsoft Office Add-ins) There are different types of add-ins that can be used by the various Office products; including Word/

## Description

Adversaries may abuse Microsoft Office add-ins to obtain persistence on a compromised system. Office add-ins can be used to add functionality to Office programs. (Citation: Microsoft Office Add-ins) There are different types of add-ins that can be used by the various Office products; including Word/Excel add-in Libraries (WLL/XLL), VBA add-ins, Office Component Object Model (COM) add-ins, automation add-ins, VBA Editor (VBE), Visual Studio Tools for Office (VSTO) add-ins, and Outlook add-ins. (Citation: MRWLabs Office Persistence Add-ins)(Citation: FireEye Mail CDS 2018)

Add-ins can be used to obtain persistence because they can be set to execute code when an Office application starts. 

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]

---
id: f6c57c13-62c6-4374-b2d0-9427f9803daf
name: AppLocker Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.394472+00:00'
updated_at: '2023-04-10T20:37:04.800844+00:00'
tags:
- '[[AppLocker]]'
- '[[Windows - Defenses]]'
---

# AppLocker Policy Enumeration

## Summary

AppLocker is a security feature in Windows that allows administrators to restrict which applications are allowed to run on a system. This procedure involves enumerating the effective AppLocker policy, which can help an attacker understand what applications are allowed to run on a target system. By 

## Description

# Description

AppLocker is a security feature in Windows that allows administrators to restrict which applications are allowed to run on a system. This procedure involves enumerating the effective AppLocker policy, which can help an attacker understand what applications are allowed to run on a target system. By understanding this policy, an attacker can identify potential weaknesses and plan their attack accordingly. From a technical perspective, this procedure involves using the 'Enumerate AppLocker Effective Policy' command to retrieve the effective AppLocker policy from a target system. The business value of this procedure is that it can help organizations identify weaknesses in their AppLocker policies and improve their overall security posture.

## Requirements

1. Authenticated access to the target system

1. Ability to run the 'Enumerate AppLocker Effective Policy' command

## Defense

1. Ensure that AppLocker policies are properly configured and up-to-date

1. Implement least privilege access controls to limit the impact of any potential attacks

1. Regularly review and update AppLocker policies to ensure that they are effective

## Objectives

1. Retrieve the effective AppLocker policy from a target system

1. Identify potential weaknesses in the AppLocker policy

1. Plan an attack based on the AppLocker policy

# Instructions

1. To enumerate the local AppLocker effective policy, run the following commands:

**Code**: [[PowerView PS C:\> Get-AppLockerPolicy -Effective |]]

> The first command 'Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections' will retrieve the effective AppLocker policy and expand the RuleCollections property to display the individual rules. The second command 'Get-AppLockerPolicy -effective -xml' will retrieve the effective AppLocker policy in XML format. The third command 'Get-ChildItem -Path HKLM:\SOFTWARE\Policies\Microsoft\Windows\SrpV2\Exe # (Keys: Appx, Dll, Exe, Msi and Script' will enumerate the AppLocker rules stored in the registry under the specified path for the given keys.

## Tags

- [[AppLocker]]
- [[Windows - Defenses]]

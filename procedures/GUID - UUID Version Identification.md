---
id: eeb9b0f1-d05e-4435-bead-2be59b39966c
name: GUID / UUID Version Identification
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.791795+00:00'
updated_at: '2023-04-06T03:55:59.805667+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
sub_techniques:
- '[[Indicator Removal from Tools|T1027.005 - Indicator Removal from Tools]]'
tags:
- '[[GUID / UUID]]'
- '[[GUID Versions]]'
- '[[Insecure Randomness]]'
commands:
- '[[UUID Generation]]'
---

# GUID / UUID Version Identification

## Summary

GUID / UUID is a way of generating unique identifiers, which can be useful in many applications. However, if the version of the GUID is not properly identified, it can lead to security issues. Attackers can use this information to identify the version of the GUID and potentially exploit vulnerabili

## Description

# Description

GUID / UUID is a way of generating unique identifiers, which can be useful in many applications. However, if the version of the GUID is not properly identified, it can lead to security issues. Attackers can use this information to identify the version of the GUID and potentially exploit vulnerabilities in the specific version. This attack can be used for obfuscation and indicator removal from tools. It can also be used to identify systems that are using outdated versions of the GUID algorithm. 

## Requirements

1. Access to a system generating GUID / UUID

## Defense

1. Ensure that the GUID / UUID algorithm being used is up-to-date and not vulnerable to known attacks.

1. Implement proper access controls and authentication to prevent unauthorized access to systems generating GUID / UUIDs.

1. Monitor for any unusual activity related to the generation or use of GUID / UUIDs, such as an increase in the use of outdated versions.

## Objectives

1. Identify the version of the GUID / UUID

1. Determine if the version is outdated and potentially vulnerable

1. Use the identified version for obfuscation and indicator removal from tools

# Instructions

1. Use the M and N values to identify the version of the GUID. 

**Code**: [[xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx]]

> The version of the GUID / UUID can be identified by the values of M and N. For example, version 4 of the GUID algorithm has a value of 4 for the M field, and the N field starts with a value between 8 and B. Other versions have different values for the M and N fields. By identifying the version of the GUID, an attacker can determine if the system is using an outdated version and potentially exploit vulnerabilities in that version.

**Command** ([[UUID Generation]]):

```bash
xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

### Sub-Techniques

- [[Indicator Removal from Tools|T1027.005 - Indicator Removal from Tools]]

## Commands Used

- [[UUID Generation]]

## Tags

- [[GUID / UUID]]
- [[GUID Versions]]
- [[Insecure Randomness]]

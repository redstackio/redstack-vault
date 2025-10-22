---
id: 86422bde-70eb-41a5-adff-c1f1d8a45568
name: Local Groups
type: sub-technique
mitre_id: T1069.001
mitre_url: null
created_at: '2023-04-06T00:31:26.649368+00:00'
updated_at: '2023-04-06T00:31:26.649368+00:00'
parent_technique: '[[Permission Groups Discovery|T1069 - Permission Groups Discovery]]'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
---

# Local Groups

**MITRE ID**: T1069.001

**Parent Technique**: [[Permission Groups Discovery|T1069 - Permission Groups Discovery]]

This is a sub-technique of T1069 - Permission Groups Discovery.

## Summary

Adversaries may attempt to find local system groups and permission settings. The knowledge of local system permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated per

## Description

Adversaries may attempt to find local system groups and permission settings. The knowledge of local system permission groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use this information to determine which users have elevated permissions, such as the users found within the local administrators group.

Commands such as <code>net localgroup</code> of the [Net](https://attack.mitre.org/software/S0039) utility, <code>dscl . -list /Groups</code> on macOS, and <code>groups</code> on Linux can list local groups.

## Tactics

This sub-technique is used in the following tactics:

- [[Discovery|TA0007 - Discovery]]

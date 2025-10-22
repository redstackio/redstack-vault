---
id: 3671968b-893b-4187-b396-c6d22775b9da
name: Match Legitimate Name or Location
type: sub-technique
mitre_id: T1036.005
mitre_url: null
created_at: '2023-04-06T00:31:25.670797+00:00'
updated_at: '2023-04-06T00:31:25.670797+00:00'
parent_technique: '[[Masquerading|T1036 - Masquerading]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Match Legitimate Name or Location

**MITRE ID**: T1036.005

**Parent Technique**: [[Masquerading|T1036 - Masquerading]]

This is a sub-technique of T1036 - Masquerading.

## Summary

Adversaries may match or approximate the name or location of legitimate files or resources when naming/placing them. This is done for the sake of evading defenses and observation. This may be done by placing an executable in a commonly trusted directory (ex: under System32) or giving it the name of 

## Description

Adversaries may match or approximate the name or location of legitimate files or resources when naming/placing them. This is done for the sake of evading defenses and observation. This may be done by placing an executable in a commonly trusted directory (ex: under System32) or giving it the name of a legitimate, trusted program (ex: svchost.exe). In containerized environments, this may also be done by creating a resource in a namespace that matches the naming convention of a container pod or cluster. Alternatively, a file or container image name given may be a close approximation to legitimate programs/images or something innocuous.

Adversaries may also use the same icon of the file they are trying to mimic.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]

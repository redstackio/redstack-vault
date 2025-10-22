---
id: 48a5c643-0010-4f35-af1b-49c5a883f3ee
name: Runtime Data Manipulation
type: sub-technique
mitre_id: T1565.003
mitre_url: null
created_at: '2023-04-06T00:31:25.871303+00:00'
updated_at: '2023-04-06T00:31:25.871303+00:00'
parent_technique: '[[Data Manipulation|T1565 - Data Manipulation]]'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# Runtime Data Manipulation

**MITRE ID**: T1565.003

**Parent Technique**: [[Data Manipulation|T1565 - Data Manipulation]]

This is a sub-technique of T1565 - Data Manipulation.

## Summary

Adversaries may modify systems in order to manipulate the data as it is accessed and displayed to an end user, thus threatening the integrity of the data.(Citation: FireEye APT38 Oct 2018)(Citation: DOJ Lazarus Sony 2018) By manipulating runtime data, adversaries may attempt to affect a business pro

## Description

Adversaries may modify systems in order to manipulate the data as it is accessed and displayed to an end user, thus threatening the integrity of the data.(Citation: FireEye APT38 Oct 2018)(Citation: DOJ Lazarus Sony 2018) By manipulating runtime data, adversaries may attempt to affect a business process, organizational understanding, and decision making.

Adversaries may alter application binaries used to display data in order to cause runtime manipulations. Adversaries may also conduct [Change Default File Association](https://attack.mitre.org/techniques/T1546/001) and [Masquerading](https://attack.mitre.org/techniques/T1036) to cause a similar effect. The type of modification and the impact it will have depends on the target application and process as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

## Tactics

This sub-technique is used in the following tactics:

- [[Impact|TA0040 - Impact]]

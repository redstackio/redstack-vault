---
id: fac9c84f-7f87-4b16-8bc8-354fbe791068
name: Transmitted Data Manipulation
type: sub-technique
mitre_id: T1565.002
mitre_url: null
created_at: '2023-04-06T00:31:26.970080+00:00'
updated_at: '2023-04-06T00:31:26.970080+00:00'
parent_technique: '[[Data Manipulation|T1565 - Data Manipulation]]'
tactics:
- '[[Impact|TA0040 - Impact]]'
---

# Transmitted Data Manipulation

**MITRE ID**: T1565.002

**Parent Technique**: [[Data Manipulation|T1565 - Data Manipulation]]

This is a sub-technique of T1565 - Data Manipulation.

## Summary

Adversaries may alter data en route to storage or other systems in order to manipulate external outcomes or hide activity, thus threatening the integrity of the data.(Citation: FireEye APT38 Oct 2018)(Citation: DOJ Lazarus Sony 2018) By manipulating transmitted data, adversaries may attempt to affec

## Description

Adversaries may alter data en route to storage or other systems in order to manipulate external outcomes or hide activity, thus threatening the integrity of the data.(Citation: FireEye APT38 Oct 2018)(Citation: DOJ Lazarus Sony 2018) By manipulating transmitted data, adversaries may attempt to affect a business process, organizational understanding, and decision making.

Manipulation may be possible over a network connection or between system processes where there is an opportunity deploy a tool that will intercept and change information. The type of modification and the impact it will have depends on the target transmission mechanism as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

## Tactics

This sub-technique is used in the following tactics:

- [[Impact|TA0040 - Impact]]

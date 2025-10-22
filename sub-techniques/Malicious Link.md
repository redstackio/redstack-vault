---
id: 07fcf763-554d-427a-ad09-244171049a72
name: Malicious Link
type: sub-technique
mitre_id: T1204.001
mitre_url: null
created_at: '2023-04-06T00:31:27.159207+00:00'
updated_at: '2023-04-06T00:31:27.159207+00:00'
parent_technique: '[[User Execution|T1204 - User Execution]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
---

# Malicious Link

**MITRE ID**: T1204.001

**Parent Technique**: [[User Execution|T1204 - User Execution]]

This is a sub-technique of T1204 - User Execution.

## Summary

An adversary may rely upon a user clicking a malicious link in order to gain execution. Users may be subjected to social engineering to get them to click on a link that will lead to code execution. This user action will typically be observed as follow-on behavior from [Spearphishing Link](https://at

## Description

An adversary may rely upon a user clicking a malicious link in order to gain execution. Users may be subjected to social engineering to get them to click on a link that will lead to code execution. This user action will typically be observed as follow-on behavior from [Spearphishing Link](https://attack.mitre.org/techniques/T1566/002). Clicking on a link may also lead to other execution techniques such as exploitation of a browser or application vulnerability via [Exploitation for Client Execution](https://attack.mitre.org/techniques/T1203). Links may also lead users to download files that require execution via [Malicious File](https://attack.mitre.org/techniques/T1204/002).

## Tactics

This sub-technique is used in the following tactics:

- [[Execution|TA0002 - Execution]]

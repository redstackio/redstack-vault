---
id: 069f792c-44eb-4736-be29-a590119c220f
name: Server
type: sub-technique
mitre_id: T1584.004
mitre_url: null
created_at: '2023-04-06T00:31:27.069848+00:00'
updated_at: '2023-04-06T00:31:27.069848+00:00'
parent_technique: '[[Compromise Infrastructure|T1584 - Compromise Infrastructure]]'
tactics:
- '[[Resource Development|TA0042 - Resource Development]]'
---

# Server

**MITRE ID**: T1584.004

**Parent Technique**: [[Compromise Infrastructure|T1584 - Compromise Infrastructure]]

This is a sub-technique of T1584 - Compromise Infrastructure.

## Summary

Adversaries may compromise third-party servers that can be used during targeting. Use of servers allows an adversary to stage, launch, and execute an operation. During post-compromise activity, adversaries may utilize servers for various tasks, including for Command and Control. Instead of purchasin

## Description

Adversaries may compromise third-party servers that can be used during targeting. Use of servers allows an adversary to stage, launch, and execute an operation. During post-compromise activity, adversaries may utilize servers for various tasks, including for Command and Control. Instead of purchasing a [Server](https://attack.mitre.org/techniques/T1583/004) or [Virtual Private Server](https://attack.mitre.org/techniques/T1583/003), adversaries may compromise third-party servers in support of operations.

Adversaries may also compromise web servers to support watering hole operations, as in [Drive-by Compromise](https://attack.mitre.org/techniques/T1189).

## Tactics

This sub-technique is used in the following tactics:

- [[Resource Development|TA0042 - Resource Development]]

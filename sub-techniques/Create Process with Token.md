---
id: 89079996-4053-4e00-9356-324d07f6b44f
name: Create Process with Token
type: sub-technique
mitre_id: T1134.002
mitre_url: null
created_at: '2023-04-06T00:31:26.274919+00:00'
updated_at: '2023-04-06T00:31:26.274919+00:00'
parent_technique: '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Create Process with Token

**MITRE ID**: T1134.002

**Parent Technique**: [[Access Token Manipulation|T1134 - Access Token Manipulation]]

This is a sub-technique of T1134 - Access Token Manipulation.

## Summary

Adversaries may create a new process with a different token to escalate privileges and bypass access controls. Processes can be created with the token and resulting security context of another user using features such as <code>CreateProcessWithTokenW</code> and <code>runas</code>.(Citation: Microsof

## Description

Adversaries may create a new process with a different token to escalate privileges and bypass access controls. Processes can be created with the token and resulting security context of another user using features such as <code>CreateProcessWithTokenW</code> and <code>runas</code>.(Citation: Microsoft RunAs)

Creating processes with a different token may require the credentials of the target user, specific privileges to impersonate that user, or access to the token to be used (ex: gathered via other means such as [Token Impersonation/Theft](https://attack.mitre.org/techniques/T1134/001) or [Make and Impersonate Token](https://attack.mitre.org/techniques/T1134/003)).

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

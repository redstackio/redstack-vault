---
id: 05ec156a-8751-4105-a45d-7aca39eb4b5f
name: Make and Impersonate Token
type: sub-technique
mitre_id: T1134.003
mitre_url: null
created_at: '2023-04-06T00:31:26.548030+00:00'
updated_at: '2023-04-06T00:31:26.548030+00:00'
parent_technique: '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Make and Impersonate Token

**MITRE ID**: T1134.003

**Parent Technique**: [[Access Token Manipulation|T1134 - Access Token Manipulation]]

This is a sub-technique of T1134 - Access Token Manipulation.

## Summary

Adversaries may make and impersonate tokens to escalate privileges and bypass access controls. If an adversary has a username and password but the user is not logged onto the system, the adversary can then create a logon session for the user using the <code>LogonUser</code> function. The function wi

## Description

Adversaries may make and impersonate tokens to escalate privileges and bypass access controls. If an adversary has a username and password but the user is not logged onto the system, the adversary can then create a logon session for the user using the <code>LogonUser</code> function. The function will return a copy of the new session's access token and the adversary can use <code>SetThreadToken</code> to assign the token to a thread.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

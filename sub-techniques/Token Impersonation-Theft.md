---
id: 2e236990-c257-4e74-af0f-373f549d687d
name: Token Impersonation/Theft
type: sub-technique
mitre_id: T1134.001
mitre_url: null
created_at: '2023-04-06T00:31:26.524386+00:00'
updated_at: '2023-04-06T00:31:26.524386+00:00'
parent_technique: '[[Access Token Manipulation|T1134 - Access Token Manipulation]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# Token Impersonation/Theft

**MITRE ID**: T1134.001

**Parent Technique**: [[Access Token Manipulation|T1134 - Access Token Manipulation]]

This is a sub-technique of T1134 - Access Token Manipulation.

## Summary

Adversaries may duplicate then impersonate another user's token to escalate privileges and bypass access controls. An adversary can create a new access token that duplicates an existing token using <code>DuplicateToken(Ex)</code>. The token can then be used with <code>ImpersonateLoggedOnUser</code> 

## Description

Adversaries may duplicate then impersonate another user's token to escalate privileges and bypass access controls. An adversary can create a new access token that duplicates an existing token using <code>DuplicateToken(Ex)</code>. The token can then be used with <code>ImpersonateLoggedOnUser</code> to allow the calling thread to impersonate a logged on user's security context, or with <code>SetThreadToken</code> to assign the impersonated token to a thread.

An adversary may do this when they have a specific, existing process they want to assign the new token to. For example, this may be useful for when the target user has a non-network logon session on the system.

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

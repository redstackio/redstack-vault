---
tags:
  - cookie-theft
  - exfiltration
type: procedure
tools:
  - '[[tools/Smuggler]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/Burp-Collaborator-Client]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/smuggler-discover-vuln]]'
  - '[[commands/http-smuggling-payload]]'
platforms:
  - Web
techniques:
  - '[[Steal Web Session Cookie]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 7f84b42a-b06d-48e6-af9f-3aaca7755814
created_at: '2025-12-11T06:10:33.355Z'
updated_at: '2025-12-11T06:10:33.355Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1539]]'
---
# Capture Leaked Session Cookies

## Summary

This procedure uses Burp Collaborator to receive and log leaked session cookies from redirected victim requests, enabling account takeovers.

## Description

Following the redirect, the backend sends requests to the attacker's Collaborator server, including cookies and IP. This collects data for mass takeovers. Applicable in scenarios involving cookie exfiltration via redirects.

## Requirements

1. Active redirects from hijacked requests.
2. Burp Collaborator Client running.
3. Polling enabled for interactions.

## Defense

Defensive measures and detection strategies:

- Set strict cookie attributes (HttpOnly, Secure) and domain scoping.
- Detect outbound requests to unknown domains in logs.

## Objectives

1. Receive leaked cookies.
2. Log victim session data.
3. Enable account takeover.

## Instructions

### Step 1: Poll Burp Collaborator

**Context**: Check the Collaborator client for incoming requests containing leaked data.

> No command; use the Burp Collaborator interface to view polled interactions, including cookies like 'd' and victim IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Collaborator-Client]]

## Tags

- [[cookie-theft]]
- [[Exfiltration]]

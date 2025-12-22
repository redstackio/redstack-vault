---
tags:
  - xss
  - execution
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 707ac910-5aa5-46f6-8620-3e2ac18dd05d
created_at: '2025-12-13T23:56:20.005Z'
updated_at: '2025-12-13T23:56:20.005Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS via Friend Request Acceptance

## Summary

This procedure triggers the execution of a previously stored XSS payload by having the victim accept the malicious friend request, leading to arbitrary JavaScript running in their browser.

## Description

Once the payload is stored, acceptance of the request renders the Message field without proper escaping, executing the embedded JavaScript. This can be used for client-side attacks like cookie theft or further exploitation. The vulnerability was fixed by adding sanitization.

## Requirements

1. Victim account with pending malicious friend request
2. Browser access to Social Club
3. No specific tools required beyond standard web browsing

## Defense

Defensive measures and detection strategies:

- Use Content Security Policy (CSP) to restrict script execution
- Monitor browser console for unexpected script errors or alerts

## Objectives

1. Execute stored payload
2. Confirm vulnerability impact
3. Enable potential session hijacking

## Instructions

### Step 1: Accept Friend Request

**Context**: Victim interacts with the notification to accept the request, triggering the payload.

> Navigate to friend requests and click Accept; observe the JavaScript execution (e.g., alert popup).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xss]]
- [[Execution]]

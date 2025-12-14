---
tags:
  - xss
  - injection
  - stored
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a294824f-4b47-4120-abb2-b3d8475d26fe
created_at: '2025-12-14T03:16:30.909Z'
updated_at: '2025-12-14T03:16:30.909Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Payload-into-Profile-Update

## Summary

Inject the bypassed XSS payload into Vimeo's profile update endpoint to achieve database storage, exploiting gaps in frontend encoding.

## Description

Exploit the filter bypass by submitting the encoded payload to profile fields, where it stores despite client-side protections. This leads to persistent XSS. Scenario: authenticated user updates profile; outcome: malicious content viewable by others.

## Requirements

1. Authenticated Vimeo session
2. Working bypass payload from testing
3. Access to profile edit page

## Defense

Defensive measures and detection strategies:

- Server-side input validation beyond regex
- Rate limiting on profile updates
- Audit logs for suspicious payloads

## Objectives

1. Store payload without detection
2. Persist across sessions
3. Enable multi-context execution

## Instructions

### Step 1: Prepare Profile Update

**Context**: Log in and navigate to editable fields.

Go to account settings > profile, locate bio or description input.

> Ensure no additional client-side checks block submission.

### Step 2: Submit Malicious Payload

**Context**: Insert and send the payload to backend.

Enter <%0crameset%20src='javascript:alert(1)'> in the field and save changes.

> Frontend may encode entities, but backend stores raw, evading filter.

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
- [[injection]]

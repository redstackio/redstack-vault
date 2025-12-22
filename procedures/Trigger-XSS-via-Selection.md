---
tags:
  - xss
  - trigger
  - javascript-execution
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:37.825Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d4130681-e1f2-4383-97f7-ac059061295f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Selection

## Summary

This procedure triggers the stored XSS payload by interacting with the malicious username in GitLab's approval dropdown, executing arbitrary JavaScript in the victim's browser.

## Description

Once the payload is stored in the username and placed in the approval field, selecting or clicking the dropdown entry causes the unsanitized HTML/JS to render and execute. In GitLab's web interface, this exploits the rendering of usernames without proper escaping, leading to client-side script execution. Outcomes include potential data theft or session manipulation in the authenticated context.

## Requirements

1. Malicious username already inserted in approval field
2. Victim-level access to view and interact with the settings page
3. Browser environment without strict XSS protections

## Defense

Defensive measures and detection strategies:

- Sanitize all user-generated content in UI rendering
- Implement output encoding (e.g., HTML entity encoding) for usernames
- Log and alert on unexpected script executions via browser console monitoring

## Objectives

1. Execute the stored JavaScript payload
2. Demonstrate impact such as alert or cookie access
3. Validate vulnerability for further exploitation

## Instructions

### Step 1: Interact with Approval Dropdown

**Context**: Select the field to load the dropdown containing the malicious entry.

Click into the approval requester field to open the user selection dropdown.

> Dropdown populates with users, including the one with XSS payload.

### Step 2: Select Malicious Username

**Context**: Trigger rendering and execution of the payload.

Click on the result corresponding to the malicious username.

> JavaScript executes immediately, e.g., alert displays or console logs sensitive data.

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
- [[trigger]]
- [[javascript-execution]]
- [[gitlab]]

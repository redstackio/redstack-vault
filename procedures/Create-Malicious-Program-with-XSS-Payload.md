---
id: proc-983077-create-program
tags:
  - xss
  - stored-xss
  - program-creation
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.866Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Program-with-XSS-Payload

## Summary

This procedure creates a new sandbox program on HackerOne with a Program Name containing an XSS payload, storing the unsanitized input for later execution in the advanced vetting example DCA.

## Description

In the context of HackerOne's platform, Program Managers can create sandbox programs. The Program Name field lacks sanitization, allowing HTML/JS tags to be stored. This payload is later passed to a Markdown React component during example DCA generation, leading to XSS. The attack is limited to sandbox mode with no real data affected, but demonstrates execution for program members.

## Requirements

1. Authenticated access as a Program Manager
2. Web browser for navigation and input
3. Target: HackerOne at https://hackerone.com/teams/new/sandbox

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs, especially names, before rendering in components
- Use Content Security Policy (CSP) to block inline scripts and unsafe HTML
- Monitor for anomalous HTML in program names via input validation logs

## Objectives

1. Store XSS payload in Program Name
2. Confirm program creation without rejection
3. Prepare for payload triggering in vetting page

## Instructions

### Step 1: Access New Program Creation

**Context**: Log in and navigate to the sandbox program creation page to input the payload.

No specific command; use browser to visit https://hackerone.com/teams/new/sandbox and fill the Program Name field with `<blink><marquee><a href="//anything">XSS</a></marquee></blink>`.

> This stores the payload directly in the backend without sanitization.

### Step 2: Submit and Verify

**Context**: Complete creation to ensure the malicious name is persisted.

Submit the form and check the program dashboard for the handle.

> Expected: Program listed with the exact payload as name, no errors.

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
- [[stored-xss]]

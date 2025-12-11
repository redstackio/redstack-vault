---
id: 23d55709-9b4a-4d76-aa53-b3e0988ec274
name: Verify Stored XSS in Separate Session
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.461Z'
updated_at: '2025-12-11T06:10:15.461Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - verification
commands:
  - '[[commands/git-clone-trac-repo]]'
platforms:
  - Web
tools:
  - '[[tools/Git]]'
  - '[[tools/Web-Browser]]'
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1059.007]]'
---

# Verify Stored XSS in Separate Session

## Summary

This procedure verifies the stored XSS by accessing the ticket in a separate browser session, confirming cross-session execution.

## Description

By using a different logged-in account, the payload executes again, demonstrating the stored nature and potential for widespread impact like cookie collection.

## Requirements

1. Ticket URL from previous step
2. Secondary Trac account
3. Web browser with private mode

## Defense

Defensive measures and detection strategies:

- Regularly audit and patch input handling in web apps
- Use XSS filters and monitoring tools

## Objectives

1. Confirm stored execution
2. Validate impact across users
3. Assess potential for data collection

## Instructions

### Step 1: Access Ticket in New Session

**Context**: Open the ticket URL in a private window with another account.

Using [[tools/Web-Browser]], copy the ticket URL, open in a private window with another logged-in account, and observe the XSS alert.

> Expected: Alert triggers in the new session.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[xss]]
- [[verification]]

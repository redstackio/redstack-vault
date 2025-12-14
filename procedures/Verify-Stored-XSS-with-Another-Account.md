---
tags:
  - xss
  - verification
  - trac
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
id: 0414b5f3-7b19-43e5-a4cc-872f43486492
created_at: '2025-12-14T00:11:25.230Z'
updated_at: '2025-12-14T00:11:25.230Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify Stored XSS with Another Account

## Summary

This procedure verifies the stored XSS by accessing the ticket with a different account to confirm cross-user impact.

## Description

The stored payload executes in any logged-in user's browser upon viewing the ticket, demonstrating the vulnerability's potential for widespread attacks like cookie theft.

## Requirements

1. Ticket URL from previous steps
2. Secondary Trac account
3. Private browser window

## Defense

Defensive measures and detection strategies:

- Isolate user sessions
- Detect cross-origin script executions

## Objectives

1. Confirm stored nature
2. Demonstrate impact on other users
3. Validate exploit success

## Instructions

### Step 1: Copy URL

**Context**: Obtain the ticket link.

Copy the ticket URL.

> URL ready for testing.

### Step 2: Access with Another Account

**Context**: Load in separate session.

Open in a private window with another logged-in account and observe the XSS alert.

> Alert executes in new context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xss
- verification
- trac

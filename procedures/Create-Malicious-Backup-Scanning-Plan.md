---
tags:
  - xss-injection
  - payload-creation
  - acronis
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.488Z'
sub_techniques: []
id: 63b380d4-5a60-4856-9eb1-05bd037ebb38
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create Malicious Backup Scanning Plan

## Summary

This procedure details the creation of a backup scanning plan in the Acronis console with an injected XSS payload in the name field, storing the vulnerability for later execution.

## Description

The stored XSS is exploited by entering a JavaScript payload during plan creation. The payload `/><svg/onload=prompt(document.domain)>` breaks out of HTML context and executes on render. Prerequisites include console access; outcomes enable persistent JavaScript execution when the plan is viewed or edited.

## Requirements

1. Authenticated session in Acronis console
2. Access to 'Backup Scanning' under 'PLANS'
3. Browser supporting SVG onload events

## Defense

Defensive measures and detection strategies:

- Sanitize and escape user inputs in plan names
- Implement Content Security Policy (CSP) to block inline scripts
- Log and review plan creation events for suspicious payloads

## Objectives

1. Inject and store XSS payload in plan metadata
2. Finalize plan creation without immediate detection
3. Set up for payload triggering

## Instructions

### Step 1: Navigate to Plan Creation

**Context**: From the dashboard, access the backup scanning section.

Click 'Backup Scanning' under 'PLANS', then 'Create Plan'.

> Form loads with fields for location and name.

### Step 2: Specify Location and Inject Payload

**Context**: Select a target location and enter the malicious name.

Choose a location like 'User's PC', then name the plan `/><svg/onload=prompt(document.domain)>`.

> Payload is inserted; proceed to create.

### Step 3: Save the Plan

**Context**: Complete creation and edit to persist.

Click 'Create', then edit icon and 'Save Changes'.

> Plan is stored with payload; alerts may appear.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mozilla-Firefox]]

## Tags

- xss-injection
- stored-xss

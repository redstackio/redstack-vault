---
id: proc-trigger-xss-program-page
tags:
  - xss
  - execution
  - hackerone
type: procedure
tools: []
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
updated_at: '2025-12-13T23:56:04.014Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Program-Page

## Summary

This procedure triggers the stored XSS by viewing and interacting with the program page where the malicious asset identifier is rendered, exploiting jQuery's improper HTML parsing.

## Description

Once injected, visiting the program page and clicking the asset causes the identifier to be truncated using jQuery.truncate, which parses HTML and executes the onerror script. This affects any viewer, leading to arbitrary JS execution in the session context, potentially for data theft or hijacking. Requires the asset from the injection procedure.

## Requirements

1. Injected malicious asset from prior procedure
2. Access to the program page URL
3. Vulnerable browser session

## Defense

Defensive measures and detection strategies:

- Replace jQuery.truncate with a safe text truncation library (e.g., using textContent)
- Audit rendering of user-controlled fields for HTML parsing
- Log and alert on unexpected JS errors or prompts in web views
- Deploy CSP headers to prevent execution

## Objectives

1. Execute the stored payload on program page load/click
2. Confirm XSS in primary viewing context
3. Impact multiple users viewing the page

## Instructions

### Step 1: Navigate to Program Page

**Context**: Load the page containing the asset list.

Visit `https://hackerone.com/[program-handle]` (replace with actual program slug).

### Step 2: Interact with Asset

**Context**: Click the malicious asset to force rendering and truncation.

Click on the asset identifier; jQuery processes it, firing the payload.

**Expected Output**: JavaScript prompt alert appears.

### Step 3: Validate Execution

**Context**: Check for successful script run in console or alerts.

Inspect browser console for errors or execution traces.

**Expected Output**: Confirmed JS execution without CSP block.

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
- trigger

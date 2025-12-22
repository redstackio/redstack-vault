---
tags:
  - xss
  - execution
  - openfolio
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:36.312Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 68a04c4b-7dbe-4ada-889e-62f2d88a3cc3
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Invite-Button

## Summary

This procedure executes the XSS payload by clicking the invite button on the malicious contact in Openfolio, injecting and running arbitrary JavaScript in the victim's browser.

## Description

The invite functionality in Openfolio's contacts page re-renders or processes the contact name without sanitization, allowing the payload to break HTML context and execute. For example, the img onerror triggers a prompt. This leads to client-side attacks like cookie theft. Prerequisites: Loaded contacts page with malicious entry. Outcomes: JS execution, potential data exfiltration.

## Requirements

1. Openfolio contacts page loaded with malicious contact
2. Victim or attacker session (stored XSS potential)
3. Browser executing JS

## Defense

Defensive measures and detection strategies:

- Sanitize contact names in all interactive elements (e.g., buttons, modals)
- Use DOMPurify or similar for client-side cleaning
- Detect JS execution via browser security tools or CSP violations

## Objectives

1. Execute injected JavaScript code
2. Demonstrate impact (e.g., alert, data theft)
3. Enable further attacks like session hijacking

## Instructions

### Step 1: Locate Malicious Contact

**Context**: Identify the entry with the payload in the list.

Scan the contacts page for the name '><img src=x onerror=prompt(1)>'.

### Step 2: Click Invite Button

**Context**: Interact with the invite option to trigger rendering of the unsanitized name.

Select the malicious contact and click the "Invite" button.

> This injects the payload into the page, executing <img src=x onerror=prompt(1)>, which fires the onerror event since src=x is invalid.

**Expected Output**: Prompt dialog with value 1 appears.

### Step 3: Validate Execution

**Context**: Confirm XSS success and assess potential impact.

Check browser console for errors or executed code; replace prompt with document.cookie for real attacks.

**Expected Output**: JS runs, e.g., alert box or logged data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[openfolio]]

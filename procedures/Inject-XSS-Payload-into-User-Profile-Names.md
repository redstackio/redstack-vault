---
tags:
  - xss
  - payload-injection
  - stored-xss
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
detection_risk: low
sub_techniques: []
id: 6c379150-96d8-4a34-b200-23915afdf9a3
created_at: '2025-12-14T03:47:12.901Z'
updated_at: '2025-12-14T03:47:12.901Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-User-Profile-Names

## Summary

This procedure involves injecting a split XSS payload into a user's first and last name fields in a web application profile, exploiting concatenation during rendering to store executable JavaScript without triggering input validation.

## Description

In the context of a Python-based web application like Quantopian's platform, user names are stored separately but concatenated when displayed in fields like 'dataset owner'. By splitting a payload across fields (e.g., `<img src=x` in first name and `onerror=alert(1)>` in last name), the rendered output becomes `<img src=x onerror=alert(1)>`, executing JavaScript when viewed. This stored XSS primarily affects enterprise users viewing shared datasets, enabling theft of algorithms. Prerequisites include valid user credentials and access to profile editing.

## Requirements

1. Valid authenticated session to the web application
2. Access to user profile editing page
3. Knowledge of the rendering context (e.g., concatenation in dashboard)

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity escaping) for all user inputs in templates
- Use Content Security Policy (CSP) to restrict inline scripts and image onerror handlers
- Validate and sanitize name fields on input to prevent script tags or event handlers
- Monitor for anomalous JavaScript execution in browser dev tools or server logs

## Objectives

1. Store malicious JavaScript in user profile without detection
2. Prepare for execution in victim browser context
3. Enable subsequent data exfiltration from enterprise dashboards

## Instructions

### Step 1: Access Profile Settings

**Context**: Log in and navigate to the user profile editing section to prepare for payload injection.

No specific command; use the web interface to reach the first/last name input fields.

> Expected: Profile form loads with editable name fields.

### Step 2: Inject Split Payload

**Context**: Enter the payload components into the name fields to exploit concatenation during output rendering.

In the first name field: `<img src=x`

In the last name field: `onerror=alert(1)>`

Submit the form to save.

> This forms a valid `<img>` tag with onerror event when displayed. Expected: Profile saves successfully; no immediate execution.

### Step 3: Verify Storage

**Context**: Optionally view a non-triggering page to confirm storage, but avoid dashboard until targeting a victim.

No command; inspect profile data via API if available or wait for Step 2 of the chain.

> Expected: Payload persists in backend storage.

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
- [[JavaScript]]

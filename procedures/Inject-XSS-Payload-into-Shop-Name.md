---
tags:
  - xss
  - payload-injection
  - javascript
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.360Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 21261575-6a8b-4a21-bf37-d5cc0310c19f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject XSS Payload into Shop Name

## Summary

This procedure details crafting and entering a malicious JavaScript payload into the Reverb LP shop name field to exploit the stored XSS vulnerability.

## Description

The shop name input lacks proper sanitization, allowing attackers to inject HTML and script tags. The payload closes any existing script or tag contexts and inserts executable JavaScript. In a real attack, this could exfiltrate session data; for testing, a simple alert is used. Prerequisites include access to the edit page.

## Requirements

1. Access to the shop edit form
2. Knowledge of XSS payloads
3. Attacker-controlled domain for exfiltration (optional)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding
- Use Content Security Policy (CSP) to block inline scripts
- Log and review anomalous input patterns in shop names

## Objectives

1. Bypass client-side validation
2. Craft payload for script execution
3. Store malicious content on the server

## Instructions

### Step 1: Craft and Enter Payload

**Context**: Replace the shop name with a payload that evades sanitization and executes on render.

Enter the following in the shop name field:

`lll"></script><script>alert('xss')</script>`

> This payload assumes a context like `<script>Shop: {name}</script>` and breaks out to inject a new script. Expected output: Input accepted without errors.

### Step 2: Validate Payload

**Context**: Use browser dev tools to inspect if the payload is reflected properly before saving.

Inspect the form element in dev tools.

> Look for the input value containing the full payload. Success if script tags are present.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
- [[JavaScript]]

---
tags:
  - stored-xss
  - execution
  - phpbb
type: procedure
tools:
  - '[[tools/Browser-Chrome]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.094Z'
sub_techniques: []
id: be77e4fe-931f-423e-8ae1-ec03a7a202b6
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Trigger-Stored-XSS-in-phpBB

## Summary

This procedure triggers the stored XSS by viewing forum sections where the malicious emoji is displayed, executing payloads for all users and enabling defacement, theft, or malware.

## Description

Once imported, the unsanitized emoji appears in posts, comments, and admin areas. Viewing these triggers the XSS, such as onmouseover alerts or inline scripts, affecting any authenticated or guest user without further interaction.

## Requirements

1. Successful XSS import from prior steps
2. Access to affected forum sections
3. Victim browser for execution

## Defense

Defensive measures and detection strategies:

- Output-encode all user-controlled data in templates
- Content Security Policy (CSP) to block inline scripts
- Audit emoji displays for anomalies

## Objectives

1. Execute XSS on page load or interaction
2. Impact multiple users persistently
3. Achieve session hijacking or defacement

## Instructions

### Step 1: Navigate to Affected Area

**Context**: Visit a post or admin page using the malicious emoji.

Load /viewtopic.php?t=1 or similar.

### Step 2: Interact to Trigger

**Context**: Hover or load to fire onmouseover/script.

Observe alert() or payload effects.

> Expected output: JavaScript execution, e.g., alert box.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Chrome]]

## Tags

- stored-xss
- execution
- phpbb


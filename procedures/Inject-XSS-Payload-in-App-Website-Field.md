---
id: proc-uuid-4
tags:
  - xss
  - self-xss
  - javascript-injection
  - twitter
  - web
type: procedure
tools:
  - '[[tools/Internet-Explorer-11]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.786Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-App-Website-Field

## Summary

This procedure injects a javascript: URL payload into the website field of a Twitter app's settings, exploiting insufficient update validation to achieve self-XSS execution upon page interaction.

## Description

After initial save, re-open the settings and replace the website field with `javascript:alert(8007)`. Saving triggers the payload when the field is rendered or clicked in vulnerable browsers. Root cause is lax validation on edits versus creation. Impact is self-XSS, limited to the owner, and often blocked by modern CSP, but reproducible in IE11.

## Requirements

1. Saved app with editable settings
2. Browser without strict CSP enforcement (e.g., IE11)
3. Payload: javascript:alert(8007)

## Defense

Defensive measures and detection strategies:

- Sanitize and validate URL schemes server-side (block javascript:)
- Implement strict CSP to prevent inline JS execution
- Log and alert on suspicious field updates

## Objectives

1. Save malicious javascript: URL
2. Trigger JS execution in browser context
3. Demonstrate arbitrary code execution potential

## Instructions

### Step 1: Re-Edit Settings

**Context**: Return to the settings page to modify the website field.

Navigate to https://apps.twitter.com/app/{app_id}/settings.

> Form loads with current values. Expected output: Editable website field.

### Step 2: Inject and Save

**Context**: Replace content to introduce the XSS payload.

Clear the website field and enter `javascript:alert(8007)`, then save.

> Payload saves; upon save or view, alert may trigger. Expected output: Alert popup with 8007 (in IE11; blocked in Chrome CSP).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Internet-Explorer-11]]
- [[tools/Google-Chrome]]

## Tags

- [[xss]]
- [[self-xss]]
- [[javascript-injection]]
- [[twitter]]
- [[web]]

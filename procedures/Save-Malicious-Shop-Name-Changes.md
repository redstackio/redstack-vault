---
tags:
  - xss
  - persistence
  - save
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
updated_at: '2025-12-14T03:46:31.345Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 9e85bfe1-aba0-4f2e-8bc3-a7ae2de869b3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save Malicious Shop Name Changes

## Summary

This procedure covers submitting the form to persist the XSS payload in the Reverb backend, making it available for rendering on public shop pages.

## Description

After injecting the payload, form submission sends the unsanitized data to the server, where it is stored without validation. This creates a persistent stored XSS. The backend failure to encode outputs leads to execution on views. Expected outcome: Payload saved and retrievable.

## Requirements

1. Payload entered in the edit form
2. Valid session for form submission
3. No server-side rate limiting

## Defense

Defensive measures and detection strategies:

- Validate and sanitize inputs server-side before storage
- Implement WAF rules to detect script tags in form data
- Audit stored content for malicious patterns periodically

## Objectives

1. Persist the injected script
2. Confirm storage without rejection
3. Enable triggering on public views

## Instructions

### Step 1: Submit Form

**Context**: Click save to transmit the payload to the server.

Locate and click the "Save" or "Update" button on the edit page.

> Server responds with a success message or redirect. Expected output: Changes confirmed, no errors about invalid characters.

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
- [[Persistence]]
- [[save]]

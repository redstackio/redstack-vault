---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
tags:
  - xss
  - execution
  - trigger
  - adobe
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:52.992Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS via Accessed Link

## Summary

This procedure involves accessing the generated anonymous sharing link to render the stored description, executing the injected JavaScript payload and confirming the vulnerability.

## Description

The final step in the stored XSS attack on Adobe's files.acrobat.com: Victims (or testers) visit the preview URL, where the description field is output without escaping, firing the onerror event in the payload. This allows arbitrary JS like alerts or data exfiltration. Targets anonymous or authenticated viewers. Prerequisites: Link created. Outcomes: JS execution, e.g., alert popup.

## Requirements

1. Generated sharing link URL
2. Victim browser (can be incognito for anonymous test)

## Defense

Defensive measures and detection strategies:

- Encode user-generated content in previews (e.g., via innerText or HTML entities)
- Monitor for JS errors or unusual DOM manipulations in previews
- Implement client-side CSP to restrict script execution

## Objectives

1. Render the stored payload to execute JS
2. Demonstrate impact on victims
3. Validate full attack chain success

## Instructions

### Step 1: Distribute or Access Link

**Context**: Simulate victim interaction by opening the link.

Copy the generated URL and paste it into a new browser tab or share via email/phishing.

> The preview page loads, showing the file and description.

### Step 2: Observe Execution

**Context**: Confirm the payload triggers on render.

As the page loads, the description injects the <img> tag, failing src load and calling onerror=alert(1).

> An alert box appears with '1', proving XSS; inspect DOM to see raw HTML.

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
- execution
- trigger

---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - execution
  - concrete-cms
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
updated_at: '2025-12-14T03:15:35.399Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Image

## Summary

This procedure triggers the stored XSS by rendering the image on a page and interacting with it, executing the injected JavaScript in the victim's browser.

## Description

When the page containing the tampered image loads, the browser parses the alt text as part of the HTML img tag. The injected onmouseover event fires on hover, running arbitrary JavaScript. This affects any authenticated or public user viewing the page, potentially leading to session theft or phishing.

## Requirements

1. Image with malicious alt text already saved
2. Page where the image is embedded and viewable
3. Victim browser without XSS protections (e.g., no strict CSP)

## Defense

Defensive measures and detection strategies:

- Escape output in HTML rendering (e.g., attribute encoding)
- Deploy browser-based protections like XSS auditors
- Log and alert on JavaScript errors or unexpected popups

## Objectives

1. Execute the payload in a viewer's browser
2. Demonstrate arbitrary JS capabilities (e.g., alerts, data exfil)
3. Highlight impact on session security

## Instructions

### Step 1: Embed Image in Page

**Context**: Place the image on a viewable page to expose it to users.

**Action** (CMS Editing):

Edit a page in Concrete CMS, insert the malicious image via the block editor, and publish or save the page.

> Ensure the image renders with alt text. Expected output: Page updates with image visible.

### Step 2: Interact to Trigger

**Context**: Simulate victim interaction to execute the code.

**Action** (Browser Interaction):

Load the page in a browser and hover the mouse over the image.

> The onmouseover event triggers `alert('Wufff!')`. Expected output: Alert dialog appears, confirming execution. For advanced payloads, inspect network tab for data theft attempts.

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
- [[Execution]]
- [[concrete-cms]]

---
id: p-trigger-xss-contact
tags:
  - xss-execution
  - svg-trigger
  - nextcloud
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
updated_at: '2025-12-14T05:32:13.193Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-in-Contact-Image

## Summary

This procedure activates the stored XSS payload in an uploaded SVG contact image by rendering it in a browser context, leading to JavaScript execution and potential compromise of the viewing user.

## Description

By opening the SVG in a new tab, the browser parses and executes embedded scripts without restrictions from the Nextcloud renderer. This impacts authenticated users, enabling attacks like session theft. The scenario assumes a prior malicious upload, with outcomes including payload execution.

## Requirements

1. Contact with uploaded malicious SVG
2. Web browser session in Nextcloud
3. User interaction capability (e.g., right-click)

## Defense

Defensive measures and detection strategies:

- Block SVG rendering in new tabs or use safe viewing modes
- Implement script-blocking proxies for image loads
- Educate users on avoiding suspicious contact images

## Objectives

1. Execute JavaScript from stored SVG
2. Demonstrate impact on contact viewers
3. Highlight risks of unsanitized image handling

## Instructions

### Step 1: Open the Contact

**Context**: Navigate to the contact containing the malicious image.

**Instructions**: In the Contacts app, search for and open the contact with the uploaded SVG image.

> The image thumbnail displays in the contact details view.

### Step 2: Interact to Trigger Payload

**Context**: Force browser rendering of the SVG to execute the script.

**Instructions**: Click the image to select it, then right-click and choose 'Open image in a new tab'.

> The new tab loads the SVG directly, parsing and running the embedded <script> tag, e.g., triggering an alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[nextcloud]]

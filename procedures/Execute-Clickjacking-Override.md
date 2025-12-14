---
id: proc-uuid-003
tags:
  - clickjacking
  - ui-redressing
  - override-bypass
type: procedure
tools:
  - '[[tools/certerror-clickjacking-html]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Windows
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Disable Cloud Logs]]'
updated_at: '2025-12-14T17:28:12.467Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Disable Cloud Logs]]'
---
# Execute-Clickjacking-Override

## Summary

Deploy a malicious HTML page that iframes the Kaspersky certificate warning and overlays a fake link to trick the user into overriding the certificate without realizing the target site.

## Description

The HTML file embeds the error page in an iframe and positions a disguised 'network protection warning' button over the real override link. User clicks the fake UI, confirming a generic popup to complete the bypass. Applies to Safe Money and phishing alerts similarly due to shared lack of framing protections.

## Requirements

1. Certificate error triggered and page accessible
2. Malicious HTML file (certerror_clickjacking.html) prepared
3. User tricked into opening the file (e.g., via phishing)

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN on all security UI pages
- Add contextual details to warnings (e.g., site name) to detect disguises
- Browser extensions to detect iframes on security domains

## Objectives

1. Trick user into single-click certificate override
2. Bypass additional confirmations via generic popups
3. Disable Kaspersky features like Safe Money without alerts

## Instructions

### Step 1: Prepare Malicious HTML

**Context**: Ensure the file is ready with iframe targeting the error page.

**Instructions**: Create or download certerror_clickjacking.html that loads the browser's current warning via iframe and overlays the fake link.

### Step 2: Open HTML in Browser

**Context**: Load the page to embed the real warning.

**Instructions**: Open [[tools/certerror-clickjacking-html]] directly from the file system in the browser where the error was triggered.

> Page masquerades as Kaspersky UI; iframe loads the certificate page transparently.

### Step 3: Induce Click and Confirmation

**Context**: Simulate user interaction to execute the override.

**Instructions**: Click the overlaid 'I understand the risks and wish to continue' link; confirm the popup 'You are about to go to an insecure web resource. Are you sure you want to continue?' by clicking Continue.

> No site-specific context in popup aids deception; override applies to www.google.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Disable Cloud Logs]] Impair Defenses: Disable or Modify Tools

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/certerror-clickjacking-html]]

## Tags

- clickjacking
- ui-redressing
- override-bypass

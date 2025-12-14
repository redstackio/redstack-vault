---
tags:
  - xss
  - share-popup
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
updated_at: '2025-12-13T23:52:20.806Z'
skill_level: low
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 4f54b646-e6f0-4083-ae5d-8bbf902e28ba
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Share-Popup

## Summary

This procedure triggers the stored XSS by having the victim open the Share popup in Gallery view, executing the JS payload in browsers lacking CSP support.

## Description

Clicking the Share icon in Gallery view causes Nextcloud to render the directory name in the popup without sanitization, due to the migration issue changing the parameter type. This executes the payload, potentially allowing session hijacking or data theft in vulnerable browsers like older IE.

## Requirements

1. Victim in Gallery view of malicious folder
2. Browser without strict CSP (e.g., IE <11)
3. Share feature enabled

## Defense

Defensive measures and detection strategies:

- Upgrade to browsers with CSP enforcement
- Patch Nextcloud to sanitize popup renders
- Monitor JS errors and alerts in browser consoles

## Objectives

1. Execute arbitrary JS in victim context
2. Demonstrate impact on non-CSP environments
3. Highlight admin targeting potential

## Instructions

### Step 1: Locate Share Icon in Gallery

**Context**: Prepare for popup interaction.

In Gallery view, hover over the malicious folder or its header to reveal the Share icon.

### Step 2: Click Share Icon

**Context**: Trigger rendering of unsanitized name.

Click the Share icon; the popup opens and displays the directory name.

### Step 3: Observe Execution

**Context**: Confirm payload runs.

The `<img src=x onerror=alert(1)>` executes, showing an alert dialog. Extend payload for real attacks (e.g., keylogging).

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
- nextcloud
- share-popup

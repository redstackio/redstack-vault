---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - dos
  - chrome-extension
  - ajax
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Chrome Browser Extension
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.858Z'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Activate-Chrome-Extension-to-Trigger-DoS

## Summary

This procedure activates a vulnerable Chrome extension on a page serving a large security.txt file, causing the getSecuritytxt function to perform an unbounded AJAX fetch and processing, resulting in extension hang, tab freeze, or crash due to resource exhaustion.

## Description

The extension's lack of timeouts or size limits in AJAX (XHR) calls to untrusted hosts allows full ingestion of the 1-2 GB file, spiking CPU and memory. Impact is localized to the current tab, demonstrating a self-DoS without system-wide effects.

## Requirements

1. Chrome with the vulnerable extension installed and enabled
2. Tab open to the site from previous procedure
3. No additional privileges needed

## Defense

Defensive measures and detection strategies:

- Add request timeouts (e.g., xhr.timeout = 10000) and abort on large responses
- Implement streaming or partial processing for files
- Extension developers: Use Chrome APIs like fetch with size limits

## Objectives

1. Invoke the extension's fetch mechanism
2. Force full file processing to exhaust resources
3. Confirm DoS via hang or crash

## Instructions

### Step 1: Trigger Extension Functionality

**Context**: With the tab on the hosting site, activate the extension to scan for security.txt.

**Instructions**: Click the extension icon in Chrome's toolbar or use its popup/context menu to initiate the getSecuritytxt function.

> Expected output: Extension attempts AJAX call, begins processing, leading to unresponsiveness.

### Step 2: Monitor and Validate Impact

**Context**: Observe resource usage to confirm exhaustion.

**Instructions**: Open Chrome Task Manager (Shift+Esc) to watch CPU/RAM for the tab/extension process.

> Expected output: CPU >80%, RAM spikes to hundreds of MB, eventual hang or crash.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dos]]
- [[chrome-extension]]

---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - dropbox
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.947Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-File-Name-in-Dropbox

## Summary

This procedure involves crafting a Dropbox file name embedded with an XSS payload, exploiting the lack of sanitization in downstream applications like ThisData that render file names directly in HTML.

## Description

In scenarios where web applications pull and display external file names without escaping, attackers can inject JavaScript via the file name itself. Here, a payload like `'><img src="x" onerror=alert(document.cookie)>.png` is used to close HTML tags and execute code on render. This targets client-side execution without needing to alter file contents, relying on the attacker's Dropbox access.

## Requirements

1. Active Dropbox account with upload permissions
2. Knowledge of target application's rendering behavior
3. Basic understanding of XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled inputs, including file names, using HTML entity encoding
- Implement Content Security Policy (CSP) to restrict inline scripts
- Monitor for anomalous file names in backups or logs

## Objectives

1. Inject XSS payload into a file name for later exploitation
2. Ensure payload survives upload and sync processes
3. Prepare for client-side execution in the victim application

## Instructions

### Step 1: Log into Dropbox

**Context**: Gain access to create or rename files.

Log into your Dropbox web interface or use the API/client to access file management.

### Step 2: Create or Rename File

**Context**: Embed the XSS payload in the file name to inject script tags.

Create a new file or rename an existing one with the payload: `'><img src="x" onerror=alert(document.cookie)>.png`. Upload any benign content if needed, but the name is the vector.

> The payload closes any open HTML tags (e.g., from a list item) and injects an image with an onerror handler to execute JavaScript, such as alerting cookies.

### Step 3: Verify Upload

**Context**: Confirm the malicious name is stored correctly.

Refresh the Dropbox file list to ensure the name displays as intended without truncation or escaping by Dropbox.

**Expected Output**: File appears with the full malicious name.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[dropbox]]
- [[payload-injection]]

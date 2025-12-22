---
tags:
  - xss
  - stored-xss
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
updated_at: '2025-12-13T23:52:20.812Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 9eba366d-e855-47de-b1c8-285ff3de3b0c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Directory-in-Nextcloud

## Summary

This procedure creates a directory in Nextcloud with a name containing a stored XSS payload, exploiting the lack of sanitization in the Gallery app's directory name parameter.

## Description

In Nextcloud's Gallery app, a regression during migration changed a parameter from integer to string without proper HTML escaping, allowing arbitrary JS in folder names to be injected and stored. This step sets up the payload for later execution when rendered in the Share popup. It requires authenticated access and targets the file creation endpoint.

## Requirements

1. Authenticated session in Nextcloud
2. Gallery app installed and enabled
3. Web browser for UI interaction

## Defense

Defensive measures and detection strategies:

- Enable strict CSP headers to block inline JS execution
- Sanitize all user-input directory names with HTML entity encoding
- Monitor for unusual folder names containing script tags

## Objectives

1. Store XSS payload in a persistent directory name
2. Ensure payload survives sharing and viewing
3. Prepare for execution in victim's browser context

## Instructions

### Step 1: Log In and Navigate to Files

**Context**: Gain access to the file manager to create the directory.

Log in to your Nextcloud account and go to the Files section.

### Step 2: Create New Folder with Payload

**Context**: Inject the malicious name to store the XSS.

Click the New Folder button. Enter the payload as the name: `<img src=x onerror=alert(1)>`. Click Create.

> This leverages the unsanitized string parameter; the name is saved without escaping.

### Step 3: Verify Creation

**Context**: Confirm the folder exists with the payload intact.

Refresh the file list; the folder should appear with the exact name, no immediate execution.

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
- directory-creation

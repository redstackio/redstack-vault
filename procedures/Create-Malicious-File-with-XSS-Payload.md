---
tags:
  - xss
  - payload-creation
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
updated_at: '2025-12-13T23:55:20.392Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 345cfac0-26b7-4f0e-85af-43ee6f95e780
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-File-with-XSS-Payload

## Summary

This procedure creates a file in Nextcloud with a filename containing an XSS payload, exploiting the lack of encoding in filename display to inject malicious JavaScript.

## Description

In the context of Nextcloud's file system, filenames are not properly sanitized when displayed in certain UI elements, such as the projects tab in Talk conversations. By crafting a filename with HTML-breaking syntax and an onerror JavaScript event, the attacker prepares a persistent XSS vector. This payload executes when the victim interacts with the file representation, potentially leading to session hijacking or data exfiltration. Prerequisites include an attacker account with file creation permissions.

## Requirements

1. Active Nextcloud user account for the attacker
2. Access to the Files app in Nextcloud
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement strict filename sanitization and HTML encoding in all UI displays
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for unusual file names with script tags in logs

## Objectives

1. Create a file whose name triggers JavaScript on display
2. Ensure the payload is persistent and non-disruptive until triggered
3. Prepare for sharing without alerting the victim

## Instructions

### Step 1: Log In and Navigate to Files

**Context**: Access the file creation interface as the attacker.

Log in to the Nextcloud instance and open the Files app.

### Step 2: Create File with Malicious Name

**Context**: Upload or create a file using a name that breaks HTML context and injects the payload.

Create a new text file named `test'><img src=x onerror=alert(document.location)>.txt`. The payload `<img src=x onerror=alert(document.location)>` will execute an alert with the current URL when the image fails to load, demonstrating the XSS.

**Expected Output**: File created and visible in the file list with the exact name intact.

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
- [[nextcloud]]

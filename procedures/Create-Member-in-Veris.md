---
tags:
  - web
  - setup
  - member-creation
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:15:31.477Z'
sub_techniques: []
id: 65ab9d18-3318-4684-88f0-1c200cda3014
validated: true
---
# Create-Member-in-Veris

## Summary

This procedure creates a new member account in the Veris web application, serving as a prerequisite for associating groups and assets in a stored XSS attack chain.

## Description

In the context of exploiting a stored XSS vulnerability in Veris, creating a member allows for linking to groups and assets where the payload can be stored and triggered. This step requires authenticated access to the portal and uses standard form inputs without malicious content. The target environment is the Veris sandbox at https://sandbox.veris.in/portal/members/. Expected outcome is a new member entry that can be referenced in subsequent steps.

## Requirements

1. Authenticated session in Veris portal
2. Web browser access to https://sandbox.veris.in
3. Basic user credentials (no admin privileges needed)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on member creation to prevent abuse
- Log all member creations with IP and user agent for anomaly detection
- Require CAPTCHA or secondary verification for new account creation

## Objectives

1. Establish a controllable member entity for attack chaining
2. Verify access to members management functionality
3. Prepare for group and asset associations

## Instructions

### Step 1: Access Members Creation Page

**Context**: Log in and navigate to the creation interface to input member details.

No command required; perform via UI:

- Open https://sandbox.veris.in/portal/members/ in a browser
- Ensure logged in; click 'Create New Member' button
- Fill form: Name (e.g., 'Test Member'), Email (e.g., 'test@example.com'), other fields as minimal
- Submit the form

> This creates the member without triggering any vulnerabilities. Expected output: Success message and member in list.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[setup]]

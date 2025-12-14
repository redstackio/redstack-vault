---
id: proc-001
tags:
  - web-access
  - form-filling
  - initial-access
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
updated_at: '2025-12-14T17:23:32.411Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-and-Complete-Request-Form

## Summary

This procedure initiates access to a web application's request form endpoint to prepare for file upload exploitation, involving navigation and basic form completion without triggering alerts.

## Description

In the context of exploiting unrestricted file uploads, this procedure targets the /request?openform endpoint in a PHP-based web application. It simulates legitimate user interaction to reach the upload stage, ensuring the attacker blends in. Expected outcomes include successful progression to the attachment section, setting up for malicious payload delivery. Prerequisites include network access and a browser session.

## Requirements

1. Web browser with cookies enabled for session persistence
2. Knowledge of the target URL (/request?openform)
3. Basic understanding of form fields (e.g., name, email, description)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on form submissions to detect automated access
- Log all form navigations and require CAPTCHA on initial access

## Objectives

1. Gain entry to the file upload workflow
2. Complete preliminary form data to avoid validation errors
3. Position for unrestricted file upload

## Instructions

### Step 1: Navigate to Endpoint

**Context**: Load the request form to start the process.

Navigate to `https://target.com/request?openform` in your browser.

> The page should display the initial request form fields.

### Step 2: Fill Initial Form

**Context**: Provide minimal required data to proceed.

Enter details such as requester name, email, and a generic description (e.g., "Test request"), then submit to redirect to the next page.

> Expect a redirect to the detailed form page with attachment options.

### Step 3: Complete Additional Details

**Context**: Fill secondary fields to reach upload.

On the next page, enter request type and any other mandatory info, preparing for file selection.

> Success: Upload browse button is visible and clickable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-access]]
- [[form-filling]]

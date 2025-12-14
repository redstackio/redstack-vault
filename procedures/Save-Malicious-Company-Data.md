---
id: proc-save-drive2-data
tags:
  - data-persistence
  - form-submission
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
updated_at: '2025-12-13T23:52:33.532Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Malicious-Company-Data

## Summary

This procedure submits the business account form on drive2.ru to persist the injected XSS payload in the backend, making it available for rendering on the company profile page.

## Description

After injecting the payload, form submission stores the unsanitized data in the site's database. This web-based action relies on POST requests to the server, with successful outcomes confirmed by a save acknowledgment, enabling the stored XSS to affect subsequent page views.

## Requirements

1. Completed form with payload in place
2. Valid session cookie for submission
3. No client-side validation blocking the payload

## Defense

Defensive measures and detection strategies:

- Server-side input validation and sanitization before storage
- Audit logs for form submissions containing script tags
- WAF rules to block suspicious payloads in POST data

## Objectives

1. Persist the malicious input without errors
2. Generate a viewable company profile
3. Confirm storage via success response

## Instructions

### Step 1: Review Form Data

**Context**: Double-check payload before submission.

Scan all fields to ensure only the company name contains the payload.

> Use form preview if available.

### Step 2: Submit the Form

**Context**: Send the data to the backend for storage.

Click the 'Save' or 'Submit' button on the company management form.

> Watch for loading spinner or progress indicator.

### Step 3: Confirm Persistence

**Context**: Verify the submission succeeded.

Look for a success message or redirect to the company overview.

> Note the company profile URL for the next step.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- data-persistence
- form-submission

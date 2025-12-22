---
tags:
  - persistence
  - xss
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
updated_at: '2025-12-13T23:52:20.833Z'
sub_techniques: []
id: d31052c3-abe9-4755-a7ae-9588ca71f897
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Malicious-Recommendation

## Summary

This procedure submits the tainted recommendation form to store the XSS payload in Judge.me's database, ensuring it persists and displays on the public profile.

## Description

Following payload injection, this step completes form submission, leveraging the lack of backend validation to save raw HTML. It targets the storage mechanism of the web app. Prerequisites: Completed form with payload. Outcomes: Payload is persisted, visible to all profile viewers.

## Requirements

1. Filled recommendation form with malicious description
2. Valid session token
3. No additional tools; browser submit action

## Defense

Defensive measures and detection strategies:

- Validate and sanitize inputs server-side before database storage
- Implement web application firewalls (WAF) to inspect submissions
- Audit database for anomalous HTML content periodically

## Objectives

1. Persist the injected payload without errors
2. Confirm storage in the profile
3. Avoid triggering validation rules

## Instructions

### Step 1: Complete Form Fields

**Context**: Fill any remaining required fields.

Enter rating, date, or other details as needed.

> Form is ready for submission.

### Step 2: Submit Recommendation

**Context**: Store the content in the backend.

Click "Save" or "Submit" button.

> Success message appears; check profile to verify payload presence.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Persistence]]
- [[xss]]

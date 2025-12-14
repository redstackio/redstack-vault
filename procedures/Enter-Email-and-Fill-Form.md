---
tags:
  - form-filling
  - web-interaction
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
updated_at: '2025-12-14T05:32:10.268Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 8d7cf51d-b2b4-4000-83a9-c7e62dcde675
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enter Email and Fill Form

## Summary

This procedure involves entering an email address and completing the request form fields to reach the upload stage in the DoD submission system.

## Description

After accessing the form, users must provide basic details to proceed. Fields include email and request specifics (redacted). This simulates a legitimate request, masking the malicious intent. The process is manual via browser and ensures the form is valid to unlock the upload tab.

## Requirements

1. Access to the loaded request form
2. A disposable email address for testing
3. Basic knowledge of form validation rules

## Defense

Defensive measures and detection strategies:

- Validate email formats and check against disposable lists
- Require CAPTCHA on form submission
- Monitor form completion rates for bots or anomalies

## Objectives

1. Authenticate the request minimally via email
2. Populate fields to enable file attachment
3. Avoid form rejection to proceed to upload

## Instructions

### Step 1: Enter Email

**Context**: Provide initial contact info to advance the form.

Fill the email field with a test address (e.g., test@example.com) and click 'Submit'.

> Expected output: Form advances to detailed fields without validation errors.

### Step 2: Complete Required Fields

**Context**: Fill all mandatory inputs to prepare for upload.

Enter details in fields like request type, description (redacted specifics).

> Expected output: Form indicates completeness, upload tab available.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[form-submission]]

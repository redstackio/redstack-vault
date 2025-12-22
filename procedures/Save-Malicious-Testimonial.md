---
tags:
  - persistence
  - storage
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
updated_at: '2025-12-14T03:15:35.357Z'
sub_techniques: []
id: f6bcd3b2-abce-4f79-a8de-7c0c9f52683a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Malicious-Testimonial

## Summary

This procedure submits the form containing the injected XSS payload, ensuring the malicious JavaScript is stored persistently in the Concrete CMS database.

## Description

Upon submission, Concrete CMS saves the unsanitized Bio/Quote content directly, allowing the payload to persist across sessions and execute when rendered. This step confirms the stored nature of the XSS in the PHP backend, affecting all users who view the testimonial page.

## Requirements

1. Completed form with payload in Bio/Quote field
2. Permissions to save testimonials
3. Active session in the CMS

## Defense

Defensive measures and detection strategies:

- Sanitize inputs before database storage (e.g., strip dangerous tags)
- Log form submissions for review of suspicious content
- Implement WAF rules to detect common XSS patterns in posts

## Objectives

1. Store the payload without alteration
2. Confirm persistence in the CMS
3. Enable execution for subsequent views

## Instructions

### Step 1: Complete Form

**Context**: Fill any mandatory fields to allow submission.

Add placeholder data to other fields like name or image if required.

> Form is ready for submission.

### Step 2: Submit and Save

**Context**: Persist the data to trigger storage vulnerability.

Click the 'Save' or 'Publish' button to submit the form.

> Success message appears; payload is now stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- persistence
- storage

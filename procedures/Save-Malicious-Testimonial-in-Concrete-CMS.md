---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
name: Save-Malicious-Testimonial-in-Concrete-CMS
tags:
  - xss
  - persistence
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.479Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Malicious-Testimonial-in-Concrete-CMS

## Summary

This procedure saves the injected XSS payload from the testimonial name field to the Concrete CMS database, ensuring persistence without output encoding or sanitization checks.

## Description

Upon form submission, Concrete CMS stores user input from the testimonial name directly into the backend database (typically MySQL via PHP), failing to escape HTML entities or JavaScript. This creates a stored vulnerability where the malicious code remains indefinitely, affecting any user who views the testimonial. The procedure assumes the prior injection step and targets PHP-based web environments. Outcomes include successful storage, enabling widespread execution on page renders.

## Requirements

1. Payload already entered in the testimonial form
2. Valid authenticated session with save permissions
3. No additional tools; uses standard form submission

## Defense

Defensive measures and detection strategies:

- Enforce server-side escaping (e.g., htmlspecialchars) before database insertion
- Audit database queries for unescaped inputs in testimonial tables
- Implement rate limiting on testimonial creations to detect abuse

## Objectives

1. Persist the payload server-side for ongoing availability
2. Confirm no submission-time validation blocks the save
3. Set up for multi-user impact via viewing

## Instructions

### Step 1: Complete Form Fields

**Context**: Fill any remaining required fields to allow submission.

Add placeholder content to other fields like description or image if mandatory, ensuring the name field retains the payload.

### Step 2: Submit the Form

**Context**: Trigger the save action to store the data.

Click the 'Save' or 'Submit' button on the testimonial form. The PHP backend processes the POST request without sanitizing the name.

> The request payload includes the unsanitized name, which is inserted into the database testimonial record.

### Step 3: Verify Save

**Context**: Check for successful persistence.

Look for a success message or redirect to the testimonials list. Optionally, query the database if accessible to confirm raw payload storage.

> Expected: No errors; testimonial listed with injected name.

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
- [[Persistence]]

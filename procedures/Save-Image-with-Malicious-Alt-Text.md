---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - persistence
  - concrete-cms
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
updated_at: '2025-12-14T03:15:35.402Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Image-with-Malicious-Alt-Text

## Summary

This procedure saves the image with the injected XSS payload in the alt text, ensuring the malicious code is persistently stored in the Concrete CMS database without sanitization.

## Description

Upon saving, Concrete CMS stores the alt text directly into the database, bypassing any output escaping. This creates a stored XSS vulnerability where the payload remains dormant until rendered in HTML. The procedure relies on the previous injection step and confirms persistence via media library inspection or database queries.

## Requirements

1. Payload already entered in alt text from prior step
2. Permissions to save images in Concrete CMS
3. Access to verify storage (e.g., via admin panel)

## Defense

Defensive measures and detection strategies:

- Enforce server-side sanitization before database insertion
- Audit alt text content for script tags or event handlers
- Implement database triggers to flag suspicious inputs

## Objectives

1. Persist the XSS payload in the CMS database
2. Ensure no sanitization occurs during save
3. Set up for multi-user exposure

## Instructions

### Step 1: Complete Upload/Edit Form

**Context**: Finalize the image properties with the malicious alt text in place.

**Action** (Form Submission):

Select or upload the image file, ensure alt text contains the payload, and click 'Save' or 'Upload'.

> The system processes the request and stores the data. Expected output: Success message and image added to library.

### Step 2: Verify Persistence

**Context**: Confirm the payload is stored unaltered.

**Action** (Inspection):

Navigate to the media library, edit the image, and check the alt text field. Alternatively, inspect the database (e.g., via phpMyAdmin) for the unescaped payload.

> Reference attachments conalt1.png (upload view) and conalt2.png (stored view) for visual confirmation. Expected output: Payload visible and intact.

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
- [[concrete-cms]]

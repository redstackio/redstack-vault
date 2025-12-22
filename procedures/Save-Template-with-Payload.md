---
tags:
  - xss
  - persistence
  - storage
type: procedure
tools:
  - '[[tools/Summernote-JS]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ad250a50-1025-4322-95e1-21dc41b1c472
created_at: '2025-12-13T23:55:20.627Z'
updated_at: '2025-12-13T23:55:20.627Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Template-with-Payload

## Summary

This procedure saves the modified email template, ensuring the XSS payload is stored persistently in the Judge.me backend.

## Description

Saving commits the unsanitized HTML to the database, making the XSS stored. The root cause is the Summernote bug allowing unsafe data in responses. This affects any user viewing the template in Shopify.

## Requirements

1. Template with injected payload open
2. Save permissions in Judge.me
3. Valid session

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all saved template content server-side
- Audit stored templates for malicious scripts periodically
- Implement versioning to rollback suspicious changes

## Objectives

1. Persist the payload without sanitization
2. Confirm retention on reload
3. Enable triggering in subsequent views

## Instructions

### Step 1: Commit Changes

**Context**: Store the template.

No command required; UI save:

- Click "Save" or "Publish Template".

> Expected output: Success message; reload template to verify link intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Summernote-JS]]

## Tags

- [[xss]]
- [[Persistence]]
- [[storage]]

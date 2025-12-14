---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - persistence
  - cms-exploit
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
updated_at: '2025-12-14T03:15:35.321Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Malicious-Changes-to-Blog-Page-Tile

## Summary

This procedure covers submitting the form to store the injected XSS payload in the Concrete CMS database, leveraging the absence of validation to achieve persistence.

## Description

Upon form submission, Concrete CMS saves the Custom Title Text directly to the database without sanitizing or escaping the content. This stored payload will then be rendered unescaped on the blog page, executing JavaScript for any viewer in this web-based PHP application.

## Requirements

1. Payload already entered in the Custom Title Text field.
2. Valid session as admin to authorize the save operation.
3. No WAF or backend validation intercepting the request.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all form submissions server-side before database insertion.
- Log and audit all admin form submissions for suspicious content patterns.

## Objectives

1. Submit the form to persist the payload.
2. Confirm storage without errors.
3. Enable the payload for later triggering.

## Instructions

### Step 1: Review and Submit Form

**Context**: Ensure the payload is in place and submit to store it.

Click the "Save" or "Update Tile" button on the editing form.

> The CMS processes the request and returns a success message, storing the malicious title in the database.

### Step 2: Verify Storage (Optional)

**Context**: Check if the changes are reflected in the dashboard.

Refresh the tile preview or dashboard listing to see the updated title (payload may display as text).

> Updated tile configuration visible, confirming persistence.

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
- [[cms-exploit]]

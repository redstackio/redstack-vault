---
id: proc-uuid-4
tags:
  - xss
  - payload-storage
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
updated_at: '2025-12-14T03:15:52.962Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-XSS-Payload-in-Account-Settings

## Summary

This procedure submits the form to persist the injected javascript: payload in the Shopify partner account profile, making it available for rendering as a clickable link.

## Description

Upon submission, the server stores the unsanitized input, rendering it later in account views as a hyperlink. This stored nature allows the XSS to affect any viewer clicking the link, such as admins or other partners. The process occurs in the web app environment post-authentication, with success indicated by no validation rejections.

## Requirements

1. Payload entered in edit form
2. Valid session
3. Form submission capability

## Defense

Defensive measures and detection strategies:

- Server-side validation to reject non-http/https URLs
- Audit logs for profile changes with suspicious content

## Objectives

1. Persist the malicious URL server-side
2. Confirm storage without sanitization
3. Enable cross-user impact

## Instructions

### Step 1: Submit Form

**Context**: Save the changes to store the payload.

No specific command; click the submit button on the edit form.

> Expect a success message; the payload is now stored in the account data.

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
- [[payload-storage]]

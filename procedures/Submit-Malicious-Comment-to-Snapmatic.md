---
id: proc-uuid-12346
name: Submit-Malicious-Comment-to-Snapmatic
tags:
  - xss
  - injection
  - ugc
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
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.599Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Malicious-Comment-to-Snapmatic

## Summary

This procedure injects a crafted XSS payload into Snapmatic's comment system on a UGC platform, storing it persistently for execution on subsequent views.

## Description

Snapmatic allows user comments on shared content, but due to filter inconsistencies, full-width bracket payloads are stored without sanitization. Once submitted, the comment is rendered for all viewers, triggering the XSS. This requires a valid account but no elevated privileges.

## Requirements

1. Logged-in user account on the Rockstar Games platform
2. Access to a Snapmatic UGC item (e.g., a shared photo)
3. Crafted payload from prior procedure

## Defense

Defensive measures and detection strategies:

- Server-side validation of all inputs, including Unicode normalization
- Content Security Policy (CSP) to block inline scripts
- Rate limiting on comment submissions and logging of suspicious inputs

## Objectives

1. Successfully store the payload without rejection
2. Ensure persistence across sessions
3. Confirm storage via page inspection

## Instructions

### Step 1: Navigate to Target UGC

**Context**: Locate a commentable item to inject the payload.

Log in to the platform, go to Snapmatic, and select a photo or gallery that accepts comments.

> Ensure you're authenticated; anonymous comments may be restricted.

### Step 2: Input and Submit Payload

**Context**: Enter the full-width XSS payload into the comment field.

Paste the payload (e.g., `＜script＞alert('XSS')＜/script＞`) into the comment box and click submit.

> The submission should succeed without errors if the bypass works.

### Step 3: Verify Storage

**Context**: Check that the comment is saved and visible.

Refresh the page or view the UGC item; the comment should appear in the list.

> Inspect element to see if the payload is stored as-is in the HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[stored-xss]]
- [[comment-injection]]

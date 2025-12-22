---
tags:
  - page-persistence
  - storage
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:26.682Z'
sub_techniques: []
id: c3c1084a-5ec4-4cd7-b7a3-d383df05b182
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Malicious-Wiki-Page

## Summary

This procedure covers submitting the edited wiki page to store the injected XSS payload on the server, making it available for later execution.

## Description

After payload insertion, saving the page commits the malicious content to the backend without validation, exploiting the stored nature of the vulnerability. This step is crucial for persistence in the attack chain, targeting the TopCoder wiki's lack of server-side checks. Expected results include the payload being retrievable in subsequent edits, leading to execution in victims' browsers.

## Requirements

1. Loaded wiki editor with modified content
2. No client-side validation blocking the save
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Server-side validation of all editable content for script patterns
- Audit trails for page saves with content diffing
- Rate limiting on edits to prevent abuse

## Objectives

1. Persist the unsanitized payload in wiki storage
2. Avoid save-time detection or errors
3. Confirm storage via read-mode preview

## Instructions

### Step 1: Submit Changes

**Context**: Use the editor's save function to store the content.

No specific command; click the submit button in the UI.

> Expected output: Success message or redirect to the saved page.

### Step 2: Validate Storage

**Context**: Reload the page in read mode to ensure payload is stored.

No specific command; navigate to view mode.

> Check if the vote macro and text appear intact without execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Persistence]]
- [[web]]

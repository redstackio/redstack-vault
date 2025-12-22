---
tags:
  - storage
  - xss
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 7c27de53-9182-4f4f-8f2d-131b6afcf827
created_at: '2025-12-14T17:32:01.954Z'
updated_at: '2025-12-14T17:32:01.954Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Generate-Key-to-Store-Payload

## Summary

This procedure submits the form to generate the API key, storing the malicious payload on the server without sanitization.

## Description

Clicking 'Generate Key' sends the payload to the backend, where lack of validation persists it. This creates a stored XSS in the web application's wallet settings.

## Requirements

1. Payload injected in form
2. Authenticated session active
3. No server-side blocks

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all form submissions server-side
- Scan stored data for malicious patterns

## Objectives

1. Persist the payload in storage
2. Create the API key with tainted name
3. Enable reflection on reload

## Instructions

### Step 1: Review Form

**Context**: Ensure payload is set.

**Action**: Double-check the name field contains the payload.

> Confirm before proceeding.

### Step 2: Submit Generation

**Context**: Trigger backend storage.

**Action**: Click the 'Generate Key' button.

> The server processes and stores the unsanitized data, returning the key.

### Step 3: Confirm Storage

**Context**: Verify key creation.

**Action**: Note the success message and check if the key appears in the list.

> Payload should be visible in the key name.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[storage]]
- [[xss]]
- [[web]]

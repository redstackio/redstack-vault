---
tags:
  - xss-verification
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
updated_at: '2025-12-14T03:15:53.032Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
id: 06a78c79-ff04-40dc-8870-6caf051b9aad
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Generate-Key-and-Verify-Stored-XSS

## Summary

This procedure submits the injected payload to generate the API key, stores it server-side without sanitization, and verifies XSS execution by re-viewing the wallet settings, where the HTML renders as executable.

## Description

In vulnerable web wallet systems, submitting the form stores the unsanitized key name, leading to reflected HTML upon page reload. This confirms the stored XSS for the owner, with potential for JavaScript if filters are bypassed. Requires prior payload injection; outcomes include visual confirmation of execution.

## Requirements

1. Payload already entered in the API key name field
2. Authenticated session with wallet access
3. Ability to reload and view settings page

## Defense

Defensive measures and detection strategies:

- Sanitize all stored inputs with HTML escaping (e.g., via libraries like DOMPurify)
- Implement Content Security Policy (CSP) to block inline scripts
- Audit rendered content in wallet views for anomalies

## Objectives

1. Persist the XSS payload server-side
2. Trigger execution in the browser
3. Confirm vulnerability impact

## Instructions

### Step 1: Submit Form to Generate Key

**Context**: Press the generation button to store the payload with the new API key.

**Action**:
- Click 'Generate Key' on the form.
- Wait for confirmation of key creation.

> Expected output: Success message with the new key details, including the payload-laden name.

### Step 2: Reopen Settings to Observe XSS

**Context**: Refresh or reopen the wallet settings to load the stored keys list and execute the payload.

**Action**:
- Navigate back to the wallet settings page.
- Locate the list of API keys.

> The injected `<a href="example.com">asdf</a>` should appear as a clickable link, not plain text, indicating successful XSS rendering.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-verification]]
- [[payload-storage]]

---
tags:
  - xss
  - persistence
  - save-config
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
updated_at: '2025-12-13T23:52:39.111Z'
sub_techniques: []
id: 68668621-1f6a-44a0-83a1-1c30b6b0df4e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Configuration-to-Store-XSS-Payload

## Summary

This procedure saves the injected payload in the Algolia explorer configuration, storing it server-side without sanitization and enabling persistence for future page visits.

## Description

Upon clicking save, the unsanitized input from the 'Attributes to index' field is persisted in the backend, likely in a user-specific or shared configuration store. This stored value is then rendered back into the HTML on page reloads or revisits, triggering the XSS. The attack relies on the absence of server-side escaping, leading to arbitrary code execution for any user loading the affected index configuration.

## Requirements

1. Payload already injected in the previous step
2. Visible 'Save' button in the UI
3. Stable internet connection for the save request

## Defense

Defensive measures and detection strategies:

- Validate and sanitize inputs on the server before storage
- Use parameterized queries or escaping libraries for configuration persistence
- Monitor save operations for anomalous payloads via WAF rules

## Objectives

1. Persist the malicious input server-side
2. Ensure no errors occur during save
3. Confirm payload retention post-save

## Instructions

### Step 1: Locate Save Button

**Context**: Find the UI element to commit the configuration changes.

**Action**:

Look for the 'Save' button, typically at the bottom or top of the ranking tab form.

> Ensure the form indicates unsaved changes if applicable.

### Step 2: Execute Save

**Context**: Submit the form to store the payload.

**Action**:

Click the 'Save' button to persist the configuration.

> The page may reload or show a success message; verify the payload remains in the field.

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
- [[save-config]]

---
id: proc-persist-xss-config
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
updated_at: '2025-12-14T03:15:35.571Z'
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
# Persist XSS Payload by Saving Search Configuration

## Summary

This procedure saves the injected XSS payload in the Concrete CMS search configuration, ensuring it is stored persistently in the backend for later execution when the search results page is viewed.

## Description

After injection, submitting the search configuration form stores the tainted title in the database or config files without encoding. This creates a stored XSS vector where the payload survives across sessions and affects multiple users. The procedure assumes the payload from the prior injection step and focuses on the save action, which lacks output escaping on storage.

## Requirements

1. Payload already injected in the title field
2. Valid session in Concrete CMS
3. Access to submit forms in the admin panel

## Defense

Defensive measures and detection strategies:

- Enforce output encoding on all stored data before database insertion
- Audit configuration changes for anomalous content (e.g., via WAF rules)
- Regular scans for stored XSS in CMS plugins and core features

## Objectives

1. Store the unsanitized payload persistently
2. Confirm save without triggering premature execution
3. Enable cross-user impact on search page renders

## Instructions

### Step 1: Submit Configuration Form

**Context**: With the payload in the title field, locate and click the save or submit button to persist the changes.

No command required; interact with the form UI.

> Expected: CMS displays a success message, and the configuration is updated in the backend.

### Step 2: Verify Persistence

**Context**: Optionally, refresh the configuration page to check if the payload remains intact.

Reload the search config page and inspect the title field.

> Expected output: Payload is reloaded and displayed as entered, confirming storage without sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- persistence

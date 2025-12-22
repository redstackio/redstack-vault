---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Modify-File-Properties-Title-with-XSS-Payload
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.477Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - stored-xss
  - file-properties
platforms:
  - Web
commands: []
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Modify-File-Properties-Title-with-XSS-Payload

## Summary

This procedure targets the file properties editing feature in Concrete CMS 5.7.2.1 to inject a stored XSS payload into the title field, persisting JavaScript that executes when victims view the properties or related pages.

## Description

The properties editing interface in Concrete CMS fails to sanitize title inputs adequately, allowing HTML and JavaScript injection. This vulnerability complements filename-based attacks and evades the incomplete sanitization from version 5.7.0.4. When another user opens the properties page, the unsanitized title renders the payload, executing in their browser context for potential data theft.

## Requirements

1. Authenticated access with permissions to edit file properties
2. An existing file in the manager (e.g., from prior upload)
3. Web browser for editing

## Defense

Defensive measures and detection strategies:

- Sanitize all editable metadata fields with HTML entity encoding
- Audit file properties changes for anomalous content
- Deploy WAF rules to block script tags in POST requests to properties endpoints

## Objectives

1. Inject XSS into file metadata without detection
2. Persist the payload for cross-user execution
3. Validate injection success via page inspection

## Instructions

### Step 1: Access File Properties

**Context**: Locate the target file and open its editable properties.

In File Manager, right-click or select the file and choose 'Properties'.

> Ensure the title field is editable and free of prior sanitization.

### Step 2: Inject and Save Payload

**Context**: Enter a JavaScript payload in the title, such as an SVG element that loads and executes code.

Set title to `<svg onload=confirm(document.cookie)>` and save.

> After saving, refresh the properties page to confirm the payload is stored and not escaped.

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
- [[stored-xss]]
- [[file-properties]]

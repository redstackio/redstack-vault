---
id: proc-uuid-002
name: Test-Unsanitized-HTML-Injection
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:21.072Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - injection
  - html
  - xss-test
platforms:
  - Web
  - Browser Extension
tools:
  - '[[tools/Awesome-Autocomplete-Extension]]'
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Test-Unsanitized-HTML-Injection

## Summary

This procedure tests the extension's failure to sanitize HTML in search queries, using a basic payload to break out of HTML tags and trigger erroneous resource loads, confirming the injection vector.

## Description

By entering a payload like `'><img src=x onerror=alert(1)>` in the GitHub search bar, the extension fetches Algolia-indexed results and inserts them unsanitized into the DOM. This leads to malformed elements and failed network requests, proving the lack of escaping for user-controlled fields like repository names.

## Requirements

1. Awesome Autocomplete extension installed and enabled
2. Access to GitHub.com search
3. Basic understanding of HTML payloads

## Defense

Defensive measures and detection strategies:

- Implement HTML entity encoding for all user inputs before DOM insertion
- Use libraries like DOMPurify for sanitization in extensions
- Audit extension updates for security fixes

## Objectives

1. Inject HTML-breaking payload to disrupt rendering
2. Observe broken elements in autocomplete dropdown
3. Validate the unsanitization root cause

## Instructions

### Step 1: Enter Payload

**Context**: Craft and input a simple HTML injection payload to test sanitization.

In the GitHub search bar, type: `'><img src=x onerror=alert(1)>`

```html
'><img src=x onerror=alert(1)>
```

> The autocomplete will render results, inserting the payload and causing a broken <img> tag.

### Step 2: Trigger Autocomplete

**Context**: Force the extension to fetch and display results with the injected content.

Press Enter or wait for suggestions; the extension pulls from Algolia and renders without escaping.

> Expect visible breakage in the dropdown UI and network errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Awesome-Autocomplete-Extension]]

## Tags

- [[injection]]
- [[html]]

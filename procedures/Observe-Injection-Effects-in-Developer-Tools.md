---
id: proc-uuid-003
name: Observe-Injection-Effects-in-Developer-Tools
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:21.070Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - observation
  - dev-tools
  - dom-inspection
platforms:
  - Web
  - Browser Extension
tools:
  - '[[tools/Browser-Developer-Tools]]'
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Observe-Injection-Effects-in-Developer-Tools

## Summary

This procedure uses browser developer tools to inspect the DOM and network activity, confirming the injection of unsanitized HTML from the extension's rendering of GitHub search results.

## Description

After injecting a payload, developer tools reveal the exact DOM insertion of malicious elements like `<img src=x onerror=>` in the GitHub.com context, along with failed requests, validating the XSS vector without full execution.

## Requirements

1. Payload injection completed from prior step
2. Browser with developer tools (F12 key)
3. GitHub search active with extension

## Defense

Defensive measures and detection strategies:

- Enable strict CSP headers on sites like GitHub to prevent DOM manipulations
- Log and alert on anomalous network requests from extensions
- Use browser extensions blockers or sandboxing

## Objectives

1. Inspect injected elements in the DOM tree
2. Monitor network tab for payload-induced errors
3. Confirm execution context is GitHub.com

## Instructions

### Step 1: Open Developer Tools

**Context**: Access inspection tools to analyze the page state post-injection.

Press F12 or right-click and select "Inspect" while the autocomplete dropdown is visible.

> Navigate to the Elements tab to view the live DOM.

### Step 2: Inspect DOM and Network

**Context**: Locate and examine the injected payload effects.

In Elements tab, search for `img src=x`; in Network tab, filter for failed loads to 'x'.

> The injected element should appear malformed, with onerror attribute partially rendered.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[observation]]
- [[dev-tools]]

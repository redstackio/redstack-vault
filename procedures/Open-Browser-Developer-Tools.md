---
tags:
  - xss
  - devtools
  - web
type: procedure
tools:
  - '[[tools/Browser-DevTools]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:26.516Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 38f34b57-6fba-4e53-85b4-9df25fc02bb4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Open Browser Developer Tools

## Summary

This procedure prepares the testing environment by accessing the browser's developer tools, enabling inspection and direct payload injection for XSS reproduction on Reddit.

## Description

Developer tools provide a console for executing JavaScript and inspecting DOM elements, crucial for manual XSS testing. In this scenario, opening the tools on Reddit's page allows preparation for injecting payloads that exploit insufficient sanitization in eval and Function contexts. Prerequisites include a loaded page; outcomes involve a ready console for safe payload testing without external dependencies.

## Requirements

1. Web browser with developer tools enabled (e.g., Chrome, Firefox)
2. Page already loaded from previous step
3. Basic familiarity with browser interfaces

## Defense

Defensive measures and detection strategies:

- Disable or monitor devtools usage via browser extensions or server-side logging
- Use anti-debugging techniques to detect tool activation

## Objectives

1. Enable script execution and inspection capabilities
2. Set up for payload delivery
3. Validate page structure for injection points

## Instructions

### Step 1: Access Developer Tools

**Context**: Invoke the tools to open the console.

No command; use keyboard shortcut or menu:

```plaintext
F12 or Right-click > Inspect > Console tab
```

> The panel opens; switch to Console for JS input. Ensure no errors in page load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-DevTools]]

## Tags

- [[xss]]
- [[devtools]]

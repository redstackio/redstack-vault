---
tags:
  - javascript
  - dom-manipulation
  - ui-reveal
type: procedure
tools:
  - '[[tools/Browser-Console]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/reveal-copilot-gui]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:25:48.181Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d555d099-a9b4-4237-9f8a-4c0fb09d7eb8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reveal-Hidden-Copilot-Interface

## Summary

This procedure uses JavaScript in the browser console to remove CSS classes hiding the unreleased HackerOne Copilot GUI, enabling interaction with the feature for vulnerability testing.

## Description

The HackerOne Copilot feature is hidden via 'hidden' and 'dark:text-white' classes on div elements. By executing a DOM manipulation script, the interface becomes visible, allowing creation of LLM conversations. This is a client-side technique requiring access to the opportunities page and is low-risk for detection as it only affects the local browser view. Prerequisites include a valid HackerOne session and developer tools enabled.

## Requirements

1. Access to https://hackerone.com/opportunities/all with a logged-in account
2. Browser with open developer console (e.g., Chrome DevTools)
3. No server-side changes; purely client-side

## Defense

Defensive measures and detection strategies:

- Obfuscate unreleased features more robustly (e.g., server-side rendering flags)
- Monitor for unusual client-side script executions via CSP or behavioral analytics
- Disable dev tools in production previews

## Objectives

1. Expose hidden UI for feature interaction
2. Enable subsequent steps in Copilot testing
3. Confirm visibility without breaking page functionality

## Instructions

### Step 1: Navigate and Open Console

**Context**: Load the page containing the hidden elements and prepare for script execution.

**Command** ([[commands/reveal-copilot-gui]]):
```javascript
document.querySelectorAll('div').forEach(e=>{ e.classList.remove('hidden'); e.classList.remove('dark:text-white'); });
```

> This script selects all divs and removes the specified classes, making hidden content visible. Expected output: Immediate UI changes in the browser; no console errors if successful.

### Step 2: Verify Visibility

**Context**: Inspect the page to ensure Copilot elements are now interactable.

No specific command; manually check for Copilot chat interface.

> Look for input fields or conversation starters. If not visible, refresh and re-run.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/reveal-copilot-gui]]

## Tools Used

- [[tools/Browser-Console]]

## Tags

- javascript
- dom-manipulation

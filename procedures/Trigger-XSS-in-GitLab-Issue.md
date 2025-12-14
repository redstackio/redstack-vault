---
tags:
  - xss
  - dom-xss
type: procedure
tools:
  - '[[tools/Mermaid]]'
  - '[[tools/Stylis]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6ab56171-dd09-4f49-bb0a-e3b49b35bc05
created_at: '2025-12-13T23:52:24.591Z'
updated_at: '2025-12-13T23:52:24.591Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-GitLab-Issue

## Summary

This procedure views a GitLab issue containing the injected Mermaid payload, triggering DOM XSS execution while noting initial CSP blocks.

## Description

Upon rendering, Mermaid uses Stylis to process directives into CSS, inserting the user-controlled string via innerHTML. This executes the injected JS in the DOM, but GitLab's CSP initially prevents it, requiring a bypass for full impact.

## Requirements

1. Access to the injected issue URL
2. Victim browser viewing the page
3. Developer tools for console inspection

## Defense

Defensive measures and detection strategies:

- Enforce CSP reporting to log violations
- Audit Mermaid rendering for injection patterns
- Limit directive usage in Markdown

## Objectives

1. Execute injected payload on render
2. Confirm XSS via console
3. Identify CSP limitations

## Instructions

### Step 1: Navigate to Issue

**Context**: Load the page to trigger rendering.

Open the issue URL in a browser.

### Step 2: Observe Rendering

**Context**: Mermaid processes and injects the payload.

Inspect the diagram; check browser console for errors.

### Step 3: Validate Injection

**Context**: Confirm DOM manipulation.

Look for attempted alert or img element in DOM; note CSP blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mermaid]]
- [[tools/Stylis]]

## Tags

- [[xss]]
- [[dom-xss]]

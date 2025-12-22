---
tags:
  - xss
  - execution
  - gitlab
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
updated_at: '2025-12-13T23:52:34.044Z'
skill_level: basic
impact_level: high
detection_risk: high
sub_techniques: []
id: b3cb8d5a-83e5-486f-ab91-01d8078dc120
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Issue

## Summary

This procedure triggers the stored XSS by loading the issue page, causing the injected payload to execute JavaScript in the viewer's browser.

## Description

Upon page load, the frontend renders the comment, processing gl-emoji which injects the onload payload, evading sanitization. This executes arbitrary JS, such as alerting the URL or stealing session data, impacting any authenticated user viewing the issue. It demonstrates the stored nature, affecting multiple victims without further interaction.

## Requirements

1. URL of the issue with injected payload
2. Victim browser (can be attacker's for testing)
3. No special permissions needed for viewing

## Defense

Defensive measures and detection strategies:

- Enable strict CSP headers to block inline JS
- Audit and sanitize rendered comments server-side
- Monitor browser consoles and network for anomalous script execution

## Objectives

1. Execute the stored JavaScript on page render
2. Verify impact like session data access
3. Demonstrate multi-user exploitation potential

## Instructions

### Step 1: Load Issue Page

**Context**: Access the page to initiate rendering and execution.

**Command** (UI action):

Navigate to the issue URL in a browser (e.g., http://gitlab.example.com/project/-/issues/1).

> Page loads; watch for automatic execution without user input.

### Step 2: Observe Execution

**Context**: Confirm JS runs via alert or console.

**Command** (UI action):

Open browser dev tools (F12) and refresh the page.

> Alert pops with document.location.href; console may log errors if any.

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
- execution
- gitlab

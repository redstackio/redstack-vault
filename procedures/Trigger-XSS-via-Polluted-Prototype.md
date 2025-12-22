---
id: proc-uuid-trigger-xss-pollution
tags:
  - xss
  - dom-xss
  - javascript
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
updated_at: '2025-12-13T23:56:04.019Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Polluted-Prototype

## Summary

This procedure triggers DOM-based XSS by visiting a URL that pollutes Object.prototype, which is then evaluated by a gadget in the Swiftype script's _convertStringHooksToFunctions method using eval().

## Description

After prototype pollution via the crafted URL, the script's _convertStringHooksToFunctions iterates over hooks and applies eval() to string values, executing the polluted payload (e.g., alert(document.domain)) in the browser context. This leads to arbitrary JS execution, potentially stealing cookies or session data on sites like https://blog.swiftype.com/. The attack requires no server-side changes and relies on client-side script behavior.

## Requirements

1. Crafted URL from prior procedure
2. Victim access to the target site via browser
3. Site must load the vulnerable st.js script

## Defense

Defensive measures and detection strategies:

- Avoid eval() on user-influenced data; use safer alternatives like Function() with restrictions
- Implement CSP to block inline scripts and eval()
- Audit third-party scripts for prototype pollution gadgets and update to patched versions

## Objectives

1. Execute arbitrary JavaScript in the victim's browser
2. Demonstrate impact like domain alerting or data exfiltration
3. Chain with social engineering for real-world delivery

## Instructions

### Step 1: Deliver and Navigate to URL

**Context**: Send the crafted URL to the victim (e.g., via email or link) and have them visit it.

Open https://blog.swiftype.com/#__proto__[asd]=alert(document.domain) in the browser.

**Expected Output**: Page loads with polluted prototype; no immediate visible change.

### Step 2: Confirm Pollution

**Context**: Verify Object.prototype has been altered by the deparam function.

In browser console: console.log(Object.prototype.asd) should return 'alert(document.domain)'.

**Expected Output**: Polluted property visible in console.

### Step 3: Trigger Gadget Execution

**Context**: Interact with the page to invoke _convertStringHooksToFunctions, which evaluates the polluted value.

The gadget triggers automatically on script execution or page interaction; observe for JS alert.

**Expected Output**: Alert box pops up with document.domain value.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dom-xss]]
- [[eval-exploitation]]

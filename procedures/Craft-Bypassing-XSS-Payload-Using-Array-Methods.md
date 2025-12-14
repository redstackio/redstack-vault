---
id: proc-uuid-2
tags:
  - xss
  - payload-crafting
  - filter-bypass
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
updated_at: '2025-12-13T23:52:33.931Z'
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
# Craft Bypassing XSS Payload Using Array Methods

## Summary

This procedure details the creation of an XSS payload that circumvents Glassdoor's filters blocking common JavaScript functions like alert and confirm by leveraging the cookie object's array-like properties and the .find() method to indirectly execute code.

## Description

After identifying the reflection point, filters prevent direct use of alert or confirm. This procedure involves iterative testing to find a bypass using [cookie].find(confirm), which treats cookie as an array and applies find, effectively calling confirm(cookie). The full payload closes the href attribute and injects a <marquee> tag with an onstart event. Requires browser console for testing and understanding of JS filter evasion.

## Requirements

1. Confirmed vulnerable endpoint from prior identification
2. Browser with JS console for payload testing
3. List of blocked functions (alert, confirm, write, prompt)

## Defense

Defensive measures and detection strategies:

- Blacklist array methods like .find() in addition to direct functions
- Use WAF rules to detect event handlers in injected tags (e.g., onstart)
- Sanitize inputs to prevent attribute breakout entirely

## Objectives

1. Develop a payload that executes without triggering filters
2. Ensure payload retrieves sensitive data like cookies
3. Test for reliable execution in the target context

## Instructions

### Step 1: Analyze Filters

**Context**: Identify blocked functions through trial and error in form submissions.

Submit payloads with alert('test') and observe blocks; note that array methods are unblocked.

### Step 2: Construct Bypass

**Context**: Build the payload using cookie as an iterable to invoke confirm.

Combine tag closure '> with <marquee onstart="[cookie].find(confirm)"> to inject and execute.

```javascript
// Test in console: [cookie].find(confirm) evaluates to confirm(cookie)
```

> This pops a dialog with cookie value, confirming bypass.

### Step 3: Full Payload Assembly

**Context**: Integrate into locationId for complete injection.

Set locationId to '><marquee onstart="[cookie].find(confirm)">' and submit to verify execution.

**Expected Output**: Marquee tag appears in DOM, onstart fires, and confirm dialog shows cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-bypass]]
- [[JavaScript]]

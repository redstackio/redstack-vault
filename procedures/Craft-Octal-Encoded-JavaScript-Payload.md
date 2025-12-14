---
id: proc-uuid-004
tags:
  - xss
  - payload-crafting
  - octal-encoding
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.614Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Octal-Encoded-JavaScript-Payload

## Summary

This procedure develops a JavaScript payload using octal escapes to represent strings without alphabetic characters, bypassing the uppercase filter while maintaining functionality for XSS execution.

## Description

Leveraging ISO-8859-1 octal values (e.g., \141 for 'a', \154 for 'l'), construct a filter-resistant payload like []['\146\151\154\164\145\162']['\143\157\156\163\164\162\165\143\164\157\162']('\141\154\145\162\164\50\61\51')() to invoke alert(1). Uppercasing backslashes and numbers does not alter octal interpretation. Test locally before injection.

## Requirements

1. Knowledge of JavaScript octal escapes
2. Reference to character encoding tables
3. Local JS environment for validation

## Defense

Defensive measures and detection strategies:

- Normalize and decode inputs before filtering
- Block or decode octal/hex escapes in user input
- Use strict CSP to prevent eval-like constructions

## Objectives

1. Create a payload immune to uppercase conversion
2. Validate execution in a controlled JS context
3. Prepare for injection into the serial parameter

## Instructions

### Step 1: Map Characters to Octal

**Context**: Convert JS keywords to octal sequences.

Reference table: 'f'=\146, 'i'=\151, etc.

> Build string: '\146\151\154\164\145\162' for 'filter'.

### Step 2: Construct Full Payload

**Context**: Assemble into executable JS.

Use [[tools/Browser]] console to test:

```javascript
[]['\146\151\154\164\145\162']['\143\157\156\163\164\162\165\143\164\157\162']('\141\154\145\162\164\50\61\51')();
```

> Expect alert(1) to pop up, confirming validity.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- [[xss]]
- [[payload-crafting]]
- [[octal-encoding]]

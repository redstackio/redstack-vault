---
id: proc-uuid-3
tags:
  - bypass
  - javascript
  - es6
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
updated_at: '2025-12-13T23:52:55.636Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass Illegal Character Blacklist with ES6 Backticks

## Summary

This procedure injects a JavaScript payload into the SWF's flashVars that evades the character blacklist by using ES6 template literal backticks, allowing code execution without forbidden delimiters like parentheses or braces.

## Description

The SWF blacklists characters in flashVars values (e.g., '(', ')', '{', ';') to prevent JS execution via ExternalInterface.call('jsinitfunction', payload). ES6 backticks (`) for template literals are overlooked, enabling payloads like 'alert`1`' to run as JS. This builds on GET bypass. Target: Browsers supporting ES6. Prerequisites: Parameter persistence. Outcome: Blacklist-evading payload ready for execution.

## Requirements

1. Modern browser with ES6 support
2. Payload value for jsinitfunction param
3. Prior GET bypass confirmed

## Defense

Defensive measures and detection strategies:

- Expand blacklist to include backticks and other ES6 syntax
- Sanitize all flashVars values server-side
- Disable Flash entirely or use HTML5 alternatives

## Objectives

1. Inject executable JS without blacklist triggers
2. Prepare payload for ExternalInterface execution
3. Maintain stealth in payload construction

## Instructions

### Step 1: Design Payload with Backticks

**Context**: Create JS that uses template literals to avoid blacklisted chars.

Payload: alert`1`

**Expected Output**: Valid JS expression: alert('1')

### Step 2: Integrate into Parameter Value

**Context**: Assign to bypassed param.

URL fragment: jsinitfunctio%gn=alert`1`

> Encodes to %61%6c%65%72%74%601%60 for transport.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bypass]]
- [[es6]]

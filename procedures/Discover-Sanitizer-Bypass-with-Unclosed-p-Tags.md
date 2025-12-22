---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - xss
  - parser-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:20.932Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover-Sanitizer-Bypass-with-Unclosed-p-Tags

## Summary

This procedure tests the HTML sanitizer's parser for confusion using multiple unclosed <p> tags, revealing a bypass that allows injection of unauthorized HTML in MercadoLibre's messaging.

## Description

HTML parsers can be tricked by unbalanced tags, leading to incomplete sanitization. In this scenario, sending payloads with eight or more unclosed <p> tags (e.g., <p><p><p><p><p><p><p><p>) overwhelms the parser, permitting extra tags to be appended and rendered. This is tested in the messaging system, where the payload is stored and viewed by recipients. Prerequisites include prior sanitizer analysis; outcomes include proof-of-concept bypass confirmation.

## Requirements

1. Knowledge of allowed tags from prior analysis.
2. Access to send and receive messages.
3. Browser tools for HTML inspection.

## Defense

Defensive measures and detection strategies:

- Use robust parsers like DOMPurify that handle unbalanced tags.
- Validate input length and tag balance server-side.
- Log and alert on payloads with excessive repeated tags.

## Objectives

1. Confirm parser vulnerability to unclosed tags.
2. Determine minimum number of <p> tags needed for bypass.
3. Prepare for payload crafting.

## Instructions

### Step 1: Prepare Test Payloads

**Context**: Create variations with increasing unclosed <p> tags.

Draft payloads starting with 4 <p> tags up to 10, e.g., <p><p><p><p> followed by a test tag like <div>Test</div>.

### Step 2: Submit and Inspect

**Context**: Send payloads and check rendering.

Submit via messaging, then inspect the stored message's HTML in the recipient view. Look for the test tag appearing unfiltered.

> With 8+ <p> tags, the parser fails to close them properly, allowing <div> to render.

### Step 3: Iterate and Confirm

**Context**: Refine based on results.

Adjust tag count until bypass occurs consistently.

**Expected Output**: Unauthorized tag visible in DOM.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[parser-bypass]]

---
id: proc-vk-senddata-analyze-001
tags:
  - function-analysis
  - ua-detection
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-13T23:52:34.014Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify-SendData-Function-Limitations

## Summary

This procedure analyzes the sendData function's behavior in VK.com's upload JS, focusing on XMLHttpRequest POST handling, mobile UA skips, and eval on responses.

## Description

sendData constructs a POST to a URL with dataUrl parameter using XMLHttpRequest; it skips execution for mobile UAs matching /iphone|ipod|ipad|opera mini|opera mobi/i due to undefined ajx2q; successful responses are passed directly to eval, enabling XSS if controllable.

## Requirements

1. JS code from upload endpoint
2. Regex testing tools for UA patterns
3. Understanding of XHR flows

## Defense

Defensive measures and detection strategies:

- Validate all XHR responses before eval
- User-agent consistency checks

## Objectives

1. Map POST construction and dataUrl usage
2. Identify mobile skip logic
3. Confirm eval on response

## Instructions

### Step 1: Examine XHR Usage

**Context**: Understand POST to manipulated URL.

Review sendData code: var xhr = new XMLHttpRequest(); xhr.open('POST', url, true); xhr.send('dataUrl=' + encodeURIComponent(data));

> Expected output: Confirmation of dataUrl parameter injection.

### Step 2: Check UA Skip

**Context**: Note mobile bypass.

Locate if (/iphone|ipod|ipad|opera mini|opera mobi/i.test(navigator.userAgent)) { return; } due to ajx2q undefined.

> Expected output: Non-mobile UAs proceed to eval.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- function-analysis
- ua-detection

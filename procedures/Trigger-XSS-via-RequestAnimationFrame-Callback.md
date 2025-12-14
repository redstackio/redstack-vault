---
id: proc-vk-xss-trigger-001
tags:
  - xss-trigger
  - callback-abuse
  - js-execution
type: procedure
tools:
  - '[[tools/imagejs]]'
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:33.995Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Trigger-XSS-via-RequestAnimationFrame-Callback

## Summary

This procedure sets the callback parameter to requestAnimationFrame and triggers an upload of the malicious proxied image, leading to eval execution of embedded JS in non-mobile browsers.

## Description

Modify the upload request's callback to 'requestAnimationFrame', use the valid hash and proxy to POST the JS-embedded image, resulting in parent.requestAnimationFrame(function() { ... }) where the response is evaluated, executing arbitrary code like alert(document.cookie) for session hijacking.

## Requirements

1. Malicious image from prior step
2. Valid proxy hash
3. Non-mobile UA
4. Upload initiation capability

## Defense

Defensive measures and detection strategies:

- Ban eval entirely
- Validate callback to known functions only
- Inspect proxied responses

## Objectives

1. Set callback to global function
2. Trigger POST with malicious payload
3. Achieve JS execution

## Instructions

### Step 1: Modify Callback Parameter

**Context**: Abuse regex by using existing global name.

In upload URL, set callback=requestAnimationFrame.

> Expected output: Callback passes validation as alphanumeric.

### Step 2: Initiate Upload

**Context**: Proxy and POST the image.

Trigger graffiti upload with proxied malicious.gif URL, using generated hash.

> Expected output: Eval executes JS, popping alert(document.cookie).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/imagejs]]

## Tags

- xss-trigger
- callback-abuse
- js-execution

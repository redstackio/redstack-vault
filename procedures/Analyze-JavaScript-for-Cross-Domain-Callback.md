---
id: proc-vk-js-analyze-001
tags:
  - js-analysis
  - cross-domain
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
updated_at: '2025-12-13T23:52:34.018Z'
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
# Analyze-JavaScript-for-Cross-Domain-Callback

## Summary

This procedure dissects the JavaScript code in VK.com's upload handler to understand cross-domain setup and callback invocation, identifying the regex-limited callback parameter.

## Description

The JS sets document.domain for cross-domain execution and calls parent.{callback value} with an anonymous function invoking sendData to a manipulated URL. The callback is restricted to /^[a-zA-Z0-9]*$/ pattern, limiting direct abuse but allowing global function hijacking.

## Requirements

1. Captured JS from upload endpoint
2. Browser or text editor for code review
3. Knowledge of JavaScript eval patterns

## Defense

Defensive measures and detection strategies:

- Avoid eval on user-controlled inputs
- Enforce strict domain policies

## Objectives

1. Confirm cross-domain document.domain usage
2. Map callback invocation flow
3. Note regex limitations

## Instructions

### Step 1: Review Document Domain Setup

**Context**: Identify cross-domain facilitation.

Locate document.domain = 'vk.com'; in the JS code.

> Expected output: Confirmation of domain relaxation for iframe communication.

### Step 2: Trace Callback Call

**Context**: Follow parent.{callback} invocation.

Examine the line: parent.{callback value}(function() { sendData('/c415824/upload.php?transport=iframe&act=add_doc&hash=...&pda=', data); });

> Expected output: Understanding of POST trigger via anonymous function.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- js-analysis
- cross-domain

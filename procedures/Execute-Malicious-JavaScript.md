---
tags:
  - xss
  - javascript
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
detection_risk: high
sub_techniques: []
id: d6a273a9-10f0-4637-b02f-1bb8edeae628
created_at: '2025-12-14T00:11:16.399Z'
updated_at: '2025-12-14T00:11:16.399Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute Malicious JavaScript

## Summary

This procedure triggers the execution of the injected JavaScript by interacting with the malicious link in Reddit's post editor.

## Description

Clicking the link in the editing interface executes the JavaScript in the page's context, potentially allowing cookie theft or other actions. This demonstrates the XSS impact, limited to the editing page but exploitable against admins.

## Requirements

1. Modified post loaded in editor
2. Browser that allows JavaScript execution on clicks
3. Understanding of XSS payloads

## Defense

Defensive measures and detection strategies:

- Filter out 'javascript:' schemes server-side
- Monitor for anomalous JavaScript execution in logs

## Objectives

1. Trigger the payload
2. Observe execution effects
3. Demonstrate potential for further compromise

## Instructions

### Step 1: Locate Malicious Link

**Context**: Identify the injected link in the editor.

In the RichText editor, find the hyperlink that was modified to 'javascript:' scheme.

### Step 2: Click to Execute

**Context**: Interact with the link to run the script.

Click the link (or use middle-click/CMD+click) to execute the payload, such as alerting document cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xss
- javascript

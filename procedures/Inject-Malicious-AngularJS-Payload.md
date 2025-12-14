---
tags:
  - xss-injection
  - angularjs
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
id: 1b64080d-3d70-4b60-ba8b-da44c9f28e63
created_at: '2025-12-13T23:56:20.321Z'
updated_at: '2025-12-13T23:56:20.321Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Malicious AngularJS Payload

## Summary

This procedure inserts a malicious AngularJS expression into the suggested edits interface of uber.readme.io, exploiting a stored XSS vulnerability to store executable JavaScript.

## Description

The payload is added to the document content and submitted as a suggestion, which is stored and later rendered without proper sanitization. This targets AngularJS environments lacking ng-nonbindable protections, leading to arbitrary code execution when viewed.

## Requirements

1. Access to the suggested edits page.
2. Knowledge of AngularJS expression injection techniques.
3. Valid session for submission.

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and escaping for user content.
- Use ng-nonbindable for dynamic content rendering.

## Objectives

1. Store the malicious payload in the system.
2. Queue it for admin review.
3. Enable persistent XSS.

## Instructions

### Step 1: Insert and Submit Payload

**Context**: Add the payload to the edit form.

Insert '{{(_="".sub).call.call({}[$="constructor"].getOwnPropertyDescriptor(_.__proto__,$).value,0,"alert(1)")()}}' into the document, provide a description, and submit.

> This submits the suggestion containing the XSS payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xss-injection
- angularjs

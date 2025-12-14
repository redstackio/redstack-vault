---
tags:
  - csp-bypass
  - angularjs
type: procedure
tools:
  - '[[tools/Browser]]'
  - '[[tools/AngularJS]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: dffd3cda-dc93-4c09-aac8-c0000e02a6db
created_at: '2025-12-13T23:56:20.396Z'
updated_at: '2025-12-13T23:56:20.396Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass CSP with AngularJS

## Summary

This procedure bypasses Content Security Policy using AngularJS loaded in an injected iframe.

## Description

AngularJS is loaded from an allowed domain (*.cloudflare.com) in srcdoc, using ng-on-error to execute arbitrary JavaScript despite CSP restrictions.

## Requirements

1. Injected iframe with srcdoc
2. CSP allowing *.cloudflare.com
3. Browser access

## Defense

Defensive measures and detection strategies:

- Restrict external script sources in CSP
- Monitor for sandbox escapes

## Objectives

1. Load AngularJS in iframe
2. Execute JS via ng-on-error
3. Bypass CSP effectively

## Instructions

### Step 1: Load AngularJS in srcdoc

**Context**: Set up iframe srcdoc with AngularJS script tag.

Include ng-app and ng-csp.

### Step 2: Execute Payload

**Context**: Use ng-on-error for JS execution.

Example: alert(document.domain)

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/AngularJS]]

## Tags

- [[csp-bypass]]
- [[tools/AngularJS]]

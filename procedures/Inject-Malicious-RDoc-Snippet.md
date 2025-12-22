---
tags:
  - xss
  - rdoc
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 62cdb4b2-c8ea-4e52-a15b-5023a088175b
created_at: '2025-12-14T00:11:16.535Z'
updated_at: '2025-12-14T00:11:16.535Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Malicious RDoc Snippet

## Summary

This procedure details injecting malicious HTML via RDoc syntax in GitLab wiki pages to exploit stored XSS vulnerabilities.

## Description

RDoc parsing in GitLab allows image link syntax that bypasses sanitization, enabling arbitrary HTML tags and attributes. This can create phishing elements or script injections. Targets GitLab's web frontend on Linux environments. Outcomes include rendered malicious content that executes on page load.

## Requirements

1. Existing GitLab wiki page
2. Knowledge of RDoc syntax for image links
3. Access to wiki editing interface

## Defense

Defensive measures and detection strategies:

- Enable strict HTML sanitization in wiki rendering
- Audit wiki content for suspicious HTML patterns

## Objectives

1. Bypass sanitization with crafted RDoc
2. Insert phishing or XSS payloads
3. Prepare for victim exploitation

## Instructions

### Step 1: Craft Malicious Syntax

**Context**: Prepare RDoc payload to inject HTML.

In the editor, input syntax like '{<a href="javascript:alert(1)" class="malicious"><img src="x"></a>}[link]' to inject attributes.

> This exploits insufficient filtering in image links.

### Step 2: Test Payload Rendering

**Context**: Preview the page to confirm injection.

Use the preview function to see if the HTML renders as intended, such as creating overlays or forms.

> Expected: Malicious elements appear without sanitization.

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
- [[rdoc]]

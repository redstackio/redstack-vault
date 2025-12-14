---
id: proc-vimeo-xss-trigger-001
name: Trigger-Stored-XSS-on-Embed-Vhx-Tv
tags:
  - xss
  - stored-xss
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
updated_at: '2025-12-13T23:55:06.801Z'
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
# Trigger-Stored-XSS-on-Embed-Vhx-Tv

## Summary

This procedure demonstrates how uploaded malicious JavaScript from the Vimeo CDN executes as stored XSS on embed.vhx.tv, affecting all users due to unsanitized script inclusions in customer embeds.

## Description

After uploading a JS file to vpe.cdn.vimeo.tv, it is referenced in embed.vhx.tv pages without validation, allowing the XSS payload to run in the victim's browser context. This can lead to session theft, keylogging, or data exfiltration for all embed users. Targets web browsers loading Vimeo embeds.

## Requirements

1. Successful upload of malicious JS to CDN (prior procedure)
2. Access to a browser or tool to load embed.vhx.tv pages
3. Knowledge of the embed site's script inclusion patterns

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all external script sources in embeds
- Implement Content Security Policy (CSP) to restrict script execution
- Monitor for unexpected alerts or behaviors in embed logs

## Objectives

1. Execute the XSS payload in the embed site context
2. Compromise user sessions or steal data
3. Demonstrate impact on all customers

## Instructions

### Step 1: Load Embed Page in Browser

**Context**: Navigate to an embed.vhx.tv page that includes the malicious JS, triggering execution.

No specific command; use a browser to visit https://embed.vhx.tv/[some-embed] and inspect for script src pointing to the uploaded file.

> Expected: Alert pops up with document.domain, confirming XSS.

### Step 2: Verify Payload Execution

**Context**: Use developer tools to confirm script load and execution.

Inspect network tab for the JS fetch from vpe.cdn.vimeo.tv and console for payload effects.

> Success if payload runs without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss

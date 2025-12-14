---
id: proc-self-xss-trigger-001
tags:
  - xss
  - self-xss
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.454Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Self-XSS-on-Save

## Summary

This procedure verifies self-XSS by observing JavaScript execution immediately after saving the modified quiz on Crowdsignal, confirming the payload's viability for the creator.

## Description

Following payload injection, this step involves completing the save action and monitoring for execution in the creator's browser. The payload, embedded via the tampered media_code, triggers on page render post-save. Applicable to web sessions on https://app.crowdsignal.com. Prerequisites: Injected payload from prior interception. Outcomes: Alert popup proving control over the creator's session.

## Requirements

1. Saved quiz with injected payload
2. Active browser session in quiz editor

## Defense

Defensive measures and detection strategies:

- Sanitize all stored content before rendering in HTML contexts
- Browser extensions or CSP to block unsanitized script execution
- Log and alert on anomalous JavaScript errors in quiz views

## Objectives

1. Confirm payload execution in creator's context
2. Validate self-XSS for immediate impact assessment
3. Identify any client-side mitigations

## Instructions

### Step 1: Complete Save and Observe Execution

**Context**: After forwarding the request, return to the editor to trigger rendering of the injected content.

No command required; use web interface:

- Ensure the forwarded request completes
- Refresh or interact with the quiz editor page

> Expected output: SVG onload triggers alert showing document.domain (e.g., app.crowdsignal.com).

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
- [[self-xss]]

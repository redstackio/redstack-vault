---
tags:
  - xss-trigger
  - javascript-execution
  - acronis
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
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
updated_at: '2025-12-13T23:56:03.486Z'
sub_techniques: []
id: 61f541c7-72b4-49ab-ab7c-e878dc0ec4df
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS Payload

## Summary

This procedure describes navigating back to the malicious plan to trigger the stored XSS, resulting in JavaScript execution in the victim's browser context.

## Description

After storage, reloading or selecting the plan causes the unsanitized name to render, executing the onload event. This leads to repeated alerts and potential for advanced payloads like cookie theft. Requires prior plan creation; outcomes include confirmed execution and impact assessment.

## Requirements

1. Existing malicious plan in Acronis console
2. Active browser session
3. No ad-blockers interfering with SVG

## Defense

Defensive measures and detection strategies:

- Output encoding for all user-controlled data in UI
- Browser-based XSS auditors or extensions
- Alert on unusual JavaScript prompts in console logs

## Objectives

1. Render the stored payload to initiate execution
2. Observe JavaScript prompts as proof-of-concept
3. Evaluate escalation to real attacks

## Instructions

### Step 1: Reload or Navigate

**Context**: Refresh the console to re-load plans.

Re-visit https://mc-beta-cloud.acronis.com/ui/ or switch tabs.

> Page reloads with session intact.

### Step 2: Select and Edit Plan

**Context**: Access the specific plan to trigger rendering.

Go to 'Backup Scanning', select the payload-named plan, and click edit.

> Payload executes, showing domain prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mozilla-Firefox]]

## Tags

- xss-trigger
- payload-execution

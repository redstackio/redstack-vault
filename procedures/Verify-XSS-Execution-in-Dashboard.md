---
id: proc-uuid-003
name: Verify-XSS-Execution-in-Dashboard
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.609Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
tags:
  - xss-execution
  - verification
platforms:
  - Web
tools: []
commands: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Verify-XSS-Execution-in-Dashboard

## Summary

This procedure confirms the stored XSS by viewing the infographic in Infogram's dashboard, triggering JavaScript execution in the attacker's or viewer's browser.

## Description

After API injection, the payload renders in the dashboard view without sanitization, executing JS like domain alerts. Targets dashboard users. Prerequisites: Created infographic ID. Outcomes: Visible JS execution confirming exploit.

## Requirements

1. Access to Infogram dashboard with the account used for creation
2. Browser with JS enabled
3. Infographic ID from API response

## Defense

Defensive measures and detection strategies:

- Output encoding in dashboard rendering
- JS execution monitoring via browser dev tools or endpoint logs
- User education on suspicious alerts

## Objectives

1. Trigger payload execution on view
2. Validate arbitrary JS capability
3. Assess impact on session

## Instructions

### Step 1: Navigate to Library

**Context**: Locate the injected infographic.

Go to https://infogram.com/app/#/library and search by title.

> Manual navigation. Expected: Infographic listed with preview.

### Step 2: Open and Observe Execution

**Context**: Render the project to execute XSS.

Click to open the infographic.

> Payload triggers <img onerror=alert(document.domain)>. Expected: Alert box showing domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]

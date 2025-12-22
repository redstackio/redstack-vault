---
id: proc-infogram-trigger-xss-001
tags:
  - xss-trigger
  - dashboard
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:10.711Z'
skill_level: basic
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Dashboard-to-Trigger-XSS-Execution

## Summary

This procedure navigates to the Infogram dashboard library to view the created infographic, triggering the stored XSS payload to execute arbitrary JavaScript like domain alerts.

## Description

Once stored via API, the malicious content renders in the dashboard view, executing on page load for authenticated users. This demonstrates impact like session hijacking. Target: https://infogram.com/app/#/library. Prerequisites: Successful API creation. Outcomes: JS execution confirming vulnerability.

## Requirements

1. Active Infogram session from login
2. Infographic ID from API response
3. Browser supporting JS

## Defense

Defensive measures and detection strategies:

- Sanitize rendered content in dashboard views
- Enable XSS Auditor or similar browser protections
- Monitor for unexpected JS alerts or errors in client logs

## Objectives

1. Render the stored payload in dashboard
2. Execute injected JavaScript
3. Validate arbitrary code execution

## Instructions

### Step 1: Navigate to Library

**Context**: Access the projects list.

Go to https://infogram.com/app/#/library in your browser.

> Lists all user infographics. Expected: Page loads with project thumbnails.

### Step 2: Open and View Infographic

**Context**: Trigger rendering of malicious content.

Locate the newly created project by title 'title' and click to open.

> XSS img onerror fires, alerting document.domain (e.g., 'infogram.com'). Expected: Alert popup confirms execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- execution-trigger
- browser

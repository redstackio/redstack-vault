---
tags:
  - xss
  - execution-trigger
  - shopify
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.246Z'
sub_techniques: []
id: 4a739d69-ad9c-4d27-b69c-9064e88d5691
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Internal-Tools

## Summary

This procedure triggers the execution of the stored XSS payload in Shopify's internal web contexts, such as admin tools, confirming arbitrary JavaScript execution and potential data access.

## Description

After injection, the payload executes when staff names are rendered in internal views, like lists or reports. Execution occurs at an internal origin (e.g., http://localhost:4567), firing a callback to XSS Hunter. This enables read access to merchant data subsets in authenticated sessions.

## Requirements

1. Successfully created staff account with payload from prior step
2. Active XSS Hunter monitoring session
3. Access to internal admin tools where names are displayed

## Defense

Defensive measures and detection strategies:

- Escape outputs in all internal views rendering user data
- Monitor for unexpected external requests from internal services
- Use browser developer tools or proxies to detect JS execution anomalies

## Objectives

1. Cause payload execution in internal context
2. Receive confirmation via callback
3. Assess impact on data access

## Instructions

### Step 1: Navigate to Triggering Views

**Context**: Access pages or tools that display the injected staff name.

Go to admin sections like staff lists, reports, or any internal tool listing staff details.

**Expected Output**: Page loads, rendering the name and executing the script silently.

### Step 2: Confirm Execution

**Context**: Monitor for the blind XSS callback to verify success.

Check XSS Hunter dashboard for hit from http://localhost:4567 origin.

**Expected Output**: Callback logged, indicating JS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- [[xss]]
- [[execution-trigger]]
- [[shopify]]

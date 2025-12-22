---
tags:
  - session-check
  - refresh
  - persistence-test
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.810Z'
sub_techniques: []
id: edea60a9-76aa-4f7b-8116-ede670101582
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Refresh Secondary Session

## Summary

This procedure reloads an isolated session to verify if authentication changes in another session have invalidated it.

## Description

Refreshing forces the browser to revalidate session state with the server, revealing flaws in session management. Used in the secondary browser during multi-session tests, this checks for unexpected persistence after password changes or logouts elsewhere. Targets web apps with cookie-based auth.

## Requirements

1. Active secondary browser session
2. Unaltered state in the secondary browser (no manual logout)
3. Current page loaded (e.g., dashboard)

## Defense

Defensive measures and detection strategies:

- Implement token revocation on auth events to force re-auth on refresh
- Detect stale sessions via timeout enforcement and logging

## Objectives

1. Trigger server revalidation of the session
2. Observe if access remains granted
3. Confirm or rule out invalidation failure

## Instructions

### Step 1: Reload the Page

**Context**: Force a fresh request to test session validity.

In the secondary browser, ensure the authenticated page (e.g., account profile) is open. Press Ctrl+R (or Cmd+R on Mac) or click the browser's refresh icon to reload the page.

**Expected Output**: If vulnerable, the page reloads with full access intact; if secure, redirects to login.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- session-check
- refresh

---
id: p-reopen-location-dialog-trigger-xss
tags:
  - xss-trigger
  - concrete-cms
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
updated_at: '2025-12-14T03:16:20.626Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reopen-Location-Dialog-to-Trigger-XSS

## Summary

This procedure reopens the Location dialog for the targeted page in Concrete CMS, causing the stored XSS payload to render in the JavaScript context and prepare for execution.

## Description

By selecting the same page in Sitemap and reopening the Location dialog as another authorized user, the unsanitized payload is fetched and inserted into the renderPagePath function, breaking out of the JavaScript object and function calls to enable execution.

## Requirements

1. Payload saved in page attributes.
2. Another authenticated session with edit permissions (or same session).
3. Browser developer tools for inspection.

## Defense

Defensive measures and detection strategies:

- Escape user-supplied data in JavaScript rendering using proper encoding.
- Implement content security policy (CSP) to block inline script execution.

## Objectives

1. Reload the dialog to render stored data.
2. Trigger JavaScript parsing of the payload.
3. Observe context breakout in source code.

## Instructions

### Step 1: Return to Sitemap

**Context**: Navigate back to the page selection area.

From the dashboard, reopen the Sitemap section.

> Sitemap reloads with the modified page.

### Step 2: Re-Select Page and Open Dialog

**Context**: Invoke the dialog to fetch and render the payload.

Right-click the targeted page and select 'Location' again.

> Dialog opens; inspect source to see payload in renderPagePath JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- concrete-cms

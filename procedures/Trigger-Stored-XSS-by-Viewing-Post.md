---
tags:
  - xss
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.075Z'
sub_techniques: []
id: db71cd21-1af6-40bc-8e0a-620f807263ef
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS by Viewing Post

## Summary

This procedure involves accessing the published post URL to render the title, causing the browser to execute the stored JavaScript payload.

## Description

When the frontend theme renders the post title, the unsanitized <script> tag executes in the viewer's context. In WordPress 5.3, titles are output via functions like the_title() without default escaping for stored content from capable users. This can lead to impacts like cookie theft (e.g., via document.cookie) or phishing, affecting any viewer including admins.

## Requirements

1. Published post permalink
2. Web browser to simulate victim view
3. No CSP blocking scripts

## Defense

Defensive measures and detection strategies:

- Escape output in themes (e.g., esc_html(the_title()))
- Deploy browser-based protections like XSS auditors
- Monitor for anomalous JavaScript execution via WAF logs

## Objectives

1. Execute arbitrary code in victim browsers
2. Demonstrate impact like domain alert or data exfil
3. Validate stored payload functionality

## Instructions

### Step 1: Obtain Permalink

**Context**: Get the frontend URL for the post.

From the editor or Posts list, copy the 'View Post' link.

> URL format: https://target.com/post-slug/

### Step 2: Load in Browser

**Context**: Trigger rendering and execution.

Paste the URL into a new browser tab or incognito window.

> The page loads, title renders, and script executes (e.g., alert pops).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]

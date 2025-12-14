---
tags:
  - open-redirect
  - web
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
id: 283eabd0-e71b-4a56-8623-e2b204725f07
created_at: '2025-12-14T17:24:34.798Z'
updated_at: '2025-12-14T17:24:34.798Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Locate-HREF-Attribute

## Summary

This procedure focuses on pinpointing the specific HREF attribute in the page's HTML that contains an internal path vulnerable to open redirect exploitation.

## Description

With dev tools open, locate attributes like 'href="/todays-selection/2"' on the target page. This step confirms the vulnerability's presence by verifying the lack of external URL restrictions. It's part of client-side testing on public web apps, leading to modification in the next phase.

## Requirements

1. Developer tools active on loaded page
2. Target page with known link structure
3. Ability to search DOM elements

## Defense

Defensive measures and detection strategies:

- Use absolute URLs with domain whitelisting in links
- Implement server-side rendering to obscure client-side edits

## Objectives

1. Find vulnerable HREF
2. Confirm internal path usage
3. Prepare for editing

## Instructions

### Step 1: Search for HREF

**Context**: Use dev tools to query the DOM.

No specific command; perform manually:

In [[tools/Browser-Developer-Tools]], use the Elements panel search (Ctrl+F) for 'href="/todays-selection/2"'.

> The matching <a> tag is highlighted, showing the exact attribute location.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[open-redirect]]
- [[web]]

---
id: 123e4567-e89b-12d3-a456-426614174003
name: View-Connected-Facebook-Pages-in-KitCRM
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.393Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - discovery
  - xss
  - web
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---

# View-Connected-Facebook-Pages-in-KitCRM

## Summary

This procedure displays the list of connected Facebook pages in KitCRM, where unsanitized page names are reflected, setting up for XSS execution.

## Description

After connection, the Facebook section in KitCRM renders a dropdown or list of pages fetched from the Facebook API. Due to lack of HTML escaping, malicious payloads in page names are injected into the DOM. This step reveals the stored payload but does not execute it yet. Inspect the page source to confirm reflection.

## Requirements

1. Successfully connected Facebook account with malicious page
2. Active KitCRM session
3. Browser developer tools for inspection

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity encoding) when rendering API data
- Use Content Security Policy (CSP) to restrict inline scripts

## Objectives

1. Reflect stored malicious input in the UI
2. Verify payload presence without execution
3. Prepare for interaction trigger

## Instructions

### Step 1: Refresh Connections Page

**Context**: Load the updated Facebook section.

Navigate back to or refresh https://kitcrm.com/users/[USER_ID]/connections.

### Step 2: Inspect Facebook Pages List

**Context**: Confirm unsanitized reflection.

Locate the Facebook dropdown; use browser dev tools to view the HTML source of the page names.

**Expected Output**: Malicious page name "><img src=x onerror=alert(9)> visible in raw HTML without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Discovery]]
- [[xss]]
- [[web]]

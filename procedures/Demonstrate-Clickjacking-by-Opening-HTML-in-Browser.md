---
tags:
  - clickjacking
  - browser
  - iframe
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.814Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 0115764a-ff8d-4a78-8747-21399bb194b8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate-Clickjacking-by-Opening-HTML-in-Browser

## Summary

This procedure loads the saved HTML file in a browser to verify the clickjacking vulnerability, showing the login page embedded without restrictions.

## Description

Opening the file in a browser simulates how a victim would interact with the malicious page. The iframe loads https://cas.acronis.com/ freely, confirming the root cause: no CSP frame-ancestors 'self'. In a full attack, overlays would trick clicks; here, it demonstrates feasibility. Target is any modern browser; outcome is visible embedding.

## Requirements

1. Web browser installed
2. Saved HTML file from previous procedure
3. Internet connection for iframe loading

## Defense

Defensive measures and detection strategies:

- Browser extensions to detect iframes from untrusted sources
- Network proxies to block external iframe loads
- User training on suspicious pop-ups or overlays

## Objectives

1. Load and render the PoC in browser
2. Confirm unrestricted iframe embedding
3. Observe potential for user trickery

## Instructions

### Step 1: Locate the File

**Context**: Find the saved HTML file.

Navigate to the directory where the file was saved.

### Step 2: Open in Browser

**Context**: Launch the file to execute the iframe.

Double-click the .html file or right-click > Open with > Chrome/Firefox.

> The page loads with the title "Clickjacking Vulnerability" and the embedded login page. If overlays were added, they would be invisible here.

### Step 3: Verify Embedding

**Context**: Check for successful load without errors.

Inspect the page source or developer tools to confirm the iframe src is active and no frame-busting occurs.

**Expected Output**: Acronis login page visible inside the iframe, fully interactive.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[browser-demo]]
- [[iframe-embed]]

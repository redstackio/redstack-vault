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
id: 4b0c1eeb-38d5-4df5-bbba-aa94be89f40a
created_at: '2025-12-14T17:24:34.816Z'
updated_at: '2025-12-14T17:24:34.816Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-Page-Source

## Summary

This procedure uses browser developer tools to examine the HTML source of a webpage, identifying potential vulnerabilities like open redirects in link attributes.

## Description

Once the target page is loaded, inspecting the source reveals the structure of links and their HREF values. In the context of xnxx.com, this uncovers internal paths in HREFs that lack validation for external URLs. Prerequisites include having the page open in a browser. The outcome is visibility into editable elements for manipulation.

## Requirements

1. Page loaded in browser
2. Browser with developer tools enabled (e.g., Chrome DevTools)
3. Basic HTML knowledge

## Defense

Defensive measures and detection strategies:

- Enable client-side integrity checks (e.g., Content Security Policy) to prevent tampering
- Monitor for developer tools usage in automated testing environments

## Objectives

1. View raw HTML source
2. Identify link elements
3. Spot vulnerable attributes

## Instructions

### Step 1: Open Developer Tools

**Context**: Access the inspection interface to view page elements.

No specific command; perform manually:

Right-click on the page and select "Inspect" or press F12 to open [[tools/Browser-Developer-Tools]].

> The Elements or Inspector panel opens, showing the DOM tree. Navigate to the Sources tab if needed for full HTML.

### Step 2: Examine Elements

**Context**: Search for relevant tags.

Use the search function in dev tools (Ctrl+F) to find "href".

> Results highlight anchor tags (<a>) with HREF attributes, such as those pointing to internal paths.

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

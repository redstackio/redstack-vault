---
tags:
  - xss
  - execution
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
updated_at: '2025-12-13T23:52:33.374Z'
sub_techniques: []
id: a81ef032-2957-4290-b988-7bb6f6b46e0f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Trigger-XSS-via-Advanced-Search

## Summary

This procedure activates the advanced search feature to parse the reflected payload in the URL, resulting in DOM-based JavaScript execution.

## Description

Clicking 'advanced search' in the results redirects to a URL like `/search/query?q=payload`, where the unsanitized payload is inserted into the DOM via JavaScript (e.g., location.search handling). This executes the script tag, running arbitrary code like the prompt POC.

## Requirements

1. Search results page with reflected payload
2. 'Advanced search' link visible
3. New tab/window capability in browser

## Defense

Defensive measures and detection strategies:

- Escape URL parameters before DOM insertion
- Validate and sanitize query strings server-side before reflection

## Objectives

1. Execute the injected script
2. Demonstrate XSS impact with POC alert
3. Capture browser console for verification

## Instructions

### Step 1: Locate Advanced Search Link

**Context**: Find the link that will trigger URL-based reflection.

In the search results, identify and hover over the 'advanced search' option.

> Expected: Link URL in status bar shows unsanitized payload.

### Step 2: Open Advanced Search

**Context**: Navigate to cause DOM parsing and execution.

Click the link to open advanced search in a new window.

> Expected: Prompt dialog with '1337' appears, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dom-execution
- advanced-search

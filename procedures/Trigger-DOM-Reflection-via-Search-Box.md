---
id: proc-uuid-1010132-2
tags:
  - dom-xss
  - reflection
  - search
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
updated_at: '2025-12-13T23:52:55.574Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-DOM-Reflection-via-Search-Box

## Summary

This procedure triggers the reflection of the injected HTML payload from an email subject into the DOM by performing a search in the Hey.com interface, demonstrating lack of sanitization in search results.

## Description

The Hey.com search functionality queries emails and renders subjects directly into the DOM without proper HTML escaping, allowing injected tags to render. This targets the web client-side rendering in an authenticated session. Outcomes include visible HTML elements in search results, confirming the injection point for potential XSS.

## Requirements

1. Malicious email already sent and present in inbox
2. Access to the search interface in https://app.hey.com/
3. Browser developer tools for inspection

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected user input in search results using HTML entity encoding
- Implement output encoding libraries like DOMPurify for client-side rendering
- Log search queries containing suspicious patterns (e.g., <script>) for anomaly detection

## Objectives

1. Cause the email subject to render in search results with injected HTML
2. Verify DOM insertion of malicious tags
3. Observe any immediate rendering impacts like UI manipulation

## Instructions

### Step 1: Access Search Functionality

**Context**: Locate the search input to initiate the query.

In the Hey.com dashboard, focus on the top left search box.

### Step 2: Enter Search Query

**Context**: Query for the payload to reflect the malicious email.

Type `TestPayload` into the search input and submit the search.

### Step 3: Inspect Reflected Content

**Context**: Examine the search results for DOM changes.

Review the displayed emails; the subject should show the injected `<a>` tag as 'ClickHere'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dom-xss]]
- [[reflection]]
- [[search]]

---
tags:
  - xss
  - payload-craft
  - url-encoding
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
updated_at: '2025-12-14T03:15:27.009Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: f53945c6-3650-4208-bed3-617f1029c7ce
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-Search-URL

## Summary

This procedure crafts a malicious URL by replacing the search query with a JavaScript payload in the Informatica community marketplace search path, URL-encoding it to bypass basic filters and prepare for XSS injection.

## Description

Building on observation of the search behavior, this step involves substituting a benign search term with an XSS payload such as ';alert(0);t=' to break out of JavaScript strings in the page's inline code. The payload is URL-encoded (e.g., to %22;alert(0);t=%22) and inserted after /search/ in the path, creating a URL like https://community.informatica.com/community/marketplace/%22;alert(0);t=%22/?blkCatIds=free+apps&view=solution. This targets the lack of escaping in client-side JavaScript processing, enabling arbitrary code execution upon visit. Prerequisites include knowledge of the target URL structure.

## Requirements

1. Text editor or URL encoder tool (built-in browser dev tools suffice)
2. Understanding of JavaScript injection syntax
3. Valid base URL from reconnaissance

## Defense

Defensive measures and detection strategies:

- Enforce strict URL decoding and validation on the backend
- Sanitize all path parameters before JavaScript insertion
- Log and block suspicious encoded characters in URLs

## Objectives

1. Create a functional XSS payload URL
2. Ensure proper encoding to evade filters
3. Test payload syntax for injection success

## Instructions

### Step 1: Select and Encode Payload

**Context**: Choose a simple test payload and encode it for URL safety.

Use ';alert(0);t=' as the payload and encode it to %22;alert(0);t=%22 using a URL encoder.

> This prevents premature decoding issues and allows the payload to reach the client-side JavaScript intact.

### Step 2: Construct Malicious URL

**Context**: Insert the encoded payload into the legitimate search URL structure.

Replace the search path segment with the encoded payload, e.g., https://community.informatica.com/community/marketplace/%22;alert(0);t=%22/?blkCatIds=free+apps&view=solution.

> Expected output is a complete, clickable URL that mimics a valid search but contains the injection.

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
- [[url-encoding]]

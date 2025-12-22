---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Identify-Sensitive-JavaScript-File-via-Network-Inspection
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:48.530Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Software]]'
tags:
  - information-disclosure
  - network-inspection
  - javascript
commands:
  - '[[commands/curl-download-js]]'
platforms:
  - Web
tools:
  - '[[tools/Browser-Network-Inspector]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---

# Identify-Sensitive-JavaScript-File-via-Network-Inspection

## Summary

This procedure uses browser network inspection to locate and access a specific minified JavaScript file that contains embedded sensitive data on a web application.

## Description

Attackers leverage the browser's network tab to monitor resource requests while loading the site, filtering for JavaScript files. In this case, the file /main.c1965c58f39a0f4aadc3.js is identified as containing hardcoded credentials. The procedure assumes a public web environment and results in direct access to the file for download or viewing. Prerequisites include browser access and basic knowledge of developer tools.

## Requirements

1. Browser with network inspector enabled
2. Target URL accessible via HTTP/HTTPS
3. Optional: Command-line tool like curl for downloading

## Defense

Defensive measures and detection strategies:

- Obfuscate or minify JS files more aggressively to hide strings
- Use server-side rendering to avoid client-side exposure of secrets
- Log and alert on unusual file access patterns

## Objectives

1. Locate the sensitive JavaScript resource
2. Confirm public accessibility
3. Download the file for analysis

## Instructions

### Step 1: Monitor Network Traffic

**Context**: Load the site and capture network requests to identify JS files.

Use [[commands/curl-download-js]] to fetch the file if known, or inspect in browser:

```bash
curl -O https://staging.empleio.stripo.email/main.c1965c58f39a0f4aadc3.js
```

> Downloads the minified JS file to the local directory.

### Step 2: Filter and Locate File

**Context**: In the network inspector, filter by 'JS' and select the target file.

View or right-click to copy the file contents.

> Expected output: Raw minified JavaScript code visible in the browser or downloaded file.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]

### Sub-Techniques


## Commands Used

- [[commands/curl-download-js]]

## Tools Used

- [[tools/Browser-Network-Inspector]]

## Tags

- [[information-disclosure]]
- [[network-inspection]]

---
tags:
  - file-download
  - misconfiguration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[File and Directory Discovery]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 75bd3ea1-d437-4123-a671-901a1ca81753
created_at: '2025-12-14T17:32:39.189Z'
updated_at: '2025-12-14T17:32:39.189Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Download-Publicly-Accessible-Internal-JavaScript-Files

## Summary

This procedure retrieves the content of internal JavaScript files identified in the 404 page source, exploiting their public accessibility due to lack of access controls.

## Description

In the Semrush case, internal JS files for system statistics are served without authentication, allowing direct download. This step involves fetching these files via browser or HTTP requests. Expected outcomes: raw JS code available for analysis, potentially containing secrets.

## Requirements

1. List of JS URLs from previous inspection
2. Web browser or HTTP client (e.g., curl)
3. Local storage for downloaded files

## Defense

Defensive measures and detection strategies:

- Enforce authentication or IP whitelisting on internal file paths
- Use .htaccess or server configs to block direct JS access
- Monitor for anomalous file downloads in access logs

## Objectives

1. Fetch JS files without errors
2. Verify public accessibility
3. Prepare files for code review

## Instructions

### Step 1: Access JS URL

**Context**: Test direct access to confirm no protections.

Copy a JS URL (e.g., https://api.semrush.com/internal/stats.js) and paste into a new browser tab.

> The file content (minified JS) should render as text without login prompts.

### Step 2: Save the File

**Context**: Store for offline analysis.

Right-click the loaded JS and select "Save As" or use curl -O <URL> to download.

> Expected: .js file saved locally, size indicating non-trivial code.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-download]]
- [[misconfiguration]]

---
tags:
  - source-inspection
  - javascript
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
impact_level: low
detection_risk: low
sub_techniques: []
id: af38e1da-54e7-4223-b32c-1efd18fca244
created_at: '2025-12-14T17:32:39.193Z'
updated_at: '2025-12-14T17:32:39.193Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Inspect-404-Page-Source-for-Internal-JS-References

## Summary

This procedure examines the HTML source code of a 404 error page to locate references to internal JavaScript files, revealing assets that should not be publicly listed.

## Description

The Semrush 404 page source contains <script> tags pointing to numerous JS files, including those for internal system statistics interfaces. This manual inspection uncovers misconfigurations where private code is exposed. Prerequisites include having triggered the 404 page; outcomes include a list of accessible JS URLs for further exploration.

## Requirements

1. Access to the loaded 404 page in a browser
2. Basic HTML knowledge for searching source code
3. Text editor or browser dev tools for analysis

## Defense

Defensive measures and detection strategies:

- Strip internal references from error page templates
- Use server-side rendering to avoid client-side exposures
- Log and alert on source code inspections via WAF rules

## Objectives

1. Parse HTML for script tags
2. Identify internal vs. public JS files
3. Document URLs for subsequent access

## Instructions

### Step 1: View Page Source

**Context**: Access the raw HTML to search for embedded resources.

Right-click the 404 page and select "View Page Source" or use Ctrl+U.

> The source will show <head> and <body> sections with <script src="..."> tags.

### Step 2: Search for JS References

**Context**: Filter for internal files by keywords like "stats" or domain paths.

Use Ctrl+F to search for ".js" or "semrush". Note URLs like /internal/stats-interface.js.

> Expected: 10+ JS references, some indicating internal use (e.g., system stats).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[source-inspection]]
- [[JavaScript]]

---
tags:
  - recon
  - web
  - bootstrap
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T03:16:08.371Z'
sub_techniques: []
id: 1a0e6788-e0df-4db9-9c86-8a47b135155f
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Search-Page-Source-for-Bootstrap-Reference

## Summary

This procedure involves searching the inspected page source for references to the Bootstrap library, helping pinpoint potential XSS vectors in frontend components.

## Description

Once developer tools are open, searching for specific strings like "bootstrap.min.js" reveals dependencies on third-party JS files. This is crucial for WordPress themes (e.g., 'icos' theme) that bundle vulnerable versions. The approach is passive and manual, focusing on static analysis to avoid alerts. It supports identifying CVE-2019-8331-affected attributes in tooltips/popovers.

## Requirements

1. Developer tools already open from prior inspection
2. Target page loaded and stable
3. Basic familiarity with browser search functions

## Defense

Defensive measures and detection strategies:

- Minify and obfuscate JS file names to hinder easy identification
- Employ SRI (Subresource Integrity) hashes for script tags to prevent tampering
- Monitor server logs for unusual direct accesses to JS files

## Objectives

1. Locate Bootstrap-related script references
2. Note file paths for further verification
3. Build evidence of library usage

## Instructions

### Step 1: Activate Search in Elements Tab

**Context**: Use built-in search to filter DOM elements efficiently.

In the Elements tab of developer tools, press Ctrl+F (Windows/Linux) or Cmd+F (macOS) to open the find bar. Enter "bootstrap.min.js" and press Enter.

> Results will highlight matching elements; cycle through with Enter key.

### Step 2: Review Search Matches

**Context**: Analyze context around matches to confirm legitimacy.

Examine highlighted script tags or links, noting attributes like src and any version parameters (e.g., ?ver=5.7.2). Ignore false positives like comments.

> Document the full reference for the next step.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
- [[bootstrap]]

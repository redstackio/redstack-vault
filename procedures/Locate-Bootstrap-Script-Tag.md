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
updated_at: '2025-12-14T03:16:08.368Z'
sub_techniques: []
id: 2d8a8ef9-5c1d-424e-a880-91b55098e673
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Locate-Bootstrap-Script-Tag

## Summary

This procedure extracts the precise script tag for the Bootstrap library from the page source, providing the URL needed for version confirmation.

## Description

Building on search results, this step involves navigating the DOM to isolate the Bootstrap script element. In WordPress environments, scripts are often in wp-content/themes paths. This manual extraction reveals details like IDs (e.g., id="bootstrap-js") and supports vulnerability scoping for XSS in data attributes.

## Requirements

1. Search results from previous step available
2. Elements tab active in developer tools
3. Ability to copy text from the inspector

## Defense

Defensive measures and detection strategies:

- Load scripts dynamically via JavaScript to avoid static HTML exposure
- Use bundle tools like Webpack to combine libraries, reducing identifiable tags
- Scan for reconnaissance patterns in user-agent logs

## Objectives

1. Isolate the exact script element
2. Capture the src URL and attributes
3. Prepare for direct file access

## Instructions

### Step 1: Navigate to Script Section

**Context**: Focus on the head or body where external scripts reside.

In the Elements tab, expand the <head> or <body> nodes. Scroll or use the outline view to find script elements matching the search.

> Look for type="text/javascript" and src attributes pointing to bootstrap.min.js.

### Step 2: Copy Script Details

**Context**: Record the full tag for analysis.

Right-click the script node and select "Copy > Copy element" or manually note: <script type="text/javascript" src="https://sifchain.finance/wp-content/themes/icos/assets/js/vendor/bootstrap.min.js?ver=5.7.2" id="bootstrap-js"></script>.

> Verify the URL is complete and accessible.

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

---
id: proc-uuid-001
name: Setup-Awesome-Autocomplete-Extension
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:21.075Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - setup
  - browser-extension
  - xss-prep
platforms:
  - Web
  - Browser Extension
tools:
  - '[[tools/Awesome-Autocomplete-Extension]]'
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Setup-Awesome-Autocomplete-Extension

## Summary

This procedure installs and configures the Awesome Autocomplete browser extension, which enhances GitHub search but contains a vulnerability allowing unsanitized HTML injection, setting the stage for XSS exploitation.

## Description

The Awesome Autocomplete extension fetches and renders GitHub search results via Algolia, inserting repository names and issue titles directly into the DOM without escaping. This procedure prepares the environment on supported browsers like Chrome or Safari, ensuring the extension is active for subsequent injection tests. It targets users or testers aiming to demonstrate the XSS flaw in a controlled manner.

## Requirements

1. Supported browser: Chrome 57.0.2987.133 or Safari 10.1
2. Operating system: macOS Sierra 10.12.4 or Windows 7 x64
3. Internet access to download and access GitHub.com
4. No prior extension conflicts

## Defense

Defensive measures and detection strategies:

- Disable or remove third-party browser extensions before accessing sensitive sites like GitHub
- Use browser content security policies (CSP) to block inline scripts
- Monitor extension permissions and audit source code for sanitization issues

## Objectives

1. Install the vulnerable extension to enable unsanitized rendering
2. Verify extension activation on GitHub search
3. Prepare for payload injection without disrupting browser functionality

## Instructions

### Step 1: Install Extension

**Context**: Download and add the extension to the browser to gain access to vulnerable autocomplete features.

Navigate to the Chrome Web Store (or Safari extensions gallery) and search for "Awesome Autocomplete for GitHub". Click install and confirm permissions.

> The extension will appear in the browser's extensions menu once installed.

### Step 2: Enable on GitHub

**Context**: Activate the extension specifically for GitHub.com to ensure it intercepts search queries.

Open GitHub.com, go to the search bar, and confirm autocomplete suggestions load with enhanced results from the extension.

> If not active, check browser extensions settings and enable for github.com domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Awesome-Autocomplete-Extension]]

## Tags

- [[setup]]
- [[browser-extension]]

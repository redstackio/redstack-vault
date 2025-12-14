---
id: p-analyze-livefyre-script
tags:
  - xss
  - recon
  - javascript
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:16:14.710Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Analyze Livefyre Script for Vulnerable Parameter

## Summary

This procedure involves static analysis of the Livefyre streamhub-permalink JavaScript library to identify how the 'lf-content' parameter is processed, revealing a domain control vulnerability that enables reflected XSS.

## Description

In the context of Uber's newsroom.uber.com, the Livefyre Media Wall uses an external JS library that parses the 'lf-content' query parameter in the format controlled-domain:collection_id:content_id. This constructs an API request to https://bootstrap.controlled-domain/api/v3.0/content/thread/?collection_id=...&content_id=...&depth_only=false. Without domain validation, an attacker can supply their own domain, leading to loading of arbitrary JSON that injects unsanitized 'bodyHtml' into the DOM. Prerequisites include access to a web browser with developer tools.

## Requirements

1. Web browser with network inspection (e.g., Chrome DevTools)
2. Public access to newsroom.uber.com
3. Basic JavaScript knowledge for code review

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script sources
- Validate and whitelist domains in third-party integrations like Livefyre
- Monitor for anomalous API requests to non-standard domains

## Objectives

1. Confirm user control over the domain in API fetches
2. Identify lack of sanitization in JSON response handling
3. Map the vulnerability for exploitation planning

## Instructions

### Step 1: Inspect the Target Page

**Context**: Load the vulnerable page and examine loaded scripts to locate the Livefyre library.

Open https://newsroom.uber.com/ in your browser, open Developer Tools (F12), and go to the Sources or Network tab. Search for 'streamhub-permalink.min.js' from cdn.livefyre.com.

**Expected Output**: Script file loaded and visible for analysis.

### Step 2: Analyze Script Parsing Logic

**Context**: Review the JavaScript code to understand parameter handling.

In the Sources tab, open the script and search for 'lf-content'. Observe how it's split by ':' to extract domain, collection_id, and content_id, then used to build the bootstrap URL without validation.

**Expected Output**: Code snippets showing unsanitized domain insertion into fetch URL.

### Step 3: Verify API Endpoint Construction

**Context**: Test the parameter parsing by simulating in console.

In the browser console, log a test parse: e.g., var parts = 'attacker.com:123:456'.split(':'); console.log('Domain: ' + parts[0]); Confirm it would lead to https://bootstrap.attacker.com/...

**Expected Output**: Parsed domain matches input, confirming control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- Browser Developer Tools

## Tags

- [[xss]]
- [[recon]]
- [[JavaScript]]

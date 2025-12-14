---
tags:
  - recon
  - headers
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a0474bc5-197f-4f7e-bc95-6cd20699f700
created_at: '2025-12-14T17:28:12.651Z'
updated_at: '2025-12-14T17:28:12.651Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Check-for-Missing-X-Frame-Options-Header

## Summary

This procedure inspects HTTP response headers of a web application to detect the absence of the X-Frame-Options header, which prevents clickjacking by blocking iframe embedding.

## Description

In a clickjacking attack, attackers embed victim sites in iframes on malicious pages to trick users into clicking hidden elements. The X-Frame-Options header (e.g., DENY or SAMEORIGIN) mitigates this. This procedure targets sites like app.lemlist.com, where the header is missing, allowing framing even in local file:// contexts. It uses browser tools for passive reconnaissance without sending malicious requests.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Internet access to the target URL (https://app.lemlist.com/)
3. No authentication required for public pages

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server responses
- Use Content-Security-Policy (CSP) frame-ancestors directive
- Monitor for anomalous iframe embeddings via WAF logs

## Objectives

1. Confirm lack of frame protection headers
2. Identify vulnerable endpoints like user settings pages
3. Establish foundation for PoC development

## Instructions

### Step 1: Access Target and Open DevTools

**Context**: Navigate to the target site and prepare to inspect network traffic.

Open your web browser and go to https://app.lemlist.com/. Press F12 to open Developer Tools, then switch to the Network tab. Ensure "Preserve log" is enabled.

### Step 2: Reload and Inspect Headers

**Context**: Trigger a page load to capture response headers and check for X-Frame-Options.

Reload the page (Ctrl+R). In the Network tab, click on the main document request (e.g., app.lemlist.com). Scroll to the Response Headers section and search for "X-Frame-Options".

> If absent, the site is vulnerable to framing. Note any other security headers like CSP for completeness.

### Step 3: Test Specific Subpaths

**Context**: Verify vulnerability on sensitive areas like user management pages.

Navigate to a subpath such as /teams/tea_sgYr5dZr478x4FQ9K/settings/user/usr_Z3GZ4DDHLLyLyZHj5/users and repeat the header inspection.

**Expected Output**: Consistent absence of X-Frame-Options across endpoints.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]

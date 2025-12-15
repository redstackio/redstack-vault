---
id: proc-bypass-html-acronis
tags:
  - broken-access-control
  - information-disclosure
  - url-manipulation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:29:28.530Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Bypass Access Controls with .html Extension

## Summary

This procedure exploits a misconfiguration in access controls by appending .html to protected URLs, allowing unauthenticated retrieval of static files like HTML, JS, and CSS that should be restricted.

## Description

On the notary.acronis.com panel, dynamic endpoints enforce authentication, but static files served via .html extensions do not. By manually modifying URLs during testing, attackers can view internal resources, potentially leaking UI details or scripts. This is a low-impact disclosure with no execution capabilities. Prerequisites include knowledge of panel URLs from prior recon.

## Requirements

1. Web browser for URL manipulation
2. Known panel function URLs (e.g., from error messages or guessing)
3. Public access to the target domain

## Defense

Defensive measures and detection strategies:

- Apply uniform authentication to all static and dynamic assets
- Configure web servers (e.g., Nginx/Apache) to deny .html access without auth tokens
- Log and alert on unusual URL patterns or static file requests from unauthenticated IPs

## Objectives

1. Gain unauthorized access to static resources
2. Expose potentially sensitive file contents
3. Demonstrate bypass without credentials

## Instructions

### Step 1: Identify Target URL

**Context**: Select a protected panel function URL to modify.

In the browser, note a panel path like https://notary.acronis.com/panel/function.

> Expected output: Base URL ready for modification.

### Step 2: Append .html and Access

**Context**: Trick the server into serving the static version by adding the extension.

Modify the URL to https://notary.acronis.com/panel/function.html and load it.

> No command; direct browser access. Expected output: File loads, showing HTML/JS/CSS content without auth prompt.

### Step 3: Repeat and Collect Files

**Context**: Test multiple endpoints to gather more resources.

Append .html to variations (e.g., /panel/dashboard.html) and save/download contents.

> Expected output: Collection of static files revealing internal structure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[broken-access-control]]
- [[information-disclosure]]
- [[url-manipulation]]

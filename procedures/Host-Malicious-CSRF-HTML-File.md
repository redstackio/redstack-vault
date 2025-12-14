---
tags:
  - hosting
  - phishing-delivery
  - web-server
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:30:07.438Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: fe701148-5ca4-4769-912b-57abec6ddf38
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host-Malicious-CSRF-HTML-File

## Summary

This procedure uploads the modified CSRF PoC HTML to a web host, creating a deliverable link for victim exploitation.

## Description

The HTML is hosted on any accessible web server, making the auto-submitting form available via URL. This step bridges PoC development to delivery in a CSRF attack chain, assuming basic hosting access. Outcomes enable cross-site request forgery when visited.

## Requirements

1. Modified PoC HTML file
2. Web hosting service (e.g., GitHub Pages, free host)
3. Public URL generation capability

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links
- Block or scan hosted files for malicious forms

## Objectives

1. Make PoC publicly accessible
2. Obtain shareable URL
3. Ensure auto-submit works remotely

## Instructions

### Step 1: Choose Hosting Platform

**Context**: Select a service.

Use a free web host or personal server.

> Examples: Upload to Netlify, Vercel, or Apache server.

### Step 2: Upload and Verify

**Context**: Deploy the file.

Upload HTML; access via generated URL to confirm load and auto-submit.

> Expected: Page loads, form submits immediately.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- hosting
- phishing-delivery

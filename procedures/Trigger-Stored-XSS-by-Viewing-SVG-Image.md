---
tags:
  - xss
  - stored-xss
  - svg
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.827Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1e84801c-0d0b-47fe-9b9a-38ccf899d0d6
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Viewing-SVG-Image

## Summary

This procedure triggers the stored XSS payload by accessing the uploaded malicious SVG in a browser, causing JavaScript execution due to the preserved `image/svg+xml` MIME type.

## Description

Once the SVG is uploaded to Airship CMS, it is served to users viewing images in the CMS interface, such as galleries or previews. Browsers parse SVGs as XML and execute embedded scripts when rendered. This leads to arbitrary JS execution in the victim's context, enabling session theft or data exfiltration. The procedure assumes the payload is already stored and targets any user who views the file, including admins.

## Requirements

1. Uploaded malicious SVG accessible via URL
2. Victim access to the CMS (e.g., shared link or logged-in view)
3. Browser that supports SVG rendering (most modern browsers)
4. Attacker-controlled endpoint for exfiltration verification

## Defense

Defensive measures and detection strategies:

- Serve SVGs with `Content-Security-Policy: script-src 'none'`
- Proxy images through a sanitizer that removes scripts
- Log and alert on anomalous JS execution in image contexts
- Educate users on phishing via shared media

## Objectives

1. Execute JS in the victim's browser session
2. Steal sensitive data like cookies or tokens
3. Achieve account compromise or further persistence

## Instructions

### Step 1: Obtain SVG URL

**Context**: Locate the direct link to the uploaded SVG for access.

After upload, note the file URL from the CMS, e.g., `https://airshipcms.example.com/uploads/xss.svg`. If shared, use the shared link.

### Step 2: View in Browser

**Context**: Render the SVG in a browser to trigger parsing and JS execution.

Open the URL in a browser tab or embed in an <img> tag on a page. The browser will fetch and parse it as SVG, executing the onload or script content.

For testing, visit the URL directly and check dev tools (Console/Network) for execution.

**Expected Output**: JS runs, e.g., alert box or HTTP request to attacker server with stolen data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- javascript
- svg-execution

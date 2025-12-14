---
tags:
  - recon
  - file-upload
  - xss
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
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:52:55.143Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c90d7396-4818-4648-a03c-08e5aca33f89
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Vulnerable-File-Upload

## Summary

This procedure involves scouting the TikTok ads ticketing platform to locate file upload features and verify insufficient validation for potentially malicious file types like SVG, setting the stage for XSS exploitation.

## Description

In the context of the ads.tiktok.com subdomain, attackers authenticate and navigate the ticketing interface to find upload endpoints. The vulnerability arises from no MIME type checks or content parsing, allowing SVG files with JavaScript. This reconnaissance confirms the attack surface without triggering alerts.

## Requirements

1. Authenticated access to ads.tiktok.com
2. Web browser with developer tools
3. Basic understanding of web forms and HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement file type whitelisting and content scanning on uploads
- Monitor for anomalous file uploads in ticketing logs
- Use WAF rules to block SVG with script tags

## Objectives

1. Locate upload functionality in ticketing platform
2. Confirm acceptance of SVG files without validation
3. Identify endpoint for subsequent exploitation

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Gain access to the platform and explore the interface.

Log in to ads.tiktok.com and proceed to the ticketing or support section. Look for attachment options in forms.

### Step 2: Inspect Upload Mechanism

**Context**: Analyze the upload feature for weaknesses.

Open developer tools (F12), go to Network tab, and attempt to upload a test SVG file (e.g., empty <svg></svg>). Check request headers and responses for validation checks.

**Expected Output**: Upload succeeds with HTTP 200, no rejection based on file type.

### Step 3: Test File Rendering

**Context**: Verify if uploaded files are rendered as HTML/SVG.

Upload a benign SVG and view it in a ticket; confirm browser parses it as vector graphics, potentially allowing script execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
- [[xss]]

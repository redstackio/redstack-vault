---
tags:
  - recon
  - web-analysis
  - endpoint-discovery
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-analyze-endpoint]]'
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 28acd8b8-2578-4861-8141-cbc289e5e959
created_at: '2025-12-14T05:32:13.800Z'
updated_at: '2025-12-14T05:32:13.800Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-File-Upload-Endpoint

## Summary

This procedure involves inspecting the network traffic and behavior of the .ashx upload endpoint on mobile.starbucks.com.sg to identify its file handling mechanisms and confirm the absence of type restrictions, setting the stage for exploitation.

## Description

In the context of the Starbucks mobile site vulnerability, the .ashx endpoint is an ASP.NET generic handler intended for image uploads but lacks server-side validation. By analyzing requests during normal usage (e.g., profile picture uploads), attackers can uncover the endpoint's URL, accepted methods, and parameters. This reconnaissance step is crucial to understand the attack surface without triggering alerts, using tools like browser dev tools or curl to mimic legitimate traffic.

## Requirements

1. Public access to https://mobile.starbucks.com.sg
2. Browser with developer tools or curl installed
3. Basic understanding of HTTP requests and multipart forms

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to log anomalous endpoint access
- Monitor server logs for unusual GET/POST patterns on upload handlers
- Enforce client-side and server-side file type whitelisting

## Objectives

1. Identify the exact .ashx endpoint URL and parameters
2. Confirm no immediate validation on file types
3. Gather evidence for vulnerability reporting or exploitation planning

## Instructions

### Step 1: Inspect Legitimate Upload

**Context**: Simulate a normal image upload to capture the endpoint details.

**Command** ([[commands/curl-analyze-endpoint]]):
```bash
curl -X GET https://mobile.starbucks.com.sg/upload.ashx -v
```

> This sends a verbose GET request to probe the endpoint, revealing headers and any error messages indicating file handling capabilities. Expected output includes server response headers confirming ASP.NET environment.

### Step 2: Monitor Network Traffic

**Context**: Use browser dev tools to observe a real upload and note form data structure.

**Command** (No specific command; use browser):

> Open developer tools (F12), navigate to the upload feature, and submit an image. Look for POST to /upload.ashx with multipart/form-data.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-analyze-endpoint]]

## Tools Used


## Tags

- [[recon]]
- [[web-analysis]]

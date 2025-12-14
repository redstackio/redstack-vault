---
id: proc-uuid-3
tags:
  - intercept
  - proxy
  - burp-suite
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:28:51.876Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Intercept-Upload-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture the HTTP POST request from the Nextcloud theming upload, allowing inspection of vulnerable parameters like 'key'.

## Description

Burp Suite acts as a man-in-the-middle proxy to intercept web traffic. During the upload initiation, the tool captures the request, revealing the 'key' parameter that controls the filename. This is essential for the subsequent modification step and works on any web-based Nextcloud setup. The interception provides visibility into the request structure, including headers, form data, and the uploaded file.

## Requirements

1. Burp Suite installed and running
2. Browser configured to use Burp as proxy (e.g., 127.0.0.1:8080)
3. Upload initiated from theming page

## Defense

Defensive measures and detection strategies:

- Enforce certificate pinning to prevent proxy interception
- Monitor network traffic for proxy-like anomalies
- Use endpoint detection to identify proxy tool signatures

## Objectives

1. Capture the full upload request
2. Inspect parameters for vulnerabilities
3. Prepare for modification without alerting the server

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp to intercept traffic from the browser.

No specific command; in Burp, go to Proxy > Options and ensure intercept is on for the target scope (e.g., localhost).

> Install Burp's CA certificate in the browser to handle HTTPS.

### Step 2: Trigger and Intercept

**Context**: Perform the upload to catch the request.

No specific command; from the theming page, upload the file while Burp is intercepting.

> Request appears in Burp's Proxy > Intercept tab, showing POST /settings/admin/theming with 'key' in the body.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[proxy]]
- [[tools/Burp-Suite]]
- [[web]]

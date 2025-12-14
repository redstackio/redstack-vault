---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - dos
  - web-hosting
  - chrome
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Chrome Browser Extension
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.871Z'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Navigate-to-Site-Hosting-Large-File

## Summary

This procedure hosts the oversized security.txt file on a local web server and navigates to it in Chrome, initiating pre-flight fetches that increase resource utilization in preparation for extension triggering.

## Description

To exploit the vulnerability, serve the 1-2 GB file via a simple HTTP server and open its URL in a Chrome tab. This step triggers initial network and CPU load from loading the large file, setting the stage for the extension's AJAX call to process it fully, resulting in self-DoS without broader impact.

## Requirements

1. The large-security.txt file prepared from prior procedure
2. Python 3 installed for http.server (or equivalent like nginx/apache)
3. Chrome browser with dev tools for monitoring

## Defense

Defensive measures and detection strategies:

- Use content-length checks in servers to reject oversized files
- Browser extensions should validate response sizes before processing
- Log and alert on large static file requests

## Objectives

1. Expose the large file via HTTP at a accessible URL
2. Load the URL in Chrome to confirm fetch behavior
3. Observe initial resource spikes without full crash

## Instructions

### Step 1: Start Local Web Server

**Context**: Host the file directory to make it available over HTTP.

**Command** (using Python http.server):
```bash
cd /path/to/large-security.txt/directory
python3 -m http.server 8000
```

> Server starts on port 8000. Expected output: "Serving HTTP on 0.0.0.0 port 8000" message.

### Step 2: Access URL in Chrome

**Context**: Open the file URL to trigger download/pre-flight, monitoring network tab for traffic.

**Instructions**: In Chrome, navigate to `http://localhost:8000/large-security.txt`. Open DevTools (F12) > Network tab to watch the request.

> Expected output: Request starts, shows large content-length, CPU/network usage rises.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dos]]
- [[web-hosting]]

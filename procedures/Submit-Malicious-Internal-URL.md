---
tags:
  - ssrf
  - exploitation
  - internal-url
type: procedure
tools:
  - '[[tools/Uppy]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.565Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1164570d-5646-49c0-a582-789a3928c1a8
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Malicious-Internal-URL

## Summary

This procedure exploits the SSRF vulnerability by submitting an internal URL through the Uppy interface, causing the Companion server to fetch it without validation and embed the response in an uploadable file.

## Description

The /get endpoint in Companion's url.js passes req.body.url directly to downloadURL, allowing fetches to internal endpoints like AWS metadata (169.254.169.254) or local services (127.0.0.1:3000). This triggers server-side requests to restricted resources, enabling network scanning, file reads, or interactions with services like Redis. The procedure uses the Uppy URL plugin to send the malicious URL, completing the upload to a Tus endpoint while the server processes the internal fetch.

## Requirements

1. Running Uppy HTML interface and Companion server
2. Access to internal network (e.g., deployed on cloud instance with metadata)
3. Target internal URL (e.g., http://169.254.169.254/metadata/v1/ for AWS IMDS)
4. Browser with no URL restrictions

## Defense

Defensive measures and detection strategies:

- Sanitize URLs in Companion code: check protocols (only HTTPS), block private IPs (RFC 1918), and whitelist hosts
- Enable request logging and alert on internal fetches
- Use VPC endpoints or disable IMDSv1 in cloud environments
- Deploy WAF rules to block SSRF patterns in upload proxies

## Objectives

1. Trigger SSRF to fetch internal content
2. Complete upload with embedded response
3. Enable subsequent exfiltration

## Instructions

### Step 1: Interact with Dashboard

**Context**: Use the Uppy UI to input and submit the malicious URL.

**Instructions**: Click 'Add More' > 'Link', enter http://169.254.169.254/metadata/v1/, then click 'Upload'.

> Expected: Progress bar advances; no rejection of internal URL.

### Step 2: Monitor Server Response

**Context**: Observe Companion logs for the fetch attempt.

**Instructions**: Check terminal running companion for debug output showing the internal request.

> Expected: Logs indicate successful fetch (e.g., 200 OK from metadata).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Uppy]]

## Tags

- ssrf
- exploitation
- internal-url

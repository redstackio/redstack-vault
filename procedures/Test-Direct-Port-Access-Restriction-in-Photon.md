---
id: proc-001
tags:
  - ssrf
  - testing
  - photon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.061Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Direct-Port-Access-Restriction-in-Photon

## Summary

This procedure tests the direct access restrictions in the WordPress Photon service by attempting to request an image from a non-standard port on an internal IP, confirming the validation filter blocks it with a 400 error.

## Description

The Photon service at http://i0.wp.com/ uses PHP and cURL for image optimization. Direct requests to non-standard ports are blocked via validation in index.php (line 142) using parse_url() and port checks. This step verifies the restriction before attempting bypasses. Prerequisites include public access to i0.wp.com and a test internal IP/port setup.

## Requirements

1. Public internet access to http://i0.wp.com/
2. A test endpoint like http://159.203.190.123:666/new.php (non-existent or controlled)
3. Browser or curl for requests

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation to block non-standard ports and internal IPs
- Log all cURL requests and monitor for suspicious redirects
- Use WAF rules to detect port scans via image endpoints

## Objectives

1. Confirm port blocking mechanism
2. Identify validation error messages
3. Prepare for bypass testing

## Instructions

### Step 1: Craft and Send Direct Request

**Context**: Send a request to Photon with an internal IP and non-standard port in the URL path, using resize parameters to trigger processing.

No specific command needed; use browser or curl:

```bash
curl "http://i0.wp.com/159.203.190.123:666/new.php?resize=0,1"
```

> This triggers the filter in index.php line 142, returning a 400 Bad Request: 'Sorry, the parameters you provided were not valid'. To bust cache, modify to ?resize=0,2 or add params.

### Step 2: Verify Response

**Context**: Check the response for the expected error, confirming the restriction.

Inspect the HTTP response status and body.

**Expected Output**: HTTP/1.1 400 Bad Request with error message.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[photon]]

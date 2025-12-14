---
id: proc-uuid-001
tags:
  - recon
  - apache
  - version-detection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-get-server-header]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:26:37.023Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-Vulnerable-Apache-Version

## Summary

This procedure identifies the Apache HTTP Server version on a target web server by inspecting the Server response header, allowing confirmation of vulnerability to CVE-2011-3192 in versions prior to 2.2.20.

## Description

In the attack scenario, reconnaissance is performed on a public-facing web application like owncloud.com. By sending a simple HTTP HEAD or GET request, the Server header discloses the version (e.g., Apache 2.2.17). This step is crucial as it confirms the target is unpatched and susceptible to Range header DoS, where overlapping byte ranges cause excessive CPU and memory usage during request parsing. Prerequisites include network access to the target on port 80/443; no authentication is needed. Expected outcome: Version disclosure enabling further exploitation.

## Requirements

1. Network connectivity to target host on port 80 or 443
2. curl or similar HTTP client installed
3. Basic knowledge of HTTP headers

## Defense

Defensive measures and detection strategies:

- Configure Apache to suppress ServerTokens (set ServerTokens Prod) to hide version info
- Use web application firewalls (WAF) to block header inspection attempts
- Monitor access logs for unusual HEAD/GET requests to root path

## Objectives

1. Gather server version information for vulnerability assessment
2. Confirm exploitability without alerting the target
3. Establish baseline for DoS testing

## Instructions

### Step 1: Send HEAD Request for Headers

**Context**: Use a lightweight HEAD request to retrieve headers without downloading the body, focusing on the Server field.

**Command** ([[commands/curl-get-server-header]]):
```bash
curl -I http://owncloud.com/
```

> This command sends an HTTP HEAD request and outputs response headers. Look for the "Server:" line to identify the Apache version. Expected output includes "Server: Apache/2.2.17 (Ubuntu)" or similar, confirming vulnerability if < 2.2.20.

### Step 2: Verify with Full GET if Needed

**Context**: If HEAD is blocked or incomplete, fall back to a full GET request.

**Command** ([[commands/curl-normal-get]]):
```bash
curl -v http://owncloud.com/
```

> The -v flag enables verbose output, showing full request/response including headers. Success is indicated by clear version disclosure in the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- [[Software]] Software

## Commands Used

- [[commands/curl-get-server-header]]
- [[commands/curl-normal-get]]

## Tools Used


## Tags

- recon
- apache
- version-detection

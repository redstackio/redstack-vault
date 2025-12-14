---
id: proc-3
tags:
  - curl
  - dos
  - memory-exhaustion
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-trigger-dos]]'
verified: false
platforms:
  - Linux
  - Unix-like
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:37.120Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Trigger-curl-Memory-Exhaustion-with-Excessive-Cookies

## Summary

This procedure loads the populated cookie jar and requests a different subdomain via the malicious server, causing curl to apply all domain cookies and exceed memory limits, resulting in CURLE_OUT_OF_MEMORY DoS.

## Description

Building on prior steps, curl loads 256 large cookies from cookie.txt when requesting targetedsite.hax.invalid (same domain). The domain-wide scope forces allocation beyond DYN_HTTP_REQUEST, exhausting memory. Affects unprivileged HTTP/HTTPS ports; discovered via analysis of curl's unlimited cookie handling.

## Requirements

1. cookie.txt from previous procedure with excessive cookies
2. Malicious server running on 127.0.0.1:9000
3. Vulnerable curl installation

## Defense

Defensive measures and detection strategies:

- Upgrade curl to 7.84.0+ with cookie limits
- Monitor process memory usage for curl spikes
- Block or throttle excessive cookie responses at proxy/firewall

## Objectives

1. Apply domain cookies to new subdomain request
2. Cause memory allocation failure in curl
3. Achieve client-side DoS

## Instructions

### Step 1: Execute curl to Load and Trigger

**Context**: Use curl to load cookies and fetch the target endpoint, proxying to the server to simulate cross-subdomain application.

**Command** ([[commands/curl-trigger-dos]]):
```bash
curl -c cookie.txt -b cookie.txt --connect-to targetedsite.hax.invalid:80:127.0.0.1:9000 http://targetedsite.hax.invalid/
```

> Command loads/saves cookies and redirects host. Expected output: curl error "Failed to connect or similar, but primarily CURLE_OUT_OF_MEMORY due to ~1MB+ allocation for cookies exceeding dynamic limits."

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]
- [[OS Exhaustion Flood]]

### Sub-Techniques

- [[OS Exhaustion Flood]]

## Commands Used

- [[commands/curl-trigger-dos]]

## Tools Used

- [[tools/curl]]

## Tags

- curl
- dos
- memory-exhaustion

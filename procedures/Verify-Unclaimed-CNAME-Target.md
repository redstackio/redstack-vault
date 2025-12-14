---
id: p-verify-unclaimed-cname
tags:
  - dns
  - verification
  - misconfiguration
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-http-check]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:49.242Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify Unclaimed CNAME Target

## Summary

This procedure confirms whether a CNAME target from a subdomain is unclaimed on the third-party hosting service, setting the stage for takeover by checking for active registration or availability.

## Description

Following DNS enumeration, probe the target resource on services like ███████ to see if it's registered. In the firefox.com case, this revealed an unclaimed pointer to www.mozilla.org hosted externally. Expected outcomes include confirmation of exploitability without triggering alerts.

## Requirements

1. Identified CNAME target from prior recon
2. Access to the third-party service's public interface
3. HTTP probing capability

## Defense

Defensive measures and detection strategies:

- Monitor third-party service logs for probe attempts
- Automate resource cleanup on expiration
- Use DNSSEC for integrity checks

## Objectives

1. Confirm resource availability for claiming
2. Assess ownership status
3. Avoid false positives on active sites

## Instructions

### Step 1: Probe HTTP Response

**Context**: Send a HEAD request to the potential resource URL to check status.

**Command** ([[commands/curl-http-check]]):
```bash
curl -I http://target-resource.███████
```

> Expected output: 404, claim prompt, or no content, indicating unclaimed.

### Step 2: Manual Service Check

**Context**: Log into the service dashboard to search for the resource.

No command; use web browser to access ███████ and query the domain.

> Look for 'available' or 'register now' indicators.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Sub-Techniques


## Commands Used

- [[commands/curl-http-check]]

## Tools Used


## Tags

- [[DNS]]
- [[verification]]

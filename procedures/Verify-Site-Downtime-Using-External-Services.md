---
id: proc-uuid-5
tags:
  - verification
  - downtime
type: procedure
tools:
  - '[[tools/isup.me]]'
  - '[[tools/check-host.net]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T05:32:10.115Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify Site Downtime Using External Services

## Summary

This procedure uses third-party web services to externally confirm if the target site is experiencing downtime or connectivity issues during or after the DoS attack.

## Description

Tools like isup.me and check-host.net provide vantage-point checks outside the attacker's network, validating the impact of resource exhaustion by reporting on HTTP availability and response times.

## Requirements

1. Internet access to external monitoring sites
2. Target URL (e.g., https://staging.uzbey.com)
3. Timing during active DoS

## Defense

Defensive measures and detection strategies:

- Monitor uptime with internal tools alongside externals
- Set alerts for detected downtimes
- Correlate with server logs for attack attribution

## Objectives

1. Confirm DoS effectiveness externally
2. Document unavailability duration
3. Validate attack success

## Instructions

### Step 1: Query isup.me

**Context**: Check basic uptime from global vantage points.

Visit http://isup.me/staging.uzbey.com/ and submit.

> Expected: "Site is down" message if attack succeeds.

### Step 2: Use check-host.net for Detailed Check

**Context**: Get precise HTTP response and timing data.

Go to http://check-host.net/check-http?host=https://staging.uzbey.com/ and run check.

> Expected: Reports of timeouts or failures confirming downtime.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/isup.me]]
- [[tools/check-host.net]]

## Tags

- [[verification]]
- [[downtime]]

---
id: proc-monitor-disruption
tags:
  - dos
  - monitoring
  - confirmation
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:56.716Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Monitor and Confirm Service Disruption

## Summary

This procedure observes the effects of the DoS flood by checking for error responses and external user reports, validating the attack's impact on service availability.

## Description

Post-flood, this monitors the web application's responsiveness, expecting progression from 500 errors (internal processing failure) to 502/504 (gateway overload). In a real scenario like HackerOne, community feedback (e.g., Discord) confirms widespread disruption. Targets any web service; requires no special tools beyond browser/network monitoring.

## Requirements

1. Access to the affected application pages
2. Ability to reload and observe HTTP responses (browser dev tools)
3. Community channels for cross-verification (if applicable)

## Defense

Defensive measures and detection strategies:

- Set up real-time alerting for error rate spikes (500/502/504)
- Use load balancers with auto-scaling to mitigate floods
- Correlate logs with external reports for incident confirmation

## Objectives

1. Detect immediate error indicators from resource exhaustion
2. Verify broader impact through user feedback
3. Document evidence of successful DoS

## Instructions

### Step 1: Observe Local Errors

**Context**: Check personal session for failure signs.

**Instructions**: Reload scope management or other pages; inspect network tab for status codes.

> Expected output: HTTP 500 initially, then 502/504 with timeouts; pages fail to load.

### Step 2: Gather External Confirmation

**Context**: Validate if disruption affects others.

**Instructions**: Query community (e.g., Discord) for reports of delays/errors during the attack window.

> Expected output: User confirmations of service issues, e.g., "Site is down for me too."

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dos]]
- [[monitoring]]
- [[confirmation]]

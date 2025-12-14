---
id: proc-1
tags:
  - sqli
  - recon
  - baseline
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-baseline-tag-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.907Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Establish Baseline Response Time for Tag Endpoint

## Summary

This procedure measures the normal response time of the Serendipity tag endpoint to provide a reference for detecting artificial delays introduced by SQL injection payloads.

## Description

In a blind time-based SQL injection attack, establishing a baseline is crucial to differentiate normal server latency from injection-induced delays. This targets the /plugin/tag/ endpoint in Serendipity CMS, using a legitimate tag query to record typical response times, typically around 0.28 seconds on the target https://betterscience.org.

## Requirements

1. Network access to the target web application over HTTPS (port 443)
2. curl or similar HTTP client
3. No authentication required for public endpoints

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and prepared statements in PHP/SQL queries
- Monitor for unusual response time spikes in web server logs
- Use Web Application Firewalls (WAF) to detect SQL payload patterns

## Objectives

1. Record normal query execution time
2. Validate endpoint accessibility
3. Set threshold for delay detection (e.g., >1s anomaly)

## Instructions

### Step 1: Send Legitimate Tag Request

**Context**: Query the endpoint with a valid tag to measure baseline latency.

**Command** ([[commands/curl-baseline-tag-request]]):
```bash
curl -s -w "%{time_total}s" "https://betterscience.org/plugin/tag/peerj" > /dev/null
```

> This command fetches articles tagged 'peerj' silently and prints the total time. Expected baseline: ~0.28s. Repeat 3-5 times for average.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-baseline-tag-request]]

## Tools Used


## Tags

- [[sqli]]
- [[recon]]

---
id: proc-amplify-dos-repeated-requests
name: Amplify DoS with Repeated Requests
tags:
  - dos
  - amplification
  - wordpress
type: procedure
tools:
  - '[[tools/Apache-JMeter]]'
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:36.828Z'
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Amplify DoS with Repeated Requests

## Summary

This procedure scales the CVE-2018-6389 exploitation by sending multiple concurrent requests to /wp-admin/load-scripts.php, overwhelming the server due to absent rate-limiting and causing full denial-of-service.

## Description

Building on the single-request impact, rapid repetition (e.g., 50+ threads) exploits the endpoint's inefficiency, leading to cumulative resource exhaustion on the PHP application server. Tested on unpatched WordPress sites, this results in site-wide unavailability.

## Requirements

1. Successful single-request test.
2. [[tools/Apache-JMeter]] configured with the crafted request.
3. Server monitoring tools (optional) to observe impact.

## Defense

Defensive measures and detection strategies:

- Deploy rate-limiting (e.g., 10 req/min per IP) using Apache mod_ratelimit or Cloudflare.
- Use intrusion detection systems (IDS) to flag burst traffic to admin endpoints.
- Regularly audit server logs for repeated load-scripts.php hits.

## Objectives

1. Overload server resources through volume.
2. Achieve sustained DoS condition.
3. Validate attack efficacy.

## Instructions

### Step 1: Scale Thread Group in JMeter

**Context**: Increase concurrency to simulate a flood.

In JMeter, edit Thread Group: Number of Threads = 50, Ramp-up Period = 1 second, Loop Count = Forever (or 100).

### Step 2: Execute and Monitor

**Context**: Run the test to amplify the attack.

Start the test and observe target site response times increasing to timeouts. Use tools like top or server metrics for CPU >90%.

**Expected Output**: Server overload, site errors (e.g., 503), unresponsive application.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Impact

### Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Flood

### Sub-Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Flood

## Commands Used


## Tools Used

- [[tools/Apache-JMeter]]

## Tags

- [[dos]]
- [[rate-limiting-bypass]]

---
tags:
  - dos
  - load-testing
  - jmeter
type: procedure
tools:
  - '[[tools/Apache-JMeter]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:55.851Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5fbc0614-a38a-47dc-810b-9ab4f58bbd56
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Simulate-DoS-Attack-with-Apache-JMeter

## Summary

This procedure uses Apache JMeter to simulate a denial-of-service attack on the vulnerable WordPress load-scripts.php endpoint by sending multiple concurrent requests, demonstrating resource exhaustion and potential site downtime.

## Description

By configuring JMeter to replicate high-volume traffic to the endpoint with the 'load' parameter, this simulates a DoS attack scalable to DDoS. Each request forces the server to concatenate and serve ~3MB of JavaScript, spiking CPU and memory usage. Applicable to any exposed WordPress instance without mitigations, as verified on targets like nordvpn.com.

## Requirements

1. Apache JMeter installed and configured
2. Verified vulnerable endpoint from prior steps
3. Monitoring tools for server impact (optional)

## Defense

Defensive measures and detection strategies:

- Deploy rate-limiting and request throttling at the web server level (e.g., nginx limit_req)
- Use intrusion detection systems (IDS) to flag high-volume requests to admin paths
- Patch WordPress and monitor for CVE-2018-6389 indicators like repeated large JS responses

## Objectives

1. Overload server resources via concurrent requests
2. Observe and measure DoS impact (e.g., response delays, crashes)
3. Validate scalability for real-world attacks

## Instructions

### Step 1: Create JMeter Test Plan

**Context**: Set up a Thread Group in JMeter to simulate multiple users.

- Add Thread Group: 100 threads, 1-second ramp-up, infinite loop.
- Add HTTP Request Sampler: Method GET, Path /wp-admin/load-scripts.php, Parameters: load=[comma-separated handles].

### Step 2: Configure and Run Test

**Context**: Execute the plan to flood the endpoint and monitor results.

Save as dos-test.jmx and run via JMeter GUI or command line: `jmeter -n -t dos-test.jmx -l results.jtl`.

**Expected Output**: JMeter listeners show increasing response times (>10s) and errors; target site may timeout.

### Step 3: Analyze Impact

**Context**: Review server-side effects if accessible, or observe site downtime.

Check for high CPU/memory via tools like top or New Relic.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Apache-JMeter]]

## Tags

- [[dos]]
- [[load-testing]]

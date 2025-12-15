---
tags:
  - dos
  - concurrent
  - flood
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.788Z'
sub_techniques:
  - '[[OS Exhaustion Flood]]'
id: 66a99846-6f6d-49a9-bd5d-27540ebaa982
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Send-Concurrent-Unicode-Payloads-for-DoS

## Summary

This procedure sends multiple concurrent POST requests with large Unicode payloads to cause denial of service through resource exhaustion.

## Description

Using Burp Suite's Intruder or Turbo Intruder, launch 20 simultaneous requests to the admin login. This amplifies the normalization delays, leading to 60-second waits and 504 timeouts, effectively DoS-ing the server.

## Requirements

1. Verified single-request delay
2. Burp Suite with concurrency support
3. Vulnerable Django on Windows

## Defense

Defensive measures and detection strategies:

- Deploy WAF to block large or malformed inputs
- Use load balancers with health checks
- Scale resources or isolate login processing

## Objectives

1. Overwhelm server with concurrent normalization tasks
2. Induce timeouts and service unavailability
3. Demonstrate impact on UsernameField forms

## Instructions

### Step 1: Configure Concurrent Requests

**Context**: Set up Burp for multiple threads.

In Burp Intruder, load the payload request, set positions for concurrency, and configure 20 threads.

### Step 2: Launch Attack

**Context**: Send simultaneous requests.

Start the attack in Burp, targeting the username field with the large '¾' payload.

> Expected output: Requests hang for 60 seconds, resulting in 504 errors; server becomes unresponsive to further traffic.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques

- [[OS Exhaustion Flood]]

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- dos
- concurrent
- flood

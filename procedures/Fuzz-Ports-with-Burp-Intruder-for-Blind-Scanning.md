---
id: proc-nextcloud-fuzz-ports-intruder
tags:
  - port-scan
  - blind
  - fuzzing
  - intruder
type: procedure
tools:
  - '[[tools/Burp-Intruder]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/JSON-Payload-SSRF-Localhost]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:39:09.877Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Fuzz-Ports-with-Burp-Intruder-for-Blind-Scanning

## Summary

This procedure uses Burp Intruder to fuzz the sievePort parameter across port ranges, detecting open internal services via response time differences in the Blind SSRF.

## Description

With the SSRF triggered, fuzzing sievePort from 1-65535 sends multiple requests, where the server's connection attempt to open ports causes delays. Thresholds (<100ms closed, >5000ms open) allow mapping of services like SSH (22), MySQL (3306), PostgreSQL (5432), and Redis (6379). This provides reconnaissance for pivoting to further exploits like RCE on vulnerable internals.

## Requirements

1. Modified SSRF request from prior procedure loaded in Burp.
2. Burp Intruder configured with port payload list.
3. Patience for ~65k requests; rate limiting awareness.

## Defense

Defensive measures and detection strategies:

- Rate-limit API endpoints to prevent fuzzing abuse.
- Monitor server logs for repeated internal connection failures/timeouts.
- Deploy internal firewalls to block application-originated probes.

## Objectives

1. Identify open ports on internal hosts.
2. Map services for targeted follow-on attacks.
3. Achieve network reconnaissance without direct access.

## Instructions

### Step 1: Set Up Intruder Payload

**Context**: Position payload on sievePort in the JSON and load port numbers.

Use [[commands/JSON-Payload-SSRF-Localhost]] as base, mark sievePort as §port§:

```json
{"sieveEnabled":true,"sieveHost":"127.0.0.1","sievePort":"§port§","sieveUser":"","sievePassword":"","sieveSslMode":"none"}
```

> In Intruder, add numbers payload 1-65535. Start attack.

### Step 2: Analyze Response Times

**Context**: Sort results by response time to flag open ports.

No command; review in Burp.

> Filter delays >5000ms; correlate with known services (e.g., 6379 for Redis).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/JSON-Payload-SSRF-Localhost]]

## Tools Used

- [[tools/Burp-Intruder]]

## Tags

- port-fuzzing
- blind-scan
- response-timing

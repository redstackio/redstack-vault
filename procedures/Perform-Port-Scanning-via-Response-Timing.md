---
id: proc-tumblr-port-scan-001
tags:
  - ssrf
  - port-scanning
  - timing-attack
  - tumblr
type: procedure
tools:
  - '[[tools/Burp-Suite-Intruder]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/burp-intruder-fuzz]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:09.727Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Vulnerability Scanning]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Perform-Port-Scanning-via-Response-Timing

## Summary

This procedure uses fuzzing on the 'url' parameter with port variations to scan internal services blindly, leveraging response time differences to detect open ports and potentially exhaust resources.

## Description

Blind SSRF enables port scanning by sending requests to http://127.0.0.1:{port}/ and measuring delays: open ports cause connection attempts (slower), closed ones return quickly. Tools like Burp Intruder automate fuzzing with payloads for common ports (e.g., 22, 80, 9090). High-volume requests can lead to DoS on internal services.

## Requirements

1. Proxy with intruder capability
2. List of ports to scan (e.g., 1-1024, focus on 9090)
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Block localhost/internal URL patterns at the application layer
- Implement response time normalization or timeouts
- Alert on bursty API usage or unusual parameter values

## Objectives

1. Map open internal ports
2. Infer service presence
3. Demonstrate resource impact

## Instructions

### Step 1: Configure Fuzzing Payloads

**Context**: Set up intruder to vary the port in 'url'.

In Burp, mark §port§ in url=http://127.0.0.1:§port§/ and load payloads (e.g., 9090, 8080).

### Step 2: Launch Attack

**Context**: Send requests and sort by response time.

**Command** ([[commands/burp-intruder-fuzz]]):
```bash
# Burp Intruder is GUI-based; simulate via script or note: Use Intruder > Start Attack with Sniper mode on port position
```

> Results table: Ports with >300ms responses likely open (e.g., 9090 open).

### Step 3: Analyze and Escalate

**Context**: Identify open ports; repeat for bulk exhaustion.

No command; export results.

> Open ports: 9090 (delayed); use for targeted SSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

## Commands Used

- [[commands/burp-intruder-fuzz]]

## Tools Used

- [[tools/Burp-Suite-Intruder]]

## Tags

- ssrf
- port-scanning
- timing-attack
- tumblr

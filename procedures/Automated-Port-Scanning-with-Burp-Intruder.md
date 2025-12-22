---
id: proc-4
name: Automated-Port-Scanning-with-Burp-Intruder
tags:
  - ssrf
  - port-scan
  - automated
  - fuzzing
type: procedure
tools:
  - '[[tools/Burp-Suite-Intruder]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/modified-port-scan-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:39:09.959Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Automated-Port-Scanning-with-Burp-Intruder

## Summary

This procedure automates the port scanning process using Burp Intruder's fuzzing capabilities to test multiple imapPort values efficiently, identifying open internal services based on response times.

## Description

Burp Intruder fuzzer positions the payload on imapPort with a list of common ports (e.g., 80, 443, 8080, 6060, 5432, 6379), sending requests while imapHost remains '127.0.0.1' and ssl modes 'none'. Results are sorted by response time or length to distinguish open from closed ports, scaling the manual scan for comprehensive reconnaissance.

## Requirements

1. Base request from manual scan procedure
2. Port list file (e.g., ports.txt with 80,443,etc.)
3. Burp Suite Professional for Intruder

## Defense

Defensive measures and detection strategies:

- Rate-limit requests to /apps/mail/api/accounts
- Monitor for high-volume similar requests (fuzzing patterns)
- Deploy IDS to detect port scan-like traffic from application servers

## Objectives

1. Automate scanning of multiple ports
2. Identify open services (e.g., Redis on 6379)
3. Gather intel for targeted internal attacks

## Instructions

### Step 1: Set Up Intruder Attack

**Context**: Configure the fuzzer with payload on imapPort.

**Command** ([[commands/modified-port-scan-payload]]):

In Burp Intruder, send to Intruder, mark §imapPort§ as payload position, load ports list.

```bash
# Base payload (fuzzed on imapPort)
{"imapHost":"127.0.0.1","imapPort":§80§,"imapSslMode":"none",...}
```

> Launch attack with timing configuration.

### Step 2: Analyze Intruder Results

**Context**: Sort by response time to identify opens.

No command; use Intruder results table.

> Filter for >1000ms responses (e.g., 80: Apache2, 5432: PostgreSQL). Success: Mapped open ports and services.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/modified-port-scan-payload]]

## Tools Used

- [[tools/Burp-Suite-Intruder]]

## Tags

- ssrf
- port-scan
- automated
- fuzzing

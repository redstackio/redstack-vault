---
id: proc-3
name: Manual-Port-Scan-on-Localhost
tags:
  - ssrf
  - port-scan
  - manual
  - localhost
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T04:39:09.961Z'
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
# Manual-Port-Scan-on-Localhost

## Summary

This procedure exploits the SSRF to manually scan ports on localhost (127.0.0.1) by varying the imapPort parameter and measuring response times, identifying open internal services.

## Description

With imapSslMode set to 'none' to avoid delays, repeated POST requests with different imapPort values (e.g., 80, 443, 5432) cause the server to attempt connections. Open ports result in longer response times (>1000ms) due to connection establishment, while closed ports respond quickly (<100ms). This enables blind reconnaissance of services like Apache2 and databases without direct access.

## Requirements

1. Confirmed SSRF from previous procedure
2. List of target ports (e.g., 80, 443, 8080, 5432, 6379)
3. Timing tool or manual stopwatch for responses

## Defense

Defensive measures and detection strategies:

- Validate and allowlist internal IPs/ports for IMAP connections
- Implement response time anomaly detection in application logs
- Use network segmentation to isolate application servers from internal services

## Objectives

1. Identify open ports on localhost
2. Map internal services for reconnaissance
3. Detect services like PostgreSQL and Redis

## Instructions

### Step 1: Prepare Modified Payload

**Context**: Set imapHost to localhost and ssl modes to none.

**Command** ([[commands/modified-port-scan-payload]]):

In Burp Repeater:

```bash
# Payload for port 80 example
{"imapHost":"127.0.0.1","imapPort":80,"imapSslMode":"none","imapUser":"user@example.com","imapPassword":"pass","smtpSslMode":"none","smtpUser":"user@example.com","smtpPassword":"pass","accountName":"user@example.com","emailAddress":"user@example.com"}
```

> Send request and time the response. Repeat for other ports.

### Step 2: Analyze Response Times

**Context**: Compare timings to infer port status.

No command; manual analysis.

> Closed ports: <100ms; Open ports: >1000ms (e.g., delay on 5432 indicates PostgreSQL). Success: Open ports identified.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/modified-port-scan-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ssrf
- port-scan
- manual
- localhost

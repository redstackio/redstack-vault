---
id: proc-verify-ssrf-netcat
tags:
  - ssrf
  - verification
  - port-scanning
type: procedure
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nc-listen-verbose]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:39:02.441Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Verify-SSRF-with-Netcat-Listener

## Summary

This procedure uses Netcat to listen on specified ports and capture incoming connections from the vulnerable application, verifying SSRF exploitation through observed protocol interactions from internal IPs.

## Description

After triggering SSRF, set up listeners on attacker-controlled ports to detect fetches from Slack's infrastructure (e.g., AWS IPs like 184.73.10.28). Supports protocols like HTTP, dict, gopher, ldap, telnet, pop3, revealing partial requests or responses. Enables timing-based port scanning and assessment of exploitable internal services.

## Requirements

1. Netcat (nc) installed on attacker server
2. Publicly accessible server with open ports (e.g., 6655, 6666)
3. Firewall allowing inbound TCP on test ports
4. Prior SSRF trigger from Step 1 procedure

## Defense

Defensive measures and detection strategies:

- Log and alert on unexpected outbound connections to unusual ports/protocols
- Implement network segmentation to limit internal service exposure
- Use IDS/IPS to detect protocol anomalies (e.g., dict over TCP)
- Rate-limit URL fetches in applications

## Objectives

1. Confirm SSRF by capturing backend connections
2. Analyze protocol-specific interactions for exploitation potential
3. Perform blind port scanning via response timing

## Instructions

### Step 1: Start Listener

**Context**: Initiate TCP listener on target port in verbose mode to log connections.

**Command** ([[commands/nc-listen-verbose]]):

```bash
nc -lvv 6655
```

> Listens on port 6655; expected output includes connection acceptance from Slack IP, e.g., 'Connection from 107.21.158.167 port 6655 [tcp/*] accepted' followed by request like 'CLIENT libcurl 7.22.0 picture-54679.jpg QUIT' for dict.

### Step 2: Trigger and Monitor

**Context**: After sending SSRF request, observe incoming data.

Run the listener before Step 1 of the attack chain. Vary ports (5555, 6655, 6666) and protocols. For each, note IP origins and interaction type (e.g., empty for telnet, 'QUIT' for pop3).

### Step 3: Analyze Output

**Context**: Review logs for Slack IPs and protocol details.

No command; manually inspect for AWS ranges (e.g., 54.197.108.234) and partial payloads indicating successful SSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques

-

## Commands Used

- [[commands/nc-listen-verbose]]

## Tools Used

- [[tools/nc]]

## Tags

- ssrf-verification
- netcat
- tcp-listener

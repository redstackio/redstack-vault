---
id: 5be83940-de36-4a10-849b-95d6e5ede9aa
type: procedure
verified: true
submitted: true
created_at: '2020-06-30T18:05:36.072614+00:00'
updated_at: '2023-05-26T00:49:55.141691+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Network Service Scanning]]'
sub_techniques: []
tags:
  - port-scan
  - masscan
  - network
platforms:
  - Linux
commands:
  - '[[commands/masscan-scan-ip-list-for-ports]]'
tools:
  - '[[tools/masscan]]'
validated: true
---

# Port-Scan-IP-List-with-Masscan

## Summary

This procedure employs Masscan to perform ultra-fast SYN scans on a list of discovered IPs across the full port range, identifying open ports for potential services.

## Description

Masscan is designed for internet-scale scanning, capable of 10M+ packets/sec. Input one IP per line; specify rate to avoid overwhelming networks (e.g., 1000-10000). Outputs in list format for easy parsing. Use after DNS recon to prioritize live hosts; focuses on discovery, not deep enumeration.

## Requirements

- IP list file (one per line)
- Masscan installed (from git or package)
- Root privileges for raw sockets

## Defense

- Intrusion detection for SYN flood patterns
- Firewall rules to drop unsolicited scans
- Rate limiting on perimeter firewalls

## Objectives

- Scan 100+ ports per IP in minutes
- Identify open TCP ports
- Generate parseable output

## Instructions

### Step 1: Execute IP List Scan

**Context**: Scan the full range (1-65535) at controlled rate.

**Command** ([[commands/masscan-scan-ip-list-for-ports]]):

```bash
masscan -iL $_IPS_FILE --rate $_RATE -p$_LOW_PORT-$_HIGH_PORT -oL $_OUTPUT_FILE
```

Use --rate=1000 for stealth; -oL for list output.

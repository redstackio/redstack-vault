---
tags:
  - dos
  - curl
  - cookies
  - memory-exhaustion
  - http
  - cve-2022-32205
type: attack_chain
tools:
  - '[[tools/Python-http-server]]'
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Linux
  - Unix-like
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Malicious-HTTP-Server-for-Excessive-Cookies]]'
  - '[[procedures/Populate-Cookie-Jar-with-Domain-Cookies-Using-curl]]'
  - '[[procedures/Trigger-curl-Memory-Exhaustion-with-Excessive-Cookies]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:37.127Z'
description: >-
  A multi-stage attack exploiting CVE-2022-32205 in curl by setting up a
  malicious server to send unlimited Set-Cookie headers, populating a cookie jar
  with domain-wide cookies, and triggering memory exhaustion when loading them
  for a different subdomain request.
skill_level: intermediate
impact_level: high
id: dbf11b68-8806-44e9-868f-f546f1461289
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# curl Denial of Service via Excessive Domain Cookies Leading to Memory Exhaustion

Multi-stage attack chain demonstrating CVE-2022-32205, where curl's cookie handling fails to limit domain-wide cookies, allowing an attacker to cause memory exhaustion and denial of service via CURLE_OUT_OF_MEMORY.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Up Malicious Server] --> B[Populate Cookies]
    B --> C[Trigger DoS]
    C --> D[Memory Exhaustion]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Python-http-server]]
- [[tools/curl]]

### Target Environment

- Linux or Unix-like OS with curl installed (vulnerable versions prior to 7.84.0)
- Ports 80 and 9000 available
- HTTP service simulation

### Initial Access Requirements

- Local network access to run server and curl
- No remote credentials needed; client-side exploitation

## Detailed Attack Procedures

### Step 1: Set Up Malicious Server
procedure: [[procedures/Set-Up-Malicious-HTTP-Server-for-Excessive-Cookies]]

**Objective**: Create a local HTTP server that responds with 256 excessive Set-Cookie headers to simulate a malicious host setting domain-wide cookies.

**Instructions**: Start the Python server using [[commands/python-server-excessive-cookies]] to listen on 127.0.0.1:9000 and send cookies with Domain=hax.invalid.

```bash
python server.py
```

**Expected Output**: Server running and responding to GET requests with 256 Set-Cookie headers, each with name f{i} and 4092 'A' characters.

**Success Indicators**:
- Server logs show HTTP 200 responses with Set-Cookie headers
- No errors on startup

### Step 2: Populate Cookie Jar
procedure: [[procedures/Populate-Cookie-Jar-with-Domain-Cookies-Using-curl]]

**Objective**: Use curl to fetch from a proxied malicious endpoint, saving the excessive domain cookies to a file for later use.

**Instructions**: Execute [[commands/curl-populate-cookies]] to connect to evilsite.hax.invalid via the local server and save cookies to cookie.txt.

```bash
curl -c cookie.txt -b cookie.txt --connect-to evilsite.hax.invalid:80:127.0.0.1:9000 http://evilsite.hax.invalid/
```

**Expected Output**: HTTP response body from server; cookie.txt populated with 256 cookies without errors.

**Success Indicators**:
- cookie.txt file created and contains multiple cookie entries
- curl completes without CURLE_OUT_OF_MEMORY

### Step 3: Trigger Memory Exhaustion
procedure: [[procedures/Trigger-curl-Memory-Exhaustion-with-Excessive-Cookies]]

**Objective**: Load the saved cookies and request a different subdomain, causing curl to allocate excessive memory for domain-wide cookies and trigger DoS.

**Instructions**: Run [[commands/curl-trigger-dos]] to fetch from targetedsite.hax.invalid, loading cookies and proxying to the server.

```bash
curl -c cookie.txt -b cookie.txt --connect-to targetedsite.hax.invalid:80:127.0.0.1:9000 http://targetedsite.hax.invalid/
```

**Expected Output**: curl fails with CURLE_OUT_OF_MEMORY due to exceeding DYN_HTTP_REQUEST memory limit from 256 large cookies.

**Success Indicators**:
- Error message: "CURLE_OUT_OF_MEMORY"
- Process memory usage spikes before crash

## Attack Chain Summary

### Key Achievements

1. Simulated malicious server sets unlimited domain cookies
2. Populated cookie jar across subdomains
3. Achieved DoS via client-side memory exhaustion in curl

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]
- [[OS Exhaustion Flood]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*

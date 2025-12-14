---
id: ac-curl-ssrf-parsing
tags:
  - ssrf
  - url-parsing
  - host-confusion
  - curl
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Curl-Host-Confusion-for-SSRF]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.387Z'
description: >-
  Demonstrates SSRF by exploiting differences in URL parsing between curl (RFC
  3986) and WHATWG standards, allowing host confusion to bypass whitelists.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF via Curl URL Parsing Host Confusion

Multi-stage attack chain demonstrating a complete attack workflow exploiting curl's URL parsing discrepancy for SSRF.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[URL Validation Bypass] --> B[SSRF Execution via Curl]
    B --> C[Access Unintended Host]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Linux platform
- Port 80 open for HTTP requests
- Application using curl with WHATWG-compliant URL validation

### Initial Access Requirements

- Access to a system or application that invokes curl for HTTP requests
- Ability to craft and inject URLs into the application

## Detailed Attack Procedures

### Step 1: Exploit URL Parsing Discrepancy
procedure: [[procedures/Exploit-Curl-Host-Confusion-for-SSRF]]

**Objective**: Craft a URL that passes WHATWG validation (appearing to target 'google.com') but directs curl to 'yahoo.com', enabling SSRF by bypassing host whitelists.

**Instructions**: Validate the URL in a WHATWG-compliant parser (e.g., browser or Node.js URL module) to confirm it parses as host 'google.com'. Then execute the SSRF using [[commands/curl-ssrf-host-confusion]]:

```bash
curl -sD - -o /dev/null "http://google.com:80\\@yahoo.com/"
```

This command uses curl to send a request, where the backslash escapes the @ in curl's RFC 3986 parsing, treating 'yahoo.com' as the host while validators see 'google.com'.

**Expected Output**: HTTP headers from yahoo.com, such as 'HTTP/1.1 200 OK' and Yahoo-specific response headers, confirming connection to the unintended host.

**Success Indicators**:
- Request headers show response from yahoo.com (e.g., 'yahoo.com' in 'Server' header)
- No errors from curl, indicating successful connection to the bypassed host
- Validation tools (e.g., browser fetch) resolve to google.com, proving the discrepancy

## Attack Chain Summary

### Key Achievements

1. Bypassed host-based URL whitelists using parsing differences
2. Demonstrated SSRF to access unintended external or internal hosts
3. Highlighted risks in mixed parser environments (curl with web validators)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*

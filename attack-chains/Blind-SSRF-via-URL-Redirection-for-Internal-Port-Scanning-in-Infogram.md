---
id: ac-uuid-1
tags:
  - ssrf
  - blind-ssrf
  - url-redirection
  - internal-scanning
  - port-scanning
type: attack_chain
tools:
  - '[[tools/TinyURL]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Redirect-URL-to-Internal-Endpoint-Using-TinyURL]]'
  - '[[procedures/Trigger-SSRF-by-Sending-Redirect-URL-to-API-Endpoint]]'
  - '[[procedures/Test-Additional-SSRF-Bypass-Techniques]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T04:39:18.685Z'
description: >-
  A multi-stage attack exploiting a blind SSRF vulnerability in Infogram's API
  by using URL redirection services to bypass URL filters, enabling internal
  port scanning and potential access to internal services.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Vulnerability Scanning]]'
---
# Blind SSRF via URL Redirection for Internal Port Scanning in Infogram

Multi-stage attack chain demonstrating exploitation of a blind Server-Side Request Forgery (SSRF) vulnerability in Infogram's /api/web_resource/url endpoint. The filter checks the provided URL but fails to follow redirects, allowing attackers to use services like TinyURL to redirect to internal addresses such as http://0:6000/. This enables scanning of internal ports and potential access to internal services, though EC2 metadata access was blocked in testing.

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
    A[Create Redirect URL] --> B[Trigger SSRF Request]
    B --> C[Test Bypass Techniques]
    C --> D[Internal Resource Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/TinyURL]]

### Target Environment

- Web application (Infogram API)
- Required services/ports: Port 6000 (internal)
- Network access requirements: Public internet access to Infogram API and URL shorteners

### Initial Access Requirements

- No credentials required
- External network position
- No prior access needed

## Detailed Attack Procedures

### Step 1: Create Redirect URL
procedure: [[procedures/Create-Redirect-URL-to-Internal-Endpoint-Using-TinyURL]]

**Objective**: Bypass the SSRF filter by creating an external URL that redirects to an internal endpoint.

**Instructions**: Use TinyURL to generate a shortened URL redirecting to http://0:6000/. For example, create https://tinyurl.com/ybk7sqrg pointing to the internal address.

**Expected Output**: A shortened external URL that resolves to the internal target upon access.

**Success Indicators**:
- TinyURL created successfully
- Redirect verified by accessing the short URL and confirming it hits the internal endpoint

### Step 2: Trigger SSRF Request
procedure: [[procedures/Trigger-SSRF-by-Sending-Redirect-URL-to-API-Endpoint]]

**Objective**: Send the redirect URL to the vulnerable API endpoint to force the server to fetch the internal resource.

**Instructions**: Execute [[commands/curl-trigger-ssrf]] to make a GET request to the API with the redirect URL as the 'q' parameter:

```bash
curl "https://infogram.com/api/web_resource/url?q=https://tinyurl.com/ybk7sqrg"
```

**Expected Output**: JSON response containing metadata about the internal resource fetched via the redirect.

**Success Indicators**:
- Server responds with internal resource details
- No direct filter block on the external URL

### Step 3: Test Additional Bypasses
procedure: [[procedures/Test-Additional-SSRF-Bypass-Techniques]]

**Objective**: Explore further evasion methods like newline injection or IP encoding to enhance SSRF exploitation.

**Instructions**: Test payloads using [[commands/curl-bypass-newline]] for newline injection:

```bash
curl "https://infogram.com/api/web_resource/url?q=\\nHost:localhost"
```

And [[commands/curl-bypass-hex-ip]] for hexadecimal encoding:

```bash
curl "https://infogram.com/api/web_resource/url?q=http://0x0:6000"
```

Reference IP encoding resources for more variants.

**Expected Output**: Server errors or responses leaking information, such as 500 errors from invalid requests.

**Success Indicators**:
- Alternative payloads trigger server-side fetches
- Evidence of filter evasion through varied techniques

## Attack Chain Summary

### Key Achievements

1. Bypassed URL filter using redirection services to access internal ports.
2. Demonstrated blind SSRF leading to internal network reconnaissance.
3. Identified multiple evasion vectors including newline injection and IP encoding.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Vulnerability Scanning]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Reconnaissance]]

---

*Last updated: 2023-10-01T00:00:00Z*

---
tags:
  - ssrf
  - libuv
  - nodejs
  - vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - 'Cross-platform (Unix, Windows)'
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Libuv-Hostname-Truncation-for-SSRF]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.589Z'
description: >-
  Multi-stage attack exploiting improper hostname truncation in libuv's
  uv_getaddrinfo function to enable SSRF and unauthorized internal API access in
  Node.js applications.
skill_level: intermediate
impact_level: high
id: b3cfff28-6311-415d-9f2e-8be93040cb7d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF via Libuv Hostname Truncation in Node.js Applications

Multi-stage attack chain demonstrating exploitation of the libuv uv_getaddrinfo vulnerability to perform SSRF attacks, allowing resolution of crafted hostnames to unintended internal IP addresses and bypassing developer checks for unauthorized access.

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
    A[Identify Vulnerable Node.js App] --> B[Craft Malicious Hostname]
    B --> C[Trigger SSRF and Access Internal Resources]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on standard HTTP clients like curl)

### Target Environment

- Node.js applications (v10 and later) using libuv for DNS resolution
- Cross-platform: Unix/Linux, Windows
- Services: Web applications with user-controlled hostname inputs (e.g., URL parsing)

### Initial Access Requirements

- Network access to the target Node.js application
- Ability to send HTTP requests with crafted payloads
- No prior credentials needed if the app exposes SSRF endpoints publicly

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Node.js Application
procedure: [[procedures/Exploit-Libuv-Hostname-Truncation-for-SSRF]]

**Objective**: Locate a Node.js application vulnerable to SSRF via libuv's hostname truncation, typically those parsing user-supplied URLs without length validation.

**Instructions**: Review the target application's dependencies for Node.js v10+ and libuv. Test for SSRF by sending requests with long hostnames to endpoints that perform DNS lookups, such as image loaders or API proxies.

Use [[commands/curl-ssrf-test]] to probe for basic SSRF:

```bash
curl -X GET "http://target-app.com/api/fetch?url=http://example.com"
```

**Expected Output**: Response indicating successful external fetch or error revealing internal resolution issues.

**Success Indicators**:
- Application responds to external URLs without blocking
- No immediate length validation on hostnames

### Step 2: Craft Malicious Hostname Payload
procedure: [[procedures/Exploit-Libuv-Hostname-Truncation-for-SSRF]]

**Objective**: Create a hostname exceeding 256 characters that, when truncated by libuv's uv_getaddrinfo, resolves to an internal IP like 127.0.0.1 or a private network address, bypassing checks.

**Instructions**: Construct a payload where the first 256 characters are padding (e.g., 'a' repeated), followed by a hex-encoded internal IP such as '0x7f000001' for 127.0.0.1. The truncation occurs before passing to getaddrinfo, allowing the hex suffix to be interpreted as an IP.

Example payload: `http://${'a'.repeat(255)}0x7f000001/internal-api`

Incorporate into a request using [[commands/curl-ssrf-payload]]:

```bash
curl -X GET "http://target-app.com/api/fetch?url=http://${'a'.repeat(255)}0x7f000001:8080/admin"
```

**Expected Output**: The application resolves the truncated hostname to the internal IP and fetches from it.

**Success Indicators**:
- Response contains data from internal service (e.g., metadata or API output)
- No DNS resolution error for the crafted hostname

### Step 3: Exfiltrate Internal Data via SSRF
procedure: [[procedures/Exploit-Libuv-Hostname-Truncation-for-SSRF]]

**Objective**: Use the SSRF to access and retrieve sensitive internal resources, such as APIs or metadata services.

**Instructions**: Target internal endpoints like localhost services or private IPs. Chain with the crafted payload to read responses from unauthorized areas.

Validate access using [[commands/curl-internal-fetch]]:

```bash
curl -X GET "http://target-app.com/api/fetch?url=http://${'a'.repeat(255)}0x7f000001:80/metadata"
```

**Expected Output**: Sensitive data from internal API, confirming unauthorized access.

**Success Indicators**:
- Retrieval of internal API responses
- Bypass of any developer-implemented hostname validations

## Attack Chain Summary

### Key Achievements

1. Identification of libuv truncation vulnerability in Node.js apps
2. Crafting of hostnames that resolve to arbitrary internal IPs
3. Successful SSRF leading to unauthorized internal access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*

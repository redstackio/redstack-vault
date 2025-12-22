---
id: ac-ipv6-libcurl-ssrf-bypass
tags:
  - ssrf
  - ipv6
  - libcurl
  - curl
  - access-bypass
  - url-parsing
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/libcurl]]'
  - '[[tools/trurl]]'
  - '[[tools/gcc]]'
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
  - '[[procedures/Set-Up-libcurl-Application-for-URL-Fetching]]'
  - '[[procedures/Submit-Malformed-IPv6-URL-with-Zone-Identifier]]'
  - '[[procedures/Parse-URL-with-libcurl-Omitting-Zone-ID]]'
  - '[[procedures/Send-Request-via-Default-Interface-for-Exploitation]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Cloud Instance Metadata API]]'
updated_at: '2025-12-14T17:29:36.082Z'
description: >-
  Multi-stage attack exploiting libcurl's inconsistent IPv6 URL parsing to omit
  zone identifiers, enabling SSRF and bypassing network interface restrictions.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Cloud Instance Metadata API]]'
---
# SSRF and Access Control Bypass via IPv6 Zone Identifier Omission in libcurl

Multi-stage attack chain demonstrating exploitation of libcurl's URL parsing flaw with IPv6 zone identifiers, allowing SSRF, access control bypass, and internal resource leakage by routing requests through unintended network interfaces.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Application Setup] --> B[Submit Malformed URL]
    B --> C[Parse and Omit Zone ID]
    C --> D[Exploit via Default Interface]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/libcurl]]
- [[tools/trurl]]
- [[tools/gcc]]

### Target Environment

- Linux platform with IPv6 networking enabled
- Web application using libcurl for HTTP requests (e.g., Ubuntu 20.04 with libcurl versions up to latest reported)
- Services: IPv6 link-local addressing with interfaces like eth0
- Network access: Attacker must submit user-controlled URLs to the application

### Initial Access Requirements

- No credentials needed; relies on user input fields for URLs
- Network position: External attacker interacting with public-facing app
- Prior access: None, but app must trust libcurl-parsed hostnames for interface confinement

## Detailed Attack Procedures

### Step 1: Application Setup
procedure: [[procedures/Set-Up-libcurl-Application-for-URL-Fetching]]

**Objective**: Configure a web application to use libcurl for fetching resources from user-supplied URLs, assuming zone IDs restrict access to specific interfaces.

**Instructions**: Integrate libcurl into the application code to handle HTTP requests, trusting the parsed hostname for network interface routing. Compile and run the application in a test environment like Ubuntu 20.04.

**Expected Output**: Application accepts and processes URLs via libcurl without errors.

**Success Indicators**:
- libcurl successfully linked and application fetches URLs
- Zone ID restrictions are in place but untested

### Step 2: Submit Malformed URL
procedure: [[procedures/Submit-Malformed-IPv6-URL-with-Zone-Identifier]]

**Objective**: Inject a specially crafted IPv6 URL with a percent-encoded zone identifier to target a link-local address on a specific interface.

**Instructions**: Use the application's input field to submit a URL like `http://[fe80::1%25eth0]/`, where `%25` encodes the `%` for the zone ID `eth0`. This should route to the eth0 interface per RFC 6874.

**Expected Output**: Application receives and begins processing the URL.

**Success Indicators**:
- URL accepted without validation errors
- Request initiation logged

### Step 3: Parse URL with libcurl
procedure: [[procedures/Parse-URL-with-libcurl-Omitting-Zone-ID]]

**Objective**: Demonstrate libcurl's parsing behavior, which strips the zone identifier, deviating from expected RFC compliance.

**Instructions**: libcurl processes the URL internally. Test this separately using [[commands/compile-parserbatch-test]] and [[commands/run-parserbatch-test]] to verify the hostname is parsed as `[fe80::1]` without `%eth0`. Alternatively, use [[commands/trurl-parse-url]] to extract components.

```bash
trurl --get 'Host: {host} Zone: {zoneid}' 'http://[fe80::1%25eth0]/'
```

**Expected Output**: Parsed hostname: `[fe80::1]`, Zone: `eth0` (but zone ignored in connection).

**Success Indicators**:
- Zone ID omitted from effective hostname
- Comparison with other parsers (e.g., Python urllib) shows preservation

### Step 4: Send Request via Default Interface
procedure: [[procedures/Send-Request-via-Default-Interface-for-Exploitation]]

**Objective**: Force the connection to use the default network interface, bypassing interface-specific restrictions and enabling SSRF or leakage.

**Instructions**: With the parsed URL, libcurl connects to `fe80::1` on the default interface, ignoring eth0. This allows access to internal services, SSRF to localhost equivalents, or bypassing firewall rules.

**Expected Output**: Successful connection to unintended internal resources, potential data leakage.

**Success Indicators**:
- Request routed incorrectly, accessing restricted networks
- Evidence of SSRF (e.g., internal IP responses) or bypass (e.g., forbidden service access)

## Attack Chain Summary

### Key Achievements

1. Bypassed IPv6 zone ID restrictions in libcurl-parsing applications
2. Enabled SSRF to internal resources via malformed URLs
3. Demonstrated access control bypass for network interface policies
4. Highlighted deviation from RFC 6874, affecting URL validation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Cloud Instance Metadata API]] Unsecured Web Services (for SSRF enabling internal access)

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access (via user-supplied URLs)
- [[Collection]] Collection (information leakage from internal resources)

---

*Last updated: 2023-10-01T00:00:00Z*

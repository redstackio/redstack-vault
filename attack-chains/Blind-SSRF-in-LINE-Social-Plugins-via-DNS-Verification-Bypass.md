---
tags:
  - ssrf
  - blind-ssrf
  - dns-bypass
  - internal-scanning
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-SSRF-via-DNS-Bypass-in-LINE-Social-Plugins]]'
  - '[[procedures/Exploit-Blind-SSRF-for-Internal-Network-Access]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T03:53:38.488Z'
description: >-
  A multi-step attack exploiting a blind SSRF vulnerability in the LINE Social
  Plugins service by bypassing DNS verification, enabling unauthorized internal
  network requests and port scanning.
skill_level: intermediate
impact_level: high
id: ce7e52c1-18e6-4dd9-9ea2-f53199b9045c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Service Scanning]]'
---
# Blind SSRF in LINE Social Plugins via DNS Verification Bypass

Multi-stage attack chain demonstrating exploitation of a blind Server-Side Request Forgery (SSRF) vulnerability in the social-plugins.line.me service of LINE Social Plugins, which allows web content sharing. The attack bypasses DNS verification on a received parameter, enabling unauthorized requests to internal servers and port scanning of the internal network. No data exfiltration was reported, but the potential for further compromise exists.

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
    A[Identify Vulnerability] --> B[Exploit SSRF]
    B --> C[Internal Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Browser or proxy tool like Burp Suite for request crafting
- [[commands/curl-ssrf-test]]

### Target Environment

- Web platform
- Access to LINE Social Plugins service at social-plugins.line.me
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Public internet access to the LINE service
- No credentials needed
- Ability to craft HTTP requests to the endpoint

## Detailed Attack Procedures

### Step 1: Identify SSRF Vulnerability
procedure: [[procedures/Identify-SSRF-via-DNS-Bypass-in-LINE-Social-Plugins]]

**Objective**: Detect the blind SSRF by testing parameter handling and bypassing DNS verification to confirm improper URL validation.

**Instructions**: Target the parameter in social-plugins.line.me requests. Use [[commands/curl-ssrf-test]] to send a crafted request with a bypassed DNS payload, such as using an IP address or alternative encoding to evade verification.

```bash
curl -X POST 'https://social-plugins.line.me/api/endpoint' -d 'url=http://169.254.169.254/latest/meta-data/' -H 'Content-Type: application/x-www-form-urlencoded'
```

Monitor for blind responses indicating internal resolution without DNS checks.

**Expected Output**: Server response without error, or timing differences suggesting internal request processing.

**Success Indicators**:
- No DNS resolution error returned
- Response time increases indicating internal fetch

### Step 2: Exploit Blind SSRF
procedure: [[procedures/Exploit-Blind-SSRF-for-Internal-Network-Access]]

**Objective**: Leverage the bypassed verification to send requests to internal resources, enabling port scanning or access to private endpoints.

**Instructions**: Craft follow-up requests using [[commands/curl-ssrf-test]] to target internal IPs or ports, such as metadata services or localhost ports.

```bash
curl -X POST 'https://social-plugins.line.me/api/endpoint' -d 'url=http://127.0.0.1:8080/admin' -H 'Content-Type: application/x-www-form-urlencoded'
```

Iterate with different ports (e.g., 22, 80, 443) to scan for open services.

**Expected Output**: Varied response times or error patterns revealing open ports.

**Success Indicators**:
- Differential response times for open vs. closed ports
- Successful internal request inference via blind indicators

## Attack Chain Summary

### Key Achievements

1. Bypassed DNS verification in parameter handling
2. Enabled blind requests to internal servers
3. Demonstrated potential for internal network port scanning

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Network Service Scanning]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*

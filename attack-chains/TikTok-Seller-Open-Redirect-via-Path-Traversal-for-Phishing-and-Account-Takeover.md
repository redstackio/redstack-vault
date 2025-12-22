---
tags:
  - open-redirect
  - path-traversal
  - phishing
  - account-takeover
  - tiktok
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Open-Redirect-via-Path-Traversal-in-redirect_url]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:31.661Z'
description: >-
  Exploits an open redirect vulnerability in the TikTok Seller login process
  using path traversal to redirect users to arbitrary malicious URLs, enabling
  phishing attacks that could lead to account takeover.
skill_level: basic
impact_level: low
id: 99de7ffb-1cce-4cd5-9013-7616f2cc5b3f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# TikTok Seller Open Redirect via Path Traversal for Phishing and Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting an open redirect vulnerability in the TikTok Seller domain's login process.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Basic |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Exploit Open Redirect] --> B[Phishing or Session Hijacking]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[commands/curl-open-redirect-test]]

### Target Environment

- Web platform
- TikTok Seller domain (e.g., seller.tiktok.com)
- Access to login endpoint

### Initial Access Requirements

- Public internet access
- No credentials required for testing redirect
- Knowledge of the login URL with redirect_url parameter

## Detailed Attack Procedures

### Step 1: Exploit Open Redirect During Login
procedure: [[procedures/Exploit-Open-Redirect-via-Path-Traversal-in-redirect_url]]

**Objective**: Manipulate the redirect_url parameter using path traversal to bypass validation and redirect the user to a malicious external site, facilitating phishing or session hijacking.

**Instructions**: Identify the login endpoint on the TikTok Seller domain. Craft a request to the login page with a path traversal payload in the redirect_url parameter to escape any intended path restrictions and point to an arbitrary URL. Use [[commands/curl-open-redirect-test]] to simulate the request:

```bash
curl -X GET "https://seller.tiktok.com/login?redirect_url=../../../http://evil-phish.com" -v
```

Observe the response headers to confirm the redirect occurs to the malicious domain. In a real attack, entice a victim to click a link that includes this manipulated parameter during the login flow.

**Expected Output**: HTTP 302 redirect response with Location header pointing to the arbitrary URL (e.g., http://evil-phish.com).

**Success Indicators**:
- Redirect to external malicious domain confirmed
- No validation blocking the path traversal

## Attack Chain Summary

### Key Achievements

1. Successful bypass of redirect validation using path traversal
2. Enablement of phishing by redirecting users to attacker-controlled sites
3. Potential for session hijacking or account takeover via stolen credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*

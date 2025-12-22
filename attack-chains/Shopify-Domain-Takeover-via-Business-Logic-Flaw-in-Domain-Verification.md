---
tags:
  - domain-takeover
  - business-logic
  - shopify
  - web
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/curl]]'
  - '[[tools/netcat]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Shopify-Trial-Account]]'
  - '[[procedures/Attempt-Open-Redirect-Bypass]]'
  - '[[procedures/Test-DNS-Check-for-RCE]]'
  - '[[procedures/Add-Unverified-Domains-via-Endpoint]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.209Z'
description: >-
  A multi-stage attack exploiting a business logic error in Shopify's domain
  verification process to register and takeover owned domains like
  myshopify.com, redirecting traffic to an attacker-controlled store.
skill_level: intermediate
impact_level: high
id: 80fae76c-b522-47a0-977f-b2543de21522
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Shopify Domain Takeover via Business Logic Flaw in Domain Verification

Multi-stage attack chain demonstrating a complete attack workflow exploiting Shopify's domain verification process.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Trial Account] --> B[Attempt Redirect Bypass]
    B --> C[Test DNS for RCE]
    C --> D[Add Unverified Domain]
    D --> E[Domain Takeover Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/curl]]
- [[tools/netcat]]

### Target Environment

- Web platform
- Shopify service
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- No prior credentials needed
- Internet access to Shopify signup
- Black box testing mindset without internal docs

## Detailed Attack Procedures

### Step 1: Create Trial Account
procedure: [[procedures/Create-Shopify-Trial-Account]]

**Objective**: Gain initial access to Shopify's store setup features as a legitimate user.

**Instructions**: Sign up for a free trial account on Shopify's website. Use standard registration without a partners account to simulate external attacker.

**Expected Output**: Active trial store dashboard accessible.

**Success Indicators**:
- Trial account created successfully
- Access to domain addition interface granted

### Step 2: Attempt Open Redirect Bypass
procedure: [[procedures/Attempt-Open-Redirect-Bypass]]

**Objective**: Explore potential open redirect vulnerabilities in login flows to chain with domain issues.

**Instructions**: Intercept the login request using [[tools/Burp-Suite]]. Modify the redirect parameter to test for bypass, e.g., submit `https://www.shopify.com/login?redirect=//acme`.

**Expected Output**: Request intercepted and modified, but redirect filter blocks the attempt.

**Success Indicators**:
- Traffic captured in Burp
- No successful redirect (indicating filter works, pivot to other vectors)

### Step 3: Test DNS Check for RCE
procedure: [[procedures/Test-DNS-Check-for-RCE]]

**Objective**: Probe the domain DNS verification tool for command injection leading to remote code execution.

**Instructions**: During domain setup, use [[tools/Burp-Suite]] to intercept DNS check requests. Attempt command injection payloads to trigger external callbacks. Set up a listener with [[commands/netcat-listen]] on an attacker server (e.g., `nc -lvnp 80`). Use [[commands/curl-external-request]] to simulate or test outbound requests from injected commands.

**Expected Output**: No incoming requests to attacker server, confirming no RCE.

**Success Indicators**:
- Payloads submitted without errors
- No callbacks received (unsuccessful, proceed to logic flaws)

### Step 4: Add Unverified Domains via Endpoint
procedure: [[procedures/Add-Unverified-Domains-via-Endpoint]]

**Objective**: Exploit business logic flaw to register Shopify-owned domains without verification.

**Instructions**: In the store setup, navigate to domain addition. Intercept the final domain submission endpoint with [[tools/Burp-Suite]]. Submit a Shopify-owned domain like `myshopify.com` directly via the last API call in the process, bypassing earlier verification steps.

**Expected Output**: Domain added as 'Not connected' but effectively registered, causing traffic redirection to the attacker's store.

**Success Indicators**:
- Domain listed in store settings
- Traffic from the domain redirects to attacker store
- Legitimate users unable to claim the domain

## Attack Chain Summary

### Key Achievements

1. Successful registration of owned domain myshopify.com via logic bypass
2. Traffic redirection to attacker-controlled store
3. No verification required, enabling full takeover

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*

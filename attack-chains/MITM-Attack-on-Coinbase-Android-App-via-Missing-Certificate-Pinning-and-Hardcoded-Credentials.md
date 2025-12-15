---
tags:
  - mitm
  - certificate-pinning
  - hardcoded-credentials
  - replay-attack
  - android
  - api-tampering
type: attack_chain
tools:
  - '[[tools/Charles-Proxy]]'
tactics:
  - '[[Credential Access]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Hardcoded-Credentials-in-Coinbase-Source-Code]]'
  - '[[procedures/Configure-Charles-Proxy-for-MITM-on-Android]]'
  - '[[procedures/Intercept-and-Tamper-with-Coinbase-API-Traffic]]'
step_count: 3
techniques:
  - '[[Credentials In Files]]'
  - '[[Adversary-in-the-Middle]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:24:41.688Z'
description: >-
  A multi-stage attack exploiting vulnerabilities in the Coinbase Android app,
  including missing SSL certificate pinning, insecure API design allowing
  replays and tampering, and hardcoded consumer credentials in public source
  code, enabling interception, modification, and replay of sensitive API
  requests for account hijacking and financial loss.
skill_level: intermediate
impact_level: high
id: 688f3472-8020-451d-8953-900cc5cf8e26
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[Adversary-in-the-Middle]]'
  - '[[Steal Web Session Cookie]]'
---
# MITM Attack on Coinbase Android App via Missing Certificate Pinning and Hardcoded Credentials

Multi-stage attack chain demonstrating exploitation of security flaws in the Coinbase Android app to perform a man-in-the-middle (MITM) attack, intercept sensitive API communications, steal access tokens, and tamper with or replay transactions like bitcoin buys, sells, or transfers, potentially leading to account hijacking and financial loss.

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
    A[Identify Exposed Credentials] --> B[Set Up MITM Proxy]
    B --> C[Intercept and Tamper API Traffic]
    C --> D[Account Hijacking and Transaction Manipulation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Charles-Proxy]]

### Target Environment

- Target OS/Platform: Android device with Coinbase app installed
- Required services/ports: Coinbase API (HTTPS on port 443), proxy on port 8888
- Network access requirements: Local network control to route device traffic through proxy

### Initial Access Requirements

- Credential requirements: None (exploits public source code and app flaws)
- Network position: Attacker must have physical access to the Android device or control over a shared network
- Prior access needed: Ability to install custom CA certificate on the device

## Detailed Attack Procedures

### Step 1: Identify Exposed Credentials
procedure: [[procedures/Identify-Hardcoded-Credentials-in-Coinbase-Source-Code]]

**Objective**: Review the public GitHub repository to locate hardcoded consumer ID and secret, enabling impersonation of the app for unauthorized API access.

**Instructions**: Access the Coinbase Android app's GitHub repository and navigate to the LoginManager.java file to extract the plaintext credentials.

**Expected Output**: Hardcoded consumer ID and secret visible in the source code.

**Success Indicators**:
- Credentials successfully identified from public repo
- Confirmation that they appear in API requests

### Step 2: Set Up MITM Proxy
procedure: [[procedures/Configure-Charles-Proxy-for-MITM-on-Android]]

**Objective**: Configure Charles Proxy as an intercepting proxy, install its CA certificate on the Android device, and route traffic to bypass SSL verification due to missing certificate pinning.

**Instructions**: Install and run Charles Proxy on the host machine, download and install the charles.crt on the Android device, set Wi-Fi proxy settings to the proxy's IP:8888, and enable SSL proxying for coinbase.com domains.

**Expected Output**: Device traffic routed through proxy with HTTPS decryption enabled.

**Success Indicators**:
- Proxy captures initial HTTP/HTTPS traffic from the app
- SSL certificate installed and trusted on device

### Step 3: Intercept and Tamper with API Traffic
procedure: [[procedures/Intercept-and-Tamper-with-Coinbase-API-Traffic]]

**Objective**: Monitor API requests to coinbase.com, view plaintext credentials and access tokens, and demonstrate tampering or replaying of sensitive transactions like bitcoin transfers.

**Instructions**: Launch the Coinbase app on the proxied device, interact with features (e.g., login, buy bitcoin), observe intercepted requests in Charles, modify parameters (e.g., change recipient or amount), and replay requests to simulate unauthorized actions.

**Expected Output**: Intercepted requests showing plaintext secrets and tokens; successful modification or replay leading to altered API calls.

**Success Indicators**:
- Access tokens and credentials visible in plaintext
- Modified transaction request accepted by API
- Replay of buy transaction executed multiple times

## Attack Chain Summary

### Key Achievements

1. Exposed hardcoded credentials from public source code, allowing app impersonation.
2. Bypassed SSL via missing pinning to decrypt API traffic in MITM setup.
3. Enabled replay and tampering of transactions, risking financial loss and account takeover.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Credentials In Files]] Credentials In Files (hardcoded secrets in source)
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (MITM via proxy and missing pinning)
- [[Steal Web Session Cookie]] Steal Web Session Cookie (interception of OAuth tokens)

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access
- [[Persistence]] Persistence (via replayable API access)

---

*Last updated: 2023-10-01T00:00:00Z*

---
id: ac-instacart-bruteforce-ios-bypass
tags:
  - brute-force
  - rate-limiting-bypass
  - mobile-app
  - authentication-bypass
type: attack_chain
tools:
  - '[[tools/BurpSuite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - iOS
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Configure-Mobile-Proxy-with-BurpSuite]]'
  - '[[procedures/Intercept-Instacart-Login-Request]]'
  - '[[procedures/Brute-Force-Passwords-via-Mobile-Endpoint]]'
step_count: 3
techniques:
  - '[[Brute Force]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:41.853Z'
description: >-
  Multi-stage attack exploiting the lack of rate limiting on Instacart's iOS app
  login endpoint to brute force passwords and bypass web-based account locks.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Exploit Public-Facing Application]]'
---
# Brute Force Login and Bypass Locked Account Restrictions via Instacart iOS App

Multi-stage attack chain demonstrating a complete attack workflow exploiting the absence of rate limiting on the Instacart iOS app's login endpoint, allowing unlimited brute force attempts even after web-based account locking.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Configure Proxy] --> B[Intercept Login]
    B --> C[Brute Force Attacks]
    C --> D[Account Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/BurpSuite]]

### Target Environment

- iOS device with Instacart app installed
- Access to the target's email or username for login attempts
- Network capable of proxying mobile traffic (e.g., Wi-Fi)

### Initial Access Requirements

- No prior credentials needed, but target username/email required
- Ability to install certificates on iOS for proxy interception
- Web access to Instacart for initial account locking simulation

## Detailed Attack Procedures

### Step 1: Configure Mobile Proxy
procedure: [[procedures/Configure-Mobile-Proxy-with-BurpSuite]]

**Objective**: Set up traffic interception for the iOS app to capture and modify login requests.

**Instructions**: Launch BurpSuite and configure it as a proxy by navigating to the Proxy tab, ensuring it listens on the default port (8080). On the iOS device, set the Wi-Fi proxy to the attacker's machine IP and port 8080. Install the Burp CA certificate on the iOS device via Safari by visiting http://burp (or the proxy IP:8080) and trusting it in Settings > General > VPN & Device Management.

**Expected Output**: App traffic routes through BurpSuite without errors; certificate trusted.

**Success Indicators**:
- iOS app connects successfully via proxy
- No SSL pinning errors in Burp logs

### Step 2: Intercept Login Request
procedure: [[procedures/Intercept-Instacart-Login-Request]]

**Objective**: Capture a legitimate login request from the Instacart iOS app to identify the endpoint and parameters.

**Instructions**: Open the Instacart app on the iOS device, navigate to the login screen, and attempt a login with any credentials. In BurpSuite, go to the Proxy > HTTP history tab to view the intercepted POST request to https://www.instacart.com/oauth/token, noting parameters like username, password, grant_type, and client_id.

**Expected Output**: Captured POST request with JSON or form data body visible in Burp.

**Success Indicators**:
- Request details including endpoint and auth parameters logged
- Response code (401 for invalid, 200 for valid) observed

### Step 3: Brute Force Passwords
procedure: [[procedures/Brute-Force-Passwords-via-Mobile-Endpoint]]

**Objective**: Replay the login request with multiple passwords to brute force access, bypassing web locks.

**Instructions**: In BurpSuite's Repeater tab, paste the intercepted request and modify the password parameter iteratively. Use a wordlist of common passwords (e.g., top 100 from SecLists). Send requests rapidly; monitor responses for 200 OK indicating success. To simulate bypass, first lock the account via web (15 failed attempts), then continue via app.

**Expected Output**: Series of 401 responses until a 200 with access token on valid password.

**Success Indicators**:
- Unlimited attempts without lockout
- Account access despite web lock
- Valid token received

## Attack Chain Summary

### Key Achievements

1. Intercepted mobile login traffic without restrictions
2. Brute forced passwords using replayed requests
3. Bypassed web account locking mechanism

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

---

*Last updated: 2023-10-01T00:00:00Z*

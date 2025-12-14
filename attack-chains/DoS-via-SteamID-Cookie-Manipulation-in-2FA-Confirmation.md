---
tags:
  - idor
  - cookie-manipulation
  - dos
  - 2fa-lockout
  - steamid
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-2FA-Login-Session]]'
  - '[[procedures/Capture-2FA-Confirmation-Request]]'
  - '[[procedures/Modify-SteamID-Cookie-for-Impersonation]]'
  - '[[procedures/Trigger-2FA-Lockout-with-Invalid-Codes]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:24:48.366Z'
description: >-
  Multi-stage attack exploiting insecure SteamID cookie validation to
  impersonate users and trigger 2FA lockouts, causing temporary
  denial-of-service on login.
skill_level: intermediate
impact_level: high
id: a60fac0c-5f13-413a-ad0a-24a9375c852e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# DoS via SteamID Cookie Manipulation in 2FA Confirmation

Multi-stage attack chain demonstrating exploitation of insecure cookie reliance in CS Money's 2FA endpoints to impersonate users and induce account lockouts, resulting in denial-of-service.

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
    A[Initiate Login] --> B[Capture Request]
    B --> C[Modify Cookie]
    C --> D[Submit Invalid Codes]
    D --> E[Trigger Lockout]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform with Steam-integrated 2FA (e.g., CS Money)
- Access to /login/confirm and /2fa/* endpoints
- No specific ports required; standard HTTPS (443)

### Initial Access Requirements

- Knowledge of victim's SteamID (e.g., from support tickets or public sources)
- Attacker's own browser or proxy tool for request interception
- No prior authentication needed; attack is unauthenticated

## Detailed Attack Procedures

### Step 1: Initiate 2FA Login Session
procedure: [[procedures/Initiate-2FA-Login-Session]]

**Objective**: Start a normal login process on a 2FA-enabled account to reach the confirmation stage and prepare for request capture.

**Instructions**: Perform the standard login flow using your own 2FA-enabled account to trigger the 2FA code prompt. This sets up the session for capturing the confirmation request.

**Expected Output**: Browser or proxy displays the 2FA code input page, with the underlying POST request to /login/confirm ready for interception.

**Success Indicators**:
- 2FA confirmation page loads
- Session cookie (including steamid) is generated

### Step 2: Capture 2FA Confirmation Request
procedure: [[procedures/Capture-2FA-Confirmation-Request]]

**Objective**: Intercept the POST request to /login/confirm to analyze and prepare for modification.

**Instructions**: Use a proxy tool to capture the request when submitting a 2FA code. The request body is {"token":"<session_token>","code":"<2fa_code>"} with a steamid cookie.

**Expected Output**: Captured HTTP POST request visible in proxy, showing headers, body, and cookies.

**Success Indicators**:
- Request intercepted successfully
- steamid cookie value visible (attacker's own SteamID)

### Step 3: Modify SteamID Cookie for Impersonation
procedure: [[procedures/Modify-SteamID-Cookie-for-Impersonation]]

**Objective**: Alter the steamid cookie to the victim's SteamID, enabling impersonation without validation checks.

**Instructions**: In the intercepted request, change the steamid cookie value from your own SteamID to the target's. Keep other elements (token, code) intact for now.

**Expected Output**: Modified request ready for forwarding, with updated cookie.

**Success Indicators**:
- Cookie value matches victim's SteamID
- Request structure remains valid

### Step 4: Trigger 2FA Lockout with Invalid Codes
procedure: [[procedures/Trigger-2FA-Lockout-with-Invalid-Codes]]

**Objective**: Submit the modified request multiple times with wrong 2FA codes to exhaust rate limits and lock the victim's account for 5 minutes.

**Instructions**: Forward the modified request 4 times, each with an invalid code (e.g., "123456"). This exploits the lack of cookie validation to apply lockouts to the impersonated account.

**Expected Output**: Server responds with lockout errors after 4 attempts; victim's login attempts will fail for 5 minutes.

**Success Indicators**:
- Lockout message received
- Victim's 2FA endpoints (e.g., /login/confirm, /2fa/delete) affected

## Attack Chain Summary

### Key Achievements

1. Impersonation of any 2FA-enabled user via SteamID cookie substitution
2. Triggering of 5-minute account lockouts without access to victim's credentials
3. Potential chaining with SteamID enumeration from support or public sources for mass DoS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Network Denial of Service]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Impact]]

---

*Last updated: 2023-10-01T00:00:00Z*

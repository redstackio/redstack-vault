---
tags:
  - race-condition
  - android
  - api-exploit
  - business-logic
  - financial-impact
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Android
  - Web
  - Cloud
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-Reddit-Coin-Purchase]]'
  - '[[procedures/Intercept-Reddit-Verification-Request]]'
  - '[[procedures/Replay-Verification-Request-in-Parallel]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.565Z'
description: >-
  Exploits a race condition in Reddit's Android app coin purchase verification
  endpoint to credit multiple coins for a single payment, leading to virtual
  currency inflation.
skill_level: intermediate
impact_level: high
id: 5f99c9fb-3401-43e3-9a2f-955a01bbafa9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Reddit Coin Inflation via Race Condition in Android Purchase Verification

Multi-stage attack chain demonstrating exploitation of a race condition in Reddit's coin purchase verification to inflate virtual currency balance.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate Purchase] --> B[Intercept Request]
    B --> C[Parallel Replay]
    C --> D[Multiple Credits]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Android device with Reddit app (version around 2020.5.0 or vulnerable)
- Rooted device or proxy setup for traffic interception
- Google Play Store access for purchases
- Network access to oauth.reddit.com

### Initial Access Requirements

- Installed Reddit Android app
- Valid Google Play account with payment method
- Ability to intercept HTTPS traffic (e.g., via Burp Suite CA certificate installation on device)

## Detailed Attack Procedures

### Step 1: Initiate Coin Purchase
procedure: [[procedures/Initiate-Reddit-Coin-Purchase]]

**Objective**: Complete a legitimate coin purchase in the Reddit app to generate a verification request.

**Instructions**: Open the Reddit Android app, navigate to the coin purchase section, select a package (e.g., 50 coins), and complete the payment via Google Play Store. This triggers the verification POST request.

**Expected Output**: Purchase confirmation in Google Play, followed by app credit attempt (which may fail initially due to race setup).

**Success Indicators**:
- Google Play transaction ID generated (e.g., GPA.3390-...)
- Purchase token obtained

### Step 2: Intercept Verification Request
procedure: [[procedures/Intercept-Reddit-Verification-Request]]

**Objective**: Capture the HTTP POST request sent to the verification endpoint after purchase.

**Instructions**: With traffic interception enabled (e.g., via [[tools/Burp-Suite]]), monitor the app's network traffic. Upon purchase completion, capture the POST to /api/v2/gold/android/verify_purchase, noting parameters like transaction_id, token, product_id, and correlation_id.

**Expected Output**: Raw HTTP request with form-encoded body containing purchase details.

**Success Indicators**:
- Request intercepted with valid token and IDs
- No immediate coin credit in app (setup for race)

### Step 3: Replay Request in Parallel
procedure: [[procedures/Replay-Verification-Request-in-Parallel]]

**Objective**: Send multiple concurrent copies of the intercepted request to exploit the TOCTOU race condition in memcache locking, resulting in multiple coin credits.

**Instructions**: Use a tool like Burp Suite Intruder or a script to fire 10+ parallel POST requests with the exact captured parameters. The server's memcache lock fails to synchronize, allowing repeated validations.

Execute the replay using [[commands/reddit-verify-purchase-replay]] (adapted for parallel execution, e.g., via curl in a loop or script):

```bash
# Example parallel replay script (use ab or similar for concurrency)
ab -n 10 -c 10 -p postdata.txt -T 'application/x-www-form-urlencoded' https://oauth.reddit.com/api/v2/gold/android/verify_purchase?raw_json=1
```

**Expected Output**: Multiple successful responses (e.g., 9/10 credits of 50 coins), inflating balance (e.g., 450 coins for one 50-coin purchase).

**Success Indicators**:
- App balance shows inflated coins
- Server logs multiple credits before lock engages

## Attack Chain Summary

### Key Achievements

1. Single payment results in multiple coin credits due to unsynchronized memcache.
2. Exploitation requires only app access and traffic interception, no auth bypass.
3. Demonstrates TOCTOU vulnerability in transaction processing, causing financial loss.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2024-10-01T00:00:00Z*

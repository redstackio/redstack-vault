---
tags:
  - 2fa-bypass
  - auth-bypass
  - social-engineering
  - line-app
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Desktop (Windows/Mac)
submitted: true
complexity: medium
procedures:
  - '[[procedures/Initiate-QR-Login-as-Attacker]]'
  - '[[procedures/Craft-Malicious-2FA-Bypass-URL]]'
  - '[[procedures/Phish-Victim-to-Click-Bypass-URL]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Phishing]]'
description: >-
  Attack chain exploiting a missing ownership check in LINE's 2FA verification
  for secondary clients like Windows/Mac, allowing unauthorized access by
  tricking the victim into clicking a crafted URL after QR login.
skill_level: intermediate
impact_level: high
id: d23166d9-669d-4e6d-a3f3-a25fdd1aaf37
created_at: '2025-12-14T17:24:48.151Z'
updated_at: '2025-12-14T17:24:48.151Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Phishing]]'
---
# LINE 2FA Bypass via Missing Ownership Check in Secondary Client Login

Multi-stage attack chain demonstrating a complete attack workflow exploiting insufficient server-side verification in LINE's 2FA for secondary clients.

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
    A[QR Login as Attacker] --> B[Craft Bypass URL]
    B --> C[Phish Victim Click]
    C --> D[Unauthorized Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (relies on manual crafting and social engineering)

### Target Environment

- LINE app on Desktop (Windows/Mac)
- Access to LINE account for QR login
- Victim using LINE secondary client

### Initial Access Requirements

- Attacker must have a LINE account
- Ability to generate QR code for login
- Communication channel to send URL to victim (e.g., email, chat)

## Detailed Attack Procedures

### Step 1: Initiate QR Login as Attacker
procedure: [[procedures/Initiate-QR-Login-as-Attacker]]

**Objective**: Start the secondary client login process on the attacker's device to expose the vulnerable 2FA verification flow.

**Instructions**: Open the LINE app on Windows or Mac, scan the QR code with your primary device to authenticate, and proceed to the 2FA step without completing it fully.

**Expected Output**: The app reaches the 2FA verification stage, generating a session vulnerable to ownership check bypass.

**Success Indicators**:
- QR login succeeds
- 2FA prompt appears but is not completed

### Step 2: Craft Malicious 2FA Bypass URL
procedure: [[procedures/Craft-Malicious-2FA-Bypass-URL]]

**Objective**: Create a specially crafted URL that exploits the missing ownership check in the server's 2FA logic.

**Instructions**: Analyze the login process (e.g., via network inspection) to identify the 2FA verification endpoint. Construct a URL with parameters mimicking the victim's session, such as device ID or token from the attacker's QR login, but targeted at the victim's account.

**Expected Output**: A functional URL that, when clicked by the victim, completes 2FA verification on the server without proper ownership validation.

**Success Indicators**:
- URL is generated with exploit parameters
- URL structure matches LINE's login flow

### Step 3: Phish Victim to Click Bypass URL
procedure: [[procedures/Phish-Victim-to-Click-Bypass-URL]]

**Objective**: Trick the victim into interacting with the crafted URL, bypassing 2FA and granting the attacker access.

**Instructions**: Send the crafted URL to the victim via a phishing message (e.g., "Click here to verify your LINE login"). When the victim clicks, the server processes it as valid 2FA completion due to the missing check.

**Expected Output**: Attacker gains full access to the victim's LINE account on the secondary client.

**Success Indicators**:
- Victim clicks the URL
- Attacker logs in successfully without further 2FA

## Attack Chain Summary

### Key Achievements

1. Bypassed 2FA using a crafted URL exploiting ownership check absence
2. Achieved unauthorized access to victim's LINE account
3. Demonstrated social engineering combined with auth logic flaw

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Phishing]] Phishing

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*

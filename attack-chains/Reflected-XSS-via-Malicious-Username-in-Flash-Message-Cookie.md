---
tags:
  - xss
  - reflected-xss
  - cookie-injection
  - flash-message
  - javascript-execution
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-10-01T12:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-User-Account-with-XSS-Payload]]'
  - '[[procedures/Trigger-SIM-Card-Request-Authorization]]'
  - '[[procedures/Exploit-Reflected-XSS-in-Flash-Cookie]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.790Z'
description: >-
  A reflected XSS vulnerability where a malicious username injects JavaScript
  into a flash message cookie, executing arbitrary code in the victim's browser
  upon rendering.
skill_level: intermediate
impact_level: high
id: 4289a151-ba44-49d5-b693-bd6930747b9a
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS via Malicious Username in Flash Message Cookie

Multi-stage attack chain demonstrating a complete reflected XSS workflow in a web application handling user authorizations for SIM card requests.

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
    A[Create Malicious User] --> B[Trigger Authorization Request]
    B --> C[Execute XSS via Cookie]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools)
- Account creation access on the target platform

### Target Environment

- Web application (e.g., Mobile Vikings platform)
- User registration and SIM card request features enabled
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Ability to register a new user account
- Access to perform SIM card requests as a legitimate user
- No prior credentials needed beyond basic registration

## Detailed Attack Procedures

### Step 1: Create Malicious User Account
procedure: [[procedures/Create-Malicious-User-Account-with-XSS-Payload]]

**Objective**: Register a user with a username containing an unescaped JavaScript payload to prepare for reflection.

**Instructions**: Navigate to the user registration page and enter a username like `name<script>alert(1)</script>`. Complete the registration process to create the account.

**Expected Output**: Successful account creation confirmation, with the malicious username stored in the system.

**Success Indicators**:
- Account created without errors
- Username includes the payload as verified in account details

### Step 2: Trigger SIM Card Request Authorization
procedure: [[procedures/Trigger-SIM-Card-Request-Authorization]]

**Objective**: Have a victim user authorize a SIM card request to the malicious user, causing the username to be reflected into a cookie.

**Instructions**: As User B (victim), log in and initiate a SIM card request. Select the malicious User A for authorization. Submit the request to trigger the backend to set the flash message cookie.

**Expected Output**: Request submitted, and a cookie named `messages` is set in the browser containing the unescaped username payload.

**Success Indicators**:
- SIM request processed
- Cookie inspector shows `messages` cookie with JSON including the payload: `messages="29972147bc558baf382bbeb0b829d4efec82de2f$[[\"__json_message\",0,25,\"Authorization will be given to name<script>alert(1)</script> once this user confirms.\"]]"; Path=/`

### Step 3: Execute XSS via Flash Message Cookie
procedure: [[procedures/Exploit-Reflected-XSS-in-Flash-Cookie]]

**Objective**: Render the flash message to execute the injected JavaScript in the victim's browser.

**Instructions**: Refresh the page or navigate to a view that processes the flash message cookie. The browser will parse and render the cookie value, executing the script.

**Expected Output**: Alert box or other JavaScript execution, such as `alert(1)`, confirming XSS success.

**Success Indicators**:
- JavaScript payload executes (e.g., alert pops up)
- Browser console shows no escaping errors; potential for further actions like cookie theft

## Attack Chain Summary

### Key Achievements

1. Successful injection of XSS payload via username registration
2. Reflection of payload into a cookie during authorization workflow
3. Arbitrary JavaScript execution in the victim's browser, enabling session hijacking or data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2024-10-01T12:00:00Z*

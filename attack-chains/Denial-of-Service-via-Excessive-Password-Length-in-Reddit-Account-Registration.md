---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - dos
  - ddos
  - resource-exhaustion
  - password
  - registration
  - web
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Submit-Excessive-Password-for-DoS]]'
step_count: 1
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:30.500Z'
description: >-
  This attack chain exploits the lack of password length restrictions in
  Reddit's account registration process to perform a denial-of-service attack by
  submitting extremely long passwords that force resource-intensive hashing
  operations on the server.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Denial of Service via Excessive Password Length in Reddit Account Registration

Multi-stage attack chain demonstrating a complete attack workflow targeting Reddit's registration process.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Registration] --> B[Resource Exhaustion DoS]
    B --> C[Server Overload]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)
- Optional: [[tools/curl]] for automated submission

### Target Environment

- Target: Reddit account registration page (https://www.reddit.com/register)
- Required services/ports: HTTPS (443)
- Network access requirements: Public internet access to Reddit

### Initial Access Requirements

- No credentials required
- No prior access needed
- Valid username and email for registration form (though email verification can be skipped for testing)

## Detailed Attack Procedures

### Step 1: Submit Excessive Password During Registration
procedure: [[procedures/Submit-Excessive-Password-for-DoS]]

**Objective**: Force the server to perform computationally expensive hashing on an extremely long password input, exhausting resources and potentially causing denial of service.

**Instructions**: Navigate to the Reddit registration page and fill out the form with a deliberately long password. Generate a password by repeating a base string like 'Crissrock3%40' approximately 40 times or more to create a string exceeding 1MB in length. Submit the form multiple times concurrently to amplify the effect for DDoS.

Use a web browser to access https://www.reddit.com/register and input the long password in the password field. For automation, use [[commands/curl-submit-long-password]] to send POST requests:

```bash
curl -X POST https://www.reddit.com/register \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&email=test@example.com&password=$(python3 -c 'print("Crissrock3%40" * 40)')"
```

**Expected Output**: The server may timeout, return an error, or process slowly due to hashing overhead. Successful exploitation shows delayed or failed responses.

**Success Indicators**:
- Server response time exceeds 30 seconds
- Registration fails with timeout or resource error
- Multiple concurrent requests cause site-wide slowdown

## Attack Chain Summary

### Key Achievements

1. Exploited lack of input validation on password length to trigger resource exhaustion
2. Demonstrated potential for scalable DoS/DDoS by parallel requests
3. Highlighted vulnerability in public-facing registration endpoint

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T12:00:00Z*

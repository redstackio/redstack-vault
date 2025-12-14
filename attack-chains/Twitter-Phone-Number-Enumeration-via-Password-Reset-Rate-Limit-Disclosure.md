---
tags:
  - information-disclosure
  - phone-enumeration
  - twitter
  - rate-limit-bypass
  - brute-force
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Reveal-Last-Two-Digits-of-Phone-Number-via-Password-Reset]]'
  - '[[procedures/Exhaust-SMS-Rate-Limit-for-Target-Username]]'
  - '[[procedures/Bypass-IP-Restrictions-by-Changing-IP-Address]]'
  - '[[procedures/Brute-Force-Full-Phone-Number-Using-Rate-Limit-Indicator]]'
step_count: 4
techniques:
  - '[[Gather Victim Identity Information]]'
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:24:42.888Z'
description: >-
  Multi-stage attack exploiting information disclosure in Twitter's password
  reset process to enumerate full mobile phone numbers associated with usernames
  through rate limit exhaustion and brute force.
skill_level: intermediate
impact_level: high
id: 9fb17eb1-3ca3-475a-9958-986d7756bf7e
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Identity Information]]'
  - '[[Brute Force]]'
---
# Twitter Phone Number Enumeration via Password Reset Rate Limit Disclosure

Multi-stage attack chain demonstrating a complete attack workflow exploiting distinct error messages in Twitter's password reset to reveal and brute-force users' full mobile phone numbers.

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
    A[Reveal Last Two Digits] --> B[Exhaust Rate Limit]
    B --> C[Change IP Address]
    C --> D[Brute Force Phone Number]
    D --> E[Full Number Enumerated]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox with developer tools for manual testing)
- IP changing capability (VPN, proxy, or Tor)

### Target Environment

- Twitter web platform
- Access to password reset endpoints
- No special ports required; standard HTTPS (443)

### Initial Access Requirements

- No credentials needed
- Public internet access
- Target username known

## Detailed Attack Procedures

### Step 1: Reveal Last Two Digits
procedure: [[procedures/Reveal-Last-Two-Digits-of-Phone-Number-via-Password-Reset]]

**Objective**: Initiate password reset to disclose the last two digits of the phone number associated with the target username.

**Instructions**: Navigate to the Twitter account lookup URL (e.g., https://twitter.com/i/flow/password_reset) and enter the target username (e.g., 'exampleuser'). Click search to trigger the reset process.

**Expected Output**: A message indicating SMS will be sent to a phone number ending in specific digits, e.g., 'We'll text a code to the phone number ending in 15'.

**Success Indicators**:
- Last two digits (e.g., '15') are revealed in the response message.
- No rate limit hit yet.

### Step 2: Exhaust Rate Limit
procedure: [[procedures/Exhaust-SMS-Rate-Limit-for-Target-Username]]

**Objective**: Repeatedly request SMS codes to exhaust the rate limit for the associated phone number.

**Instructions**: Repeat the password reset initiation from Step 1 multiple times (typically 5-10 attempts) until the rate limit is triggered.

**Expected Output**: Error message 'You've exceeded the number of attempts. Please try again later.' confirming the phone number ending in the known digits is now blocked.

**Success Indicators**:
- Rate limit message appears.
- Further requests are blocked for the specific phone number.

### Step 3: Bypass IP Restrictions
procedure: [[procedures/Bypass-IP-Restrictions-by-Changing-IP-Address]]

**Objective**: Switch to a new IP to avoid any account-level or global rate limiting that might block further attempts.

**Instructions**: Use a VPN, proxy service, or change network to obtain a new IP address. Verify the new IP via a service like whatismyipaddress.com.

**Expected Output**: New IP confirmed, allowing fresh requests without prior exhaustion affecting the new session.

**Success Indicators**:
- IP address changed successfully.
- Able to access Twitter without blocks from previous IP.

### Step 4: Brute Force Phone Number
procedure: [[procedures/Brute-Force-Full-Phone-Number-Using-Rate-Limit-Indicator]]

**Objective**: Systematically test possible phone numbers ending in the known digits to identify the exact one by observing rate limit responses.

**Instructions**: From the new IP, access the begin_password_reset page and input variations of phone numbers in the format for the country (e.g., 8-digit prefix + known '15'). Focus on common operator prefixes (e.g., 26-27 or 56-57) to narrow to ~10,000 attempts. For each, attempt password reset; the matching number will trigger the 'exceeded attempts' message due to prior exhaustion.

**Expected Output**: For the correct number, 'You've exceeded the number of attempts. Please try again later.'; others show 'We'll send a code' or 'not associated'.

**Success Indicators**:
- Exact full phone number identified via unique rate limit response.
- Privacy compromise confirmed.

## Attack Chain Summary

### Key Achievements

1. Revealed partial phone number (last two digits) through info disclosure.
2. Exhausted rate limits to create a detectable state for brute forcing.
3. Bypassed IP-based restrictions to enable enumeration.
4. Enumerated full mobile number, enabling privacy violations like targeted phishing.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Identity Information]] Gather Victim Identity Information
- [[Brute Force]] Brute Force

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*

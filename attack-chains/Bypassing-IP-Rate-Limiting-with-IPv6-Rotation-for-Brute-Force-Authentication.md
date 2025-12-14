---
id: ac-hackerone-brute-force-ipv6
tags:
  - brute-force
  - rate-limiting-bypass
  - ipv6
  - vps
  - authentication-bypass
type: attack_chain
tools:
  - '[[tools/Hetzner-VPS]]'
  - '[[tools/SecLists]]'
  - '[[tools/hackeronebrute.py]]'
  - '[[tools/Python]]'
tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Analyze-Login-Rate-Limiting-Mechanism]]'
  - '[[procedures/Setup-VPS-with-IPv6-Addresses]]'
  - '[[procedures/Prepare-Password-Dictionary]]'
  - '[[procedures/Verify-Network-Configuration]]'
  - '[[procedures/Execute-Brute-Force-Script]]'
  - '[[procedures/Login-with-Discovered-Password]]'
step_count: 6
techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
  - '[[Archive via Utility]]'
updated_at: '2025-12-14T17:31:52.796Z'
description: >-
  Multi-stage attack demonstrating brute-force of web authentication by
  bypassing IP-based rate limiting using IPv6 address rotation on a VPS.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
  - '[[Archive via Utility]]'
---
# Bypassing IP Rate Limiting with IPv6 Rotation for Brute-Force Authentication

Multi-stage attack chain demonstrating a complete brute-force workflow against a web authentication endpoint by exploiting weak IP-based rate limiting using IPv6 address rotation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~335 seconds |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Analyze Rate Limiting] --> B[Setup VPS with IPv6]
    B --> C[Prepare Password List]
    C --> D[Verify Network]
    D --> E[Execute Brute-Force Script]
    E --> F[Login with Password]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Hetzner-VPS]]
- [[tools/SecLists]]
- [[tools/Python]]
- [[tools/hackeronebrute.py]]

### Target Environment

- Web platform with login endpoint (e.g., https://hackerone.com/sessions)
- No CAPTCHA or account-level lockouts
- IP-based rate limiting only

### Initial Access Requirements

- Access to a VPS provider with IPv6 /64 subnet
- Target username (e.g., test account)
- Network access to the login endpoint

## Detailed Attack Procedures

### Step 1: Analyze Rate Limiting
procedure: [[procedures/Analyze-Login-Rate-Limiting-Mechanism]]

**Objective**: Determine the rate limiting mechanism to identify bypass opportunities.

**Instructions**: Test POST requests to the login endpoint to measure delays and limits.

**Expected Output**: Confirmation of 4-second delay per IP, allowing 15 guesses per minute.

**Success Indicators**:
- Requests blocked faster than 4 seconds per IP
- Calculated limits: 15/min, 900/hour per IP

### Step 2: Setup VPS with IPv6 Addresses
procedure: [[procedures/Setup-VPS-with-IPv6-Addresses]]

**Objective**: Provision a VPS with multiple IPv6 addresses to enable IP rotation.

**Instructions**: Deploy a Hetzner VPS and configure 500+ IPv6 addresses on the venet0 interface.

**Expected Output**: VPS with /64 IPv6 subnet assigned.

**Success Indicators**:
- Multiple IPv6 addresses visible on interface
- Ability to route traffic through different IPs

### Step 3: Prepare Password Dictionary
procedure: [[procedures/Prepare-Password-Dictionary]]

**Objective**: Create a wordlist of common passwords including the target test password.

**Instructions**: Download from SecLists and append the known test password.

Use [[commands/count-passwords-in-dictionary]] to verify count:

```bash
cat 10k_most_common.txt | wc -l
```

Then use [[commands/view-end-of-password-list]] to inspect:

```bash
tail 10k_most_common.txt
```

**Expected Output**: 10001 passwords, last entry 'Geniaal2!!'.

**Success Indicators**:
- Wordlist contains 10,001 entries
- Target password appended at end

### Step 4: Verify Network Configuration
procedure: [[procedures/Verify-Network-Configuration]]

**Objective**: Confirm multiple IPv6 addresses are assigned for rotation.

**Instructions**: Run network interface check on VPS.

Use [[commands/display-network-interfaces]]:

```bash
ifconfig
```

**Expected Output**: venet0 with multiple IPv6 like 2a04:XXXX:0:32::1001/64.

**Success Indicators**:
- 500+ IPv6 addresses listed
- Interface ready for IP rotation

### Step 5: Execute Brute-Force Script
procedure: [[procedures/Execute-Brute-Force-Script]]

**Objective**: Perform high-speed brute-force using IP rotation to evade limits.

**Instructions**: Run the custom Python script with 50 threads rotating through 677 IPv6 addresses.

Use [[commands/run-hackerone-brute-force-script]]:

```bash
python hackeronebrute.py ██████████ 10k_most_common.txt venet0 50
```

**Expected Output**: Password found in 335 seconds at ~30 pw/s.

**Success Indicators**:
- Script outputs '[SUCCESS] Found the right password: Geniaal2!!'
- Total attempts: 10,001

### Step 6: Login with Discovered Password
procedure: [[procedures/Login-with-Discovered-Password]]

**Objective**: Authenticate to confirm account compromise.

**Instructions**: Use the discovered password to login via the endpoint.

**Expected Output**: Successful session without additional verification.

**Success Indicators**:
- Full access to test account
- Access to confidential bug reports

## Attack Chain Summary

### Key Achievements

1. Bypassed 4-second IP rate limit using IPv6 rotation
2. Brute-forced password in 335 seconds with common list
3. Gained unauthorized access to HackerOne account

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Valid Accounts]] Valid Accounts
- [[Archive via Utility]] Archive Collected Data: Archive via Utility (for wordlist prep)

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Defense Evasion]] Defense Evasion

---
*Last updated: 2023-10-01T00:00:00Z*

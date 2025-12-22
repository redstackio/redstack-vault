---
id: ac-burp-session-persistence-001
tags:
  - burp-suite
  - session-management
  - authentication-bypass
  - persistent-access
type: attack_chain
tools: []
tactics:
  - '[[Persistence]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Login-to-Burp-Suite-Admin-Account]]'
  - '[[procedures/Reset-Burp-Suite-Admin-Password-via-Script]]'
  - '[[procedures/Verify-Persistent-Session-Access]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:07.141Z'
description: >-
  An attack chain exploiting a session management flaw in Burp Suite Enterprise
  where password resets do not invalidate existing admin sessions, allowing
  persistent unauthorized access.
skill_level: low
impact_level: high
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Persistent Admin Access in Burp Suite Enterprise via Uninvalidated Sessions After Password Reset

Multi-stage attack chain demonstrating a complete attack workflow exploiting a session management vulnerability in Burp Suite Enterprise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Compromise Admin Session] --> B[Password Reset Attempt]
    B --> C[Session Persistence Check]
    C --> D[Maintain Unauthorized Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- Burp Suite Enterprise installation
- Access to admin console
- Java-based web application

### Initial Access Requirements

- Compromised admin credentials or session (e.g., via phishing or prior breach)
- Network access to the Burp Suite Enterprise web interface
- No prior access needed beyond initial session compromise

## Detailed Attack Procedures

### Step 1: Compromise and Login to Admin Account
procedure: [[procedures/Login-to-Burp-Suite-Admin-Account]]

**Objective**: Establish a valid admin session in the browser to simulate a compromised session.

**Instructions**: Open a web browser and navigate to the Burp Suite Enterprise admin dashboard. Enter valid admin credentials to authenticate and create an active session.

**Expected Output**: Successful login to the admin console, with access to administrative functions.

**Success Indicators**:
- Admin dashboard loads without errors
- Session cookies or tokens are set in the browser

### Step 2: Attempt Password Reset via Admin Console Script
procedure: [[procedures/Reset-Burp-Suite-Admin-Password-via-Script]]

**Objective**: Simulate the legitimate admin attempting to lock out the attacker by resetting the password using the provided script.

**Instructions**: Access the server where Burp Suite Enterprise is installed. Execute the reset script to change the admin password, as per official documentation.

**Expected Output**: Password reset confirmation, but no session invalidation.

**Success Indicators**:
- Script runs without errors
- New password is set successfully

### Step 3: Verify Persistent Session Access
procedure: [[procedures/Verify-Persistent-Session-Access]]

**Objective**: Confirm that the original compromised session remains valid despite the password change, allowing continued admin access.

**Instructions**: Return to the original browser session and attempt to perform admin actions, such as viewing user lists or modifying settings, without re-entering credentials.

**Expected Output**: Full admin access granted without prompting for new credentials.

**Success Indicators**:
- Admin actions execute successfully
- No authentication challenges appear

## Attack Chain Summary

### Key Achievements

1. Established a persistent admin session
2. Demonstrated that password resets fail to invalidate sessions
3. Enabled ongoing unauthorized access to the admin console

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Persistence]]

---
*Last updated: 2023-10-01T00:00:00Z*

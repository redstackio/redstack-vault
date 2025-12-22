---
id: ac-uuid-placeholder
tags:
  - self-xss
  - social-engineering
  - xss
  - browser-security
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Check-for-Browser-Self-XSS-Protection]]'
  - '[[procedures/Trick-User-into-Executing-Self-XSS-JS]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T03:16:02.731Z'
description: >-
  A low-severity social engineering attack exploiting the absence of browser
  self-XSS protection on PortSwigger's website, tricking users into executing
  malicious JavaScript in their browser console to compromise accounts.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Phishing]]'
---
# Social Engineering Self-XSS via Unprotected Browser Console on PortSwigger Website

Multi-stage attack chain demonstrating a social engineering workflow to exploit missing self-XSS protections on the PortSwigger website, allowing attackers to trick users into self-injecting malicious JavaScript via the browser console.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Social Engineering] --> B[User Self-Injection]
    B --> C[Account Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual browser interaction)

### Target Environment

- Web platform
- Access to PortSwigger website (https://portswigger.net/)
- No specific services or ports required

### Initial Access Requirements

- Ability to communicate with target user (e.g., via email or chat)
- No prior credentials needed
- User must visit the site and have developer tools enabled

## Detailed Attack Procedures

### Step 1: Verify Missing Self-XSS Protection
procedure: [[procedures/Check-for-Browser-Self-XSS-Protection]]

**Objective**: Confirm the target website lacks protections against self-XSS, such as console blocking or alerts, making it vulnerable to social engineering.

**Instructions**: Navigate to the target website and inspect the browser console for any protective mechanisms. Compare against sites like Facebook that disable or alert on console JS execution.

**Expected Output**: No alerts or blocks when attempting to execute sample JS in the console, confirming the vulnerability.

**Success Indicators**:
- Console opens without restrictions
- JS executes freely without warnings

### Step 2: Social Engineer User into Self-XSS Execution
procedure: [[procedures/Trick-User-into-Executing-Self-XSS-JS]]

**Objective**: Trick a low-knowledge user into pasting and executing malicious JavaScript in their browser console while on the PortSwigger site, leading to potential account compromise or fraud.

**Instructions**: Craft a phishing message urging the user to "debug" an issue by opening the console (F12) on https://portswigger.net/ and pasting a provided JS payload, such as one that steals session cookies or propagates spam.

**Expected Output**: User executes the JS, resulting in malicious actions like cookie exfiltration to an attacker-controlled server.

**Success Indicators**:
- User confirms execution or attacker receives exfiltrated data
- No site-level blocks interrupt the process

## Attack Chain Summary

### Key Achievements

1. Identified missing self-XSS protection on a major security website
2. Demonstrated feasibility of social engineering to induce self-injection
3. Highlighted low-severity risk of user compromise via fraud or spam

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Phishing]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*

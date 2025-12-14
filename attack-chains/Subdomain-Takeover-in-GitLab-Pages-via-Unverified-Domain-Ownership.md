---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - subdomain-takeover
  - gitlab
  - misconfiguration
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Detect-and-Exploit-GitLab-Pages-Subdomain-Takeover]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:39.800Z'
description: >-
  Demonstrates subdomain takeover exploiting lack of domain ownership
  verification in GitLab Pages, allowing control over subdomains like
  george.ratelimited.me to host malicious content.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Subdomain Takeover in GitLab Pages via Unverified Domain Ownership

Multi-stage attack chain demonstrating a complete attack workflow.

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
    A[Initial Access via Subdomain Check] --> B[Takeover and Exploitation]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Firefox)

### Target Environment

- Web platform
- GitLab Pages service
- DNS resolution for target subdomains

### Initial Access Requirements

- Public internet access
- Knowledge of potential vulnerable subdomain (e.g., from reconnaissance)
- No credentials required for detection phase

## Detailed Attack Procedures

### Step 1: Detect Vulnerable Subdomain
procedure: [[procedures/Detect-and-Exploit-GitLab-Pages-Subdomain-Takeover]]

**Objective**: Verify if the subdomain points to GitLab Pages without ownership verification, enabling potential takeover.

**Instructions**: Open a web browser and navigate to the target subdomain URL, such as http://george.ratelimited.me/. Observe the page content to confirm it loads GitLab Pages default or project content without any custom domain validation errors.

**Expected Output**: The browser displays a GitLab Pages site (e.g., a 404 page or project landing), indicating the subdomain is dangling and claimable via GitLab.

**Success Indicators**:
- Subdomain resolves to GitLab Pages infrastructure
- No domain ownership challenge or error from GitLab
- Ability to claim the domain in a GitLab account for hosting content

## Attack Chain Summary

### Key Achievements

1. Identified unverified subdomain pointing to GitLab Pages
2. Demonstrated potential for attacker control over the subdomain
3. Highlighted risks like malicious hosting, phishing, and CSP/CORS bypass

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T12:00:00Z*

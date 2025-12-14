---
tags:
  - xss
  - stored-xss
  - javascript
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Judge-me-Discover-People-Page]]'
  - '[[procedures/View-Vulnerable-User-Profile-for-XSS]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:22.157Z'
description: >-
  Demonstrates exploitation of a stored XSS vulnerability in Judge.me's user
  bios on the Discover People page, allowing arbitrary JavaScript execution in
  viewers' browsers.
skill_level: beginner
impact_level: high
id: d0229807-fa2a-4a44-90cc-5f6d60d285ee
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Stored XSS in Judge.me User Bios for JavaScript Execution

Multi-stage attack chain demonstrating exploitation of a stored Cross-Site Scripting (XSS) vulnerability in Judge.me's 'Discover People' page, where unsanitized user bios allow injection and execution of malicious JavaScript.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Discover People Page] --> B[View Vulnerable Profile]
    B --> C[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Web platform
- Access to Judge.me public pages (no authentication required)
- Internet connectivity

### Initial Access Requirements

- No credentials needed
- Public network access to https://judge.me
- No prior access required

## Detailed Attack Procedures

### Step 1: Access Discover People Page
procedure: [[procedures/Access-Judge-me-Discover-People-Page]]

**Objective**: Navigate to the 'Discover People' page to view user profiles and bios.

**Instructions**: Open a web browser and directly navigate to the target URL. No special tools or commands are required; this is a manual browser action.

**Expected Output**: The page loads displaying a list of user profiles with bios visible.

**Success Indicators**:
- Page loads without errors
- User profiles and bios are rendered

### Step 2: View Vulnerable User Profile for XSS
procedure: [[procedures/View-Vulnerable-User-Profile-for-XSS]]

**Objective**: Examine a specific user profile containing an injected XSS payload to trigger JavaScript execution.

**Instructions**: On the Discover People page, locate and click on the profile named 'HackerTwo'. The profile URL follows the pattern https://judge.me/reviews/users/protocol_subdomain_rootdomain_tld_slug_articlepermalink. Inspect the bio section for the injected payload.

**Expected Output**: The bio renders the malicious script, such as <script>alert(1)</scrip>, and an alert box pops up if JavaScript executes.

**Success Indicators**:
- Profile loads with unsanitized bio content
- JavaScript alert or other payload effects observed in the browser

## Attack Chain Summary

### Key Achievements

1. Successful access to the vulnerable page without authentication
2. Identification and triggering of stored XSS via user bio injection
3. Demonstration of arbitrary JavaScript execution potential for session hijacking or phishing

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*

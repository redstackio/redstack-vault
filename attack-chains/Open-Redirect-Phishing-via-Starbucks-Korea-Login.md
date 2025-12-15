---
tags:
  - open-redirect
  - phishing
  - web
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Open-Redirect-in-Login]]'
step_count: 3
techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:31.568Z'
description: >-
  Demonstrates phishing attack exploiting an open redirect vulnerability in the
  Starbucks Korea login page to redirect authenticated users to malicious sites.
skill_level: beginner
impact_level: medium
id: 663bde04-c0e4-46d4-8251-f50ac8a93a46
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirect Phishing via Starbucks Korea Login

Multi-stage attack chain demonstrating a phishing workflow via open redirect in the Starbucks Korea login page.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Construct Malicious Login URL] --> B[User Authentication]
    B --> C[Redirect to Malicious Site]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#e74c3c
```

## Prerequisites & Requirements

### Required Tools

- None (browser-based)

### Target Environment

- Web platform
- Access to Starbucks Korea login page
- No specific services/ports required beyond HTTP/HTTPS

### Initial Access Requirements

- Valid Starbucks credentials for testing
- Network access to https://www.istarbucks.co.kr
- No prior access needed

## Detailed Attack Procedures

### Step 1: Construct Malicious Login URL
procedure: [[procedures/Exploit-Open-Redirect-in-Login]]

**Objective**: Create a crafted login URL with a malicious redirect_url parameter to bypass validation using a protocol-relative scheme.

**Instructions**: Manually construct the URL in a browser or via a simple request. Use a protocol-relative URL (//) to point to an external domain like www.bughunting.net.

**Expected Output**: The login page loads with the malicious redirect_url parameter preserved.

**Success Indicators**:
- Login page accessible at the crafted URL
- Parameter visible in the browser address bar

### Step 2: Perform User Login
procedure: [[procedures/Exploit-Open-Redirect-in-Login]]

**Objective**: Authenticate with valid credentials to trigger the redirect processing.

**Instructions**: Enter Starbucks Korea credentials into the login form on the crafted page.

**Expected Output**: Successful authentication without errors.

**Success Indicators**:
- User logged in
- No validation errors on the redirect parameter

### Step 3: Observe Redirection to Malicious Site
procedure: [[procedures/Exploit-Open-Redirect-in-Login]]

**Objective**: Confirm the open redirect by observing the post-login navigation to the external site.

**Instructions**: After submitting credentials, monitor the browser for automatic redirection.

**Expected Output**: Browser navigates to http://www.bughunting.net (or specified malicious site).

**Success Indicators**:
- Redirection to external domain
- Potential for phishing payload delivery

## Attack Chain Summary

### Key Achievements

1. Successful construction of malicious redirect URL
2. Bypassing redirect validation via protocol-relative scheme
3. Enabling post-authentication phishing

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Phishing]] Phishing
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*

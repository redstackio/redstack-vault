---
tags:
  - open-redirect
  - phishing
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Open-Redirect-in-Login]]'
  - '[[procedures/Craft-Phishing-Redirect-Link]]'
step_count: 2
techniques:
  - '[[T1566.002]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.516Z'
description: >-
  A multi-stage attack leveraging an open redirect vulnerability in the
  Moneybird login procedure to facilitate phishing by redirecting authenticated
  users to malicious external sites.
id: 09db305b-92af-4d21-8837-d25df93f4d7f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirect in Moneybird Login Procedure Enabling Phishing Attacks

Multi-stage attack chain demonstrating exploitation of an unvalidated redirect parameter in the Moneybird login process to enable phishing attacks. The vulnerability allows attackers to specify arbitrary external URLs, tricking users into visiting malicious sites after login, potentially leading to credential theft or further compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Endpoint] --> B[Craft Malicious Redirect]
    B --> C[Phishing Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for testing redirects

### Target Environment

- Web platform
- Access to Moneybird login endpoint (https://moneybird.com/login)
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Public internet access to the target site
- No credentials required for discovery
- Ability to craft and distribute phishing links

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Endpoint
procedure: [[procedures/Identify-Open-Redirect-in-Login]]

**Objective**: Discover the open redirect vulnerability by testing the login redirect parameter for validation bypass.

**Instructions**: Navigate to the Moneybird login page and append a test redirect parameter, such as ?redirect_to=http://example.com. Use a browser or [[commands/curl-test-redirect]] to follow the redirect and confirm it leads to the external site without domain validation.

```bash
curl -L "https://moneybird.com/login?redirect_to=http://example.com" -v
```

**Expected Output**: HTTP response showing a 302 redirect to the external URL, confirming the vulnerability.

**Success Indicators**:
- Redirect occurs to arbitrary external domain
- No error or validation blocking the redirect

### Step 2: Craft Phishing Redirect Link
procedure: [[procedures/Craft-Phishing-Redirect-Link]]

**Objective**: Construct a malicious link that exploits the open redirect to lure users to a phishing site after login.

**Instructions**: Create a phishing email or link pointing to the vulnerable login URL with a redirect to a controlled malicious domain, e.g., https://moneybird.com/login?redirect_to=https://fake-moneybird-phish.com. Host a fake login page on the malicious site to capture credentials post-redirect.

```bash
# No direct command; use URL construction in phishing payload
# Example phishing link: https://moneybird.com/login?redirect_to=https://attacker.com/steal-creds
```

**Expected Output**: User follows the link, logs in legitimately, and gets redirected to the attacker's phishing page where credentials can be harvested.

**Success Indicators**:
- User redirected to malicious site after authentication
- Potential capture of session cookies or credentials on fake page

## Attack Chain Summary

### Key Achievements

1. Identification of unvalidated redirect in login flow
2. Successful bypass leading to external domain redirection
3. Enablement of phishing attacks targeting Moneybird users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1566.002]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*

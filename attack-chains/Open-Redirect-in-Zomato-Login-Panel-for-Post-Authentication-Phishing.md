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
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Open-Redirect-in-Zomato-Login]]'
step_count: 3
techniques:
  - '[[Phishing]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:27.227Z'
description: >-
  Exploits an open redirect vulnerability in Zomato's login endpoint by
  injecting a malicious redirect_url parameter, redirecting authenticated users
  to external malicious sites to facilitate phishing attacks.
skill_level: beginner
impact_level: medium
id: ca00fb0d-c6df-4405-a9a8-498d052d317a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[Drive-by Compromise]]'
---
# Open Redirect in Zomato Login Panel for Post-Authentication Phishing

Multi-stage attack chain demonstrating a complete attack workflow exploiting an open redirect in Zomato's login panel to redirect users to malicious sites after authentication, enabling phishing for credential theft.

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
    A[Construct Malicious Login URL] --> B[Perform Login] --> C[Redirect to Malicious Site]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- Web platform
- Access to Zomato login endpoint: https://www.zomato.com/login
- No specific services or ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Valid Zomato user credentials (for testing post-auth redirect)
- Network access to the internet
- No prior access needed; public-facing vulnerability

## Detailed Attack Procedures

### Step 1: Construct Malicious Login URL
procedure: [[procedures/Exploit-Open-Redirect-in-Zomato-Login]]

**Objective**: Create a login URL with an arbitrary external redirect_url to bypass validation and set up redirection to a controlled malicious site.

**Instructions**: Manually construct the login URL by appending a malicious redirect_url parameter pointing to an attacker-controlled domain. For example, use a site like askdcodes.org for testing.

Open a web browser and navigate to:

```url
https://www.zomato.com/login?redirect_url=https://askdcodes.org
```

**Expected Output**: The Zomato login page loads with the malicious redirect_url parameter embedded in the URL.

**Success Indicators**:
- Login page displays without errors
- URL bar shows the injected redirect_url parameter

### Step 2: Perform Authenticated Login
procedure: [[procedures/Exploit-Open-Redirect-in-Zomato-Login]]

**Objective**: Authenticate with valid credentials to trigger the redirect mechanism after successful login.

**Instructions**: On the loaded login page, enter valid Zomato credentials and submit the form to complete authentication.

Fill in the username/email and password fields, then click the login button.

**Expected Output**: Successful login processing without immediate errors.

**Success Indicators**:
- Authentication succeeds (e.g., no invalid credential message)
- Browser begins to process the post-login redirect

### Step 3: Verify Redirect to Malicious Site
procedure: [[procedures/Exploit-Open-Redirect-in-Zomato-Login]]

**Objective**: Confirm that the application redirects the authenticated user to the injected malicious URL, enabling phishing.

**Instructions**: After submitting credentials, monitor the browser's navigation. The application should automatically redirect to the specified external URL.

Observe the browser's address bar and network requests (via developer tools if needed).

**Expected Output**: Browser navigates away from Zomato to the malicious site (e.g., https://askdcodes.org).

**Success Indicators**:
- User is redirected to the external malicious domain
- No internal Zomato page loads post-login; external site appears

## Attack Chain Summary

### Key Achievements

1. Successful injection of arbitrary redirect_url without validation
2. Post-authentication redirection to attacker-controlled site
3. Potential for phishing attacks to capture user data on the malicious page

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Phishing]] Phishing
- [[Drive-by Compromise]] Drive-by Compromise

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*

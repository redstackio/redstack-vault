---
id: ac-uuid-001
tags:
  - open-redirect
  - phishing
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Manipulate-Redirect-URL-in-Fabric-io-Login]]'
  - '[[procedures/Authenticate-with-Valid-Credentials-on-Fabric-io]]'
  - '[[procedures/Observe-Malicious-Redirect-After-Login]]'
step_count: 3
techniques:
  - '[[T1566.002]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.075Z'
description: >-
  A multi-step attack exploiting an open redirect vulnerability in the Fabric.io
  login endpoint to facilitate phishing by redirecting authenticated users to
  arbitrary external sites.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
  - '[[Exploit Public-Facing Application]]'
---
# Phishing via Open Redirect in Fabric.io Login Endpoint

Multi-stage attack chain demonstrating exploitation of an open redirect vulnerability in the Fabric.io login endpoint to enable phishing attacks. An attacker crafts a malicious login URL with a manipulated 'redirect_url' parameter prefixed with '@' followed by an arbitrary domain. When a victim accesses this URL and logs in with valid credentials, they are redirected to the attacker's controlled site, where credentials can be phished or malware distributed.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Manipulate Login URL] --> B[Victim Authentication]
    B --> C[Malicious Redirect]
    C --> D[Phishing Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox]]
- [[tools/Chrome]]

### Target Environment

- Web platform
- Access to Fabric.io login endpoint (https://www.fabric.io/login)
- No specific services or ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Ability to craft and distribute phishing links to victims
- Victim must have valid Fabric.io credentials
- No prior access to the target system needed; relies on social engineering

## Detailed Attack Procedures

### Step 1: Manipulate Redirect URL in Fabric.io Login
procedure: [[procedures/Manipulate-Redirect-URL-in-Fabric-io-Login]]

**Objective**: Craft a malicious login URL that includes an arbitrary external redirect target to bypass validation.

**Instructions**: Construct the login URL by appending the 'redirect_url' parameter prefixed with '@' and the desired malicious domain, such as '@attacker-phish-site.com'. This tricks the endpoint into allowing the redirect without proper domain checks.

**Expected Output**: A valid-looking Fabric.io login page URL that, upon login, will redirect to the specified external site.

**Success Indicators**:
- URL loads the Fabric.io login page without errors
- Parameter is accepted in the browser address bar

### Step 2: Authenticate with Valid Credentials on Fabric.io
procedure: [[procedures/Authenticate-with-Valid-Credentials-on-Fabric-io]]

**Objective**: Have the victim enter their credentials on the manipulated login page, completing authentication to trigger the redirect.

**Instructions**: Direct the victim to the crafted URL via email, message, or link. The victim enters their username and password in the standard login form. No special commands are needed; the browser handles the form submission with the embedded redirect parameter.

**Expected Output**: Successful login confirmation from Fabric.io, immediately followed by an automatic redirect.

**Success Indicators**:
- Victim sees the login form and submits credentials
- Authentication succeeds without alerting the victim to the manipulation

### Step 3: Observe Malicious Redirect After Login
procedure: [[procedures/Observe-Malicious-Redirect-After-Login]]

**Objective**: Confirm the redirect to the attacker's site post-authentication, enabling phishing or malware delivery.

**Instructions**: After login, monitor the browser's navigation. The application will redirect to the domain specified in the 'redirect_url' (e.g., attacker-phish-site.com), bypassing any intended restrictions. On the attacker's site, capture entered data or serve malicious content.

**Expected Output**: Browser navigates away from Fabric.io to the external malicious domain.

**Success Indicators**:
- Redirect occurs seamlessly after login
- Victim interacts with the phishing site, potentially exposing additional credentials or downloading malware

## Attack Chain Summary

### Key Achievements

1. Successful manipulation of the redirect parameter to point to an arbitrary external site
2. Bypassing validation in the login endpoint to enable post-authentication redirects
3. Facilitation of phishing attacks leading to credential theft or malware distribution

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1566.002]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*

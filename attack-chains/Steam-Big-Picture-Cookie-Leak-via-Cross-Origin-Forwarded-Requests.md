---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Steam Big Picture Cookie Leak via Cross-Origin Forwarded Requests
tags:
  - cookie-leak
  - information-disclosure
  - cross-origin
  - steam
  - browser-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
  - Desktop Application (Steam Big Picture)
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Setup-Malicious-Page-for-Cookie-Leak]]'
  - '[[procedures/Capture-Leaked-Cookies-via-Redirect]]'
step_count: 2
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:33:24.520Z'
description: >-
  Attack chain exploiting the Steam Big Picture web browser's improper handling
  of secure cookies in cross-origin forwarded requests, leading to disclosure of
  login credentials and potential account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Credentials In Files]]'
---
# Steam Big Picture Cookie Leak via Cross-Origin Forwarded Requests

Multi-stage attack chain demonstrating a complete attack workflow exploiting the vulnerability in Steam Big Picture mode's web browser, where secure login cookies are leaked in cross-origin requests initiated from a trusted domain but forwarded to an attacker-controlled origin.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Malicious Page] --> B[Initiate Cross-Origin Request]
    B --> C[Capture Leaked Cookies]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web server (e.g., Python's SimpleHTTPServer or Apache)
- Browser developer tools for testing

### Target Environment

- Steam client with Big Picture mode enabled
- Victim using Steam web features in Big Picture browser
- Attacker controls a domain or server for receiving requests

### Initial Access Requirements

- Social engineering to lure victim into loading malicious content in Big Picture mode
- No prior credentials needed, but victim must be logged into Steam

## Detailed Attack Procedures

### Step 1: Setup Malicious Page for Cookie Leak
procedure: [[procedures/Setup-Malicious-Page-for-Cookie-Leak]]

**Objective**: Create a webpage hosted on an attacker-controlled domain that mimics a trusted Steam domain and initiates a request to forward to the attacker's server, tricking the browser into including secure cookies.

**Instructions**: Host a simple HTML page on your server that loads an iframe or script from a trusted Steam origin (e.g., steamcommunity.com) and then redirects or forwards the request to your capture server. Use a tool like ngrok to expose your local server publicly if needed.

**Expected Output**: A hosted webpage that, when loaded in Big Picture mode, sends a request with leaked cookies to the attacker's endpoint.

**Success Indicators**:
- Page loads without errors in the target's browser
- Request is initiated from trusted origin

### Step 2: Capture Leaked Cookies via Redirect
procedure: [[procedures/Capture-Leaked-Cookies-via-Redirect]]

**Objective**: Receive and log the cross-origin request containing the victim's secure Steam login cookies, enabling session hijacking or account takeover.

**Instructions**: Monitor your server logs for incoming requests from the Steam Big Picture browser. The request will include cookies like session IDs and authentication tokens due to the browser's failure to strip them in cross-origin forwards.

**Expected Output**: Server logs showing HTTP request headers with sensitive cookies (e.g., steamLoginSecure, sessionid).

**Success Indicators**:
- Cookies received in request headers
- Ability to replay cookies for account access

## Attack Chain Summary

### Key Achievements

1. Successful leakage of secure Steam login cookies
2. Capture of sensitive session data without direct access to the victim's machine
3. Potential for full account takeover using stolen credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[Credentials In Files]] Credentials In Files (adapted for cookies)

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access

---
*Last updated: 2023-10-01T12:00:00Z*

---
tags:
  - open-redirect
  - phishing
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/BurpSuite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-and-Manipulate-Open-Redirect-in-Expired-Auth-Token]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.185Z'
description: >-
  An attack chain exploiting an open redirect vulnerability in Brave Software's
  publishers.basicattentiontoken.org by manipulating the X-FORWARDED-HOST header
  to redirect users to arbitrary phishing sites.
skill_level: intermediate
impact_level: high
id: 1215e5d0-4546-4b41-97c4-27886f9c9acf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Open Redirect via X-FORWARDED-HOST Manipulation in Brave Publishers

Multi-stage attack chain demonstrating a complete attack workflow exploiting an open redirect in Brave Software's publisher authentication system to facilitate phishing.

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
    A[Trigger Redirect Request] --> B[Intercept and Modify Header]
    B --> C[Arbitrary Redirection to Phishing Site]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/BurpSuite]]

### Target Environment

- Web application at https://publishers.basicattentiontoken.org/
- No specific ports or services beyond standard HTTPS (443)
- Network access to the public-facing publisher endpoint

### Initial Access Requirements

- No credentials required
- Direct network access to the internet
- No prior access needed; targets public endpoint

## Detailed Attack Procedures

### Step 1: Trigger Redirect Request

procedure: [[procedures/Trigger-and-Manipulate-Open-Redirect-in-Expired-Auth-Token]]

**Objective**: Initiate a 302 redirect from the expired_auth_token endpoint using a valid publisher_id to set up for interception.

**Instructions**: Access the expired_auth_token endpoint with a specific publisher_id to trigger the initial redirect. This can be done via browser or using [[commands/curl-trigger-redirect]]:

```bash
curl -i "https://publishers.basicattentiontoken.org/publishers/expired_auth_token?publisher_id=587fb66a-9fdb-4419-9d05-f38ce41666ca"
```

**Expected Output**: A 302 HTTP response with a Location header pointing to an internal redirect URL.

**Success Indicators**:
- 302 status code received
- Redirect Location header present in response

### Step 2: Intercept and Modify Header

procedure: [[procedures/Trigger-and-Manipulate-Open-Redirect-in-Expired-Auth-Token]]

**Objective**: Intercept the redirect request and inject a custom X-FORWARDED-HOST header to control the redirect destination, enabling redirection to an arbitrary external site.

**Instructions**: Use BurpSuite to intercept the request from Step 1 and add the X-FORWARDED-HOST header with a malicious domain. Forward the modified request using BurpSuite's Repeater or Proxy features.

**Expected Output**: The server responds with a 302 redirect to the injected URL (e.g., http://injectedurl.com).

**Success Indicators**:
- Redirect Location header points to the injected domain
- Browser or client follows to the arbitrary external site

## Attack Chain Summary

### Key Achievements

1. Successful triggering of the vulnerable redirect endpoint
2. Manipulation of X-FORWARDED-HOST to bypass validation and control redirect
3. Demonstration of phishing potential by making malicious links appear legitimate

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*

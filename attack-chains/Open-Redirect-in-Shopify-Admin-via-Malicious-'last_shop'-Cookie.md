---
id: ac-open-redirect-shopify-cookie
tags:
  - open-redirect
  - phishing
  - cookie-manipulation
  - shopify
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
  - '[[procedures/Set-Malicious-last-shop-Cookie]]'
  - '[[procedures/Trigger-Shopify-Admin-Redirect]]'
step_count: 2
techniques:
  - '[[Drive-by Compromise]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:26.494Z'
description: >-
  A two-step attack exploiting an open redirect vulnerability in Shopify's admin
  endpoint by manipulating the 'last_shop' cookie to redirect users to arbitrary
  malicious domains, enabling phishing attacks.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[T1566.002]]'
---
# Open Redirect in Shopify Admin via Malicious 'last_shop' Cookie

Multi-stage attack chain demonstrating a complete attack workflow exploiting an open redirect in Shopify's admin endpoint.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Malicious Cookie] --> B[Trigger Redirect]
    B --> C[Phishing Success]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser Developer Tools (e.g., Chrome DevTools)
- Or [[commands/curl-set-cookie-and-visit]]

### Target Environment

- Web platform
- Access to Shopify admin URL: https://www.shopify.com/admin/*
- No specific ports or services required beyond HTTP/HTTPS

### Initial Access Requirements

- Ability to set cookies on the victim's browser (e.g., via XSS or user interaction)
- Network access to Shopify domains
- No prior credentials needed, but victim must visit the admin page

## Detailed Attack Procedures

### Step 1: Set Malicious Cookie
procedure: [[procedures/Set-Malicious-last-shop-Cookie]]

**Objective**: Modify the 'last_shop' cookie to point to an attacker-controlled domain, preparing for the redirect.

**Instructions**: Use browser developer tools or curl to set the cookie. In Chrome DevTools, go to Application > Cookies > https://www.shopify.com and edit 'last_shop' to 'https://attacker.com'. Alternatively, use [[commands/curl-set-cookie-and-visit]] to simulate:

```bash
curl -c cookies.txt -b "last_shop=https://attacker.com" https://www.shopify.com/admin/auth
```

**Expected Output**: Cookie set successfully; no immediate redirect.

**Success Indicators**:
- Cookie value updated to arbitrary domain
- Verified via browser inspection or curl verbose output

### Step 2: Trigger the Redirect
procedure: [[procedures/Trigger-Shopify-Admin-Redirect]]

**Objective**: Access the admin endpoint with the tampered cookie to force a redirect to the malicious site.

**Instructions**: Visit https://www.shopify.com/admin/* with the modified cookie. In browser, navigate to the URL after setting the cookie. Or use curl:

```bash
curl -b cookies.txt https://www.shopify.com/admin/ -L -v
```

**Expected Output**: HTTP 302 redirect to https://attacker.com/admin/*.

**Success Indicators**:
- Redirect observed in network logs
- User lands on attacker-controlled phishing page

## Attack Chain Summary

### Key Achievements

1. Successful cookie manipulation without authentication
2. Arbitrary domain redirect from trusted Shopify context
3. Enabled phishing by impersonating Shopify redirects

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[T1566.002]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*

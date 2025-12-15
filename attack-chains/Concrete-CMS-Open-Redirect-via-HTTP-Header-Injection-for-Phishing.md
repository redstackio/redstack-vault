---
tags:
  - open-redirect
  - phishing
  - header-injection
  - concrete-cms
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Open-Redirect-via-Header-Injection-in-Concrete-CMS]]'
step_count: 1
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.149Z'
description: >-
  Attack chain exploiting an open redirect vulnerability in Concrete CMS by
  injecting extra HTTP headers to redirect users to arbitrary malicious sites,
  enabling phishing or malware delivery.
skill_level: intermediate
impact_level: high
id: b6d66c01-0ea3-4dea-aa7b-2ef5fdb61b5c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Concrete CMS Open Redirect via HTTP Header Injection for Phishing

Multi-stage attack chain demonstrating a complete attack workflow exploiting an open redirect in Concrete CMS to redirect users to malicious sites for phishing credentials or delivering malware.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Header Injection] --> B[Trigger Redirect]
    B --> C[Phishing or Malware Delivery]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- Concrete CMS web application
- Accessible HTTP endpoint handling redirects
- No specific ports beyond standard 80/443

### Initial Access Requirements

- Network access to the target Concrete CMS instance
- Ability to send crafted HTTP requests (e.g., via browser, proxy, or MITM)
- No prior credentials needed for unauthenticated redirect

## Detailed Attack Procedures

### Step 1: Inject Headers to Trigger Open Redirect
procedure: [[procedures/Exploit-Open-Redirect-via-Header-Injection-in-Concrete-CMS]]

**Objective**: Manipulate HTTP request headers to force the Concrete CMS application to redirect the user to an attacker-controlled remote website, enabling phishing or malware distribution.

**Instructions**: Craft an HTTP request to a redirect-handling endpoint in Concrete CMS, injecting extra headers such as X-Forwarded-Host or similar to override the redirect destination. This can be done directly via curl or through a proxy like Burp Suite for testing. For example, send a request that simulates a forwarded host pointing to the malicious site:

Use [[commands/curl-header-injection-redirect]] to test the injection:

```bash
curl -H "Host: target.com" -H "X-Forwarded-Host: evil.com" -H "X-Forwarded-Proto: http" http://target.com/redirect-endpoint -v
```

Monitor the response for a 3xx redirect status pointing to the evil.com domain. In a real attack, chain this with MITM to intercept user traffic or use request smuggling if applicable.

**Expected Output**: HTTP response with Location header set to http://evil.com/, confirming the redirect.

**Success Indicators**:
- Redirect Location header points to arbitrary external domain
- No validation errors in response
- User browser follows redirect to malicious site

## Attack Chain Summary

### Key Achievements

1. Successful header injection bypassing redirect validation
2. Redirection of users to phishing site for credential theft
3. Potential for malware delivery via drive-by download on the remote site

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*

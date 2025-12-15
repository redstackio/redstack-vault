---
id: ac-hackerone-open-redirect-52035
tags:
  - open-redirect
  - phishing
  - dos
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Malformed-URL-with-Double-Slashes]]'
  - '[[procedures/Trigger-Redirect-via-Language-Switcher]]'
  - '[[procedures/Observe-Open-Redirect-and-DoS-Effect]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:24:30.692Z'
description: >-
  A multi-step attack exploiting an open redirect vulnerability in HackerOne's
  language change feature using double slashes in URLs, enabling phishing and
  temporary DoS effects.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# HackerOne Open Redirect via Malformed URLs in Language Switcher

Multi-stage attack chain demonstrating exploitation of an open redirect in HackerOne's language change feature, allowing redirects to external domains for phishing and a secondary DoS via CloudFlare errors.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Malformed URL] --> B[Interact with Language Switcher]
    B --> C[Observe Redirect and DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- Web platform
- HackerOne application (public-facing)
- CloudFlare-protected services

### Initial Access Requirements

- No credentials required (public access)
- Direct network access to https://hackerone.com
- No prior access needed

## Detailed Attack Procedures

### Step 1: Access Malformed URL with Double Slashes
procedure: [[procedures/Access-Malformed-URL-with-Double-Slashes]]

**Objective**: Load a page using a URL with double slashes followed by an external domain to bypass proper path handling.

**Instructions**: Manually navigate to a crafted URL in your web browser, such as `https://hackerone.com//example.com/ru/faq` or `https://hackerone.com//example.com/faq`. The page will load, but the web server will misinterpret the path due to excess slashes, treating it as if the request originates from the external FQDN.

**Expected Output**: The HackerOne page loads, but internal redirects prepare for external domain handling.

**Success Indicators**:
- Page loads without immediate error
- URL bar shows the malformed path

### Step 2: Trigger Redirect via Language Switcher
procedure: [[procedures/Trigger-Redirect-via-Language-Switcher]]

**Objective**: Interact with the language change feature to force a redirect to the external domain.

**Instructions**: On the loaded page, scroll to the right side of the interface and select a different language, such as English, from the language switcher dropdown. This action triggers the redirect mechanism, which fails to sanitize the malformed URL path.

**Expected Output**: Browser redirects to the external site, e.g., `http://example.com/`.

**Success Indicators**:
- Language switcher activates
- Immediate redirect to external domain observed

### Step 3: Observe Open Redirect and DoS Effect
procedure: [[procedures/Observe-Open-Redirect-and-DoS-Effect]]

**Objective**: Confirm the phishing-enabling redirect and note any temporary DoS from CloudFlare errors.

**Instructions**: After the redirect, verify the landing on the external domain. Separately, test double-slash URLs like `https://hackerone.com//anything/hacktivity` to trigger CloudFlare error 523, which may persist briefly on subsequent clean URL accesses.

**Expected Output**: Successful redirect to external site; error 523 on malformed URLs with temporary caching effect.

**Success Indicators**:
- External domain loads via redirect
- CloudFlare 523 error displayed on double-slash access
- Brief DoS on follow-up requests

## Attack Chain Summary

### Key Achievements

1. Successful open redirect to arbitrary external domain, enabling phishing attacks by luring users via trusted HackerOne links.
2. Exploitation of web server slash handling flaws combined with language feature.
3. Secondary DoS impact via CloudFlare's response to malformed requests, though not primary bounty focus.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Denial of Service]] Network Denial of Service

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*

---
id: ac-hackerone-open-redirect-57163
tags:
  - open-redirect
  - url-parsing
  - phishing
  - cloudflare
  - bypass
type: attack_chain
tools:
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Encoded-Slash-Redirect]]'
  - '[[procedures/Observe-Double-Slash-Behavior]]'
  - '[[procedures/Identify-Partial-Domain-Redirect]]'
  - '[[procedures/Bypass-Domain-Parsing-with-Double-Encoding]]'
  - '[[procedures/Explore-Invalid-Double-Slash-Effects]]'
  - '[[procedures/Note-Invalid-URL-Interaction-with-Redirect]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.348Z'
description: >-
  Multi-stage exploitation of an open redirect vulnerability on hackerone.com
  using malformed URLs with encoded slashes, double slashes, and double encoding
  to bypass parsing and redirect to arbitrary external sites, enabling phishing.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HackerOne Open Redirect via Encoded Slashes and Double Encoding

Multi-stage attack chain demonstrating exploitation of an open redirect vulnerability on hackerone.com through malformed URLs, including encoded slashes (%2F), double slashes (//), and double encoding (%252E) to redirect users to arbitrary external sites for potential phishing attacks. The chain also highlights side effects like triggering CloudFlare cached pages or alerts, which can disrupt normal site access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Encoded Slash Redirect] --> B[Observe Double Slash Behavior]
    B --> C[Identify Partial Domain Redirect]
    C --> D[Bypass with Double Encoding]
    D --> E[Explore Invalid Double Slash Effects]
    E --> F[Note URL Interaction with Redirect]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Chrome-Browser]]

### Target Environment

- Web platform
- Access to hackerone.com
- No specific services/ports beyond standard HTTPS (443)

### Initial Access Requirements

- Public access to hackerone.com (no credentials needed)
- Network access to external sites for redirect testing
- No prior access required

## Detailed Attack Procedures

### Step 1: Discover Encoded Slash Redirect
procedure: [[procedures/Discover-Encoded-Slash-Redirect]]

**Objective**: Identify the initial open redirect vulnerability using an encoded slash in the URL path to force a redirect to an external IP or domain.

**Instructions**: Open a web browser and navigate to a malformed URL on hackerone.com with an encoded slash, such as `https://hackerone.com/%2F1572395042`. Observe the redirect behavior to an external endpoint (e.g., example.com as a placeholder).

**Expected Output**: Browser redirects to the external IP or domain specified after the encoded slash.

**Success Indicators**:
- Redirect occurs to external site
- No validation error from the server

### Step 2: Observe Double Slash Behavior
procedure: [[procedures/Observe-Double-Slash-Behavior]]

**Objective**: Test how double slashes in the URL path affect access and parsing on hackerone.com, noting differences between valid and invalid domains.

**Instructions**: In the browser, test `https://hackerone.com//hackerone.com` (which resolves normally) versus `https://hackerone.com//hackerone1.com` (which fails or behaves differently). Document the access outcomes.

**Expected Output**: Valid double-slash URLs load the site, while invalid ones may trigger errors or alternative behaviors.

**Success Indicators**:
- Difference in loading between valid and invalid domains observed
- Potential for further malformed URL exploration identified

### Step 3: Identify Partial Domain Redirect
procedure: [[procedures/Identify-Partial-Domain-Redirect]]

**Objective**: Demonstrate a partial redirect where the server truncates the domain, leading to incomplete but still exploitable redirects.

**Instructions**: Navigate to `https://hackerone.com/%2Fgoogle.com` in the browser. Observe how the server cuts off the `.com` portion, redirecting to `https://google` instead of the full domain.

**Expected Output**: Redirect to a truncated domain like `https://google`.

**Success Indicators**:
- Partial redirect confirms URL parsing flaw
- Redirect to incomplete external site occurs

### Step 4: Bypass Domain Parsing with Double Encoding
procedure: [[procedures/Bypass-Domain-Parsing-with-Double-Encoding]]

**Objective**: Bypass the truncation issue by using double encoding for the dot (.), achieving a full redirect to the intended external domain.

**Instructions**: Access `https://hackerone.com/%2Fgoogle%252Ecom` in Chrome. The double-encoded dot (%252E decodes to %2E, then to .) tricks the parser into handling the full domain.

**Expected Output**: Full redirect to `https://google.com`.

**Success Indicators**:
- Complete external domain redirect achieved
- Bypasses single-encoding limitations

### Step 5: Explore Invalid Double Slash Effects
procedure: [[procedures/Explore-Invalid-Double-Slash-Effects]]

**Objective**: Investigate side effects of invalid double-slash URLs, including triggering CloudFlare alerts and serving cached pages.

**Instructions**: Navigate to `https://hackerone.com//hackerone.com1`, then attempt to access other pages like `https://hackerone.com/hacktivity`. Note the CloudFlare intervention showing the site as offline with a cached page.

**Expected Output**: CloudFlare alert page with cached content; site appears disrupted.

**Success Indicators**:
- CloudFlare alert triggered
- Cached page served, indicating DoS-like disruption

### Step 6: Note Invalid URL Interaction with Redirect
procedure: [[procedures/Note-Invalid-URL-Interaction-with-Redirect]]

**Objective**: Understand how prior invalid URL access affects subsequent open redirect proof-of-concepts due to CloudFlare state changes.

**Instructions**: After accessing an invalid URL like `https://hackerone.com//hackerone1.com`, attempt previous redirect PoCs (e.g., from Step 4). Observe failures or altered behavior due to CloudFlare's security state.

**Expected Output**: Open redirect tests fail or are blocked post-invalid URL access.

**Success Indicators**:
- Interaction between invalid URLs and redirects confirmed
- Potential for chaining effects in real attacks noted

## Attack Chain Summary

### Key Achievements

1. Discovered and exploited open redirect via encoded slashes for arbitrary external redirects.
2. Bypassed domain parsing flaws using double encoding to enable full phishing-capable redirects.
3. Identified side effects like CloudFlare disruptions, which could aid in evasion or DoS.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*

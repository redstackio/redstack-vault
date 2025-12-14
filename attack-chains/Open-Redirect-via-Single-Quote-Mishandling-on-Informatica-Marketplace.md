---
id: f90dbb4a-6d5d-4a78-bb66-49e5211a9e19
name: Open Redirect via Single Quote Mishandling on Informatica Marketplace
type: attack_chain
description: >-
  A single-stage attack exploiting an open redirect vulnerability on
  marketplace.informatica.com by crafting URLs with single quotes to bypass
  rewrite rules and redirect users to arbitrary external sites for phishing.
verified: false
submitted: true
step_count: 1
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.222Z'
procedures:
  - '[[procedures/Trigger-Open-Redirect-with-Single-Quote]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tactics:
  - '[[Initial Access]]'
tags:
  - open-redirect
  - phishing
  - web-vulnerability
platforms:
  - Web
tools: []
complexity: low
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Open Redirect via Single Quote Mishandling on Informatica Marketplace

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Crafted URL] --> B[Redirect to Malicious Site]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Web platform
- Target: marketplace.informatica.com
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Internet access to the target domain

### Initial Access Requirements

- No credentials required
- External network position (public internet)
- No prior access needed

## Detailed Attack Procedures

### Step 1: Trigger Open Redirect
procedure: [[procedures/Trigger-Open-Redirect-with-Single-Quote]]

**Objective**: Craft and send a malicious URL to the target site to exploit the open redirect vulnerability, redirecting the user to an arbitrary external domain.

**Instructions**: Construct a URL with a single quote in the path to trigger the flawed rewrite rule. Use [[commands/http-get-trigger-open-redirect]] to send the request:

```bash
curl -X GET 'https://marketplace.informatica.com//google.com?q=ohdear&a%27b' -H 'Host: marketplace.informatica.com' -H 'Connection: close' -i
```

This simulates the GET request to the crafted path, resulting in a 302 redirect.

**Expected Output**: A 302 Found response with Location header pointing to the protocol-relative URL (e.g., //google.com?q=ohdear&a), stripping the single quote.

**Success Indicators**:
- 302 redirect response received
- Location header contains the arbitrary external URL without the single quote
- Browser or client follows redirect to the malicious site

## Attack Chain Summary

### Key Achievements

1. Successful exploitation of open redirect to bypass URL validation
2. Demonstration of phishing potential by mimicking legitimate domain redirects
3. Identification of the vulnerability in the URL rewrite rule handling single quotes

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*

---
tags:
  - open-redirect
  - phishing
  - web-vuln
  - path-traversal
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-open-redirect-test]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Craft-Malicious-URL-for-Open-Redirect-Bypass]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploits an open redirect vulnerability on the admin.c2fo.com root path by
  using multiple consecutive slashes and URL-encoded path traversal to bypass
  restrictions and redirect to arbitrary external sites.
skill_level: beginner
impact_level: medium
id: 46529e1d-183b-4b25-b9ca-0cf3342aa024
created_at: '2025-12-14T17:24:27.221Z'
updated_at: '2025-12-14T17:24:27.221Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Open-Redirect-on-Admin-C2FO-via-Multiple-Slashes-and-Path-Traversal

## Overview

This attack chain demonstrates the exploitation of an open redirect vulnerability on the root path of https://admin.c2fo.com. By crafting a malformed URL with multiple consecutive slashes (///) followed by an external domain and URL-encoded path traversal characters (%2e%2e), the attacker bypasses any intended redirect restrictions. This allows redirection to arbitrary external websites, which can facilitate phishing attacks, session hijacking, or unauthorized navigation to malicious sites. The vulnerability stems from improper validation of URLs, enabling attackers to trick users or automated systems into visiting harmful destinations.

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
    A[Initial Access via Malformed URL] --> B[Trigger Redirect to External Site]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-open-redirect-test]]

### Target Environment

- Web platform
- Access to https://admin.c2fo.com root path
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Public internet access to the target domain
- No credentials required for the root path
- Ability to craft and send HTTP GET requests

## Detailed Attack Procedures

### Step 1: Craft and Trigger Malformed URL
procedure: [[procedures/Craft-Malicious-URL-for-Open-Redirect-Bypass]]

**Objective**: Bypass redirect restrictions on the admin panel to force a redirection to an arbitrary external domain, enabling potential phishing or unauthorized navigation.

**Instructions**: Construct a URL starting with the target domain's root path, appending multiple slashes followed by the desired external domain and URL-encoded path traversal (%2e%2e). Send a GET request to this URL using [[commands/curl-open-redirect-test]]:

```bash
curl -i -L "https://admin.c2fo.com///www.google.com/%2e%2e"
```

This sends a GET request to the root path with the malformed path appended, triggering a 3xx redirect response.

**Expected Output**: A 3xx redirect status code in the response headers, with Location header pointing to //www.google.com/%2e%2e/, confirming the open redirect.

**Success Indicators**:
- HTTP response includes a 3xx status code
- Location header redirects to the injected external domain without scheme or host validation
- Browser or curl follows the redirect to the arbitrary site

## Attack Chain Summary

### Key Achievements

1. Successful bypass of URL validation using multiple slashes and %2e%2e encoding
2. Achievement of arbitrary external redirection from the admin domain
3. Potential enablement of phishing by luring users to malicious sites via trusted domain

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*

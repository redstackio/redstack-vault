---
tags:
  - open-redirect
  - path-traversal
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-open-redirect-test]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 41ba30ca-6470-4ecb-9c54-434b520d7003
created_at: '2025-12-14T17:24:27.216Z'
updated_at: '2025-12-14T17:24:27.216Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-URL-for-Open-Redirect-Bypass

## Summary

This procedure exploits an open redirect vulnerability by crafting a specially formatted URL that uses multiple consecutive slashes and URL-encoded path traversal sequences to evade validation checks on the target web application's redirect mechanism. It allows redirection to arbitrary external domains, which can be leveraged for phishing or bypassing security controls.

## Description

In the context of the admin.c2fo.com domain, the root path (/) lacks proper sanitization for URLs containing multiple slashes (e.g., ///) followed by an external hostname and %2e%2e (encoded ../). When a GET request is made to such a URL, the server interprets the path incorrectly, resulting in a redirect to the injected location without enforcing scheme (http/https) or host restrictions. This can trick users into visiting malicious sites under the guise of the legitimate domain, facilitating attacks like phishing or credential theft. Prerequisites include public access to the target and a tool like curl for testing; no authentication is needed for the root path.

## Requirements

1. Network access to https://admin.c2fo.com over HTTPS
2. Ability to send custom HTTP GET requests (e.g., via curl or browser)
3. Basic understanding of URL encoding and HTTP redirects

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation on redirects, normalizing paths and rejecting multiple slashes or traversal sequences
- Enforce absolute URL checks, requiring explicit schemes and whitelisting allowed hosts
- Monitor server logs for anomalous redirect patterns, such as 3xx responses to malformed paths
- Use Content Security Policy (CSP) headers to restrict navigation from the domain

## Objectives

1. Bypass redirect validation to reach arbitrary external sites
2. Demonstrate potential for phishing by redirecting users to attacker-controlled domains
3. Highlight improper input handling in web applications

## Instructions

### Step 1: Construct the Malicious URL

**Context**: Build the URL by appending ///[external-domain]/%2e%2e to the target root path. This exploits the lack of path normalization, causing the server to treat the external domain as a relative redirect target.

**Command** ([[commands/curl-open-redirect-test]]):
```bash
curl -i -L "https://admin.c2fo.com///www.google.com/%2e%2e"
```

> This command sends a GET request with verbose headers (-i) and follows redirects (-L). Expected output includes a 302 or 301 status followed by Location: //www.google.com/%2e%2e/, confirming the bypass. The %2e%2e ensures any residual path is traversed away, cleaning the redirect.

### Step 2: Verify the Redirect

**Context**: Follow the redirect manually or via tool to confirm it leads to the external site, simulating a phishing scenario.

**Command** ([[commands/curl-open-redirect-test]]):
```bash
curl -i -L "https://admin.c2fo.com///www.google.com/%2e%2e" | grep -i location
```

> Grep for the Location header to isolate the redirect target. Success is indicated by the external domain appearing in the output without the original scheme enforced.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-open-redirect-test]]

## Tools Used


## Tags

- [[open-redirect]]
- [[path-traversal]]
- [[Phishing]]
